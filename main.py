import PyPDF2
def merge_pdfs(pdffiles, output_filename):
    merger = PyPDF2.PdfMerger()

    for filename in pdfiles:
        try:
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            merger. append (pdfReader)
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
        except PyPDF2.PdfReaderError as e:
            print(f"Error reading PDF: {filename} - {e}")
        finally:
            if pdfFile:  # Close the file only if it was successfully opened
                pdfFile.close()

    try:
        merger.write('merged.pdf')
        print(f"PDFs successfully merged into: {output_filename}")
    except PyPDF2.PdfWriterError as e:
        print(f"Error writing merged PDF: {e}")

# Example usage
pdfiles = ["Sample1.pdf", "Sample2.pdf"]  # Include a non-existent file
output_filename = 'merged.pdf'

merge_pdfs(pdfiles, output_filename)