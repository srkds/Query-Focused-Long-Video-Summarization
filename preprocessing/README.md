> Data Preprocessing We preprocess the videos in queryfocused video summarization dataset as follow. To get the shot features, we sample the video to 1 fps, then reshape the size of all frames to 224×224. Next, we extract visual representation of each frame with the pretrained ResNet (Szegedy et al. 2017) which is pretrained on ImageNet (Deng et al. 2009), and taking the 2048-dimensional vector for each frame. Similar to the setting in (Sharghi, Laurel, and Gong 2017), we take 5 seconds as a shot and compute the average of each frame from a shot as its shot-level feature.

Preprocessing Steps:

1. [extract frames](extract_images.py) from video
2. [extract features](get_CLIP_features.py) from any pretrain model and save it
3. to [create shot feature](Create_shot_features.py) take average of five frames in sequence.
