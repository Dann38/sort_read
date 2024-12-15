from collections import OrderedDict
from tesseract_reader.bbox.bbox import BBox

class newBbox(BBox):
    
    def __init__(self, x_top_left: int, y_top_left: int, width: int, height: int) -> None:
        super().__init__(x_top_left, y_top_left, width, height)
        
    
    @staticmethod
    def converter(bbox: 'BBox'):
        x = bbox.x_top_left
        y = bbox.y_top_left
        w = bbox.width
        h = bbox.height
        
        return newBbox(x, y, w, h)
        
    def __gt__(self, bbox: 'BBox'):
        eps = max(self.y_bottom_right - self.y_top_left, bbox.y_bottom_right - bbox.y_top_left)
        if self.y_top_left> bbox.y_top_left + eps:
            return True
        elif abs(bbox.y_top_left - self.y_top_left) < eps and self.x_top_left < bbox.x_top_left:
            return True
        return False
    
    def __lt__(self, bbox: 'BBox'):
        eps = max(self.y_bottom_right - self.y_top_left, bbox.y_bottom_right - bbox.y_top_left)
        if self.y_top_left  + eps < bbox.y_top_left:
            return True
        elif abs(bbox.y_top_left - self.y_top_left) < eps and bbox.x_top_left > self.x_top_left:
            return True
        return False
    
    def point_is_in_bbox(self, point : list) -> bool:
        x = point[0]
        y = point[1]
        print(x)
        print(y)
        
        return (x > self.x_top_left and x < self.x_bottom_right and y > self.y_top_left and y < self.y_bottom_right)
        
        
        
        
        