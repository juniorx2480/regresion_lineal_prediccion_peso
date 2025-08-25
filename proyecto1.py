import heapq

CAP4, CAP5 = 4, 5
objetivo = 2

# funcion heuristica
def heuristica(estado):
    
    return abs(estado[1] - objetivo)

def sucesores(estado):
    j4, j5 = estado
    res = []

    # llenar jarra 4
    if j4 < CAP4:
        res.append(((CAP4, j5), "llenar jarra 4 :)"))
    # llenar jarra 5
    if j5 < CAP5:
        res.append(((j4, CAP5), "llenar jarra 5 :)"))

    # vaciar jarra 4
    if j4 > 0:
        res.append(((0, j5), "vaciar jarra 4 :("))
    # vaciar jarra 5
    if j5 > 0:
        res.append(((j4, 0), "vaciar jarra 5 :("))

    # verter jarra 4 en jarra 5
    if j4 > 0 and j5 < CAP5:
        t = min(j4, CAP5 - j5)
        res.append(((j4 - t, j5 + t), "verter de 4 a 5 :3"))

    # verter jarra 5 en jarra 4
    if j5 > 0 and j4 < CAP4:
        t = min(j5, CAP4 - j4)
        res.append(((j4 + t, j5 - t), "verter de 5 a 4 :3"))

    return res

# algoritmo de busqueda best first
def best_first():
    

    return 

# funcion main
def main():
    ini = (0, 0)  # las dos jarras empiezan vacias :(
    camino, acciones = best_first(ini)

    if camino:
        print("solucion encontrada :) \n")
        for i, (s, acc) in enumerate(zip(camino[1:], acciones), 1):
            print(f"paso {i}: {acc} -> estado {s}")
    else:
        print("no se encontro solucion :(")

# punto de entrada
if __name__ == "__main__":
    main()
