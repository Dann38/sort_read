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
