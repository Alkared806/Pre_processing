import cv2 as cv
from sys import argv
import os

files_path = argv[1]
os.chdir(files_path)

def add_contrast(img, contrast, art):
    for s in contrast:
        f = 131*(s + 127)/(127*(131-s))
        alpha_c = f
        gamma_c = 127*(1-f)
        buf = cv.addWeighted(img, alpha_c, img, 0, gamma_c)
        cv.imwrite (art.split ('.')[0] + '_contrast' + str(s).replace('.', '') + '.jpg', buf)
    return buf

for art in os.listdir('.'):
    if art.endswith('.jpg'):
        img = cv.imread (art)
        name, ext = art.split('.')
        add_contrast(img, [100], name)