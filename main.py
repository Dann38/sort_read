import os
from tesseract_reader import ImageReader, TesseractReader, TesseractReaderConfig

if __name__ == '__main__':
    # Image path /example_img/img_1.jpeg
    path_project = os.path.abspath(os.path.join(os.getcwd(), "."))
    path_img = os.path.join(path_project, 'example_img', "img_1.jpeg")

    # Objects
    image_reader = ImageReader()
    tesseract_config = TesseractReaderConfig()
    tesseract_reader = TesseractReader(tesseract_config)

    img = image_reader.read(path_img)
    a = tesseract_reader.read(img)
    bboxes = a[0]
    for i in range(len(bboxes)):
        bboxes[i].index=i
    for i in range(len(bboxes)):
        print(bboxes[i].index, end=' ')

    for i in range(len(bboxes)):
        for j in range(len(bboxes)):
            if bboxes[i] > bboxes[j]:
                bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
    print('Отсротированы ббоксы')

    for i in range(len(bboxes)):
        print(bboxes[i].index, end=' ')
