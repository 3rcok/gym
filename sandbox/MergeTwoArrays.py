#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      used to test if file names ended with 'bat or ext'
#
# Author:      wanglei2
#
# Created:     27/05/2011
# Copyright:   (c) wanglei2 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    array6 = [1, 3, 4, 8, 20, 32]
    array4 = [14, 16, 17, 21, 39,-1,-1, -1, -1, -1, -1]
    #array2 = [2, 5, 8, 20, 32]
    array8NoDuplicate = [2, 5, 7, 14, 15, 30, 31, 38, -1,-1, -1, -1, -1, -1]
    array4NoDuplicate = [2, 5, 7, 14, -1,-1, -1, -1, -1, -1]
    array4Duplicate = [2, 4, 7, 14, -1,-1, -1, -1, -1, -1]
    array8Duplicate1 = [2, 4, 7, 14, 15, 30, 31, 38, -1,-1, -1, -1, -1, -1]
    array10Duplicate2 = [2, 4, 8, 14, 15, 30, 31, 32, -1,-1, -1, -1, -1, -1]



def mergeArray(a1, a2):
    lenA1 = len(a1)
    lenA2 = len(a1)
    print("start merging two arrays")
    print("First array:" + a1)
    print("Second array:" + a2)
    print("a1 length " + lenA1)
    print("a2 length " + lenA2)
    if lenA1 <= lenA2:
        raise ValueError("one of the arrays need be longer than the other")
    else:
        lenA2Filled = lenA2 - lenA1
    k = lenA2-1
    for i in range(lenA1-1,0,-1):
        for j in range(lenA2Filled-1,0,-1):

            if a1[i] > a2[j]:
                a2[k]= a1[i]
                k=k-1
                i--
            elif a1[i] = a2[j]:
                a2[k]=a1[i]
                a2[k-1]=a1[i]
                i--
                j--
                k--
            else:
                a2[k]=a2[j]
                k--
                j--








    return

if __name__ == '__main__':
    main()