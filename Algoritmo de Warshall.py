grafo=[
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
]

def warshall(grafo):
    n= len(grafo)
    buscar= [fila[:] for fila in grafo ]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                buscar[i][j]= buscar[i][j] or (buscar[i][k] and buscar[k][j])
    
    return buscar
matriz_accesible= warshall(grafo)
print("Matriz de cerradura transitiva: ")
for fila in matriz_accesible:
    print(fila)