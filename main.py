import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig
from newBbox import newBbox
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
    rez = Bbox_sorter.sort_bboxes(readed_img=readed_img)

    for i in rez:
        readed_img[0][i] = newBbox.converter(readed_img[0][i])
        print(f'bbox номер {i}: {readed_img[0][i]}')
    
    points = []
    for r in rez:
        print(readed_img[0][r])
        print(readed_img[1][r])
        print(f'point for tests: x = {readed_img[0][r].x_top_left+readed_img[0][r].width/2}, y = {readed_img[0][r].y_top_left+readed_img[0][r].height/2}', end = '\n\n')
        points.append((readed_img[0][r].x_top_left+readed_img[0][r].width/2, readed_img[0][r].y_top_left+readed_img[0][r].height/2))
    
    print(points)
