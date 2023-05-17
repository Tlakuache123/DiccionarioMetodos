import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd
from sympy import lambdify

st.set_page_config(page_title="Casi Newton", page_icon="🍏")

st.write("# Casi Newton")

st.write(
    r"""
Sea $f:R^n\rightarrow R$ la forma general de los métodos cuasi-newton es:

$x_{k+1}=x_k-(\alpha)_k*B^{-1}_k\bigtriangledown f(x_k)$

Donde: $\alpha$ es un parametro de busqueda de línea y $B_k$ es la aproximacion del Hessiano.

_Nota:_

- En optimizacion, la estrategia de busqueda se usa en los enfoques iterativos basicos para encontrar un minimo local.
- Lo que hace es encontrar una direccion de descenso y luego calcula un tamaño de pasos.
- Determina que tan lejos debe moverse $x$ en esta direccion.
"""
)

# Ejemplo
## Text

st.write(
    """
# Ejemplo

Sea el siguiente sistema de ecuaciones

"""
)
st.latex(
    r"""
F(x,y) = 
\begin{equation*}
\begin{cases}
\begin{split}
  &3x - \cos(yz) - \frac{1}{2} = 0 \\
  &x^2 - 81(y+0.1)^2 + \sin(z) + 1.06 \\
  &e^{-xy} + 20z + \frac{10\pi -3}{3}
\end{split}
\end{cases}
\end{equation*}
"""
)

## Code
max_iteraciones = 100
error = 0.0000001

x, y, z = sp.symbols("x,y,z")
x_0 = np.array([0.1, 0.1, 0.1])
soluciones = []
soluciones.append(x_0)

f1 = 3 * x - sp.cos(y * z) - 1 / 2
f2 = x**2 - 81 * (y + 0.1) ** 2 + sp.sin(z) + 1.06
f3 = sp.exp(-x * y) + 20 * z + (10 * sp.pi - 3) / 3

system = sp.Matrix([f1, f2, f3])
jaco = system.jacobian([x, y, z])

np_system = lambdify([[x, y, z]], system, modules=["numpy"])
np_jaco = lambdify([[x, y, z]], jaco, modules=["numpy"])

A = np.linalg.inv(np_jaco(x_0))
v = np_system(x_0)

s = -np.matrix(A) * v
x0 = np.matrix(x_0).T + s


def mat_to_arr(matrix):
    return np.squeeze(np.asarray(matrix))


for i in range(max_iteraciones):
    w = v
    v = np_system(mat_to_arr(x0))
    y = v - w
    k = -np.matrix(A) * y
    p = float(s.T * A * y)
    A = A + 1 / p * (s + k) * s.T * A
    s = -A * v
    x0 = x0 + s

    soluciones.append(mat_to_arr(x0))
    if np.linalg.norm(mat_to_arr(s)) <= error:
        break
solucion = mat_to_arr(x0)

# Contenedor de tabla iterativa
iteraciones_container = st.expander(label="Iteraciones")
with iteraciones_container:
    df = pd.DataFrame(soluciones, columns=(["x", "y", "z"]))
    st.table(df)

st.write("Solucion")
df_sol = pd.DataFrame(x0.T, columns=(["x", "y", "z"]))
st.table(df_sol)
