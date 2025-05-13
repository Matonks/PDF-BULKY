from flask import Flask, render_template, request, redirect
import os
import subprocess
import pandas as pd
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, BooleanObject

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
GENERATED_FOLDER = 'generated'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files.get('pdf')
    excel_file = request.files.get('excel')

    # Save uploaded PDF
    if pdf_file:
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
        pdf_file.save(pdf_path)

        # Print available field names
        reader = PdfReader(pdf_path)
        print("📄 PDF Form Fields:")
        for name in (reader.get_fields() or {}).keys():
            print(" -", name)

    # Process Excel and generate filled PDFs
    if excel_file:
        excel_path = os.path.join(UPLOAD_FOLDER, excel_file.filename)
        excel_file.save(excel_path)
        df = pd.read_excel(excel_path)

        for idx, row in df.iterrows():
            # Build a string-only dict of values
            data = {k: str(v) for k, v in row.items() if pd.notnull(v)}
            print(f"\n👉 Row {idx+1} data:", data)

            # 1) Fill PDF with pypdf into a raw file
            reader = PdfReader(pdf_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # Copy AcroForm and set NeedAppearances
            if "/AcroForm" in reader.trailer["/Root"]:
                ac = reader.trailer["/Root"]["/AcroForm"]
                ac.update({NameObject("/NeedAppearances"): BooleanObject(True)})
                writer._root_object.update({NameObject("/AcroForm"): ac})

            writer.update_page_form_field_values(writer.pages[0], data)

            raw_name = f"raw_filled_{idx+1}.pdf"
            raw_path = os.path.join(GENERATED_FOLDER, raw_name)
            with open(raw_path, "wb") as f:
                writer.write(f)
            print("  • raw saved:", raw_name)

            # 2) Flatten via Ghostscript
            final_name = f"filled_{idx+1}.pdf"
            final_path = os.path.join(GENERATED_FOLDER, final_name)
            subprocess.run([
                "gs",
                "-dSAFER", "-dBATCH", "-dNOPAUSE",
                "-sDEVICE=pdfwrite",
                f"-sOutputFile={final_path}",
                raw_path
            ], check=True)
            print("  • flattened:", final_name)

            # Remove raw file
            os.remove(raw_path)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
