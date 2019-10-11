import os
PATH = 'darknet/labels/'
TGT_PATH = 'mAP/input/ground-truth/'
files = os.listdir(PATH)

def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):
    ## remove normalization given the size of the image
    x_c = float(x_c_n) * img_width
    y_c = float(y_c_n) * img_height
    width = float(width_n) * img_width
    height = float(height_n) * img_height
    ## compute half width and half height
    half_width = width / 2
    half_height = height / 2
    ## compute left, top, right, bottom
    ## in the official VOC challenge the top-left pixel in the image has coordinates (1;1)
    left = int(x_c - half_width) + 1
    top = int(y_c - half_height) + 1
    right = int(x_c + half_width) + 1
    bottom = int(y_c + half_height) + 1
    return left, top, right, bottom

for f in files:
    with open(PATH + f, 'r') as src_file:
        with open(TGT_PATH + f, 'w+') as tgt_file:
            for line in src_file:
                olist = line.split(' ')
                left, top, right, bottom = convert_yolo_coordinates_to_voc(float(olist[1]), 
                float(olist[2]), float(olist[3]), float(olist[4]), 2448, 2048)
                tgt_file.write('abnormal ' +  ' ' + str(left) + ' ' + str(top) +
                ' ' + str(right) + ' ' + str(bottom) + '\n')