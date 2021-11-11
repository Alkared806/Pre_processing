from sys import argv
import os
import skimage
from skimage import io
import numpy as np

files_path = argv[1]
os.chdir(files_path)

def add_noise(img, coeff, name):
    for s in coeff:
        temp = skimage.util.random_noise(img,mode="s&p",seed=None, clip=True, amount = s)
        io.imsave(name + '_noise' + str(s).replace('.', '') + '.jpg', temp)


for art in os.listdir('.'):
    if art.endswith('.jpg'):
        img = io.imread (art)
        img = np.array (img)
        name, ext = art.split('.')
        add_noise(img, [0.2, 0.15, 0.25], name)