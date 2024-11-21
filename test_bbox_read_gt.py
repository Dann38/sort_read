import unittest
from main import BBox
class Test_Bbox_gr(unittest.TestCase):
    first_bbox = BBox({"x0":10, "y0" : 10 , "x1" : 40, "y1" : 20})
    second_bbox = BBox({"x0":50, "y0" : 10 , "x1" : 110, "y1" : 20})
    third_bbox = BBox({"x0":10, "y0" : 30 , "x1" : 60, "y1" : 40})
    fourth_bbox = BBox({"x0":70, "y0": 30, "x1" : 110, "y1" : 40})

    def test_size(self) -> None:
        self.assertEqual(self.first_bbox > self.third_bbox,False)
        self.assertEqual(self.second_bbox > self.first_bbox,True)
        self.assertEqual(self.fourth_bbox > self.third_bbox,True)
        self.assertEqual(self.fourth_bbox > self.first_bbox,True)
        self.assertEqual(self.second_bbox > self.fourth_bbox,False)

