import unittest
import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig
from newBbox import newBbox

class test_reading_order_sort(unittest.TestCase):
    
    
    def test_order(self):
        filenames = [ "test_image1.jpeg",  "test_image2.jpeg", "test_image3.jpeg", "test_image4.jpeg"]
        expected_points_in_right_order = [
            [(58.0, 34.5), (373.5, 264.0), (835.0, 369.0)],
            [(285.0, 55.0), (75.5, 184.0), (488.5, 210.0), (91.5, 542.0)],
            [(61.0, 58.0), (491.5, 56.0), (277.5, 118.0)],
            [(301.5, 72.0), (86.5, 94.0), (572.5, 72.5)],
            ]

        image_reader = ImageReader()
        tesseract_config = TesseractReaderConfig()
        tesseract_reader = TesseractReader(tesseract_config)
        path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
        
        for i in range(len(filenames)):
            path_img = os.path.join(path_project, 'testing_imgs', filenames[i])
            img = image_reader.read(path_img)
            readed_img = tesseract_reader.read(img)
            for j in range(len(readed_img[0])):
                readed_img[0][j] = newBbox.converter(readed_img[0][j])
            current_result = Bbox_sorter.sort_bboxes(readed_img=readed_img)
            
                
            for index, result in zip([_ for _ in range(len(current_result))], current_result):
                self.assertTrue(readed_img[0][result].point_is_in_bbox(expected_points_in_right_order[i][index]))
        