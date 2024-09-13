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

    def busqueda_bidireccional(self, inicio, objetivo):
        if inicio == objetivo:
            return [inicio]

        visitado_inicio = {inicio}
        visitado_objetivo = {objetivo}
        frontera_inicio = [[inicio]]
        frontera_objetivo = [[objetivo]]

        while frontera_inicio and frontera_objetivo:
            camino_inicio = frontera_inicio.pop(0)
            nodo_inicio = camino_inicio[-1]

            if nodo_inicio in visitado_objetivo:
                return camino_inicio

            for vecino in self.grafo.get(nodo_inicio, []):
                if vecino not in visitado_inicio:
                    nuevo_camino = camino_inicio + [vecino]
                    frontera_inicio.append(nuevo_camino)
                    visitado_inicio.add(vecino)

            camino_objetivo = frontera_objetivo.pop(0)
            nodo_objetivo = camino_objetivo[-1]

            if nodo_objetivo in visitado_inicio:
                return camino_objetivo[::-1]

            for vecino in self.grafo.get(nodo_objetivo, []):
                if vecino not in visitado_objetivo:
                    nuevo_camino = camino_objetivo + [vecino]
                    frontera_objetivo.append(nuevo_camino)
                    visitado_objetivo.add(vecino)

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

# Búsqueda bidireccional
inicio = 'CETI'
objetivo = 'Rotonda de los Jaliscienses Ilustres'
camino = grafo.busqueda_bidireccional(inicio, objetivo)
print(f"Camino bidireccional de {inicio} a {objetivo}: {camino}")
