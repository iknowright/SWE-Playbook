import argparse
from pathlib import Path
from weasyprint import HTML


BASE_DIR = Path(__file__).resolve().parent
HTML_DIR = BASE_DIR / "html"
PDF_DIR = BASE_DIR / "pdfs"

HTML_DIR.mkdir(exist_ok=True)
PDF_DIR.mkdir(exist_ok=True)

parser = argparse.ArgumentParser(description="Convert HTML chapters into PDFs.")
parser.add_argument(
	"html_file",
	nargs="?",
	help="One HTML filename to convert, such as 17 or 17.html. Omit for all files.",
)
args = parser.parse_args()

if args.html_file:
	requested_name = args.html_file
	if not requested_name.endswith(".html"):
		requested_name += ".html"
	html_files = [HTML_DIR / requested_name]
else:
	html_files = sorted(HTML_DIR.glob("*.html"))

if not html_files:
	print(f"No HTML files found in: {HTML_DIR}")
else:
	for html_file in html_files:
		if not html_file.exists():
			print(f"HTML file not found: {html_file.name}")
			continue
		pdf_file = PDF_DIR / f"{html_file.stem}.pdf"
		if not html_file.read_text(encoding="utf-8").strip():
			# print(f"Skipped (empty HTML): {html_file.name}")
			continue
		if pdf_file.exists():
			# print(f"Skipped (already exists): {pdf_file.name}")
			continue
		HTML(filename=str(html_file), base_url=str(HTML_DIR)).write_pdf(str(pdf_file))
		print(f"Created: {pdf_file.name}")