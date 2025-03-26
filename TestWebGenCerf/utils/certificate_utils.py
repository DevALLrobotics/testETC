import os
import re
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# ===== ฟอนต์เริ่มต้น =====
font_path = "static/fonts/DancingScript-VariableFont_wght.ttf"
if os.path.exists(font_path):
    pdfmetrics.registerFont(TTFont("DancingScript-VariableFont_wght", font_path))
    font_name = "DancingScript-VariableFont_wght"
else:
    font_name = "Helvetica"

def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name)

def load_data(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == ".csv":
        return pd.read_csv(file_path, encoding="utf-8-sig")
    elif file_extension.lower() == ".xlsx":
        return pd.read_excel(file_path, engine="openpyxl")
    else:
        raise ValueError("❌ รองรับเฉพาะไฟล์ .csv และ .xlsx เท่านั้น")

def create_certificate(output_path, name, course):
    pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    background = "static/images/certificate_bg.png"
    if os.path.exists(background):
        pdf.drawImage(background, 0, 0, width=width, height=height)

    pdf.setFont(font_name, 56)
    pdf.setFillColorRGB(0.1, 0.1, 0.1)
    pdf.drawCentredString(width / 2, height / 2 - 15, name)

    pdf.setFont(font_name, 26)
    pdf.drawCentredString(width / 2 + 150, height / 2 + 60, f"Course: {course}")

    pdf.save()
    print(f"✅ สร้างใบเกียรติบัตร: {output_path}")
