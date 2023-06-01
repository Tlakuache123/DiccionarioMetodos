import streamlit as st
import pandas as pd
import numpy as np
import sympy as sy
from matplotlib import pyplot as plt
from sympy.plotting.plot import MatplotlibBackend, Plot
from sympy.plotting import plot3d, plot3d_parametric_line
import plotly.express as ex
import plotly.graph_objects as gro
from plotly.subplots import make_subplots

st.write("# Interpolación de Lagrange")

st.write(
    r"""
### Teorema(Lagrange) Para n+1 puntos.


$\{ y_0, y_1, y_2,...,y_n$, existe un úncio $P\in P_n(R)$ tal que $P(x_i)=y_i$ con $i=0,n$


Idea de la demostración.
$P(x_0)=a_n x_0^n+...+a_1 x_0 + a_0 = y_0$

$P(x_1)=a_n x^n+...+a_1 x_1 + a_0 = y_1$

$P(x_1)=a_n x^n+...+a_1 x_n + a_0 = y_n$


Sistema de n+1 ecuaciones con n+1 incognitas

Reescribiendo en forma matricial.

$
 \begin{pmatrix}
1 & x_0 & ...... & x_0^n\\
1 & x_1 & ...... & x_1^n\\
1 & x_2 & ...... & x_2^n\\
1 & x_n & ...... & x_n^n\\
 \end{pmatrix}
$

$
 \begin{pmatrix}
a_0\\
a_1\\
a_2\\
a_n\\
 \end{pmatrix}
$

$
 \begin{pmatrix}
y_0\\
y_1\\
y_2\\
y_n\\
 \end{pmatrix}
$

Existencia de $P$ se de una vez se pruebe que el determinante de la matriz

$
 \begin{pmatrix}
1 & x_0 & ...... & x_0^n\\
1 & x_1 & ...... & x_1^n\\
1 & x_2 & ...... & x_2^n\\
1 & x_n & ...... & x_n^n\\
 \end{pmatrix}
$

Sea diferente de 0, a ese determinante lo llamaremos el determinante de Vandermonde.
"""
)

st.write("# Ejemplo")


st.subheader("Método")


def get_sympy_subplots(plot: Plot):
    backend = MatplotlibBackend(plot)

    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt


def li(v, i):
    x = sy.symbols("x")

    s = 1
    st = ""
    for k in range(0, len(v)):
        if k != i:
            st = (
                st
                + "(("
                + str(x)
                + "-"
                + str(v[k])
                + ")/("
                + str(v[i])
                + "-"
                + str(v[k])
                + "))"
            )
            s = s * ((x - v[k]) / (v[i] - v[k]))

    return s


def Lagrange(v, fx):
    # print(v)
    # print(fx)
    lis = []
    for i in range(0, len(v)):
        lis.append(li(v, i))

    sums = 0

    for k in range(0, len(v)):
        sums = sums + (fx[k] * lis[k])

    # print(sums)

    sy.simplify(sums)

    sy.pprint(sums)

    p1 = sy.plot(sums, show=False)
    p2 = get_sympy_subplots(p1)
    p2.plot(v, fx, "o")
    # p2.show()
    return sy.expand(sums), p2, lis


xxs = st.text_input("Ingrese los valores de $x_k$: ", value="0,1,2")

xsstr = ""

for i in xxs:
    if i not in "(){}[] ":
        xsstr = xsstr + i

fxxs = st.text_input("Ingrese los valores de $f(x_k)$: ", value="1,3,0")

x = list(map(float, xsstr.split(",")))
intstrr = ""

for t in fxxs:
    if t not in "()[]{} ":
        intstrr = intstrr + t

fx = list(map(float, intstrr.split(",")))


# st.write(x)
# st.write(fx)
# data = [x,fx]
# st.write(data)


method = Lagrange(x, fx)

st.write("Los polinomios fundamentales de Lagrange estan dados por:")
lli = r"""l_i(x) = \begin{cases}"""
for t in range(0, len(method[2])):
    lli = lli + "l_" + str(t) + r"=" + sy.latex(sy.expand(method[2][t])) + r"\\"
lli = lli + r"\end{cases}"
st.latex(lli)
st.write("El polinomio de Interpolacion está dado por:")
st.latex("p_n(x) =" + sy.latex(method[0]))

func = sy.lambdify(sy.symbols("x"), method[0])
funcdata = pd.DataFrame(
    dict(x=np.linspace(-10, 10, 1000), y=func(np.linspace(-10, 10, 1000)))
)

plo = gro.Figure()

plo.add_trace(
    gro.Scatter(
        x=np.linspace(-10, 10, 1000),
        y=func(np.linspace(-10, 10, 1000)),
        name="Interpolación",
    )
)
plo.add_trace(gro.Scatter(x=x, y=fx, marker_color="rgba(152, 0, 0, .8)", name="Datos"))
# plo.add_hline(y=0)
# plo.add_vline(x=0)
plo.update_layout(title="Grafica de la Interpolación")
st.plotly_chart(plo)
