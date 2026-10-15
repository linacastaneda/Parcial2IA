"""Punto 4 - Modelo simplificado de ACO con tres rutas de A a Z."""
import random

RUTAS = {"A-B-Z": 6, "A-C-Z": 8, "A-D-Z": 10}
HORMIGAS = 10
ITERACIONES = 20
ALFA, BETA = 1, 2
RHO = 0.2
Q = 10
SEMILLA = 42


def probabilidades(feromonas):
    pesos = {r: (feromonas[r] ** ALFA) * ((1 / L) ** BETA) for r, L in RUTAS.items()}
    total = sum(pesos.values())
    return {r: w / total for r, w in pesos.items()}


def aco():
    random.seed(SEMILLA)
    tau = {r: 1.0 for r in RUTAS}
    frecuencias = {r: 0 for r in RUTAS}
    mejor_ruta, mejor_L = None, float("inf")
    nombres = list(RUTAS)
    for it in range(1, ITERACIONES + 1):
        p = probabilidades(tau)                                   # 1. probabilidades
        elecciones = random.choices(nombres, weights=[p[r] for r in nombres], k=HORMIGAS)  # 2.
        for r in tau:                                             # 3. evaporacion
            tau[r] *= (1 - RHO)
        for r in elecciones:                                      # 4. deposito
            tau[r] += Q / RUTAS[r]
            frecuencias[r] += 1
            if RUTAS[r] < mejor_L:
                mejor_ruta, mejor_L = r, RUTAS[r]
        conteo = {r: elecciones.count(r) for r in nombres}
        print(f"It {it:2d}: p=" + ", ".join(f"{r}:{p[r]:.3f}" for r in nombres)
              + f" | elecciones={conteo} | tau=" + ", ".join(f"{r}:{tau[r]:.3f}" for r in nombres))
    return frecuencias, tau, mejor_ruta, mejor_L


if __name__ == "__main__":
    # Parte A
    d = {"B": 2, "C": 4, "D": 5}
    t = {"B": 1, "C": 2, "D": 1}
    w = {j: t[j] ** ALFA * (1 / d[j]) ** BETA for j in d}
    s = sum(w.values())
    for j in d:
        print(f"A->{j}: peso={w[j]:.4f}, p={w[j]/s:.4f}")
    nuevas = {j: (1 - RHO) * t[j] + (Q / 10 if j == "B" else 0) for j in d}
    print("Feromonas actualizadas:", nuevas, "\n")

    frec, tau, ruta, L = aco()
    total = sum(frec.values())
    print("\nFrecuencias de eleccion:")
    for r in RUTAS:
        print(f"  {r}: {frec[r]} ({frec[r]/total:.1%})")
    print("Feromonas finales:", {r: round(v, 4) for r, v in tau.items()})
    print(f"Mejor ruta observada: {ruta} (longitud {L})")
