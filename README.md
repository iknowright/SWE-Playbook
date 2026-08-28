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

`html/0.html` is the curriculum index. Each day has its own numbered HTML file. Each volume also has an empty lesson marker named with the first day after the volume:

```text
html/0.html          -> pdfs/0.pdf
html/1.html          -> pdfs/1.pdf
html/30.html         -> pdfs/30.pdf
html/31. Lesson 1.html -> pdfs/31. Lesson 1.pdf
html/365.html        -> pdfs/365.pdf
html/366. Lesson 12.html -> pdfs/366. Lesson 12.pdf
```

Lesson names and markers:

| Marker file | Lesson name | Days |
| --- | --- | ---: |
| `31. Lesson 1.html` | Silicon, Machine Architecture &amp; Low-Level Math | 1-30 |
| `61. Lesson 2.html` | Data Structures, Memory Layouts &amp; Cache Alignment | 31-60 |
| `91. Lesson 3.html` | Algorithmic Mastery, SDE Sheet Patterns &amp; Optimization | 61-90 |
| `121. Lesson 4.html` | Dynamic Programming, Graph Theory &amp; Backtracking | 91-120 |
| `151. Lesson 5.html` | Operating Systems, Kernel Internals &amp; Memory Architecture | 121-150 |
| `181. Lesson 6.html` | I/O Models, POSIX, Assembly &amp; Binary Exploitation | 151-180 |
| `211. Lesson 7.html` | Multithreading, Lock-Free Concurrency &amp; Memory Models | 181-210 |
| `241. Lesson 8.html` | Asynchronous Engines, Network Protocols &amp; Sockets | 211-240 |
| `271. Lesson 9.html` | Web Protocols, Application Security &amp; Framework Internals | 241-270 |
| `301. Lesson 10.html` | Database Internals, Storage Engines &amp; Query Optimization | 271-300 |
| `336. Lesson 11.html` | Distributed Systems, Consensus, Cloud Native &amp; Data Engineering | 301-335 |
| `366. Lesson 12.html` | High-Scale System Design, Production Triage &amp; Staff+ Leadership | 336-365 |

The marker is placed after the preceding numbered day when sorted, so `31. Lesson 1.html` is the lesson marker between days 30 and 31. All lesson markers and numbered day files are empty until content is added. Only files ending in `.html` inside the `html` folder are processed.

Lesson pages use the shared `html/common.css` stylesheet instead of
duplicating their common CSS in every file.

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