# Handwritten Character Recognition with Transfer Learning

This project demonstrates a handwritten character recognition system using transfer learning with the VGG19 model and image augmentation techniques. The model's performance was further optimized with hyperparameter tuning to achieve a final accuracy of 91% from a baseline of 68%.

## Project Overview

The goal of this project is to build an accurate model for recognizing handwritten characters by leveraging pre-trained deep learning architectures and enhancing the model through data augmentation and hyperparameter tuning.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Dataset Source](#dataset-source)
- [Results](#results)
- [Kaggle Notebook](#kaggle-notebook)

## Project Description

The project began with a custom neural network model for handwritten character recognition, achieving an initial accuracy of 68%. By generating more images using image augmentation, accuracy was improved. Further optimization was achieved using the VGG19 pre-trained model for transfer learning, resulting in an accuracy of 85%. Finally, hyperparameter tuning with Keras Tuner was used to enhance the model’s performance to a final accuracy of 91%.

## Features

- **Custom Model Development**: Initial model architecture with 68% accuracy.
- **Image Augmentation**: Techniques applied to generate new training images and improve model generalization.
- **Transfer Learning**: Utilized VGG19 pre-trained model to boost accuracy to 85%.
- **Hyperparameter Tuning**: Optimized model parameters using Keras Tuner to achieve 91% accuracy.

## Dataset Source

The dataset used for this project is sourced from Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/sujaymann/handwritten-english-characters-and-digits). Image Augmentation was used on [this dataset](https://www.kaggle.com/datasets/dhruvildave/english-handwritten-characters-dataset) to generate new images. The dataset includes a variety of handwritten characters that were used to train and evaluate the model.
(Please feel free to upvote the dataset).

## Results

- **Initial Custom Model Accuracy**: 68%
- **Accuracy After Image Augmentation**: 72%
- **VGG19 Transfer Learning Accuracy**: 85%
- **Final Model Accuracy After Hyperparameter Tuning**: 91%

## Kaggle Notebook

You can view and run the project notebook on Kaggle: [Handwritten Character Recognition](https://www.kaggle.com/code/sujaymann/handwritten-character-classification-2)
