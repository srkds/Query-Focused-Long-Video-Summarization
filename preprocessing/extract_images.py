import imageio
import os

n = 1
def extract_frames(input_video, output_folder, frame_rate=1):
    # Create the output folder if it doesn't exist
    global n
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    vid = imageio.get_reader(input_video, 'ffmpeg')

    # Get video metadata
    fps = vid.get_meta_data()['fps']

    # Calculate the frame interval for the desired frame rate
    frame_interval = int(round(fps / frame_rate))

    # Extract frames and save them to the output folder
    for i, frame in enumerate(vid):
        if i % frame_interval == 0:
            imageio.imwrite(os.path.join(output_folder, f'frame_{n}.png'), frame)
            n += 1

    print(f"Frames extracted successfully to {output_folder}")

# Example usage
# input_video = 'clip_1.mp4'  # Replace with your input video file
output_folder = '../video_clips/P04/P04_frames'  # Replace with your desired output folder

# extract_frames(input_video, output_folder, frame_rate=1)


input_video = f'../video_clips/P04.mp4'
extract_frames(input_video, output_folder, frame_rate=1)

