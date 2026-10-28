import networkx as nx
import matplotlib.pyplot as plt
import math

def proyecto():
    try:
        n = int(input("Ubicaciones a considerar: "))
    except ValueError:
        return
    
    vertices = []
    coordenadas = {}
    
    for i in range(n):
        nombre = input(f"Nombre {i+1}: ").strip()
        vertices.append(nombre)
        lat = input(f"Latitud de {nombre}: ").strip()
        lon = input(f"Longitud de {nombre}: ").strip()
        coordenadas[nombre] = (float(lat) if lat else 0.0, float(lon) if lon else 0.0)
        
    grafo = {v: [] for v in vertices}
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    k_vecinos = min(2, n - 1) if n > 1 else 0
    
    for v in vertices:
        dists = []
        for otro in vertices:
            if otro != v:
                c1, c2 = coordenadas[v], coordenadas[otro]
                d = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
                dists.append((d, otro))
        dists.sort(key=lambda x: x[0])
        for i in range(min(k_vecinos, len(dists))):
            vecino = dists[i][1]
            if vecino not in grafo[v]:
                grafo[v].append(vecino)
            if v not in grafo[vecino]:
                grafo[vecino].append(v)

    indice = {v: idx for idx, v in enumerate(vertices)}
    for v1 in grafo:
        for v2 in grafo[v1]:
            matriz[indice[v1]][indice[v2]] = 1
            matriz[indice[v2]][indice[v1]] = 1

    print("\n--- MATRIZ DE ADYACENCIA ---")
    print(f"{'':12}" + "".join([f"{v:>12}" for v in vertices]))
    for i, v1 in enumerate(vertices):
        fila = "".join([f"{matriz[i][j]:>12}" for j in range(n)])
        print(f"{v1:12}" + fila)

    G = nx.Graph()
    for v in vertices:
        G.add_node(v, pos=coordenadas[v])
    for v1 in grafo:
        for v2 in grafo[v1]:
            G.add_edge(v1, v2)
            
    pos = {v: (coordenadas[v][1], coordenadas[v][0]) for v in vertices}
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold', width=2, edge_color='gray')
    plt.title("Grafo de Ubicaciones", fontsize=12, fontweight='bold')
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    proyecto()