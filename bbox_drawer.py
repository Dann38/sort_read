from tesseract_reader.bbox.bbox import BBox
from typing import Tuple, Dict
import numpy as np
from drawer import Drawer
class BBoxDrawer():
    
    
    @staticmethod
    def draw_bbox(bboxes : Tuple['BBox']):
        x_bottom = 0
        y_bottom = 0
        
        for i in range(len(bboxes)):
            if x_bottom < bboxes[i].x_bottom_right:
                x_bottom = bboxes[i].x_bottom_right
            if y_bottom < bboxes[i].y_bottom_right:
                y_bottom = bboxes[i].y_bottom_right
        
        x_bottom +=10
        y_bottom += 10
        print(x_bottom, y_bottom)
        image_for_bboxes = np.zeros((y_bottom, x_bottom, 3))
        
        for i in range(len(bboxes)):

            for height in range(bboxes[i].height):
                
                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([225, 225, 225])
                    
        Drawer.draw_and_img(image_for_bboxes)
        
        
        
        
        
        