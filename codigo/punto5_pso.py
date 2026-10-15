"""Punto 5 - PSO para minimizar f(x, y) = x^2 + y^2 en [-5, 5]^2."""
import numpy as np

N_PART = 10
DIM = 2
LIM_INF, LIM_SUP = -5.0, 5.0
W, C1, C2 = 0.5, 1.5, 1.5
ITERACIONES = 30
SEMILLA = 42


def f(pos):
    return np.sum(pos ** 2, axis=-1)


def pso():
    rng = np.random.default_rng(SEMILLA)
    x = rng.uniform(LIM_INF, LIM_SUP, size=(N_PART, DIM))
    v = np.zeros((N_PART, DIM))
    pbest = x.copy()
    pbest_val = f(x)
    g = np.argmin(pbest_val)
    gbest, gbest_val = pbest[g].copy(), pbest_val[g]
    historial = [gbest_val]
    print(f"Iter  0: gbest={gbest}, f={gbest_val:.6e}")

    for it in range(1, ITERACIONES + 1):
        r1 = rng.random((N_PART, DIM))   # nuevos por particula, dimension e iteracion
        r2 = rng.random((N_PART, DIM))
        # todas las particulas usan el mismo gbest de esta iteracion
        v = W * v + C1 * r1 * (pbest - x) + C2 * r2 * (gbest - x)
        x = x + v
        # ajuste al dominio: posicion al limite y velocidad de esa componente en cero
        fuera = (x < LIM_INF) | (x > LIM_SUP)
        x = np.clip(x, LIM_INF, LIM_SUP)
        v[fuera] = 0.0
        # evaluar y actualizar memorias
        val = f(x)
        mejora = val < pbest_val
        pbest[mejora] = x[mejora]
        pbest_val[mejora] = val[mejora]
        g = np.argmin(pbest_val)
        if pbest_val[g] < gbest_val:
            gbest, gbest_val = pbest[g].copy(), pbest_val[g]
        historial.append(gbest_val)
        print(f"Iter {it:2d}: gbest=({gbest[0]: .6f}, {gbest[1]: .6f}), f={gbest_val:.6e}")
    return gbest, gbest_val, historial


if __name__ == "__main__":
    # Parte A
    x, v, pb, gb = 4, -1, 2, 1
    inercia = 0.5 * v
    cognitivo = 1.5 * 0.4 * (pb - x)
    social = 1.5 * 0.6 * (gb - x)
    v_new = inercia + cognitivo + social
    x_new = x + v_new
    print(f"Inercia={inercia}, cognitivo={cognitivo:.2f}, social={social:.2f}")
    print(f"v_nuevo={v_new:.2f}, x_nuevo={x_new:.2f}, f={x_new**2:.4f}\n")

    gbest, val, hist = pso()
    print(f"\nMejor posicion final: ({gbest[0]:.6f}, {gbest[1]:.6f})")
    print(f"Valor de la funcion: {val:.6e}")
