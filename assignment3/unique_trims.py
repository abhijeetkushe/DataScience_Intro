import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    sequence_id = record[0]
    nucleotides = record[1][:-10]
    mr.emit_intermediate(nucleotides , sequence_id)

# Part 3
def reducer(nucleotides_trimm, sequence_id):
 mr.emit(nucleotides_trimm)


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
