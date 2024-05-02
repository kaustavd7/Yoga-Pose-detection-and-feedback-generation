# Pose Detection And Feedback Generation For Different Yoga Asanas

## About the project

- We have created a comprehensive classification framework for yoga poses, with the goal of accurately identifying the specific posture being demonstrated by the participant in a given video recording.
- Develop a structured feedback mechanism for evaluating yoga pose videos, focusing on aligning them with the standards of an ideal yoga demonstration.

## Table of Contents
- [Dataset and Feature Extraction](##dataset)
- [Installation](#installation)
- [Usage](#usage)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

### Dataset and Feature Extraction

- Download yoga videos of 6 asanas from [Yoga-data](https://archive.org/details/YogaVidCollected) and extract feature by running the file "json_data_extractor_skip9".
- Or you can download the feature already extracted in JSON format from the dataset above.

- Clone the git repository

Once the repository is cloned, open the Yoga_Classification folder

#### **Yoga Classification**
 - Begin by executing the preproc-seq.ipynb script. This will generate six .npy files denoted as "trainX", "testX", "valX", "trainY", "testY", and "valY".
 - Proceed with the [CNN-LSTM-model.ipynb](Yoga_Classification/CNN-LSTM-model.ipynb) script. This step involves generating and evaluating the model weights using the test data.
 - Lastly, execute the [predict-continuous-FINAL.ipynb](Yoga_Classification/predict-continous-FINAL.ipynb) script. This enables the prediction of yoga asanas for any given video.

Onto, the second part of our project, open the Feedback-Generation folder.

#### Feedback Generation 
 - Run the [Find_best_intermediate.ipynb](Feedback-Generation/Find_best_intermediate.ipynb) file, just edit the folder path of the ideal yoga pose(available in the dataset above) test video and input_word of the yoga pose the test video is performing wherever required.

### Result and Presentations

Screen recorded video of execution of our code and presentation uploaded above.

   
