from tqdm import tqdm
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import h5py
import torch as pt

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")


def get_image_embeddings(img_url: str):
    image = Image.open(img_url)
    # print(image)
    inputs = clip_processor(images=image, return_tensors="pt")
    image_embeddings = clip_model.get_image_features(**inputs)
    return image_embeddings

features = []

for i in tqdm(range(17941)):
    ipath = f"./../video_clips/P04/P04_frames/frame_{i+1}.png"
    # print(ipath)
    image_embedding = get_image_embeddings(ipath)
    features.append(image_embedding.detach().numpy())
    del(image_embedding)


with h5py.File('P04_all_frames.h5', 'w') as f:
    dset = f.create_dataset("feature", data=features)

