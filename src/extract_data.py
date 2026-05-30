import gdown
import zipfile
import os

# رابط الملف المباشر بعد تعديل الصلاحية
# ملاحظة: الكود سيستخدم FILE_ID المستخرج من الرابط مباشرة
url = "https://drive.google.com/file/d/1unXG-YmVGI0xensQKWd7-R_eSZ3fTSXw/view?usp=drive_link"

# استخراج FILE_ID من الرابط
FILE_ID = url.split('/d/')[1].split('/')[0]
print(f"📁 معرّف الملف المستخرج: {FILE_ID}")

print("="*50)
print("📥 جاري تحميل مجموعة البيانات...")
print("="*50)

# تحميل الملف باستخدام gdown
gdown.download(f"https://drive.google.com/uc?id={FILE_ID}", "dataset.zip", quiet=False)

# التحقق من نجاح التحميل
if os.path.exists("dataset.zip"):
    size = os.path.getsize("dataset.zip")
    print(f"\n✅ تم تحميل الملف! الحجم: {size/1024/1024:.2f} MB")
    
    # فك الضغط
    print("\n📦 جاري فك ضغط الملف...")
    with zipfile.ZipFile("dataset.zip", 'r') as zip_ref:
        zip_ref.extractall("dataset")
    
    print("✅ تم فك الضغط بنجاح!")
    
    # عرض محتويات المجلد
    print("\n📁 محتويات المجلد المستخرج:")
    !ls -la dataset/
    
    # البحث عن ملف data.yaml
    print("\n🔍 البحث عن data.yaml:")
    !find dataset -name "data.yaml" 2>/dev/null
    
else:
    print("❌ فشل التحميل. تأكد من إعدادات المشاركة (Anyone with the link)")
