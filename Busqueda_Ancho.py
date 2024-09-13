class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        self.grafo[nodo1].append(nodo2)

        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo2].append(nodo1)

    def bfs(self, inicio, objetivo):
        visitado = set()
        cola = [[inicio]]

        if inicio == objetivo:
            return [inicio]

        while cola:
            camino = cola.pop(0)
            nodo = camino[-1]

            if nodo not in visitado:
                for vecino in self.grafo.get(nodo, []):
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)

                    if vecino == objetivo:
                        return nuevo_camino
                visitado.add(nodo)

        return None

grafo = Grafo()
# Agregar nodos
grafo.agregar_arista('CETI', 'Plaza de la Liberación')
grafo.agregar_arista('CETI', 'Teatro Degollado')
grafo.agregar_arista('Plaza de la Liberación', 'Templo Expiatorio')
grafo.agregar_arista('Teatro Degollado', 'Templo Expiatorio')
grafo.agregar_arista('Teatro Degollado', 'Rotonda de los Jaliscienses Ilustres')
grafo.agregar_arista('Templo Expiatorio', 'Rotonda de los Jaliscienses Ilustres')
grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza de la Liberación')
grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza Tapatía')
grafo.agregar_arista('Plaza Tapatía', 'Parque Revolución')

# Búsqueda en anchura (BFS)
inicio = 'CETI'
objetivo = 'Rotonda de los Jaliscienses Ilustres'
camino = grafo.bfs(inicio, objetivo)
print(f"Camino BFS de {inicio} a {objetivo}: {camino}")
