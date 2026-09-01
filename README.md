# Python PDF Creator

Convert HTML chapters into PDF files with WeasyPrint.

## Project layout

```text
PDF Creator/
├── code.py          # PDF conversion script
├── html/            # Put HTML chapter files and shared CSS here
├── common.css       # Shared styles used by chapters
├── pdfs/            # Generated PDF files appear here
└── README.md
```

The folders are created automatically by `code.py` if they do not already exist.

## File naming

`html/0.html` is the curriculum index. Each day has its own numbered HTML file. Each module also has a marker file named with the first day of that module:

```text
html/0.html           -> pdfs/0.pdf
html/1.html           -> pdfs/1.pdf
html/1. Module 1.html -> pdfs/1. Module 1.pdf
html/16. Module 2.html -> pdfs/16. Module 2.pdf
html/365.html         -> pdfs/365.pdf
html/310. Module 19.html -> pdfs/310. Module 19.pdf
```

Module names and markers reflect the 365-day engineering architecture:

| Marker file | Module name | Days |
| --- | --- | ---: |
| `Module 1.html` | Foundations, Tooling &amp; Terminal Mastery | 1-15 |
| `Module 2.html` | Client-Side Scripting, UI &amp; Extension Development | 16-23 |
| `Module 3.html` | Scripting Languages &amp; Enterprise Automation (Python &amp; C# Core) | 24-47 |
| `Module 4.html` | Code Quality, Static Analysis &amp; Architectural Patterns | 48-60 |
| `Module 5.html` | Relational Databases &amp; Storage Engines | 61-75 |
| `Module 6.html` | Web APIs, Protocols &amp; Enterprise Integration | 76-99 |
| `Module 7.html` | Microsoft Fabric &amp; Big Data Engineering | 100-120 |
| `Module 8.html` | Containers, Kubernetes, Messaging &amp; GitOps | 121-138 |
| `Module 9.html` | Enterprise Security, Authentication &amp; Cryptography | 139-150 |
| `Module 10.html` | Cloud Infrastructure, IaC &amp; Serverless Computing | 151-167 |
| `Module 11.html` | Artificial Intelligence, LLMs, Vector DBs &amp; Multi-Agent Systems | 168-191 |
| `Module 12.html` | Client UI (.NET MAUI &amp; Blazor) | 192-197 |
| `Module 13.html` | Core Data Structures &amp; Algorithms (DSA) | 198-219 |
| `Module 14.html` | Applied FAANG Execution &amp; LeetCode Hard Patterns | 220-229 |
| `Module 15.html` | Low-Level (LLD) &amp; High-Level System Design (HLD) | 230-249 |
| `Module 16.html` | Performance Profiling, Observability &amp; Compilers | 250-261 |
| `Module 17.html` | Advanced Systems Engineering, Kernels &amp; Storage Internals | 262-294 |
| `Module 18.html` | DevOps, Enterprise Operations &amp; Leadership | 295-309 |
| `Module 19.html` | Additional Engineering Projects &amp; The Mega Capstone | 310-365 |

The marker is placed at the first day of each module. All marker files and numbered day files are empty until content is added. Only files ending in `.html` inside the `html` folder are processed.

Module pages use the shared `html/common.css` stylesheet instead of duplicating their common CSS in every file.

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