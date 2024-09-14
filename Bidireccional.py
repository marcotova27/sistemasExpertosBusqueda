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

    def busqueda_bidireccional(self, inicio, objetivo):
        if inicio == objetivo:
            return [inicio], 0

        visitado_inicio = {inicio}
        visitado_objetivo = {objetivo}
        frontera_inicio = [[(inicio, 0)]]
        frontera_objetivo = [[(objetivo, 0)]]

        while frontera_inicio and frontera_objetivo:
            # Expansión desde el inicio
            camino_inicio = frontera_inicio.pop(0)
            nodo_inicio, distancia_total_inicio = camino_inicio[-1]

            if nodo_inicio in visitado_objetivo:
                return [n[0] for n in camino_inicio], distancia_total_inicio

            for vecino, distancia in self.grafo.get(nodo_inicio, []):
                if vecino not in visitado_inicio:
                    nuevo_camino = list(camino_inicio)
                    nuevo_camino.append((vecino, distancia_total_inicio + distancia))
                    frontera_inicio.append(nuevo_camino)
                    visitado_inicio.add(vecino)

            # Expansión desde el objetivo
            camino_objetivo = frontera_objetivo.pop(0)
            nodo_objetivo, distancia_total_objetivo = camino_objetivo[-1]

            if nodo_objetivo in visitado_inicio:
                return [n[0] for n in camino_objetivo[::-1]], distancia_total_objetivo

            for vecino, distancia in self.grafo.get(nodo_objetivo, []):
                if vecino not in visitado_objetivo:
                    nuevo_camino = list(camino_objetivo)
                    nuevo_camino.append((vecino, distancia_total_objetivo + distancia))
                    frontera_objetivo.append(nuevo_camino)
                    visitado_objetivo.add(vecino)

        return None, None

# Variables de nodos
nodo_1 = "CETI"
nodo_2 = "Plaza de la Liberación"
nodo_3 = "Teatro Degollado"
nodo_4 = "Templo Expiatorio"
nodo_5 = "Rotonda de los Jaliscienses Ilustres"
nodo_6 = "Instituto Cultural Cabañas"
nodo_7 = "Plaza Tapatía"
nodo_8 = "Parque Revolución"
nodo_9 = "Glorieta La Minerva"

def switch_nodo(nodo_numero):
    return {
        1: nodo_1,
        2: nodo_2,
        3: nodo_3,
        4: nodo_4,
        5: nodo_5,
        6: nodo_6,
        7: nodo_7,
        8: nodo_8,
        9: nodo_9,
    }.get(nodo_numero, None)

def elegir_nodos():
    while True:
        print("\nElige el nodo de inicio:")
        print("1. CETI\n2. Plaza de la Liberación\n3. Teatro Degollado\n4. Templo Expiatorio\n5. Rotonda de los Jaliscienses Ilustres")
        print("6. Instituto Cultural Cabañas\n7. Plaza Tapatía\n8. Parque Revolución\n9. Glorieta La Minerva")

        nodo_inicio = int(input("Ingresa el número del nodo de inicio: "))
        nodo_objetivo = int(input("Ingresa el número del nodo objetivo: "))

        if nodo_inicio == nodo_objetivo:
            print("\nEl nodo de inicio y objetivo no pueden ser el mismo. Inténtalo de nuevo.")
        else:
            return switch_nodo(nodo_inicio), switch_nodo(nodo_objetivo)

# Crear el grafo y añadir aristas
grafo = Grafo()

grafo.agregar_arista(nodo_1, nodo_2, 2)
grafo.agregar_arista(nodo_1, nodo_3, 4)
grafo.agregar_arista(nodo_2, nodo_4, 3)
grafo.agregar_arista(nodo_3, nodo_4, 2)
grafo.agregar_arista(nodo_3, nodo_5, 1)
grafo.agregar_arista(nodo_4, nodo_5, 5)
grafo.agregar_arista(nodo_6, nodo_2, 1)
grafo.agregar_arista(nodo_6, nodo_7, 2)
grafo.agregar_arista(nodo_7, nodo_8, 3)

# Elige nodos de inicio y objetivo
inicio, objetivo = elegir_nodos()

# Ejecuta la búsqueda bidireccional
camino, distancia = grafo.busqueda_bidireccional(inicio, objetivo)

if camino:
    print(f"\nCamino bidireccional de {inicio} a {objetivo}: {camino}, Distancia: {distancia}")
else:
    print(f"\nNo se encontró un camino entre {inicio} y {objetivo}.")
