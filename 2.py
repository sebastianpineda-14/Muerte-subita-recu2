from functools import reduce
nums = [5, 20, 50, 80, 10, 23, 31, 35, 36, 47, 50, 77, 93]

listas=[[1,2,3],[4,5,6],[7,8,9]]
result=list(map((lambda x: reduce((lambda x, y: x if x>y else y),x)),listas))

print (result)
