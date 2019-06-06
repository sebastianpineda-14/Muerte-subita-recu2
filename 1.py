lista2=[[8,5,7,98,5],[3,5,7,98,345],[898,5,7,98,12333]]
        
proceso1 = list(   map(lambda x: x[0],lista2)  )
proceso2 = list(   map(lambda x: x[4],lista2)  )

print("primeros:")
print(proceso1)
print("ultimos:")
print(proceso2)
