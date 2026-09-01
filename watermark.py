import sys
import os

from pypdf import PdfReader, PdfWriter

if len(sys.argv) < 2:
    print("Usage: python3 watermark.py [demo|input.pdf] [output.pdf]")
    sys.exit(1)

mode = sys.argv[1]

if mode == "demo":
    input_pdf = "sources/demo_input.pdf"
    output_name = sys.argv[2] if len(sys.argv) > 2 else "demo_output.pdf"
else:
    input_pdf = mode
    output_name = sys.argv[2] if len(sys.argv) > 2 else "output.pdf"

if not os.path.exists("output/"):
    os.makedirs("output/")

if not os.path.exists(input_pdf):
    print(f"File not found: {input_pdf}")
    sys.exit(1)

watermark = PdfReader("sources/wtr.pdf").pages[0]
writer = PdfWriter(clone_from=input_pdf)

for page in writer.pages:
    page.merge_page(watermark, over=False)  # False = watermark, True = stamp

writer.write(f"output/{output_name}")
