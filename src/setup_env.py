# ============================================
# setup_env.py
# تهيئة البيئة والتحقق من GPU
# استخدام: python src/setup_env.py
# ============================================

import torch
import sys

def check_environment():
    """التحقق من البيئة وإظهار المعلومات"""
    print("="*50)
    print("📊 معلومات بيئة العمل")
    print("="*50)
    print(f"Python version: {sys.version}")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    
    if torch.cuda.is_available():
        print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
        print(f"✅ GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    else:
        print("❌ GPU غير متاح - تأكد من اختيار T4 GPU في Runtime settings")
    
    print("="*50)
    return torch.cuda.is_available()

def install_yolov8():
    """تثبيت YOLOv8"""
    print("\n🚀 تثبيت YOLOv8...")
    import subprocess
    subprocess.run(["pip", "install", "ultralytics", "-q"])
    print("✅ تم التثبيت!")

def test_yolov8():
    """اختبار YOLOv8"""
    print("\n🔄 اختبار YOLOv8...")
    from ultralytics import YOLO
    model = YOLO('yolov8n.pt')
    results = model('https://ultralytics.com/images/bus.jpg')
    print("✅ YOLOv8 يعمل بنجاح!")
    return model

if __name__ == "__main__":
    print("🚀 بدء تهيئة البيئة...\n")
    
    # 1. التحقق من البيئة
    cuda_available = check_environment()
    
    if not cuda_available:
        print("\n⚠️ يرجى تفعيل GPU من: Runtime → Change runtime type → T4 GPU")
    else:
        # 2. تثبيت YOLOv8
        install_yolov8()
        
        # 3. اختبار YOLOv8
        test_yolov8()
        
        print("\n✅✅✅ البيئة جاهزة تماماً! ✅✅✅")
