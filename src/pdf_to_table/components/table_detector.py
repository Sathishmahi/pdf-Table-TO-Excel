# Import necessary libraries and modules
import os
import uuid
import cv2
import matplotlib.pyplot as plt
import layoutparser as lp

# Import custom modules and configurations
from pdf_to_table import logging
from pdf_to_table.config import Configuration
from pdf_to_table.entity import TableDetectorConfig
from pdf_to_table.constant import (
    LAYOUT_PARSER_MODEL_CLASS_DICT,
    LAYOUT_PARSER_MODEL_CONFIG_PATH,
)
from pdf_to_table.utils import read_yaml

# Define a constant for the stage name
STAGE_NAME = "TABLE DETECTOR"


# Define the TableDetector class
class TableDetector:
    def __init__(self, configuration=Configuration()):
        """
        Initialize the TableDetector with a configuration object.

        Args:
            configuration: The configuration object to use.
        """
        # Get configuration settings
        self.table_detector_config = configuration.get_table_detector_config()
        self.table_detector_params_config = (
            configuration.get_table_detector_params_config()
        )

        # Load layout parser model with specified parameters
        self.model = lp.PaddleDetectionLayoutModel(
            config_path=LAYOUT_PARSER_MODEL_CONFIG_PATH,
            threshold=self.table_detector_params_config.threshold,
            label_map=LAYOUT_PARSER_MODEL_CLASS_DICT,
            enforce_cpu=self.table_detector_params_config.enforce_cpu,
            enable_mkldnn=self.table_detector_params_config.enable_mkldnn,
        )

    def get_bb_points(self):
        """
        Detect tables in images and save them as separate image files.
        """
        # Get image and table image directory paths
        images_dir_name = self.table_detector_config.images_dir_name
        table_imgs_dir_name = self.table_detector_config.table_imgs_dir_name

        # Check if the images directory is empty
        if not os.listdir(images_dir_name):
            e = Exception(f"images dir is empty {images_dir_name} ")
            raise e

        # Loop through images in the directory
        for imgs in os.listdir(images_dir_name):
            img_path = os.path.join(images_dir_name, imgs)
            imarr = cv2.imread(img_path)
            imarr = imarr[..., ::-1]  # Reverse BGR to RGB
            layout = self.model.detect(imarr)

            # Iterate through detected blocks in the layout
            for blk in layout.to_dict()["blocks"]:
                p1, p2 = (int(blk["x_1"]), int(blk["y_1"])), (
                    int(blk["x_2"]),
                    int(blk["y_2"]),
                )
                typ = blk["type"]

                if typ == "Table":
                    # Crop the table from the image
                    crop_img = imarr[p1[0] : p2[0], p1[1] : p2[1], :]

                    # Generate a unique file name for the table image
                    file_path = os.path.join(table_imgs_dir_name, f"{uuid.uuid1()}.png")

                    # Save the cropped table image
                    cv2.imwrite(file_path, crop_img)

        # Return 0 if the images directory is empty, else return 1
        return 0 if not os.listdir(images_dir_name) else 1


if __name__ == "__main__":
    # Print a start message
    print(f"  >>>>>>>>  START   {STAGE_NAME}   >>>>>>>>")

    # Create an instance of the TableDetector class
    table_detector = TableDetector()

    # Call the get_bb_points method to detect and save tables
    table_detector.get_bb_points()

    # Print an end message
    print(f"  >>>>>>>>  END   {STAGE_NAME}   >>>>>>>>")
