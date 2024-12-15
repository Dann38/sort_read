import unittest
import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig
from SortableBBox import SortableBBox

class test_reading_order_sort(unittest.TestCase):
    
    
    def test_order(self):
        filenames = os.listdir('testing_imgs')
        images = os.listdir('tests/results')
        
        image_reader = ImageReader()
        tesseract_config = TesseractReaderConfig()
        tesseract_reader = TesseractReader(tesseract_config)
        path_project = os.path.abspath(os.path.join(os.getcwd(), "."))

        for i in range(len(filenames)):
            file = open('tests/results/' + images[i], 'r')
            line = file.readline().split()
            line = [float(line[i]) for i in range(len(line))]
            
            
            path_img = os.path.join(path_project, 'testing_imgs', filenames[i])
            img = image_reader.read(path_img)
            readed_img = tesseract_reader.read(img)
            
            for j in range(len(readed_img[0])):
                readed_img[0][j] = SortableBBox.converter(readed_img[0][j])
                
            current_result = Bbox_sorter.sort_bboxes(readed_img=readed_img)
            
            for index, result in zip([_ for _ in range(len(current_result))], current_result):
                self.assertTrue(readed_img[0][result].point_is_in_bbox((line[2*index], line[2*index+1])))
        