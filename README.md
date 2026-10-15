# Parcial 2 — Inteligencia Artificial

**Integrantes:** Brayan Hernández, Jorge García y Lina Castañeda.

**Universidad:** Universidad Sergio Arboleda.

## Estructura

- `main.tex`: informe académico editable en LaTeX, sin código Python incrustado, introducción, metodología ni conclusiones.
- `codigo/`: cinco implementaciones independientes en Python.
- `salidas/`: resultados de cada ejercicio.
- `figuras/`: gráficas de las simulaciones.

El informe se compila con **pdfLaTeX** en Overleaf. La gráfica de ascenso de colinas está definida directamente en `main.tex` con PGFPlots.

Para ejecutar los scripts:

```bash
python codigo/punto1_genetico.py
python codigo/punto2_ascenso_colinas.py
python codigo/punto3_temple_simulado.py
python codigo/punto4_aco.py
python codigo/punto5_pso.py
```

El punto 5 requiere `numpy`. La propuesta de reinicios guiados por memoria en el apartado 2.A.5 es conceptual; el código implementa la versión original del enunciado.
