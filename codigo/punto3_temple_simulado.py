"""Punto 3 - Temple simulado para minimizar E(x) = x^2, x en {-5,...,5}."""
import math
import random

X_MIN, X_MAX = -5, 5
X0 = 5
T0 = 10.0
ALFA = 0.90
ITERACIONES = 100
SEMILLA = 42


def energia(x):
    return x ** 2


def vecino_aleatorio(x):
    vecinos = [v for v in (x - 1, x + 1) if X_MIN <= v <= X_MAX]
    return random.choice(vecinos)


def temple_simulado():
    random.seed(SEMILLA)
    actual, T = X0, T0
    mejor = actual
    historial = []   # (iteracion, T, x_actual, E_actual, mejor, E_mejor)
    for k in range(1, ITERACIONES + 1):
        candidato = vecino_aleatorio(actual)
        dE = energia(candidato) - energia(actual)
        if dE <= 0:
            actual = candidato
        else:
            u = random.random()
            if u < math.exp(-dE / T):
                actual = candidato
        if energia(actual) < energia(mejor):
            mejor = actual
        historial.append((k, T, actual, energia(actual), mejor, energia(mejor)))
        T *= ALFA
    return mejor, historial


if __name__ == "__main__":
    # Parte A: los tres casos
    for nombre, xa, xc, T, u in [("A", 3, 2, 5, 0.70), ("B", 2, 3, 5, 0.30), ("C", 2, 3, 1, 0.30)]:
        dE = energia(xc) - energia(xa)
        p = 1.0 if dE <= 0 else math.exp(-dE / T)
        decision = "acepta" if (dE <= 0 or u < p) else "rechaza"
        print(f"Caso {nombre}: dE={dE}, P={p:.4f}, u={u} -> {decision}")

    mejor, hist = temple_simulado()
    print(f"\n{'k':>3} {'T':>9} {'x':>3} {'E':>3} {'mejor':>5} {'E_mejor':>7}")
    for k, T, x, E, m, Em in hist:
        print(f"{k:>3} {T:>9.5f} {x:>3} {E:>3} {m:>5} {Em:>7}")
    print(f"\nMejor solucion: x = {mejor}, energia minima = {energia(mejor)}")
