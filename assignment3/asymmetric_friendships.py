import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA , personB)
    mr.emit_intermediate(personB , personA)

# Part 3
def reducer(A, Afriends):
    friend_count = dict( [ (i, Afriends.count(i)) for i in set(Afriends) ] )
    for friend,count in friend_count.iteritems():
    	if count == 1:
           mr.emit((A, friend))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
