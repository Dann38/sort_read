
from tesseract_reader.bbox.bbox import BBox
import math
import json

class SortableBBox(BBox):
    
    def __init__(self, x_top_left: int, y_top_left: int, width: int, height: int) -> None:
        super().__init__(x_top_left, y_top_left, width, height)
        
    
    @staticmethod
    def converter(bbox: 'BBox'):
        x = bbox.x_top_left
        y = bbox.y_top_left
        w = bbox.width
        h = bbox.height
        
        return SortableBBox(x, y, w, h)
        
        
    @staticmethod 
    def json_converter(filename):
        with open(filename, 'r') as file:
            boxes = json.load(file)
            boxes = boxes['words']
        text = []
        new_bboxes = []
        for i in range(len(boxes)):
            x_top_left = boxes[i]['x_top_left']
            y_top_left = boxes[i]['y_top_left']
            w = -(boxes[i]['x_top_left'] - boxes[i]['x_bottom_right'])
            h = -(boxes[i]['y_top_left'] - boxes[i]['y_bottom_right'])
            new_bboxes.append(SortableBBox(x_top_left, y_top_left, w, h))
            text.append(boxes[i]['text'])
            
        return new_bboxes, text
        
    @property
    def eps(self, bbox):
        eps = max(self.y_bottom_right - self.y_top_left, bbox.y_bottom_right - bbox.y_top_left)
        return eps
    
    def __get_dist(self, l, r, c):
        A = math.sqrt((l[0] - r[0])**2 + (l[1] - r[1])**2)
        B = math.sqrt((l[0] - c[0])**2 + (l[1] - c[1])**2)
        C = math.sqrt((c[0] - r[0])**2 + (c[1] - r[1])**2)
        return A, B, C
        
    def __get_min_cos(self, l, r, c):
        A, B, C = self.__get_dist(l, r, c)
        return min([(B**2+C**2-A**2)/(2*B*C), (A**2+C**2-B**2)/(2*A*C), (B**2+A**2-C**2)/(2*B*A)])
            

    def greater_then_horizont(self, BBox: 'BBox'):
        w1 = abs(self.x_top_left - self.x_bottom_right)
        w2 = abs(BBox.x_top_left - BBox.x_bottom_right)
        l1, c1, r1 = (self.x_top_left,      self.y_top_left), \
                     (self.x_top_left+w1/2, self.y_top_left), \
                     (self.x_bottom_right,  self.y_top_left)
        
        l2, c2, r2 = (BBox.x_top_left,      BBox.y_top_left), \
                     (BBox.x_top_left+w2/2, BBox.y_top_left), \
                     (BBox.x_bottom_right,  BBox.y_top_left)
       
        cos1 = self.__get_min_cos(l1, r1, c2)
        cos2 = self.__get_min_cos(l2, r2, c1)
        
        if cos1 < 0 and cos2 < 0:
            return (BBox.x_top_left + BBox.width/2) < (self.x_top_left + self.width/2)
        else:
            return None # ответ на вопрос больше будет отрицателен, не сравнимы
        
        
    def greater_then_vertical(self, BBox: 'BBox'):
        h1 = abs(self.y_top_left - self.y_bottom_right)
        h2 = abs(BBox.y_top_left - BBox.y_bottom_right)
        l1, c1, r1 = (self.x_top_left, self.y_top_left), \
                     (self.x_top_left, self.y_top_left + h1/2), \
                     (self.x_top_left, self.y_bottom_right)
            
        l2, c2, r2 = (BBox.x_top_left, BBox.y_top_left), \
                     (BBox.x_top_left, BBox.y_top_left + h2/2), \
                     (BBox.x_top_left, BBox.y_bottom_right)
            
        cos1 = self.__get_min_cos(l1, r1, c2)
        cos2 = self.__get_min_cos(l2, r2, c1)

        if cos1 < 0 and cos2 < 0:
            return (BBox.y_top_left + BBox.height/2) < (self.y_top_left + self.height/2)
        else:
            return None
    
    def __gt__(self, bbox: 'BBox'):
        eps = max(self.y_bottom_right - self.y_top_left, bbox.y_bottom_right - bbox.y_top_left)
        if self.y_top_left> bbox.y_top_left + eps:
            return True
        elif abs(bbox.y_top_left - self.y_top_left) < eps and self.x_top_left < bbox.x_top_left:
            return True
        return False
    
    def __lt__(self, bbox: 'BBox'):
        eps = max(self.height, bbox.height)
        # eps = max(self.y_bottom_right, bbox.y_top_left) - min(self.y_bottom_right, bbox.y_top_left)
        # eps = eps/2
        if  abs(bbox.y_top_left - self.y_top_left) < eps and bbox.x_top_left > self.x_top_left:
            return True
        elif self.y_top_left  + eps < bbox.y_bottom_right or self.y_top_left  + eps < bbox.y_top_left :
            return True
        return False
    
    def point_is_in_bbox(self, point : list) -> bool:
        x = point[0]
        y = point[1]
        
        return (x >= self.x_top_left and x <= self.x_bottom_right and y >= self.y_top_left and y <= self.y_bottom_right)
        
        
        
        
        