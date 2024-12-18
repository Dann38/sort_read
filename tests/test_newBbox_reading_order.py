import unittest
import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig
from SortableBBox import SortableBBox

class test_reading_order_sort(unittest.TestCase):
    
    
    @staticmethod
    def get_points(line):
        points = []
        xs = []
        ys = []
        for point in range(len(line)):
            if point%2==0:
                xs.append(line[point])
            else:
                ys.append(line[point])
        for i in range(len(xs)):
            points.append((xs[i], ys[i]))
        return points
            
    def test_order(self):
        filenames = os.listdir('testing_imgs')
        images = os.listdir(os.path.join('tests', 'results'))
        
        image_reader = ImageReader()
        tesseract_config = TesseractReaderConfig()
        tesseract_reader = TesseractReader(tesseract_config)
        path_project = os.path.abspath(os.path.join(os.getcwd(), "."))

        for i in range(len(filenames)):
            with open(os.path.join(os.path.join('tests', 'results'), images[i]), 'r') as file:
                line = file.readline().split()
                line = [float(line[i]) for i in range(len(line))]
                
            points = test_reading_order_sort.get_points(line)
            path_img = os.path.join(path_project, 'testing_imgs', filenames[i])
            img = image_reader.read(path_img)
            readed_img = tesseract_reader.read(img)
            
            for j in range(len(readed_img[0])):
                readed_img[0][j] = SortableBBox.converter(readed_img[0][j])
                
            current_result = Bbox_sorter.sort_bboxes(readed_img=readed_img)
            
            for index, result in zip([_ for _ in range(len(current_result))], current_result):
                self.assertTrue(readed_img[0][result].point_is_in_bbox(points[index]))