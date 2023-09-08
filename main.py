import math
import numpy as np
##import matplotlib as mpl ; ##import matplotlib.pyplot as plt
# numHist = [] ; numHistLen = [] ; plt.xlabel('Steps') ; plt.ylabel('Highest Value') ; plt.title('Collatz Graph')
from pynput.keyboard import *
num = (eval(input("No: ")))
starter = num ; iterations = 0 ; m_rule = 0 ; d_rule = 0 ; complete = False ; a = [0, 0, 0]; counter = 0
def press_on(key):
    if key == Key.esc:
        exit()

def sequence_test():
    global a, counter
    global iterations
    global num
    global d_rule, m_rule
    global complete
    #numHist.append(num)

    while True:
        if num%2 == 0:
            num = (num/2)
            print("=" +str(num))
            d_rule+=1

        if num%2 !=0:
            num = (num*3)+1
            ##  *3+3    ~12,6,3    *3+5      ~20,10,5
            ##  *3+7    ~4,2,1     ~20,10,5  ~28,14,7
            ##  *3+9    ~36,18,9
            print("=" + str(num))
            iterations +=1
            #numHist.append(num)
            m_rule+=1

        with Listener(on_press = press_on) as listener:
            listener.join()

#        a[counter] = num;
#        counter += 1
#        if counter == 3:
#            last = a
#            counter = 0
#            if last == a:
#                exit()==

        if num == 1:
            print('Exit')
            exit()
            complete = True
            print("iterations: " +str(iterations),' ','d',d_rule, ' ', 'm',m_rule,)
            #numHistLen = list(range(1,(iterations +2)))
            ##plt.plot(numHistLen, numHist)
            ##plt.show()
            ##plt.savefig("SequenceResults.pdf")
            ##print(starter) ; sequence_test()

sequence_test()