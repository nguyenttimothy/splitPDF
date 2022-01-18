import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'PayoffDocument.pdf'
file_base_name = pdf_file_path.replace('.pdf', '')
output_folder_path = os.path.join(os.getcwd(), 'Output')

pdf = PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(page_num))

    with open(os.path.join(output_folder_path, '{0}_Page{1}.pdf'.format(file_base_name, page_num+1)), 'wb') as f:
        pdf_writer.write(f)
        f.close()


