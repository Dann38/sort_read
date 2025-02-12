import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig
from SortableBBox import SortableBBox
from drawer import Drawer
import json
import copy
if __name__ == '__main__':
    # Image path /example_img/img_1.jpeg
    path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
    path_img = os.path.join(path_project, 'testing_imgs', "test_image4.jpeg")

    # Objects
    image_reader = ImageReader()
    tesseract_config = TesseractReaderConfig()
    tesseract_reader = TesseractReader(tesseract_config)

    img = image_reader.read(path_img)
    readed_img = tesseract_reader.read(img)
    new_image = list(readed_img)
    new_new_image = copy.deepcopy(new_image)
    bboxes = new_new_image[0]
    text = new_new_image[1]
    new_bboxes = []
    
    for i in bboxes:
        new_bboxes.append(SortableBBox.converter(i))
        
    print(new_bboxes)
    print(text)
    Drawer.draw_bbox(new_bboxes, text=text)
    print(new_bboxes[1].greater_then_vertical(new_bboxes[0]))
    
    sorted_boxes = Bbox_sorter.sort_bboxes_using_triangles(new_bboxes)
    for i in sorted_boxes:
        print(text[i])
        
        
    # bboxes = []
    # for i in bboxes:
    #     bboxes[0][i] = SortableBBox.converter(readed_img[0][i])

    #     bboxes.append(readed_img[0][i])

    new_bboxes = []
    with open('boxes4.json', 'r') as file:
        boxes = json.load(file)
        boxes = boxes['words']
        
    text = []
    for i in range(len(boxes)):
        x_top_left = boxes[i]['x_top_left']
        y_top_left = boxes[i]['y_top_left']
        w = -(boxes[i]['x_top_left'] - boxes[i]['x_bottom_right'])
        h = -(boxes[i]['y_top_left'] - boxes[i]['y_bottom_right'])
        new_bboxes.append(SortableBBox(x_top_left, y_top_left, w, h))
        text.append(boxes[i]['text'])
    
    print(new_bboxes)
    print(text)
    Drawer.draw_bbox(new_bboxes, text=text)

    print(new_bboxes[2].greater_then_horizont(new_bboxes[0]))
    sorted_boxes = Bbox_sorter.sort_bboxes_using_triangles(new_bboxes)
    
    for i in sorted_boxes:
        print(text[i])
    Drawer.draw_bbox([new_bboxes[i] for i in sorted_boxes], text=[f"{j}/{text[i]}" for j, i in enumerate(sorted_boxes)])
    # points = []
    # for r in rez:
    #     print(readed_img[0][r])
    #     print(readed_img[1][r])
    #     print(f'point for tests: x = {readed_img[0][r].x_top_left+readed_img[0][r].width/2}, y = {readed_img[0][r].y_top_left+readed_img[0][r].height/2}', end = '\n\n')
    #     points.append((readed_img[0][r].x_top_left+readed_img[0][r].width/2, readed_img[0][r].y_top_left+readed_img[0][r].height/2))
    