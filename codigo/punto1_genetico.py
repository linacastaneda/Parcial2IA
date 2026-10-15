"""Punto 1 - Algoritmo genetico para maximizar f(x) = x^2, x en {0,...,31}."""
import random

N_BITS = 5
P_CRUCE = 0.8
P_MUT = 0.05
GENERACIONES = 20
SEMILLA = 42


def decodificar(crom):
    return int(crom, 2)


def aptitud(crom):
    return decodificar(crom) ** 2


def seleccion_ruleta(poblacion):
    aptitudes = [aptitud(c) for c in poblacion]
    total = sum(aptitudes)
    if total == 0:
        return random.choice(poblacion)
    r = random.uniform(0, total)
    acumulado = 0
    for crom, f in zip(poblacion, aptitudes):
        acumulado += f
        if r <= acumulado:
            return crom
    return poblacion[-1]


def cruce_un_punto(p1, p2):
    if random.random() < P_CRUCE:
        punto = random.randint(1, N_BITS - 1)
        return p1[:punto] + p2[punto:], p2[:punto] + p1[punto:]
    return p1, p2


def mutar(crom):
    bits = list(crom)
    for i in range(len(bits)):
        if random.random() < P_MUT:
            bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)


def algoritmo_genetico(poblacion):
    random.seed(SEMILLA)
    historial = []
    for gen in range(1, GENERACIONES + 1):
        elite = max(poblacion, key=aptitud)          # elitismo
        nueva = [elite]
        while len(nueva) < len(poblacion):
            p1 = seleccion_ruleta(poblacion)
            p2 = seleccion_ruleta(poblacion)
            h1, h2 = cruce_un_punto(p1, p2)
            nueva.append(mutar(h1))
            if len(nueva) < len(poblacion):
                nueva.append(mutar(h2))
        poblacion = nueva
        mejor = max(poblacion, key=aptitud)
        historial.append(aptitud(mejor))
        print(f"Gen {gen:2d}: poblacion={poblacion} mejor={mejor} "
              f"x={decodificar(mejor)} f={aptitud(mejor)}")
    mejor = max(poblacion, key=aptitud)
    return mejor, historial


if __name__ == "__main__":
    inicial = ["00101", "01100", "10010", "11001"]
    print("Poblacion inicial:")
    total = sum(aptitud(c) for c in inicial)
    for c in inicial:
        print(f"  {c} -> x={decodificar(c)}, f={aptitud(c)}, p={aptitud(c)/total:.4f}")
    mejor, hist = algoritmo_genetico(inicial)
    print("\nMejor cromosoma final:", mejor)
    print("x =", decodificar(mejor), " aptitud =", aptitud(mejor))
    print("Historial mejor aptitud:", hist)
