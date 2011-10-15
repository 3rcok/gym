#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      How will you merge two sorted arrays. This is a question from Java world.
#               The first array has enough empty spaces to accomodate the second array.
#               http://www.careercup.com/question?id=2168
# Author:      wanglei2
#
# Created:     27/05/2011
# Copyright:   (c) wanglei2 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# TODO: using logging, testsuit
# Each test should have comment on the test case
# Is there a way to set up those lists instead of duplicated code in the test method?
# How to print red line for failure?
#!/usr/bin/env python

def main():

    test1()
    test2()
    test3()
    test4()

def test1():
    array6 = [10, 20, 32, 33, 34,35]
    array5 = [14, 16, 17, 21, 39]
    array2 = [2, 5, 8]
    array3 = [15,40, 43,88]
    array4 = [40, 43,88]
    array8NoDuplicate = [2, 5, 7, 14, 15, 30, 31, 38]
    array4NoDuplicate = [2, 5, 7, 14]
    array4Duplicate = [2, 4, 7, 14]
    array8Duplicate1 = [2, 4, 7, 14, 15, 30, 31, 38]
    array10Duplicate2 = [2, 4, 8, 14, 15, 30, 31, 32]
    mergeArrayStart(array6, array4Duplicate)

def test2():
    array6 = [10, 20, 32, 33, 34,35]
    array5 = [14, 16, 17, 21, 39]
    array2 = [2, 5, 8]
    array3 = [15,40, 43,88]
    array4 = [40, 43,88]
    array8NoDuplicate = [2, 5, 7, 14, 15, 30, 31, 38]
    array4NoDuplicate = [2, 5, 7, 14]
    array4Duplicate = [2, 4, 7, 14]
    array8Duplicate1 = [2, 4, 7, 14, 15, 30, 31, 38]
    array10Duplicate2 = [2, 4, 8, 14, 15, 30, 31, 32]
    mergeArrayStart(array6, array2)


def test3():
    array6 = [10, 20, 32, 33, 34,35]
    array5 = [14, 16, 17, 21, 39]
    array2 = [2, 5, 8]
    array3 = [15,40, 43,88]
    array4 = [40, 43,88]
    array8NoDuplicate = [2, 5, 7, 14, 15, 30, 31, 38]
    array4NoDuplicate = [2, 5, 7, 14]
    array4Duplicate = [2, 4, 7, 14]
    array8Duplicate1 = [2, 4, 7, 14, 15, 30, 31, 38]
    array10Duplicate2 = [2, 4, 8, 14, 15, 30, 31, 32]
    mergeArrayStart(array6, array3)
def test4():
    array6 = [10, 20, 32, 33, 34,35]
    array5 = [14, 16, 17, 21, 39]
    array2 = [2, 5, 8]
    array3 = [15,40, 43,88]
    array4 = [40, 43,88]
    array8NoDuplicate = [2, 5, 7, 14, 15, 30, 31, 38]
    array4NoDuplicate = [2, 5, 7, 14]
    array4Duplicate = [2, 4, 7, 14]
    array8Duplicate1 = [2, 4, 7, 14, 15, 30, 31, 38]
    array10Duplicate2 = [2, 4, 8, 14, 15, 30, 31, 32]
    mergeArrayStart(array6, array4)

def mergeArrayStart(a1, a2):
    print("mergeArrayStart")
    print("First array:",a1, "Lengh:", len(a1) )
    print("Second array:",a2,"Lengh:", len(a2))

    result1 = mergeArrayUsingSort(a1,a2)

    if len(a1)<=len(a2):
        result2 = mergeArray(a1, a2)
    else:
        result2 = mergeArray(a2, a1)


    print("Test Result:",result2, "Lengh:", len(a1))

    if result1==result2:
        print("Test Succeeded!")
    else:
        print("Test Failed!")


def mergeArrayUsingSort(fArray, sArray):
    sArray = sArray+fArray
    sArray.sort()
    print("Expected Result:",sArray,"Lengh:", len(sArray) )
    return sArray


#if the two array have same length, then the order doesn't matter
#otherwise, we want the first array to be the shorter one
def mergeArray(fArray, sArray):
    print("fArray:",fArray)
    print("sArray:",sArray)

    if len(fArray) == 0:
        return sArray
    if len(sArray) == 0:
        return fArray

    j = 0
    for index, v in enumerate(fArray):
        if v >= sArray[-1]:
            return sArray + fArray[index:]
        elif fArray[-1] <= sArray[j]:
            sArray[j:j]=fArray[index:]
            return sArray
        else:
            if j == len(sArray):
                sArray.expand(fArray[index:])
                return sArray
            if v < sArray[j]:
                sArray.insert(j,v)
                j += 1
            elif v == sArray[j]:
                sArray.insert(j,v)
                j += 1
            else:
                while v > sArray[j]:
                    j +=1
                    if v < sArray[j]:
                        sArray.insert(j,v)
                    elif v == sArray[j]:
                        sArray.insert(j,v)
                    j += 1
    return sArray

if __name__ == '__main__':
    main()