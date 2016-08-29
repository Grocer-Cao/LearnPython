i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

print "======================="
test = []
for i in range(0, 20):
    test.append(i)
    i = i + 1

print "%s" % test
print "======================="

tst = []
i = 0
while i < 15:
    tst.append(i)
    i += 1
print "%s" % tst
