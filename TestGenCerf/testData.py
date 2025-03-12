import os
import pandas as pd
import mimetypes
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# ตรวจสอบและสร้างโฟลเดอร์ output
os.makedirs("output", exist_ok=True)

# ลงทะเบียนฟอนต์ใหม่
font_path = "fonts/DancingScript-VariableFont_wght.ttf"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont("DancingScript", font_path))
    font_name = "DancingScript"
else:
    print("⚠ ฟอนต์ไม่พบ ใช้ Helvetica แทน")
    font_name = "Helvetica"

def create_certificate(output_path, name, course):
    pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    # ตรวจสอบภาพพื้นหลัง
    background = "images/test_certificate.png"
    if os.path.exists(background):
        pdf.drawImage(background, 0, 0, width=width, height=height)
    else:
        print("⚠ ไม่พบภาพพื้นหลัง เกียรติบัตรจะไม่มีภาพพื้นหลัง")

    # ใช้ฟอนต์ที่กำหนดเอง
    pdf.setFont(font_name, 56)


    pdf.setFillColorRGB(0.1, 0.1, 0.1)  # ตัวอักษรสีขาว
    pdf.drawCentredString(width / 2, height / 2 - 15, name)

    # เพิ่มรายละเอียดหลักสูตร
    pdf.setFont(font_name, 26)
    

    pdf.setFillColorRGB(0.1, 0.1, 0.1)  # ตัวอักษรสีขาว
    pdf.drawCentredString(width / 2, height / 2 + 60, f"Course: {course}")

    # บันทึกไฟล์ PDF
    pdf.save()
    print(f"✅ เกียรติบัตรสร้างสำเร็จ: {output_path}")

# ฟังก์ชันโหลดข้อมูลจากไฟล์ Excel หรือ CSV
def load_data(file_path):
    _, file_extension = os.path.splitext(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)

    if file_extension.lower() == ".xlsx" and mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return pd.read_excel(file_path, engine="openpyxl")
    elif file_extension.lower() == ".csv":
        return pd.read_csv(file_path, encoding="utf-8-sig")
    else:
        raise ValueError("❌ ไฟล์ที่ระบุไม่ใช่ไฟล์ .xlsx หรือ .csv กรุณาตรวจสอบอีกครั้ง!")

# ตั้งค่าไฟล์ที่ต้องการใช้
file_path = "data/testXlsx.xlsx"  # หรือใช้ "data/certificate_data.csv"

# โหลดข้อมูลจากไฟล์
try:
    df = load_data(file_path)
except Exception as e:
    print(f"❌ ไม่สามารถโหลดข้อมูลจากไฟล์ได้: {e}")
    exit(1)

# ตรวจสอบว่ามีข้อมูลหรือไม่
if df.empty:
    print("❌ ไม่มีข้อมูลในไฟล์ กรุณาตรวจสอบไฟล์ที่ใช้งาน")
else:
    # วนลูปสร้างเกียรติบัตรสำหรับแต่ละแถว
    for index, row in df.iterrows():
        name = str(row["Name"]).strip()
        course = str(row["Course"]).strip()
        output_path = f"output/{name}_certificate.pdf"
        create_certificate(output_path, name, course)
