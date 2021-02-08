
# Print 0-150

for i in range(151):
    print(i)

#Print multiples of 5 from 5-5000

for i in range(5,5001,5):
    print(i)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(1,100,1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#Add odd integers from 0 to 500,000, and print the final sum.


def sumOdds():
    sum = 0
    for i in range(500000):
        if i % 2 != 0:
            sum += i
    return sum

print(sumOdds())

#Print positive numbers starting at 2018, counting down by fours.

def countDownPositives():
    for i in range(2018,0,-4):
        print(i)

countDownPositives()

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def getMultiples(low_num, high_num, mult):
    for i in range(low_num, high_num+1):
        if i % mult == 0:
            print(i)

getMultiples(0,10,2)
getMultiples(2,9,3)