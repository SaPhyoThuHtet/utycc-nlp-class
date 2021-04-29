import sys
import re

with open(sys.argv[1],'r') as file:
    for i in file:
        #print(i)
        
        for ii in i.strip().split(" "):
             line = re.sub(r'([က-အ|ဥ|ဦ]([က-အ][့း]*[်]|္[က-အ]|[ါ-ှ]){0,}|.)',r'\1 ',ii)
             
             if(len(line.split()) == 1):
                 iii = line.split()
                 print(iii[0],'\t0')
             
             else:
                 #print(len(line.split()))
                 count = 0
                 for iii in line.split():
                      #print(iii,'......')
                      
                      if (count == len(line.split())-1):
                          print(iii,'\t0')
                          
                      else:
                          print(iii,'\t0')
                          count = count+1                

        print()

