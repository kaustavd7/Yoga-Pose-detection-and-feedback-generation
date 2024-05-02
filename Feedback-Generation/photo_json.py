import cv2
import mediapipe as mp
import json
import mediapipe.python.solutions.pose as mp_pose

image=cv2.imread("/home/nishita/UGP_Nishita/Feedback generation/Correct_intermediate_poses/Dhanuarasana/Dhanuarasana_intermediate_1.png")

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.5
)
# detecting_pose=return_detect_landmarks(image)
# detecting_pose_landmark=detecting_pose.landmark
pose_data = []

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
            
# Open a file for writing
with open('my_list.json', 'w') as f:
    # Use json.dump to write the list to the file
    json.dump(pose_data, f)            
# print(pose_data) 