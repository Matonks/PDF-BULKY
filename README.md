````markdown
# 📝 PDF Form Filler

Welcome to the **PDF Form Filler**! Ever wished you could magically auto-fill a PDF form using data from an Excel sheet? Well, your wish is granted! 🎩✨

---

## 🔍 What’s Inside?

- A **slick, drag-and-drop UI** built with plain HTML/CSS/JS for seamless uploads and real-time progress feedback
- A **Flask** backend (`app.py`) that:
  1. Reads your PDF form template  
  2. Loads data from an Excel file via **pandas**  
  3. Fills each row into the PDF form with **pypdf**  
  4. Flattens the result using **Ghostscript** for a polished, non-editable PDF ✨

---

## 🚀 Features

- **Drag & Drop** uploads (PDF & Excel)  
- **Progress bar & processing overlay** so you know exactly how far along you are  
- **Auto-flattening** of filled PDFs to lock in those sweet, sweet changes  
- **Batch processing**: fill multiple forms in one go! 📑➡️📄

---

## 🔧 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourname/pdf-form-filler.git
   cd pdf-form-filler
````

2. **Install dependencies**
   Make sure you have Python 3.7+ and Ghostscript installed.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**

   ```bash
   python app.py
   ```

   Then head to `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```text
pdf-form-filler/
├── app.py              # Flask server & PDF/Excel magic 🐍
├── templates/
│   └── index.html      # User-facing drag-and-drop form UI 🎨
├── uploads/            # Temporary storage for uploads 📤
├── generated/          # Final filled (& flattened) PDFs 📥
├── requirements.txt    # Python deps (Flask, pandas, pypdf, etc.) 📦
└── README.md           # You’re looking at it! 😉
```

---

## 🎉 How to Use

1. Open the web page.
2. Drag your **PDF form template** into the first box.
3. Drag your **Excel data file** into the second box.
4. Click **Generate Forms** and watch the magic happen! 🪄
5. Peek into the `generated/` folder for your batch of filled PDFs.

---

## 🤝 Contributing

Bug reports, feature requests, or just want to say hi?

* Open an issue
* Submit a PR
* Share your emojis 🎈

---

## 📜 License

This project is licensed under the **MIT License** – because who doesn’t love open source? ❤️

---

> “Automate the boring stuff” – you, after using this tool. 😎

```
```
