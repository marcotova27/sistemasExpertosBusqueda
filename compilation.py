
class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, nodo1, nodo2):
        # Añadir la arista de nodo1 a nodo2 (si nodo1 no existe en el grafo)
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        if nodo2 not in self.grafo[nodo1]:
            self.grafo[nodo1].append(nodo2)

        # Añadir la arista de nodo2 a nodo1 (si nodo2 no existe en el grafo) - para grafos no dirigidos
        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        if nodo1 not in self.grafo[nodo2]:
            self.grafo[nodo2].append(nodo1)

    def mostrar_grafo(self):
        # Imprime las conexiones de cada nodo en el grafo
        for nodo in self.grafo:
            print(f"{nodo} -> {self.grafo[nodo]}")

    def bfs(self, inicio, objetivo):
        visitado = set()  # Conjunto de nodos visitados para evitar ciclos
        cola = [[inicio]]  # Cola de caminos, inicializada con el nodo de inicio

        if inicio == objetivo:
            return [inicio]  # Si el nodo de inicio es el objetivo, retorna el camino inmediato

        while cola:
            camino = cola.pop(0)  # Extrae el primer camino en la cola
            nodo = camino[-1]  # Último nodo en el camino actual

            if nodo not in visitado:
                # Explora todos los vecinos del nodo actual
                for vecino in self.grafo.get(nodo, []):
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)  # Agrega el nuevo camino a la cola

                    if vecino == objetivo:
                        return nuevo_camino  # Retorna el camino si encuentra el objetivo
                visitado.add(nodo)  # Marca el nodo como visitado

        return None  # Si no se encuentra un camino, retorna None

    def dfs(self, inicio, objetivo):
        visitado = set()  # Conjunto de nodos visitados
        pila = [[inicio]]  # Pila de caminos, inicializada con el nodo de inicio

        if inicio == objetivo:
            return [inicio]  # Si el nodo de inicio es el objetivo, retorna el camino inmediato

        while pila:
            camino = pila.pop()  # Extrae el último camino en la pila
            nodo = camino[-1]  # Último nodo en el camino actual

            if nodo not in visitado:
                # Explora todos los vecinos del nodo actual
                for vecino in self.grafo.get(nodo, []):
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    pila.append(nuevo_camino)  # Agrega el nuevo camino a la pila

                    if vecino == objetivo:
                        return nuevo_camino  # Retorna el camino si encuentra el objetivo
                visitado.add(nodo)  # Marca el nodo como visitado

        return None  # Si no se encuentra un camino, retorna None

    def dls(self, inicio, objetivo, limite):
        # Función auxiliar para realizar la búsqueda recursiva limitada en profundidad
        def dls_recursivo(nodo, objetivo, limite, visitado, camino):
            if nodo == objetivo:
                return camino  # Si se encuentra el objetivo, retorna el camino
            if limite <= 0:
                return None  # Si se llega al límite de profundidad, retorna None
            visitado.add(nodo)

            for vecino in self.grafo.get(nodo, []):
                if vecino not in visitado:
                    nuevo_camino = camino + [vecino]
                    resultado = dls_recursivo(vecino, objetivo, limite - 1, visitado, nuevo_camino)
                    if resultado:
                        return resultado  # Retorna el camino si se encuentra
            return None

        # Llamada inicial a la función recursiva con el límite establecido
        return dls_recursivo(inicio, objetivo, limite, set(), [inicio])

    def ids(self, inicio, objetivo, limite_max):
        # Realiza múltiples búsquedas DLS aumentando el límite de profundidad
        for profundidad in range(limite_max + 1):
            resultado = self.dls(inicio, objetivo, profundidad)
            if resultado:
                return resultado  # Retorna el camino si se encuentra en alguna iteración
        return None  # Si no se encuentra ningún camino, retorna None

    def busqueda_bidireccional(self, inicio, objetivo):
        if inicio == objetivo:
            return [inicio]  # Si el nodo de inicio es el objetivo, retorna el camino inmediato

        # Inicialización de las estructuras para la búsqueda bidireccional
        visitado_inicio = {inicio}  # Nodos visitados desde el inicio
        visitado_objetivo = {objetivo}  # Nodos visitados desde el objetivo
        frontera_inicio = [[inicio]]  # Frontera de caminos desde el inicio
        frontera_objetivo = [[objetivo]]  # Frontera de caminos desde el objetivo

        while frontera_inicio and frontera_objetivo:
            # Expansión desde el inicio
            camino_inicio = frontera_inicio.pop(0)  # Extrae el primer camino de la frontera inicial
            nodo_inicio = camino_inicio[-1]  # Último nodo en el camino actual desde el inicio

            if nodo_inicio in visitado_objetivo:
                return camino_inicio + camino_objetivo[::-1]  # Une los caminos cuando se encuentran

            for vecino in self.grafo.get(nodo_inicio, []):
                if vecino not in visitado_inicio:
                    nuevo_camino = camino_inicio + [vecino]
                    frontera_inicio.append(nuevo_camino)
                    visitado_inicio.add(vecino)

            # Expansión desde el objetivo
            camino_objetivo = frontera_objetivo.pop(0)  # Extrae el primer camino de la frontera del objetivo
            nodo_objetivo = camino_objetivo[-1]  # Último nodo en el camino actual desde el objetivo

            if nodo_objetivo in visitado_inicio:
                return camino_inicio + camino_objetivo[::-1]  # Une los caminos cuando se encuentran

            for vecino in self.grafo.get(nodo_objetivo, []):
                if vecino not in visitado_objetivo:
                    nuevo_camino = camino_objetivo + [vecino]
                    frontera_objetivo.append(nuevo_camino)
                    visitado_objetivo.add(vecino)

        return None  # Si no se encuentra un camino, retorna None


