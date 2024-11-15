from abc import ABC
from typing import Dict


class BBox(ABC):

    def __init__(self, cord : Dict[str, int]):
        self.x0 = cord["x0"]
        self.x1 = cord["x1"]
        self.y0 = cord["y0"]
        self.y1 = cord["y1"]

    def __gt__(self, bbox : "BBox"):
        eps = max(self.y0 - self.y1, bbox.y0 - bbox.y1)
        if self.y0 > bbox.y0 + eps:
            return True
        elif abs(bbox.y0 - self.y0) < eps and bbox.x0 > self.x0:
            return True
        return False

first_bbox = BBox({"x0":10, "y0" : 10 , "x1" : 40, "y1" : 20})
second_bbox = BBox({"x0":50, "y0" : 10 , "x1" : 110, "y1" : 20})
third_bbox = BBox({"x0":10, "y0" : 30 , "x1" : 60, "y1" : 40})
fourth_bbox = BBox({"x0":70, "y0": 30, "x1" : 110, "y1" : 40})
print("Первый дальше третьего", first_bbox > third_bbox)
print("Второй дальше первого", second_bbox > first_bbox)
print("Четвертый дальше третьего", fourth_bbox > third_bbox)
print("Четвертый дальше первого", fourth_bbox > first_bbox)
print("Второй дальше четвертого", second_bbox > fourth_bbox)