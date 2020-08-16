
import math
import sys
import re

"""
The main function to implement dynamic programming
"""
def solveWordWrap(fulltxt,wordLength, n, width):
    val=[[0 for i in range(1,n+1)] for i in range(1,n+1)]

    for i in range(0,n):
        for j in range(i,n):
            if i==j:
                val[i][j]=width-wordLength[j]
            else:
                val[i][j]=val[i][j-1]-wordLength[j]-1

    cost = [[0 for i in range(1, n + 1)] for i in range(1, n + 1)]

    for i in range(0,n):
        for j in range(i,n):
            if val[i][j]>=0 and j==n-1:
                cost[i][j]=0
            elif val[i][j]<0:
                cost[i][j]=math.inf
            else:
                cost[i][j]=val[i][j]

    """
    this array represents total cost from word 1 to word j
    """
    total=[math.inf for i in range(0,n+1)]
    total[0]=0

    """
    using pointer to keep track of the final result
    """
    pointer=[0 for i in range(0,n+1)]

    for column in range(0,n):
        for row in range(0,column+1):
            if total[row]!=math.inf and cost[row][column]!=math.inf and total[row]+cost[row][column]<total[column+1]:
                total[column+1]=total[row]+cost[row][column]
                pointer[column+1]=row+1
    showResult(fulltxt,pointer, n)


"""
print the neatly printed paragraph
using recursive method
"""
def showResult(fulltxt,pointer,index):
    if pointer[index]==1:
        # print((pointer[index],index))
        if pointer[index]==index:
            print(fulltxt[index-1])
        else:
            for i in range(pointer[index],index+1):
                print(fulltxt[i-1],end="")
                if i==index:
                    print(" ")
                else:
                    print(" ",end="")
        return
    else:
        showResult(fulltxt,pointer,pointer[index]-1)
        # print((pointer[index],index))
        if pointer[index]==index:
            print(fulltxt[index-1])
        else:
            for i in range(pointer[index],index+1):
                print(fulltxt[i-1],end="")
                if i == index:
                    print(" ")
                else:
                    print(" ", end="")

"""
pre-process the paragraph
we only care about the word
so we should filter the noises
such as comma and other symbols
"""
def processData():
    fulltxt=[]

    """
    give the file name which needs to be printed
    """
    filename = sys.argv[1] + '.txt'
    with open(filename) as f:
        for line in f:
            word1 = " ".join(re.findall("[a-zA-Z]+", line))
            data=word1.split()
            fulltxt.extend(data)
    count=[]
    for i in range(0,len(fulltxt)):
        count.append(len(fulltxt[i]))

    """
    fulltxt returns the content of the paragraph
    count returns each length of the paragraph
    """
    return fulltxt,count

def main():
    fulltxt,count=processData()

    """
    the width per line needs to be provided
    """
    width = int(sys.argv[2])
    n = len(count)
    solveWordWrap(fulltxt,count, n, width)

    # counter = 0
    # if len(count) < 2000:
    # else:
    #     n = len(fulltxt[:50])
    #     solveWordWrap(fulltxt[:50], count[:50], n, width)
    #     for i in range(0,len(count)):
    #         counter+=1
    #         if counter==50:
    #             counter=0
    #             first=fulltxt[i:i+50]
    #             second=count[i:i+50]
    #             n = len(second)
    #             solveWordWrap(first, second, n, width)

if __name__ == '__main__':
    main()
