from datetime import datetime
import time


def partition(limit):
    u_limit_list = []
    l_limit_list = []
    for i in range(1,limit):
        mid = limit/2
        if(i >= mid):
            u_limit_list.append(i)
        elif(i < mid):
            l_limit_list.append(i)
    return (u_limit_list,l_limit_list)

    
def printRandU(ul):
    # get the time in microsecond and generate the random index using mod
    now = datetime.now()
    now = int(now.microsecond)
    uIndex = now % len(ul)
    print("Upper Range Value "+  str(ul[uIndex]))


    
    
def printRandL(ll):
    # get the time in microsecond and generate the random index using mod
    now = datetime.now()
    now = int(now.microsecond)
    lIndex = now % len(ll)
    print("Lower Range Value " +  str(ll[lIndex]))
   
   

if __name__ == "__main__":
    uFactor = 0.73 # upper limit bias
    lFactor = 0.27 # lower limit bias
    rangeW,times = input().split() # input range limit and no of times you want the numbers to printed
    times = int(times)
    rangeW = int(rangeW)
    ul, ll = partition(rangeW+1) # split the range of number in upper and lower half
    ucount = 0
    lcount = 0
    for i in range(int(times*uFactor)+1): # print the random number from upper list using upper limit bias
        time.sleep(1) # added a sleep of 1 second to get the different value of microsecond
        printRandU(ul)
    for j in range(int(times*lFactor)+1): # print the random number from lower list using lower limit bias
        time.sleep(1) # added a sleep of 1 second to get the different value of microsecond
        printRandL(ll)
  


        
    
    
