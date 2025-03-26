import os
from flask import Flask, render_template, request, send_file, send_from_directory, url_for
from werkzeug.utils import secure_filename
from utils.certificate_utils import load_data, create_certificate, sanitize_filename

app = Flask(__name__)

# ตั้งค่าโฟลเดอร์
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
PREVIEW_FOLDER = os.path.join("static", "preview")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(PREVIEW_FOLDER, exist_ok=True)

# ================== 🌐 Routes ==================

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "❌ ไม่มีไฟล์ที่อัปโหลด", 400

        file = request.files["file"]
        if file.filename == "":
            return "❌ กรุณาเลือกไฟล์", 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        try:
            df = load_data(file_path)
        except Exception as e:
            return f"❌ ไม่สามารถโหลดไฟล์ได้: {e}", 400

        if "Name" not in df.columns or "Course" not in df.columns:
            return "❌ ไม่พบคอลัมน์ 'Name' หรือ 'Course' ในไฟล์", 400

        previews = []
        for _, row in df.iterrows():
            name = str(row["Name"]).strip()
            course = str(row["Course"]).strip()
            safe_name = sanitize_filename(name)
            output_path = os.path.join(OUTPUT_FOLDER, f"{safe_name}_certificate.pdf")

            create_certificate(output_path, name, course)

            previews.append({
                "name": name,
                "course": course,
                "pdf": os.path.basename(output_path)
            })

        return render_template("result.html", previews=previews)

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    """ดาวน์โหลด PDF เป็นไฟล์แนบ"""
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

@app.route("/output/<filename>")
def serve_pdf(filename):
    """แสดง PDF สำหรับ preview ใน iframe"""
    return send_from_directory(OUTPUT_FOLDER, filename, mimetype='application/pdf')

# ================== 🚀 Run App ==================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
