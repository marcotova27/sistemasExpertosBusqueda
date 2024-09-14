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

    def dls(self, inicio, objetivo, limite):
        def dls_recursivo(nodo, objetivo, limite, visitado, camino, distancia_total):
            if nodo == objetivo:
                return camino, distancia_total
            if limite <= 0:
                return None, None
            visitado.add(nodo)

            for vecino, distancia in self.grafo.get(nodo, []):
                if vecino not in visitado:
                    nuevo_camino = camino + [vecino]
                    resultado, distancia_final = dls_recursivo(vecino, objetivo, limite - 1, visitado, nuevo_camino, distancia_total + distancia)
                    if resultado:
                        return resultado, distancia_final
            return None, None

        return dls_recursivo(inicio, objetivo, limite, set(), [inicio], 0)

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

# Búsqueda en profundidad limitada (DLS) con un límite de 3
inicio = 'CETI'
objetivo = 'Rotonda de los Jaliscienses Ilustres'
limite = 3
camino, distancia = grafo.dls(inicio, objetivo, limite)
print(f"Camino DLS de {inicio} a {objetivo} con límite {limite}: {camino}, Distancia: {distancia}")