# Interfaz del sistema experto
def sistema_experto_busqueda():
    grafo = Grafo()

    # Añadir nodos que representan locaciones conmemorativas de Guadalajara, Jalisco
    grafo.agregar_arista('CETI', 'Plaza de la Liberación')
    grafo.agregar_arista('CETI', 'Teatro Degollado')
    grafo.agregar_arista('Plaza de la Liberación', 'Templo Expiatorio')
    grafo.agregar_arista('Teatro Degollado', 'Templo Expiatorio')
    grafo.agregar_arista('Teatro Degollado', 'Rotonda de los Jaliscienses Ilustres')
    grafo.agregar_arista('Templo Expiatorio', 'Rotonda de los Jaliscienses Ilustres')
    
    # Añadir nuevos nodos
    grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza de la Liberación')
    grafo.agregar_arista('Instituto Cultural Cabañas', 'Plaza Tapatía')
    grafo.agregar_arista('Plaza Tapatía', 'Parque Revolución')

    print("Grafo:")
    grafo.mostrar_grafo()

    # Selección de algoritmo de búsqueda
    print("\n¿Qué algoritmo de búsqueda te gustaría usar?")
    print("1. Búsqueda en anchura (BFS)")
    print("2. Búsqueda en profundidad (DFS)")
    print("3. Búsqueda en profundidad limitada (DLS)")
    print("4. Búsqueda iterativa en profundidad (IDS)")
    print("5. Búsqueda bidireccional")
    opcion = input("Selecciona el número del algoritmo: ")

    inicio = input("Ingresa el nodo de inicio: ")
    objetivo = input("Ingresa el nodo objetivo: ")

    if opcion == '1':
        camino = grafo.bfs(inicio, objetivo)
        algoritmo = "Búsqueda en anchura (BFS)"
    elif opcion == '2':
        camino = grafo.dfs(inicio, objetivo)
        algoritmo = "Búsqueda en profundidad (DFS)"
    elif opcion == '3':
        limite = int(input("Ingresa el límite de profundidad: "))
        camino = grafo.dls(inicio, objetivo, limite)
        algoritmo = "Búsqueda en profundidad limitada (DLS)"
    elif opcion == '4':
        limite_max = int(input("Ingresa el límite máximo de profundidad: "))
        camino = grafo.ids(inicio, objetivo, limite_max)
        algoritmo = "Búsqueda iterativa en profundidad (IDS)"
    elif opcion == '5':
        camino = grafo.busqueda_bidireccional(inicio, objetivo)
        algoritmo = "Búsqueda bidireccional"
    else:
        print("Opción no válida.")
        return

    # Mostrar el resultado del camino encontrado
    if camino:
        print(f"\nCamino encontrado usando {algoritmo}: {camino}")
    else:
        print(f"\nNo se encontró un camino entre {inicio} y {objetivo}.")


# Ejecutar el sistema experto
if __name__ == "__main__":
    sistema_experto_busqueda()
