from newBbox import newBbox
import copy
class Bbox_sorter:
    
    @staticmethod
    def sort_bboxes(readed_img):

        new_image = list(readed_img)
        new_new_image = copy.deepcopy(new_image)
        bboxes = new_new_image[0]
        for i in range(len(bboxes)):
            bboxes[i] = newBbox.converter(bboxes[i])
            bboxes[i].index = i

        for i in range(len(bboxes)):
            for j in range(len(bboxes)):
                if bboxes[i] < bboxes[j]:
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
        result = []
        for i in range(len(bboxes)):
            result.append(bboxes[i].index)
        return result

