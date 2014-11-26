import MapReduce
import sys
import itertools

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    personA = record[0]
    personB = record[1]
    friends = [personB]
    mr.emit_intermediate(personA, friends)

# Part 3
def reducer(key, list_of_values):
    friends_count = len(list(itertools.chain(*list_of_values)))
    mr.emit((key, friends_count))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
