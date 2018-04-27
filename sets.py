def union(set1, set2):
    return set1 + [ x for x in set2 if x not in set1 ]

print "union([1,2,3], [2,3,4]):"
print union([1,2,3], [2,3,4])
print "union([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 10]):"
print union([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 10])

def intersection(set1, set2):
    return [ x for x in set1 if x in set2 ]

print "intersection([1,2,3], [2,3,4]): "
print intersection([1,2,3], [2,3,4])
print "intersection([1,2,3,4], [2,3,4,5]): "
print intersection([1,2,3,4], [2,3,4,5])

def setdiff(set1, set2):
    return [ x for x in set1 if x not in set2 ]

print "setdiff([1,2,3], [2,3,4]):"
print setdiff([1,2,3], [2,3,4])
print "setdiff([2,3,4], [1,2,3]):"
print setdiff([2,3,4], [1,2,3])

def symmdiff(set1, set2):
    return union(setdiff(set1, set2), setdiff(set2, set1))

print "symmdiff([1,2,3], [2,3,4]):"
print symmdiff([1,2,3], [2,3,4])

def cartesian(set1, set2):
    return [ [x,y] for x in set1 for y in set2 ]


print "cartesian([1, 2], ['red', 'white']):"
print cartesian([1, 2], ["red", "white"])
print "cartesian([1, 2, 3], ['red', 'white', 'blue']):"
print cartesian([1, 2, 3], ["red", "white", "blue"])
