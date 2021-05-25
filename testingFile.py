from  functional import *
import collections

a =[1,2,3,8,4,5,6,3,2,1,8,9]
b =[1,2,"3",8,4,5,6,3,"2",1,8,9]

# Test 2
print("=> Test 2 (integers sum) ")  
print(a),
intOccurence(a),
print(b),
intOccurence(b)
# Test 3
print("=> Test 3 (persistence)")
persistence()
#Test 4
print("=> Test 4 (the sum of the numbers that repeat consecutively)")
print(a),
print ("sum_consecutives ({} ➞ {}) ".format(a, integersSum(a))),
