from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader

# ลงทะเบียนฟอนต์ใหม่ (เปลี่ยนเป็นฟอนต์ที่ต้องการ)
pdfmetrics.registerFont(TTFont("DancingScript-VariableFont_wght", "fonts/DancingScript-VariableFont_wght.ttf"))

def create_certificate(output_path, name, course):
    pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    # ใส่ภาพพื้นหลัง (เปลี่ยนเป็นไฟล์ของคุณ)
    background = "images/test_certificate.png"  # เปลี่ยนเป็นไฟล์ภาพของคุณ
    pdf.drawImage(background, 0, 0, width=width, height=height)

    # ใช้ฟอนต์ที่กำหนดเอง
    pdf.setFont("DancingScript-VariableFont_wght", 48)
    pdf.setFillColorRGB(0.1, 0.1, 0.1)  # สีดำ

    # วางชื่อกลางเกียรติบัตร
    pdf.drawCentredString(width / 2 , height / 2 - 15, name)

    # เพิ่มรายละเอียดหลักสูตร
    pdf.setFont("DancingScript-VariableFont_wght", 22)
    pdf.drawCentredString(width /2 + 130, height / 2 + 60, f"Course => {course}")

    # # ลายเซ็น (ถ้ามี)
    # signature = "signature.png"
    # pdf.drawImage(signature, width - 300, 50, width=200, height=50)

    # บันทึกไฟล์ PDF
    pdf.save()
    print(f"เกียรติบัตรสร้างสำเร็จ: {output_path}")

# ตัวอย่างการเรียกใช้ฟังก์ชัน
create_certificate("output/DemoCertificate.pdf", "Non Good ", "Basic : Python")
