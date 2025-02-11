from SortableBBox import SortableBBox
import copy
class Bbox_sorter:
    

    
    @staticmethod
    def sort_bboxes_using_triangles(Bboxes):
        
        bboxes = copy.copy(Bboxes)
        for i in range(len(bboxes)):
            bboxes[i] = SortableBBox.converter(bboxes[i])
            bboxes[i].index = i

        for i in range(len(bboxes)):
            for j in range(i, len(bboxes)):
                if bboxes[j].greater_then_horizont(bboxes[i]):
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
                elif bboxes[j].greater_then_vertical(bboxes[i]):
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
                    
        result = []
        for i in range(len(bboxes)):
            result.append(bboxes[i].index)
        return result[::-1]
    
    
    @staticmethod
    def sort_bboxes(readed_img):

        new_image = list(readed_img)
        new_new_image = copy.deepcopy(new_image)
        bboxes = new_new_image[0]
        for i in range(len(bboxes)):
            bboxes[i] = SortableBBox.converter(bboxes[i])
            bboxes[i].index = i

        for i in range(len(bboxes)):
            for j in range(len(bboxes)):
                if bboxes[i] < bboxes[j]:
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
        result = []
        for i in range(len(bboxes)):
            result.append(bboxes[i].index)
        return result
    
    @staticmethod
    def sort_bboxes2(Bboxes):

        bboxes = copy.copy(Bboxes)
        for i in range(len(bboxes)):
            bboxes[i] = SortableBBox.converter(bboxes[i])
            bboxes[i].index = i

        for i in range(len(bboxes)):
            current_min = bboxes[i]
            min_index = i
            
            for j in range(i, len(bboxes)):
                if bboxes[j] < current_min:
                    current_min = bboxes[j]
                    min_index = j
                    
            bboxes[i], bboxes[min_index] = bboxes[min_index], bboxes[i]
                    
        result = []
        for i in range(len(bboxes)):
            result.append(bboxes[i].index)
        return result

