
from tesseract_reader.bbox.bbox import BBox
import math
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
        
    @property
    def eps(self, bbox):
        eps = max(self.y_bottom_right - self.y_top_left, bbox.y_bottom_right - bbox.y_top_left)
        return eps
    
    def greater_then_horizont(self, BBox: 'BBox'):
        
        l1, c1, r1 = (self.x_top_left, self.y_top_left), \
            (abs(self.x_top_left - self.x_bottom_right)/2, self.y_top_left), \
            (self.x_bottom_right, self.y_top_left)
            
        l2, c2, r2 = (BBox.x_top_left, BBox.y_top_left), \
            (abs(BBox.x_top_left - BBox.x_bottom_right)/2,BBox.y_top_left), \
            (BBox.x_bottom_right, BBox.y_top_left)
        
        
        
        A1 = abs(l1[0] - r1[0])
        B1 = math.sqrt((l1[0] - c2[0])**2 + (l1[1] - c2[1])**2)
        C1 = math.sqrt((c2[0] - r1[0])**2 + (c2[1] - r1[1])**2)
        
        A2 = abs(r2[0] - l2[0])
        B2 = math.sqrt((l2[0] - c1[0])**2 +  (l2[1] - c1[1])**2)
        C2 = math.sqrt((c1[0] - r2[0])**2 + (c1[1] - r2[1])**2)
        
        cos1 = [(B1**2+C1**2-A1**2)/(2*B1*C1), (A1**2+C1**2-B1**2)/(2*A1*C1) , (B1**2+A1**2-C1**2)/(2*B1*A1)]
        
        cos2 = [(B2**2+C2**2-A2**2)/(2*B2*C2), (A2**2+C2**2-B2**2)/(2*A2*C2), (B2**2+A2**2-C2**2)/(2*B2*A2)]
        counter = 0
        for cos in cos1: 
            if cos < 0:
                counter += 1
        for cos in cos2:
            if cos < 0:
                counter += 1
        
        if counter == 2:
            return (BBox.x_top_left + BBox.width/2) < (self.x_top_left + self.width/2)
        else:
            return None
        
        
    def greater_then_vertical(self, BBox: 'BBox'):
        
        l1, c1, r1 = (self.x_top_left, self.y_top_left), \
            ( self.x_top_left, self.y_top_left + self.height/2), \
            (self.x_top_left, self.y_bottom_right)
            
        l2, c2, r2 = (BBox.x_top_left, BBox.y_top_left), \
            ( BBox.x_top_left, abs(BBox.y_top_left - BBox.y_bottom_right)/2), \
            (BBox.x_top_left, BBox.y_bottom_right)
            
        
        A1 = abs(l1[1] - r1[1])
        B1 = math.sqrt((l1[0] - c2[0])**2 + (l1[1] - c2[1])**2)
        C1 = math.sqrt((c2[0] - r1[0])**2 + (c2[1] - r1[1])**2)
        
        A2 = abs(r2[1] - l2[1])
        B2 = math.sqrt((l2[0] - c1[0])**2 +  (l2[1] - c1[1])**2)
        C2 = math.sqrt((c1[0] - r2[0])**2 + (c1[1] - r2[1])**2)
        
        
        cos1 = [(B1**2+C1**2-A1**2)/(2*B1*C1), (A1**2+C1**2-B1**2)/(2*A1*C1) , (B1**2+A1**2-C1**2)/(2*B1*A1)]
        
        cos2 = [(B2**2+C2**2-A2**2)/(2*B2*C2), (A2**2+C2**2-B2**2)/(2*A2*C2), (B2**2+A2**2-C2**2)/(2*B2*A2)]
        counter = 0
        for cos in cos1: 
            if cos < 0:
                counter += 1
        for cos in cos2:
            if cos < 0:
                counter += 1
        
        if counter == 2:
            return (BBox.y_top_left + BBox.height/2) < self.y_top_left + self.height/2
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
        
        
        
        
        