import MapReduce
import sys

mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    matrix = record[0]
    i = int(record[1])
    j = int(record[2])
    value = record[3]

    for k in range(5):
        if matrix == 'a':
           mr.emit_intermediate((i,k) , ('a',j , value))
        else:
           mr.emit_intermediate((k,j) , ('b',i , value))
             

# Part 3
def reducer(key, list_of_values):
    vectorA=[0, 0, 0, 0, 0]  
    vectorB =[0, 0, 0, 0, 0]
    for m,k, value in list_of_values:
        if m == 'a':
           vectorA.insert(k, value)
        else:
           vectorB.insert(k, value)  

    sum = 0

    for k in range(5):
        sum += vectorA[k] * vectorB[k]
    mr.emit((key[0], key[1], sum))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
