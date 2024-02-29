# TinyModels

TinyModels is a Python library for efficiently processing PDF files. It simplifies the process of parsing PDFs, extracting text, and handling large files by breaking them down into manageable chunks.

## Features

- Upload PDF files and parse them asynchronously.
- Break down large PDF files into smaller chunks for easier processing.
- Extract text from PDF files with a simple API call.

## Installation

Install TinyModels using pip:

```bash
pip install TinyModels


### Quick Start
Here's how to get started with TinyModels:

from TinyModels import pdfParser

# Create a pdfParser instance
parser = pdfParser()

# Get text from a PDF file
text = parser.getText('path/to/your/file.pdf')

print(text)

### License

TinyModels is released under the MIT License. See the LICENSE file for more details.
