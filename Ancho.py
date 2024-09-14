class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2, distancia):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        self.grafo[nodo1].append((nodo2, distancia))

        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo2].append((nodo1, distancia))

    def bfs(self, inicio, objetivo):
        visitado = set()
        cola = [[(inicio, 0)]]

        if inicio == objetivo:
            return [inicio], 0

        while cola:
            camino = cola.pop(0)
            nodo, distancia_total = camino[-1]

            if nodo not in visitado:
                for vecino, distancia in self.grafo.get(nodo, []):
                    nuevo_camino = list(camino)
                    nuevo_camino.append((vecino, distancia_total + distancia))
                    cola.append(nuevo_camino)

                    if vecino == objetivo:
                        return [n[0] for n in nuevo_camino], nuevo_camino[-1][1]
                visitado.add(nodo)

        return None, None

# Crear el grafo
grafo = Grafo()

# Agregar nodos con distancias
grafo.agregar_arista('CETI', 'Plaza de la Liberación', 2)
grafo.agregar_arista('CETI', 'Teatro Degollado', 4)
grafo.agregar_arista('Plaza de la Liberación', 'Templo Expiatorio', 3)
grafo.agregar_arista('Teatro Degollado', 'Templo Expiatorio', 2)
grafo.agregar_arista('Teatro Degollado', 'Rotonda de los Jaliscienses Ilustres', 1)
grafo.agregar_arista('Templo Expiatorio', 'Rotonda de los Jaliscienses Ilustres', 5)
grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza de la Liberación', 1)
grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza Tapatía', 2)
grafo.agregar_arista('Plaza Tapatía', 'Parque Revolución', 3)

# Búsqueda en anchura (BFS) con inicio y objetivo diferentes
inicio = 'Instituto Cultural Cabañas'
objetivo = 'Templo Expiatorio'
camino, distancia = grafo.bfs(inicio, objetivo)
print(f"Camino BFS de {inicio} a {objetivo}: {camino}, Distancia: {distancia}")
