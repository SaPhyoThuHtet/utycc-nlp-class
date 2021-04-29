import sys

with open(sys.argv[1],'r') as user_input_file:
    with open (sys.argv[2],'r') as crf_predict_file:
        for i,j in zip (user_input_file,crf_predict_file):
            if i == j:
                print(i)
            else:
                print(i)
                print('<',j,'>')
