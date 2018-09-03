from os import listdir
from os.path import isfile, join
import cv2
path = "D:\\FOTO DATA SKRIPSI\\"
for folder in listdir(path):
    pathtofolder_eachImage = join(path, folder)
    idImage = [0, 0, 0, 0]
    for image in listdir(pathtofolder_eachImage):
        idImage[0] += 1
        for i in range(len(idImage)):
            if idImage[i] > 9:
                idImage[i] = 0
                if i != len(idImage)-1:
                    idImage[i+1] += 1
        strId = ''
        for f in reversed(idImage):
            strId += str(f)
        path_to_image = join(pathtofolder_eachImage, image)
        img = cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED)
        new_name = folder+'_'+strId+'_'+'SAMSUNGJ7PRIME.jpg'
        path_to_save = join(pathtofolder_eachImage, new_name)
        print(path_to_save)
        cv2.imwrite(path_to_save, img)
cv2.destroyAllWindows()
