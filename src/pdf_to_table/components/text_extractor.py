from paddleocr import PaddleOCR
from pdf_to_table import logging
from pdf_to_table.config import Configuration
import pandas as pd
import os
import cv2

model = PaddleOCR(lan="en")


class TextExtractor:
    def __init__(self, configuration: Configuration = Configuration()):
        self.text_extractor_config = configuration.get_text_extractor_config()

    def get_text_bboxs(self, limit_range: int = 9):
        images_dir_name = self.text_extractor_config.table_imgs_dir_name
        csv_dir_name = self.text_extractor_config.csv_dir_name
        excel_file_name = self.text_extractor_config.excel_file_name

        if not os.listdir(images_dir_name):
            raise Exception(f" images dir empty {images_dir_name}  ")
        for i, img in enumerate(os.listdir(images_dir_name)):
            imarr = cv2.imread(os.path.join(images_dir_name, img))
            imarr = cv2.cvtColor(imarr, cv2.COLOR_BGR2RGB)
            result = model.ocr(imarr)
            all_x1 = []
            for pt in result[0]:
                all_x1.append(pt[0][0][0])
            all_dict = {
                (i, i + limit_range): None
                for i in range(int(min(all_x1)), int(max(all_x1)), limit_range + 1)
            }

            all_dict = self._helper_fun_bboxes_2(all_dict, result)
            all_dict_1 = {key: val for key, val in all_dict.items() if val}
            final_dict = self._helper_fun_bboxes_1(all_dict_1, result)
            high_len = max([len(val) for val in final_dict.values()])
            for key in final_dict:
                final_dict[key] += [pd.NA] * (high_len - len(final_dict[key]))
            df = pd.DataFrame(final_dict)
            df.to_csv(os.path.join(csv_dir_name, f"{i}.csv"), index=None)
        self.excel_writer(csv_dir_name, excel_file_name)

    @staticmethod
    def _helper_fun_bboxes_2(all_dict: dict, result):
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
    def _helper_fun_bboxes_1(all_dict_1: dict, result):
        final_dict = {val: [] for val in all_dict_1.values()}
        for pt in result[0]:
            x1 = pt[0][0][0]
            for key, val in all_dict_1.items():
                if x1 >= key[0] and x1 <= key[1]:
                    text = pt[1][0]
                    final_dict[val].append(text)
        return final_dict

    def excel_writer(self, csv_dir_name, excel_file_name):
        excel_file = excel_file_name
        writer = pd.ExcelWriter(excel_file, engine="xlsxwriter")

        # Write each DataFrame to a separate sheet in the Excel file
        for idx, csv in enumerate(os.listdir(csv_dir_name)):
            fn = os.path.join(csv_dir_name, csv)
            df = pd.read_csv(fn)
            df.to_excel(writer, sheet_name=f"Sheet{idx+1}", index=False)


if __name__ == "__main__":
    text_extractor = TextExtractor()
    text_extractor.get_text_bboxs()
