# watermark.py

This script adds a watermark to a PDF file using the `pypdf` library.

## What it does

The program reads a watermark PDF from `sources/wtr.pdf` and overlays it onto every page of the selected PDF.

It then saves the result in the `output/` folder.

## Files expected by the program

- `sources/wtr.pdf` - the watermark image/PDF to place on each page
- `output/` - folder where the new watermarked PDF is saved

## Requirements

Install the dependency:

```bash
pip install pypdf
```

## Usage

Run the script with an input PDF:

```bash
python3 watermark.py your_file.pdf
```

This will create an output file named `output.pdf` in the `output/` folder.

You can also choose your own output filename:

```bash
python3 watermark.py your_file.pdf my_output.pdf
```

## Demo mode

There is a built-in demo mode that uses the sample file `sources/twopage.pdf`:

```bash
python3 watermark.py demo
```

This creates a file called `demo_output.pdf` in the `output/` folder.

You can also specify a custom demo output name:

```bash
python3 watermark.py demo custom_demo.pdf
```

## How it works

1. The script checks the command-line arguments.
2. It chooses either the demo PDF or the PDF you passed in.
3. It opens the watermark from `sources/wtr.pdf`.
4. It loops through each page in the input PDF.
5. It overlays the watermark on each page.
6. It saves the result to `output/`.

## Example

```bash
python3 watermark.py demo
python3 watermark.py report.pdf final_report.pdf
```

After running, your watermarked PDFs will be available in the `output/` folder.