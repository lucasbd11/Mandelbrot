import numpy as np
from PIL import Image
import cmath as cpx



def is_bounded(SIZE_HEIGHT,SIZE_WIDTH,INTERVAL_REAL,INTERVAL_COMPLEX):
    
    def check_bound(c):
        z = 0
        count = 0
        while count < 30 and cpx.polar(z)[0] < 2:
            z = z**2 + c
            count += 1
        if count == 30:
            return True,count
        else:
            return False,count
    
    
    step_real = (INTERVAL_REAL[1]-INTERVAL_REAL[0])/SIZE_WIDTH
    step_complex = (INTERVAL_COMPLEX[1]-INTERVAL_COMPLEX[0])/SIZE_HEIGHT
    

    c = complex(INTERVAL_REAL[0],INTERVAL_COMPLEX[1])
    
    for y in range(SIZE_HEIGHT):
        for x in range(SIZE_WIDTH):
            result,color_multi = check_bound(c)
            yield result,y,x,color_multi
            c = complex(INTERVAL_REAL[0]+step_real*x,INTERVAL_COMPLEX[1]-step_complex*y)

        if y%(SIZE_HEIGHT/20) == 0:
            print("progress: "+str(y//SIZE_HEIGHT*100)+"%")


SIZE_HEIGHT = 1000
SIZE_WIDTH = 1000
INTERVAL_REAL = [-1,1]
INTERVAL_COMPLEX = [-1,1]
SAVE_PATH = "C:/example/mandelbrot.png" #edit here the location where the file will by saved



image_data = np.zeros((SIZE_HEIGHT, SIZE_WIDTH, 3), dtype=np.uint8)
image_data.fill(255)


for i in is_bounded(SIZE_HEIGHT,SIZE_WIDTH,INTERVAL_REAL,INTERVAL_COMPLEX):
    # if i[0]:
    #     image_data[i[1], i[2]] = [0,0,0]

    color = np.array([255,255,255])-8.5*i[3]
    image_data[i[1], i[2]] = color



image = Image.fromarray(image_data)
#image.save(SAVE_PATH)
image.show()
