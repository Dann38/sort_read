import os
from BBOX_sorter import Bbox_sorter
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig

if __name__ == '__main__':
    # Image path /example_img/img_1.jpeg
    path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
    path_img = os.path.join(path_project, 'testing_imgs', "test_image2.jpeg")

    # Objects
    image_reader = ImageReader()
    tesseract_config = TesseractReaderConfig()
    tesseract_reader = TesseractReader(tesseract_config)

    img = image_reader.read(path_img)
    readed_img = tesseract_reader.read(img)
    print(Bbox_sorter.sort_bboxes(readed_img=readed_img))

