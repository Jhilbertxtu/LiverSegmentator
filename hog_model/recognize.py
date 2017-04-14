import cv2
import numpy as np
from imutils import paths
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

from hog_model import hog

TRAINING_LIVER = "C:/Users/acer/Desktop/TestSamples/ML-Dataset/LBP_Texture/liver/training/"
TRAINING_NONLIVER = "C:/Users/acer/Desktop/TestSamples/ML-Dataset/LBP_Texture/non-liver/training/"
TESTING = "C:/Users/acer/Desktop/TestSamples/ML-Dataset/LBP/non-liver/testing/"

desc = hog.HistOrientGrad(9, (2,2), (3,3))
data = []
labels = []

hist, img = desc.describe(cv2.imread("C:/Users/acer/Desktop/TestSamples/ML-Dataset/CT_SCAN/testing/"+'scan6.jpg',0))
print(hist[0])
cv2.imwrite('C:/Users/acer/Desktop/TestSamples/hogTest.jpg',img)
cv2.waitKey(0)