import cv2     #untuk install library opencv: sudo apt-get install python-opencv
import numpy as np

imgori = cv2.imread("contoh2.jpg")
img = cv2.imread("contoh2.jpg")

mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1,65), np.float64)
fgdmodel = np.zeros((1,65), np.float64)

rect = (30,30,img.shape[0],img.shape[1])

cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0 ,1).astype('uint8')
img = img*mask2[:,:, np.newaxis]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) #parameter (numpy image, jumlah max corner, ketelitian, kualitas corner, jarak min antar corner)
corners = np.int0(corners)

koordinat_x = []
koordinat_y = []

for corner in corners:
    x, y = corner.ravel()
    koordinat_x.append(x)
    koordinat_y.append(y)
    cv2.circle (img, (x,y), 3, (200,100,100), -1)   #parameter (numpy image, koordinat corner, radius lingkaran, warna BGR, ketebalan lingkaran)

min_x = min(koordinat_x)
max_x = max(koordinat_x)
min_y = min(koordinat_y)
max_y = max(koordinat_y)


print(min_x, min_x + 500, min_y, min_y + 500)

cv2.circle(img, (min_x, min_y), 3, (225, 0,0), -1)
cv2.circle(img, (max_x, max_y), 3, (225, 0,0), -1)

img2 = img[min_x:min_x+500, min_y:min_y+500]

cv2.imshow("image asli", imgori)
cv2.imshow("contoh sblm crop", img)
cv2.imshow("contoh crop", img2)

cv2.waitKey()
cv2.destroyAllWindows()
