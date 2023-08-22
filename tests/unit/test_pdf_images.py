import os
import pytest
import wget
from src.pdf_to_table.components.pdf_saver import PdfTOImages
from src.pdf_to_table.config.configuration import Configuration

configuration =  Configuration()
pdf_saver_config = configuration.get_pdf_saver_config()
images_dir_name = pdf_saver_config.images_dir_name
file_name = pdf_saver_config.file_name

def test_pdf_saver():
    test_pdf_url = "https://d2cyt36b7wnvt9.cloudfront.net/exams/wp-content/uploads/2021/03/15164528/Multiplication-Tables-1-to-100.pdf"
    wget.download(test_pdf_url,out = file_name)
    pdf_images  =  PdfTOImages()
    pdf_images.pdf_images()
    assert os.path.exists(images_dir_name)
    assert len(os.listdir(images_dir_name))>0
