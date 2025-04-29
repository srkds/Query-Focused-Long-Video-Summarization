import numpy as np
import h5py
import math

f = h5py.File("P04_all_frames.h5", "r") # features of all individual frames/images


shot_features = []

# total features
total_features = f['feature'].shape[0] # (no of samples, 1, feature vector)

end = total_features - (total_features%5)

step = 5
for shot_no in range(0, end+1, step):
    print(f"shot no: {shot_no}")
    current_shot_feature = []
    if shot_no+5 > total_features:
        for frame_no in range(shot_no, total_features):
            print("frame: ", frame_no)
            current_shot_feature.append(f['feature'][frame_no][0])
    else:
        for frame_no in range(shot_no, shot_no+5):
            # print("frame: ", frame_no)
            current_shot_feature.append(f['feature'][frame_no][0])
    shot_features.append(np.mean(current_shot_feature, axis=0))
    # if(shot_no > 100):
    #     break


feat = np.array(shot_features)
# feat.shape

# Saving Shot features to h5py file
with h5py.File('P04_CLIP_SHOT_FEATURES.h5', 'w') as f:
    dset = f.create_dataset("feature", data=feat)