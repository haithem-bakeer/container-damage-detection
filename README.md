# container-damage-detection .
Container damage detection using YOLOv8 .
📋 Overview :
This project aims to automate the detection of container damage (scratches, dents, rust, cracks) using the YOLOv8 model.
🛠️ Requirements
```bash
pip install -r requirements.txt
📥 Download data : python src/download_data.py
🏋️ Model Training : python src/train.py
🧪 Model testing : python src/test.py
📤 Export the model to the camera : python src/export.py
📊 Results : After the project is completed
👨‍💻 Author : Haitham Abdel-Adim Bakeer
## ⚠️ Challenges We Faced
### Data Compatibility Issue with YOLOv8
Upon starting the first training, we encountered a warning indicating the presence of Segmentation comments alongside Bounding Boxes in the dataset. This resulted in unsatisfactory results (mAP50 = 0.03).
**Solution:** The data was reloaded in Detection only format (`yolov8`) and `single_cls=True` was added to the training parameters.
For complete details, see the file [`CHALLENGES.md`](CHALLENGES.md).
