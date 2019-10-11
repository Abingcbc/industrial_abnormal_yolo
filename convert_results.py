PATH = 'mAP/input/detection-results/'

with open('darknet/results/comp4_det_test_abnormal.txt', 'r') as src_file:
    for line in src_file:
        olist = line.split(' ')
        str_list = map(str,map(int, map(eval, olist[2:])))
        with open(PATH + olist[0] + '.txt', 'a') as tgt_file:
            tgt_file.write('abnormal ' + olist[1] + ' ' + ' '.join(str_list) + '\n')