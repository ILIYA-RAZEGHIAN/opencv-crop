import cv2
import matplotlib.pyplot as plt
image=cv2.imread('enter you photo file location') #'c:/users/iliya/downloads/1.jpg'
plt.imshow(image[:,:,::-1])
plt.show()
sheight,eheight,swidth,ewidth=map(int,input('enter').split())
cropped=image[sheight:eheight,swidth:ewidth,0:3]
cv2.imshow('cropped',cropped)
cv2.waitKey(0)
cv2.imwrite('khar.jpg',cropped)

