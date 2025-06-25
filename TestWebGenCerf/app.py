import os
from flask import Flask, render_template, request, send_file, send_from_directory, url_for
from werkzeug.utils import secure_filename
from utils.certificate_utils import (
    load_data, 
    create_certificate, 
    sanitize_filename,
    create_zip_from_pdfs
)

app = Flask(__name__)

# ตั้งค่าโฟลเดอร์
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ================== 🌐 Routes ==================

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("error.html", error_message="❌ ไม่มีไฟล์ที่อัปโหลด"), 400

        file = request.files["file"]
        if file.filename == "":
            return render_template("error.html", error_message="❌ กรุณาเลือกไฟล์"), 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        try:
            df = load_data(file_path)
        except Exception as e:
            error_msg = f"❌ ไม่สามารถโหลดไฟล์ได้: {e}"
            return render_template("error.html", error_message=error_msg), 400

        if "Name" not in df.columns or "ID" not in df.columns:
            return render_template("error.html", error_message="❌ ไม่พบคอลัมน์ 'Name' หรือ 'ID' ในไฟล์"), 400

        previews = []
        for _, row in df.iterrows():
            name = str(row["Name"]).strip()
            ID = str(row["ID"]).strip()
            safe_name = sanitize_filename(name)
            output_path = os.path.join(OUTPUT_FOLDER, f"{safe_name}_certificate.pdf")
            
            print(f"ID : {ID}")

            create_certificate(output_path, name, ID)

            previews.append({
                "name": name,
                "ID": ID,
                "pdf": os.path.basename(output_path)
            })

        pdf_paths = [os.path.join(OUTPUT_FOLDER, p["pdf"]) for p in previews]
        zip_filename = create_zip_from_pdfs(pdf_paths)

        return render_template("result.html", previews=previews, zip_filename=zip_filename)

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    """ดาวน์โหลดไฟล์ PDF เป็นไฟล์แนบ"""
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

@app.route("/output/<filename>")
def serve_pdf(filename):
    """แสดง PDF ใน iframe"""
    return send_from_directory(OUTPUT_FOLDER, filename, mimetype='application/pdf')

@app.route("/download_all/<filename>")
def download_all(filename):
    """ดาวน์โหลดไฟล์ ZIP รวมทุก PDF"""
    zip_path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(zip_path, as_attachment=True)

# ================== 🚀 Run App ==================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
