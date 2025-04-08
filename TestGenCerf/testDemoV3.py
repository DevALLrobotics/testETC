import os
import pandas as pd
import mimetypes
import re
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path


# --- สร้างโฟลเดอร์ output ---
os.makedirs("output", exist_ok=True)

# --- ลงทะเบียนฟอนต์ ---
font_path = "fonts/DancingScript-VariableFont_wght.ttf"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont("DancingScript", font_path))
    font_name = "DancingScript"
else:
    print("⚠ ฟอนต์ไม่พบ ใช้ Helvetica แทน")
    font_name = "Helvetica"

# --- ปรับตำแหน่งข้อความด้วยตัวแปรเดียว ---
y_offset = 0 * mm  # ✅ ปรับค่าบรรทัดนี้เพื่อเลื่อนข้อความทั้งหมด ขึ้น(+)/ลง(-)

# --- เลือกไฟล์ข้อมูล ---
data_dir = "data"
data_files = [f for f in os.listdir(data_dir) if f.lower().endswith((".xlsx", ".csv"))]

if not data_files:
    print("❌ ไม่พบไฟล์ในโฟลเดอร์ data/")
    exit(1)

print("\n📋 เลือกไฟล์ข้อมูล:")
for i, f in enumerate(data_files, 1):
    print(f"{i}. {f}")
while True:
    try:
        data_choice = int(input("เลือกหมายเลขไฟล์ข้อมูล: "))
        if 1 <= data_choice <= len(data_files):
            file_path = os.path.join(data_dir, data_files[data_choice - 1])
            break
        else:
            print("❌ หมายเลขไม่ถูกต้อง")
    except:
        print("❌ กรุณาใส่ตัวเลข")

# --- เลือกพื้นหลัง ---
background_dir = "images"
bg_files = [f for f in os.listdir(background_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".pdf"))]

if not bg_files:
    print("❌ ไม่พบพื้นหลังในโฟลเดอร์ images/")
    exit(1)

print("\n🎨 เลือกพื้นหลัง:")
for i, f in enumerate(bg_files, 1):
    print(f"{i}. {f}")
while True:
    try:
        bg_choice = int(input("เลือกหมายเลขพื้นหลัง: "))
        if 1 <= bg_choice <= len(bg_files):
            selected_background = os.path.join(background_dir, bg_files[bg_choice - 1])
            break
        else:
            print("❌ หมายเลขไม่ถูกต้อง")
    except:
        print("❌ กรุณาใส่ตัวเลข")

is_pdf_bg = selected_background.lower().endswith(".pdf")

# --- ฟังก์ชันสร้างข้อความ overlay สำหรับ PDF background ---
def create_text_overlay(code, name, course):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = landscape(A4)

    # วาดกรอบหน้า A4

    # ลองวางข้อความตรงกลางแบบเห็นแน่ ๆ
    pdf.setFont("DancingScript", 20)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(400,700, code)
    pdf.drawString(100, height - 150, name)
    pdf.drawString(100, height - 200, course)

    pdf.save()
    buffer.seek(0)
    return buffer

# --- ฟังก์ชันสร้างเกียรติบัตร ---
def create_certificate(output_path, code, name, course, background, is_pdf):
    width, height = landscape(A4)

    if is_pdf:
        overlay = create_text_overlay(code, name, course)
        bg_reader = PdfReader(background)
        overlay_reader = PdfReader(overlay)
        writer = PdfWriter()
        bg_page = bg_reader.pages[0]
        overlay_page = overlay_reader.pages[0]
        bg_page.merge_page(overlay_page)
        writer.add_page(bg_page)
        with open(output_path, "wb") as f:
            writer.write(f)
    else:
        pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
        if os.path.exists(background):
            pdf.drawImage(background, 0, 0, width=width, height=height)

        pdf.setFont("Helvetica", 15)
        pdf.setFillColorRGB(0, 0, 0)
        pdf.drawRightString(width - 25 * mm, height - 10 * mm + y_offset, f"ID: {code}")

        pdf.setFont(font_name, 56)
        pdf.drawCentredString(width / 2, height / 2 - 15 + y_offset, name)

        pdf.setFont(font_name, 26)
        pdf.drawCentredString(width / 2 + 100, height / 2 + 60 + y_offset, f"Course: {course}")
        pdf.save()

    print(f"✅ สร้าง PDF: {output_path}")

# --- โหลดข้อมูล ---
def load_data(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".xlsx":
        return pd.read_excel(path, engine="openpyxl")
    elif ext == ".csv":
        return pd.read_csv(path, encoding="utf-8-sig")
    else:
        raise ValueError("❌ ต้องเป็น .xlsx หรือ .csv เท่านั้น")

# --- ประมวลผล ---
try:
    df = load_data(file_path)
except Exception as e:
    print(f"❌ โหลดไฟล์ไม่สำเร็จ: {e}")
    exit(1)

if df.empty:
    print("❌ ไม่มีข้อมูลในไฟล์")
    exit(1)

for _, row in df.iterrows():
    code = str(row["ID"]).strip()
    name = str(row["Name"]).strip()
    course = str(row["Course"]).strip()
    safe_name = re.sub(r'[\\/*?:"<>|]', "", name)
    output = f"output/{safe_name}_certificate.pdf"
    create_certificate(output, code, name, course, selected_background, is_pdf_bg)
