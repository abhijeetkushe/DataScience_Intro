import MapReduce
import sys
import itertools

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # table: table name
    # order_id: document contents
  
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

# Part 3
def reducer(key, list_of_values):
    orderValues = []
    for value in list_of_values:
        if value[0] == 'order':
           orderValues = value
    for value in list_of_values:
        if value[0] == "line_item":
           tuples = orderValues[:]
           tuples.extend(value)
           mr.emit(tuples)


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
