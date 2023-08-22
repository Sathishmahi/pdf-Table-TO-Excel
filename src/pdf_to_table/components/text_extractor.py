from paddleocr import PaddleOCR
from pdf_to_table import logging
from pdf_to_table.config import Configuration
import pandas as pd
from tqdm import tqdm
import os
import cv2

model = PaddleOCR(lan="en")

STAGE_NAME = "TEXT EXTRACTOR"


class TextExtractor:
    def __init__(self, configuration: Configuration = Configuration()):
        """
        Initialize the TextExtractor with a configuration object.

        Args:
            configuration (Configuration): The configuration object to use.
        """
        self.text_extractor_config = configuration.get_text_extractor_config()

    def get_text_bboxs(self, limit_range: int = 9):
        """
        Extract text bounding boxes from images and save them as CSV files.

        Args:
            limit_range (int, optional): The range to use for creating bounding boxes. Default is 9.
        """
        images_dir_name = self.text_extractor_config.table_imgs_dir_name
        csv_dir_name = self.text_extractor_config.csv_dir_name
        excel_file_name = self.text_extractor_config.excel_file_name

        # Check if the images directory is empty
        if not os.listdir(images_dir_name):
            msg = f" table dir are empty {images_dir_name} "
            logging.info(msg)
            return
        try:
            for i, img in tqdm(
                enumerate(os.listdir(images_dir_name)), desc="text extract"
            ):
                imarr = cv2.imread(os.path.join(images_dir_name, img))
                imarr = cv2.cvtColor(imarr, cv2.COLOR_BGR2RGB)
                result = model.ocr(imarr)
                all_x1 = []

                # Extract x1 coordinates from the OCR results
                for pt in result[0]:
                    all_x1.append(pt[0][0][0])

                # Create a dictionary of bounding box ranges
                all_dict = {
                    (i, i + limit_range): None
                    for i in range(int(min(all_x1)), int(max(all_x1)), limit_range + 1)
                }

                # Assign IDs to bounding boxes
                all_dict = self._helper_fun_bboxes_2(all_dict, result)
                all_dict_1 = {key: val for key, val in all_dict.items() if val}

                # Organize text data based on assigned IDs
                final_dict = self._helper_fun_bboxes_1(all_dict_1, result)

                # Ensure all lists in the final_dict have the same length
                high_len = max([len(val) for val in final_dict.values()])
                for key in final_dict:
                    final_dict[key] += [pd.NA] * (high_len - len(final_dict[key]))

                # Convert the dictionary to a DataFrame and save it as a CSV file
                df = pd.DataFrame(final_dict)
                df.to_csv(os.path.join(csv_dir_name, f"{i}.csv"), index=None)

            # Log the path to the final Excel file
            logging.info(f" final excel file path {excel_file_name} ")
            self.excel_writer(csv_dir_name, excel_file_name)

        except Exception as e:
            # Log any exceptions and re-raise them
            logging.info(e)
            raise e

    @staticmethod
    def _helper_fun_bboxes_2(all_dict: dict, result) -> dict:
        """
        Helper function to create bounding boxes and assign IDs.

        Args:
            all_dict (dict): Dictionary of bounding box ranges.
            result: OCR results.

        Returns:
            dict: Updated dictionary with assigned IDs.
        """
        ids = 0
        for pt in result[0]:
            x1 = pt[0][0][0]
            text = pt[1][0]
            for key, val in all_dict.items():
                x1 = pt[0][0][0]
                if x1 >= key[0] and x1 <= key[1] and not val:
                    all_dict[key] = ids
                    ids = ids + 1
        return all_dict

    @staticmethod
    def _helper_fun_bboxes_1(all_dict_1: dict, result) -> dict:
        """
        Helper function to organize text data based on assigned IDs.

        Args:
            all_dict_1 (dict): Dictionary of assigned IDs.
            result: OCR results.

        Returns:
            dict: Final dictionary with organized text data.
        """
        final_dict = {val: [] for val in all_dict_1.values()}
        for pt in result[0]:
            x1 = pt[0][0][0]
            for key, val in all_dict_1.items():
                if x1 >= key[0] and x1 <= key[1]:
                    text = pt[1][0]
                    final_dict[val].append(text)
                    break
        return final_dict

    def excel_writer(
        self, csv_dir_name: str, excel_file_name: str, ther: float = 0.8
    ) -> None:
        """
        Write CSV files to an Excel file.

        Args:
            csv_dir_name (str): Directory containing CSV files.
            excel_file_name (str): Excel file name.
        """
        excel_file = excel_file_name
        writer = pd.ExcelWriter(excel_file, engine="xlsxwriter")

        # Write each DataFrame to a separate sheet in the Excel file
        for idx, csv in enumerate(os.listdir(csv_dir_name)):
            fn = os.path.join(csv_dir_name, csv)
            df = pd.read_csv(fn)
            all_rm_col = [
                col for col in df.columns if df[col].isna().sum() / len(df) >= ther
            ]
            df.drop(columns=all_rm_col, inplace=True)
            df.to_excel(writer, f"sheet_{idx}", index=False)
        writer.save()


if __name__ == "__main__":
    print(f"  >>>>>>>>  START   {STAGE_NAME}   >>>>>>>>")
    text_extractor = TextExtractor()
    text_extractor.get_text_bboxs(5)
    print(f"  >>>>>>>>  END   {STAGE_NAME}   >>>>>>>>")
