# Import modules
import mediapipe as mp
import cv2
import numpy as np
import json
import os

# Create a pose object
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.5
)

# Get the video files in the folder
folder = "/home/nishita/UGP_Nishita/Feedback generation/Test_videos/Dhanurasana"
video_files = [f for f in os.listdir(folder) if f.endswith(".mp4")]

# Loop through the video files
for video_file in video_files:
    # Create a video capture object
    cap = cv2.VideoCapture(os.path.join(folder, video_file))
    # Create an empty list to store the pose data
    pose_data = []
    # Loop through the frames
    while cap.isOpened():
        
        # cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 9)
        
        # Read a frame
        success, image = cap.read()
        # Check if the frame is valid
        if not success:
            break
        # Convert the image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Process the image with the pose object
        results = pose.process(image)
        # Check if pose landmarks are present
        if results.pose_landmarks:
            # Convert the pose landmarks to a list of dictionaries
            landmarks = results.pose_landmarks.landmark
            # xi = landmark.x
            # yi = landmark.y
             
            pose_dict = [
                (
                    landmark.x,
                    landmark.y
                )
                for i, landmark in enumerate(landmarks)
            ]
            # Append the pose dictionary to the pose data list
            pose_data.append(pose_dict)
    # Write the pose data to a JSON file
    json_file = video_file.split(".")[0] + ".json"
    with open(json_file, "w") as f:
        json.dump(pose_data, f, indent=4)
    # Release the video capture object
    cap.release()
    # Close all windows
    cv2.destroyAllWindows()
