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

`html/0.html` is the curriculum index. Each day has its own numbered HTML file. Each module also has a lesson marker named with the first day after the module:

```text
html/0.html                  -> pdfs/0.pdf
html/1.html                  -> pdfs/1.pdf
html/25.html                 -> pdfs/25.pdf
html/26. Module 2.html       -> pdfs/26. Module 2.pdf
html/365.html                -> pdfs/365.pdf
html/366. Module 20.html     -> pdfs/366. Module 20.pdf
```

Module names and markers reflect our updated 365-day engineering architecture:

| Marker file | Module name | Days |
| --- | --- | ---: |
| `13. Module 1.html` | Computing History &amp; Foundations | 1-12 |
| `26. Module 2.html` | Terminal, Version Control &amp; Collaboration | 13-25 |
| `31. Module 3.html` | Web Substrates (HTML, CSS, Tailwind &amp; JavaScript) | 26-30 |
| `59. Module 4.html` | C# Language Core &amp; Advanced Mechanics | 31-58 |
| `72. Module 5.html` | Clean Code, Complexity &amp; Static Analysis (Sonar Ecosystem) | 59-71 |
| `90. Module 6.html` | Python Full-Track (Beginner to Intermediate &amp; AI Libs) | 72-89 |
| `99. Module 7.html` | Design Patterns &amp; Clean Architecture | 90-98 |
| `115. Module 8.html` | Relational Databases &amp; Azure SQL Platform | 99-114 |
| `136. Module 9.html` | Web APIs, OData &amp; Kiota SDKs | 115-135 |
| `145. Module 10.html` | Microsoft Graph &amp; Enterprise Integration | 136-144 |
| `176. Module 11.html` | Microsoft Fabric &amp; Data Engineering | 145-175 |
| `189. Module 12.html` | Containers, Kubernetes, Service Mesh, GitOps &amp; Kafka | 176-188 |
| `202. Module 13.html` | Enterprise Security, OAuth2 &amp; Microsoft Entra ID | 189-201 |
| `219. Module 14.html` | Azure Compute, Serverless &amp; Cert Sandbox | 202-218 |
| `239. Module 15.html` | Multi-Agent AI Systems, Local LLMs, Vector DBs &amp; RAG | 219-238 |
| `266. Module 16.html` | Tier-1 Data Structures &amp; Algorithms (DSA) | 239-265 |
| `289. Module 17.html` | Low-Level (LLD) &amp; High-Level System Design (HLD) | 266-288 |
| `299. Module 18.html` | Client UI (.NET MAUI &amp; Blazor) | 289-298 |
| `309. Module 19.html` | Performance Profiling, Observability &amp; Compilers | 299-308 |
| `366. Module 20.html` | DevOps, IaC, Roslyn &amp; The Enterprise Mega Capstone | 309-365 |

The marker is placed after the preceding numbered day when sorted. All marker files and numbered day files are empty until content is added. Only files ending in `.html` inside the `html` folder are processed.

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