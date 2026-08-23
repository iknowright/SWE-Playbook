# PDF Creator

Convert HTML chapters into PDF files with WeasyPrint.

## Project layout

```text
PDF Creator/
├── code.py          # PDF conversion script
├── html/            # Put HTML chapter files and shared CSS here
│   └── common.css   # Shared styles used by chapters
├── pdfs/            # Generated PDF files appear here
└── README.md
```

The folders are created automatically by `code.py` if they do not already exist.

## File naming

Use matching chapter names:

```text
html/0.html   -> pdfs/0.pdf
html/1.html   -> pdfs/1.pdf
html/25.html  -> pdfs/25.pdf
```

Only files ending in `.html` inside the `html` folder are processed.

Chapters use the shared `html/common.css` stylesheet instead of
duplicating their common CSS in every file. Phase-two title and answer-key
differences are scoped with the `phase-two` body class, and the unique
`synthesis-box` and capstone workspace components are defined in the shared
stylesheet.

## How to use

1. Put your HTML files in the `html` folder.
2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Run the converter:

   ```bash
   python code.py
   ```

   You can also run it without activating the environment:

   ```bash
   ./venv/bin/python code.py
   ```

   To convert only one HTML file, pass its name with or without `.html`:

   ```bash
   ./venv/bin/python code.py 17
   ./venv/bin/python code.py 17.html
   ```

4. Open the generated files in the `pdfs` folder.

## Customising a chapter

To customise a PDF:

1. Edit the matching HTML file in `html`.
2. Delete its existing PDF from `pdfs`.
3. Run the converter again.

For example:

```bash
rm pdfs/1.pdf
python code.py
```

The script will recreate `pdfs/1.pdf` using the updated `html/1.html`.

## Existing PDFs are skipped

If a matching PDF already exists, the script skips that chapter:

```text
Skipped (already exists): 1.pdf
```

This prevents unchanged chapters from being rendered again. With many chapters, this is considerably faster than overwriting every PDF because PDF rendering is the expensive part; checking whether a file exists is very quick.

To regenerate a chapter, delete its PDF first.

## Empty HTML files are skipped

HTML files that are empty or contain only whitespace are not converted to PDFs:

```text
Skipped (empty HTML): 2.html
```

## How the code works

`code.py`:

1. Finds the folder containing the script.
2. Creates the `html` and `pdfs` folders when needed.
3. Finds all `.html` files in `html`.
4. Skips empty HTML files.
5. Builds a PDF path using the HTML filename without its extension.
6. Skips the conversion when that PDF already exists.
7. Uses WeasyPrint to render missing PDFs into `pdfs`.

The script does not combine chapters into one PDF. Each HTML file becomes its own PDF file.

## Requirements

- Python 3
- WeasyPrint

The project already includes a virtual environment in `venv`. If setting up the project on another computer, install WeasyPrint with:

```bash
python -m pip install weasyprint
```