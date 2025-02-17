import unittest
from Code.main import BBox
from SortableBBox import SortableBBox
from BBOX_sorter import Bbox_sorter
import os
class Test_Bbox_gr(unittest.TestCase):
    
    
    
        
    

    def test_order(self) -> None:
    # Decode the current working directory from bytes to string
        cwd = os.getcwdb().decode('utf-8')
        
        with open(os.path.join(cwd, "bboxes", "filenames.txt"), 'r') as file:
            filenames = file.readline().split()
            print(filenames)
        with open(os.path.join(cwd, 'bboxes', 'results.txt'), 'r') as file:
            results = [b.split(',') for b in file.readlines()]
            results = [list(map(int, item)) for item in results]
            
        for i, filename in enumerate(filenames):
            expected_result = results[i]
            bboxes = SortableBBox.json_converter(os.path.join(cwd, "bboxes",filename))
            
            result = Bbox_sorter.sort_bboxes_using_triangles(bboxes[0])
            self.assertEqual(expected_result, result)       
        
        
    

