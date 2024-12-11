import unittest
import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig


class test_reading_order_sort(unittest.TestCase):
    
    
    def test_order(self):
        filenames = [ "test_image1.jpeg",  "test_image2.jpeg"]
        results = [[0,1,2], [0,1,2,3]]

        image_reader = ImageReader()
        tesseract_config = TesseractReaderConfig()
        tesseract_reader = TesseractReader(tesseract_config)
        path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
        
        for i in range(len(filenames)):
            path_img = os.path.join(path_project, 'testing_imgs', filenames[i])
            img = image_reader.read(path_img)
            readed_img = tesseract_reader.read(img)
            current_result = Bbox_sorter.sort_bboxes(readed_img=readed_img)
            print(f'test{i}')
            self.assertEqual(current_result, results[i])
        