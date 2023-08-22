from pdf_to_table import logging
from pdf_to_table.config import Configuration
from pdf_to_table.entity import TableDetectorConfig
import layoutparser as lp
import matplotlib.pyplot as plt
import os
import uuid
import cv2


class TableDetector:
    def __init__(self,configuration = Configuration() ):
        self.table_detector_config = configuration.get_table_detector_config()
        self.model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
                                threshold=0.5,
                                label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
                                enforce_cpu=True,
                                enable_mkldnn=True)

    def get_bb_points(self):
        images_dir_name = self.table_detector_config.images_dir_name
        table_imgs_dir_name = self.table_detector_config.table_imgs_dir_name
        if not os.listdir(images_dir_name):
            raise Exception(f"images dir is empty {images_dir_name} " )
        for imgs in os.listdir(images_dir_name):
            img_path = os.path.join(images_dir_name,imgs)
            imarr = cv2.imread(img_path)
            imarr = imarr[..., ::-1]
            layout = self.model.detect(imarr)
            for blk in layout.to_dict()["blocks"]:
                p1,p2= ( int(blk["x_1"]) , int(blk["y_1"]) ),( int(blk["x_2"]) , int(blk["y_2"]) )
                typ = blk["type"]
                if typ == "Table":
                    
                    crop_img = imarr[p1[0]:p2[0],p1[1]:p2[1]]
                    plt.imshow(crop_img)
                    plt.show()
                    file_path = os.path.join(table_imgs_dir_name,f"{uuid.uuid1()}.png")
                    cv2.imwrite(file_path,crop_img)

        return 0 if not os.listdir(images_dir_name) else 1
            




if __name__ == "__main__":
    table_detector=TableDetector()
    table_detector.get_bb_points()