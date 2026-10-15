"""Punto 2 - Ascenso de colinas en un espacio discreto."""

VALORES = [1, 4, 7, 5, 3, 6, 9, 8, 5]   # f(x) para x = 0..8


def ascenso_colinas(valores, inicio):
    """Devuelve el estado final y la trayectoria."""
    actual = inicio
    trayectoria = [actual]
    while True:
        vecinos = [v for v in (actual - 1, actual + 1) if 0 <= v < len(valores)]
        mejor_vecino = max(vecinos, key=lambda v: valores[v])
        if valores[mejor_vecino] > valores[actual]:   # solo mejora estricta
            actual = mejor_vecino
            trayectoria.append(actual)
        else:
            return actual, trayectoria


if __name__ == "__main__":
    maximo_global = max(VALORES)
    exitos = 0
    print(f"{'Inicio':>6} | {'Trayectoria':<18} | {'Final':>5} | {'f(final)':>8}")
    print("-" * 48)
    for inicio in range(len(VALORES)):
        final, tray = ascenso_colinas(VALORES, inicio)
        tray_txt = " -> ".join(map(str, tray))
        print(f"{inicio:>6} | {tray_txt:<18} | {final:>5} | {VALORES[final]:>8}")
        if VALORES[final] == maximo_global:
            exitos += 1
    print(f"\nInicios que llegan al maximo global (f={maximo_global}): "
          f"{exitos}/{len(VALORES)} = {exitos/len(VALORES):.2%}")
