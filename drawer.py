from matplotlib import pyplot as plt
from tesseract_reader.bbox.bbox import BBox
from typing import Tuple, Dict
import numpy as np

class Drawer():
    
    
    @staticmethod
    def font_sizes(bboxes : Tuple['BBox']):
        sizes = []
        for i in range(len(bboxes)):
            sizes.append(bboxes[i].height)
            
        return sizes
        
    
    @staticmethod
    def draw_and_img(img, labeling = None , sizes = None):
        
        plt.imshow(img, interpolation='nearest')
        i = 0
        if labeling:
            for x_coord, y_coord, label in labeling:
                plt.text(x_coord, y_coord, label, ha='left', va='top', fontsize = sizes[i])
                i+=1
                
        plt.show()
        
        
    @staticmethod
    def draw_bbox(bboxes : Tuple['BBox'], text : Tuple['str']):
        x_bottom = 0
        y_bottom = 0
        
        for i in range(len(bboxes)):
            if x_bottom < bboxes[i].x_bottom_right:
                x_bottom = bboxes[i].x_bottom_right
            if y_bottom < bboxes[i].y_bottom_right:
                y_bottom = bboxes[i].y_bottom_right
        labeling = []
        
        x_bottom +=10
        y_bottom += 10
        
        image_for_bboxes = np.zeros((y_bottom, x_bottom, 3))
        
        for i in range(len(bboxes)):
            labeling.append((bboxes[i].x_top_left, bboxes[i].y_top_left, text[i]))

            for height in range(bboxes[i].height):
                
                for width in range(bboxes[i].width):
                    image_for_bboxes[bboxes[i].y_top_left+height][bboxes[i].x_top_left+width] = np.array([225, 225, 225])
                    
                    
        sizes = Drawer.font_sizes(bboxes)
        Drawer.draw_and_img(image_for_bboxes, labeling=labeling, sizes=sizes)
        
        
        