import os
import pytest
from src.pdf_to_table.components.pdf_saver import PdfTOImages
from src.pdf_to_table.config.configuration import Configuration

configuration =  Configuration()
pdf_saver_config = configuration.get_pdf_saver_config()
images_dir_name = pdf_saver_config.images_dir_name

def test_pdf_saver():
    
    pdf_images  =  PdfTOImages()
    pdf_images.pdf_images()
    assert os.path.exists(images_dir_name)
    assert len(os.listdir(images_dir_name))>0
