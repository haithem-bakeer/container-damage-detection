Advanced Programming Project Proposal
Container Damage Detection Using YOLOv8
Project Information
•	Project Title: Container Damage Detection Using YOLOv8
•	Student: [ Haitham Abdel-Adim Bakeer ]
•	Supervisor: Dr. [Youssef O. Gdura]
•	Date: [30/05/2026]
________________________________________
1. Introduction
Container inspection is a critical process in ports, logistics centers, and transportation industries. Traditional inspection methods rely heavily on human operators, which can be time-consuming, costly, and prone to errors. Recent advances in Artificial Intelligence and Computer Vision have enabled the development of automated inspection systems capable of detecting defects with high accuracy.
This project proposes the development of an intelligent container damage detection system using the YOLOv8 object detection model. The system will automatically identify and classify different types of container damage from images in real time.
________________________________________
2. Project Objectives
The main objectives of this project are:
1.	To develop an automated system for detecting container damages, including:
o	Scratches
o	Dents
o	Rust
o	Cracks
2.	To implement the YOLOv8 deep learning model for real-time object detection.
3.	To train and evaluate the model using a publicly available container damage dataset.
4.	To export the trained model into ONNX format for deployment on surveillance camera systems and edge devices.
5.	To compare the performance of YOLOv8 with the YOLO-NAS model presented in the original research study.
________________________________________

3. Dataset Description
The dataset used in this project is obtained from Roboflow Universe.
Dataset Details
•	Source: Roboflow Universe (thanh-fscay/container-damage-hmv17)
•	Total Images: 4,736 images
Damage Categories
Damage Type	Percentage
Dents	40%
Scratches	30%
Rust	20%
Cracks	10%
Dataset Split
Dataset Portion	Percentage
Training Set	70%
Validation Set	15%
Test Set	15%
________________________________________
4. Tools and Technologies
Tool/Technology	Purpose
Python 3.10	Programming Language
YOLOv8	Damage Detection Model
Ultralytics	YOLOv8 Framework
Roboflow	Dataset Management
ONNX	Model Export and Deployment
Google Colab	Training Environment
________________________________________
5. Methodology
The project will be conducted according to the following steps:
1.	Download and preprocess the dataset.
2.	Configure and train the YOLOv8 model.
3.	Evaluate model performance using standard object detection metrics.
4.	Optimize the model for deployment.
5.	Export the trained model to ONNX format.
6.	Test the model on surveillance camera footage.
7.	Compare the obtained results with those reported for YOLO-NAS.
________________________________________
6. Expected Results
The expected performance metrics are as follows:
Metric	Expected Value
mAP50	85–90%
Precision	85–90%
Recall	80–85%
The system is expected to provide accurate real-time detection of container damages while maintaining low computational requirements suitable for practical deployment.
________________________________________
7. Project Structure
container-damage-detection/
│
├── README.md                 # Project documentation
├── PROPOSAL.md               # Project proposal
├── requirements.txt          # Required libraries
│
├── src/
│   ├── download_data.py      # Dataset download script
│   ├── train.py              # Model training
│   ├── test.py               # Model evaluation
│   └── export.py             # ONNX export
│
├── notebooks/
│   └── training.ipynb        # Training notebook
│
└── models/                   # Trained models
________________________________________
8. Project Timeline
Week	Task
Week 1	Environment setup and code development
Week 2	Model training and optimization
Week 3	Model export and camera testing
Week 4	Final report writing and project documentation
________________________________________
9. Conclusion
This project aims to develop an intelligent container damage detection system using YOLOv8 for automated inspection in logistics and port environments. The proposed solution will improve inspection efficiency, reduce human effort, and provide accurate real-time damage detection. Furthermore, the project will explore the deployment of AI models on edge devices through ONNX conversion and compare the results with state-of-the-art approaches such as YOLO-NAS.

