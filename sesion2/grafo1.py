grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

def contar_vertices(grafo):
    return len(grafo)


def contar_aristas(grafo):
    total = 0

    for vecinos in grafo.values():
        total += len(vecinos)

    return total // 2


def estan_conectados(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False

    return destino in grafo[origen]


def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def agregar_arista(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False

    if origen == destino:
        return False

    if destino not in grafo[origen]:
        grafo[origen].append(destino)

    if origen not in grafo[destino]:
        grafo[destino].append(origen)

    return True


def recorrido_amplitud(grafo, inicio):
    if inicio not in grafo:
        return []

    visitados = [inicio]
    cola = [inicio]
    recorrido = []

    while cola:
        actual = cola.pop(0)
        recorrido.append(actual)

        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return recorrido



def existe_ruta(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return False

    if origen == destino:
        return True

    visitados = [origen]
    cola = [origen]

    while cola:
        actual = cola.pop(0)

        for vecino in grafo[actual]:
            if vecino == destino:
                return True

            if vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return False



print("========== RETO 1 ==========")
print("Cantidad de vértices:", contar_vertices(grafo))
print("Cantidad de aristas:", contar_aristas(grafo))

print("\n========== RETO 2 ==========")
print("A y B conectados:", estan_conectados(grafo, "A", "B"))
print("A y F conectados:", estan_conectados(grafo, "A", "F"))
print("X y A conectados:", estan_conectados(grafo, "X", "A"))

print("\n========== RETO 3 ==========")
agregar_vertice(grafo, "G")
agregar_arista(grafo, "F", "G")

print("Vecinos de F:", grafo["F"])
print("Vecinos de G:", grafo["G"])

print("\n========== RETO 4 ==========")
print("Recorrido desde A:", recorrido_amplitud(grafo, "A"))

print("\n========== RETO 5 ==========")
print("Existe ruta de A a F:", existe_ruta(grafo, "A", "F"))
print("Existe ruta de A a A:", existe_ruta(grafo, "A", "A"))
print("Existe ruta de A a X:", existe_ruta(grafo, "A", "X"))