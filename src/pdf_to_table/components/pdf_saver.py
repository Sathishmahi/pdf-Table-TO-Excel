import os
import fitz
from pathlib import Path
from pdf_to_table import logging
from pdf_to_table.config import Configuration
from pdf_to_table.entity import PdfSaverConfig


class PdfTOImages:
    def __init__(self,configuration:Configuration = Configuration()):
        self.pdf_saver_config = configuration.get_pdf_saver_config()
        
    def pdf_images(self):
        file_path = self.pdf_saver_config.file_name
        images_dir_name = self.pdf_saver_config.images_dir_name
        pdf_document = fitz.open(file_path)
        # Iterate through each page in the PDF
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document.load_page(page_number)

            # Convert the page to a pixmap (image)
            pix = page.get_pixmap()

            # Save the pixmap as an image file (e.g., PNG)
            image_file_name = os.path.join(images_dir_name,f'page_{page_number + 1}.png')
            pix.save(image_file_name)

    



if __name__ == "__main__":
    pdftoimages =  PdfTOImages()
    pdftoimages.pdf_images()