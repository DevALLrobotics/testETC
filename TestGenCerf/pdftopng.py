import os
from pdf2image import convert_from_path

# --- กำหนดไฟล์ PDF และโฟลเดอร์ปลายทาง ---
pdf_path = "../TestGenCerf/images/CERg.pdf"
output_dir = "../TestGenCerf/images"
os.makedirs(output_dir, exist_ok=True)

# --- แปลง PDF เป็น PNG ด้วยความละเอียดสูง ---
images = convert_from_path(pdf_path, dpi=600)  # 🔥 dpi 600 = ชัดระดับพิมพ์โปสเตอร์

for i, image in enumerate(images):
    output_path = os.path.join(output_dir, f"page_{i+1}_highres.png")
    image.save(output_path, "PNG")
    print(f"✅ บันทึก: {output_path}")
