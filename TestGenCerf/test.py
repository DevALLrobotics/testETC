from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# ฟังก์ชันสร้างเกียรติบัตร
def create_certificate(output_path, name, course):
    # ตั้งค่าหน้ากระดาษแนวนอน (A4)
    pdf = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)

    # เพิ่มพื้นหลัง (ใช้ไฟล์รูปภาพ)
    background = "../TestWebIQ/images/cover.png"  # เปลี่ยนเป็นไฟล์ภาพของคุณ
    pdf.drawImage(background, 0, 0, width=width, height=height)

    # กำหนดฟอนต์
    pdf.setFont("Helvetica-Bold", 40)
    pdf.setFillColorRGB(0.1, 0.1, 0.1)  # สีดำ

    # เพิ่มชื่อผู้รับรางวัล
    pdf.drawCentredString(width/10, height / 2, name)

    # เพิ่มข้อความรายละเอียด
    pdf.setFont("Helvetica", 24)
    pdf.drawCentredString(width / 2, height / 2 - 50, f"ได้รับการรับรองว่าได้ผ่าน {course}")

    # # ลายเซ็น (สามารถเพิ่มรูปภาพลายเซ็น)
    # signature = "signature.png"  # เปลี่ยนเป็นไฟล์ลายเซ็น
    # pdf.drawImage(signature, width - 300, 50, width=200, height=50)

    # บันทึกไฟล์
    pdf.save()
    print(f"เกียรติบัตรสร้างเสร็จแล้ว: {output_path}")

# ตัวอย่างการเรียกใช้งาน
create_certificate("certificate.pdf", "สมชาย ใจดี", "หลักสูตร Python ขั้นสูง")
