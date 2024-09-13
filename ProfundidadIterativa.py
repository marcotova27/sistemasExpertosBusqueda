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

    def ids(self, inicio, objetivo, limite_max):
        def dls_recursivo(nodo, objetivo, limite, visitado, camino):
            if nodo == objetivo:
                return camino
            if limite <= 0:
                return None
            visitado.add(nodo)

            for vecino in self.grafo.get(nodo, []):
                if vecino not in visitado:
                    nuevo_camino = camino + [vecino]
                    resultado = dls_recursivo(vecino, objetivo, limite - 1, visitado, nuevo_camino)
                    if resultado:
                        return resultado
            return None

        for profundidad in range(limite_max + 1):
            resultado = dls_recursivo(inicio, objetivo, profundidad, set(), [inicio])
            if resultado:
                return resultado

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

# Búsqueda iterativa en profundidad (IDS)
inicio = 'CETI'
objetivo = 'Rotonda de los Jaliscienses Ilustres'
limite_max = 5
camino = grafo.ids(inicio, objetivo, limite_max)
print(f"Camino IDS de {inicio} a {objetivo} con límite máximo {limite_max}: {camino}")
