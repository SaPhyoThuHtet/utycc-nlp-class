import sys
sentence = ''
with open(sys.argv[1],'r') as file:
    for i in file:
        
            data = i.split()
            if (len(data) != 0):
                if(data[-1] =='E'):
                    sentence += data[0]+" "
                else:
                    sentence += data[0]
               
                
            else:
                print(sentence)
                sentence = ''
            
