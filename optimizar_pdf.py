import os
import subprocess

input_dir = "pdf"
output_dir = "build"
os.makedirs(output_dir, exist_ok=True)

def compress_pdf(input_path, output_path):
    command = [
        "C:\\Program Files\\gs\\gs10.05.0\\bin\\gswin64c.exe",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/printer",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        print(f"🔄 Comprimiendo: {filename}")
        compress_pdf(input_path, output_path)
        print(f"✅ Guardado en: {output_path}")

print("\n🎉 Compresión completa")
