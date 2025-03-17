import os
import pandas as pd
import re
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

app = Flask(__name__)

# ตั้งค่าโฟลเดอร์
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ลงทะเบียนฟอนต์
font_path = "static/fonts/DancingScript-VariableFont_wght.ttf"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont("DancingScript-VariableFont_wght", font_path))
    font_name = "DancingScript-VariableFont_wght"
else:
    font_name = "Helvetica"

# ฟังก์ชันสร้าง PDF ใบเกียรติบัตร
def create_certificate(output_path, name, course):
    pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    # ตรวจสอบภาพพื้นหลัง
    background = "static/images/certificate_bg.png"
    if os.path.exists(background):
        pdf.drawImage(background, 0, 0, width=width, height=height)

    # ใช้ฟอนต์ที่กำหนดเอง
    pdf.setFont(font_name, 56)
    pdf.setFillColorRGB(0.1, 0.1, 0.1)  # สีดำ
    pdf.drawCentredString(width / 2, height / 2 - 15, name)

    # เพิ่มรายละเอียดหลักสูตร
    pdf.setFont(font_name, 26)
    pdf.drawCentredString(width / 2, height / 2 + 60, f"Course: {course}")

    # บันทึกไฟล์ PDF
    pdf.save()
    print(f"✅ เกียรติบัตรสร้างสำเร็จ: {output_path}")

# ฟังก์ชันอ่านไฟล์ CSV หรือ Excel
def load_data(file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == ".csv":
        return pd.read_csv(file_path, encoding="utf-8-sig")
    elif file_extension.lower() == ".xlsx":
        return pd.read_excel(file_path, engine="openpyxl")
    else:
        raise ValueError("❌ รองรับเฉพาะไฟล์ .csv และ .xlsx เท่านั้น")

# ฟังก์ชันล้างชื่อไฟล์ให้ปลอดภัย
def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name)

# เส้นทางหน้าเว็บหลัก
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "❌ ไม่มีไฟล์ที่อัปโหลด", 400

        file = request.files["file"]
        if file.filename == "":
            return "❌ กรุณาเลือกไฟล์", 400

        # บันทึกไฟล์ที่อัปโหลด
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # โหลดข้อมูลจากไฟล์
        try:
            df = load_data(file_path)
        except Exception as e:
            return f"❌ ไม่สามารถโหลดไฟล์ได้: {e}", 400

        # ตรวจสอบว่ามีคอลัมน์ Name และ Course หรือไม่
        if "Name" not in df.columns or "Course" not in df.columns:
            return f"❌ ไม่พบคอลัมน์ 'Name' หรือ 'Course' ในไฟล์", 400

        # วนลูปสร้างเกียรติบัตร
        output_files = []
        for index, row in df.iterrows():
            name = str(row["Name"]).strip()
            course = str(row["Course"]).strip()
            safe_name = sanitize_filename(name)
            output_path = os.path.join(OUTPUT_FOLDER, f"{safe_name}_certificate.pdf")

            create_certificate(output_path, name, course)
            output_files.append(output_path)

        return f"✅ สร้างใบเกียรติบัตรสำเร็จ {len(output_files)} ใบ"

    return render_template("index.html")

# รันเว็บแอป
if __name__ == "__main__":
    app.run(debug=True)
