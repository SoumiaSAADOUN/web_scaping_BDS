import collections
# Test 02
def intOccurence(theList):
    #print ('Entrer la liste:')
    #theList = [int(x) for x in input().split()] # pour saisir la liste
    count = 0  # the counter to count how many integers we have in the list
    itemsSum =0 # the sum of the integers in the list
    # we iterate over the list
    for i in theList:
        if (type(i) == int):
            count += 1
            itemsSum += i
    print ("The provided list contains {} integer, and their sum is equal to {}".format(count, itemsSum)),
                   
    return count, itemsSum

# Test 03
def persistence():
    print('Enter a number:')
    n = int(input())
    nn= n
    count =0
    while (n>9):
        count += 1
        toStr = str(n)
        mult=1
        for i in str(n):
            mult *= int(i)
        n= mult
    print( "persistence({}) ➞ {}".format(nn, count))   
    return (count)

# Test 04


def integersSum (theList):
    listSum=[]
    occurences = collections.Counter(theList)
    for k,v in occurences.items():
        listSum.append(k*v)    
    return (listSum)