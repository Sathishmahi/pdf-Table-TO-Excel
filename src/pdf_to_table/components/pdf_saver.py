
# Import necessary libraries and modules
import os
import fitz
from pathlib import Path
from pdf_to_table import logging
from pdf_to_table.config import Configuration
from pdf_to_table.entity import PdfSaverConfig
from tqdm import tqdm

# Define a constant for the stage name
STAGE_NAME = "PDF SAVER"

# Define the PdfTOImages class
class PdfTOImages:
    def __init__(self, configuration: Configuration = Configuration()):
        """
        Initialize the PdfTOImages with a configuration object.

        Args:
            configuration: The configuration object to use.
        """
        self.pdf_saver_config = configuration.get_pdf_saver_config()

    def pdf_images(self):
        """
        Convert pages of a PDF to image files (e.g., PNG).
        """
        # Get file path and images directory name from the configuration
        file_path = self.pdf_saver_config.file_name
        images_dir_name = self.pdf_saver_config.images_dir_name

        # Open the PDF document using PyMuPDF (fitz)
        pdf_document = fitz.open(file_path)

        # Iterate through each page of the PDF
        for page_number in tqdm(range(pdf_document.page_count), desc="pdf to page convert"):
            # Get the page
            page = pdf_document.load_page(page_number)

            # Convert the page to a pixmap (image)
            pix = page.get_pixmap()

            # Generate the image file name
            image_file_name = os.path.join(images_dir_name, f"page_{page_number + 1}.png")

            # Save the pixmap as an image file (e.g., PNG)
            pix.save(image_file_name)

if __name__ == "__main__":
    # Print a start message
    print(f"  >>>>>>>>  START   {STAGE_NAME}   >>>>>>>>")

    # Create an instance of the PdfTOImages class
    pdftoimages = PdfTOImages()

    # Call the pdf_images method to convert PDF pages to images
    pdftoimages.pdf_images()

    # Print an end message
    print(f"  >>>>>>>>  END   {STAGE_NAME}   >>>>>>>>")
