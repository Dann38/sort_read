class Bbox_sorter:
    
    @staticmethod
    def sort_bboxes(readed_img):
        bboxes = readed_img[0]
        for i in range(len(bboxes)):
            bboxes[i].index = i

        for i in range(len(bboxes)):
            for j in range(len(bboxes)):
                if bboxes[i] > bboxes[j]:
                    bboxes[i], bboxes[j] = bboxes[j], bboxes[i]
        result = []
        bboxes = bboxes[::-1]
        for i in range(len(bboxes)):
            result.append(bboxes[i].index)
        return result

