import streamlit as st
import sympy as sp
import numpy as np
from sympy import lambdify
import plotly.express as px
import plotly.graph_objects as go

st.title("Splines Cubicos")

st.write(
    r"""
##  Método de Interpolacion(Splines Cubicos)
(Hipotesis $Dom(f)$ sea cerrado y acotado).


 Debe ser continua sobre su dominio y que sea acotada.
 

 $Etiquetas_{(Puntos Prescritos)} {y_1,....,y_n}$
 

 Particion sobre cada $y$

 ${a=x_1, x_2, x_3,..., x_n=b}$


Lo que estamos dando es una coleccion finita de datos.


${(x_i, y_i)}_{i=0^n}$ Así generamos $(n_1)$ Splines Cubicos.


Si $i=1,...,n-1 \in P_3(R) \forall i=1,...,n-1$
\newpage

$S_i(x)=a_i x^3 + b_i x^2 + c_i x + d_i$


Condiciones:

$S_1(x_1) \neq S_1(x_2)$

$S_2(x_2) \neq S_2(x_3)$

$S_i(x_i) \neq S_i(x_{i+1})$ con $i=1,....,n-1$

$S_i(x_i)=y_i$

$S_i(x_{i+1})=y_{i+1}$


Nota: El join de los $S_i$ debe ser suave(Diferenciable).


$(2)$ $(S'_i(x_{i+1})=S'_{i+1}(x_{i+1})$ con $i=1,....,n-2)_{ecuaciones totales}$

$2(n-1)+(n-2) = (3n-4)$-ecuaciones.


$(3)$ ${S''_i(x_{i+1})=S''_{i+1}(x_{i+1})}$ con $(i=1,....,n-2)_{ecuacuiones totales}$


$(4n-6)$-ecuaciones


$S''_i(x_1)=0$ $S''_n(x_n)=0$


Para $n=4$


$S_1(x_1)=a_1 x_1^3+b_1 x_1^2+c_1 x_1+d_1 = y_1$

$S_2(x_2)=a_1 x_2^3+b_1 x_2^2+c_1 x_2+d_1 = y_2$

$S_3(x_3)=a_1 x_3^3+b_1 x_3^2+c_1 x_3+d_1 = y_3$


$S_1(x_2)=a_1 x_2^3+b_1 x_2^2+c_1 x_2+d_1 = y_2$

$S_2(x_3)=a_2 x_3^3+b_2 x_3^2+c_2 x_3+d_2 = y_3$

$S_3(x_4)=a_3 x_4^3+b_3 x_4^2+c_3 x_4+d_3 = y_4$


$S'_1(x_1)=3a_1 x_1^2+2b_1 x_1+c_1 = 0$

$S'_2(x_2)=3a_2 x_2^2+2b_2 x_2+c_2 = 1$

$S'_3(x_3)=3a_3 x_3^2+2b_3 x_3+c_3 = 0$


$S'_1(x_2)=3a_1 x_2^2+2b_1 x_2+c_1 = 1$

$S'_2(x_3)=3a_2 x_3^2+2b_2 x_3+c_2 = 1$

$S'_3(x_4)=3a_3 x_3^2+2b_3 x_3+c_3 = 1$


$S''_1(x_1)=6a_1 x_1+2b_1 = 1$

$S''_2(x_2)=6a_2 x_2+2b_2 = 1$

$S''_3(x_3)=6a_3 x_3+2b_3 = 1$


$S''_1(x_2)=6a_1 x_2+2b_1 = 1$

$S''_2(x_3)=6a_2 x_3+2b_2 = 1$

$S''_3(x_4)=6a_3 x_4+2b_3 = 0$

"""
)

st.write("# Ejemplo")


def text_to_array(text: str, separator: str = ","):
    return [float(x) for x in text.strip().split(separator)]


def spline(fx, v, fpx0, fpx1):
    inter = []
    fxinter = []

    hi = []
    for i in range(0, len(v) - 1):
        inter.append((v[i], v[i + 1]))
        fxinter.append((fx[i], fx[i + 1]))

    # print(inter)
    for i in range(0, len(inter)):
        hi.append(inter[i][1] - inter[i][0])

    m = np.zeros(len(v) ** 2).reshape(len(fx), len(fx))
    # print(hi)
    # print(m)
    for i in range(0, len(v)):
        for j in range(0, len(v)):
            if i == j and i == 0 and j == 0:
                m[i][j] = 2 * hi[i]
                m[i][j + 1] = hi[i]
                continue
            elif j == i and i == len(v) - 1 and j == len(v) - 1:
                m[i][j] = 2 * hi[-1]
                m[i][j - 1] = hi[-1]
                continue
            else:
                if i == j:
                    m[i][j] = 2 * (hi[i - 1] + hi[i])
                    m[i][j - 1] = hi[i - 1]
                    m[i][j + 1] = hi[i]

    b = np.zeros(len(v))
    b[0] = ((3 / hi[0]) * (fx[1] - fx[0])) - (3 * fpx0)
    b[-1] = (3 * fpx1) - ((3 / hi[-1]) * (fx[-1] - fx[len(fx) - 2]))

    for i in range(1, len(v) - 1):
        b[i] = ((3 / hi[i]) * (fx[i + 1] - fx[i])) - (
            (3 / hi[i - 1]) * (fx[i] - fx[i - 1])
        )

    # print(m)
    # pprint(Matrix(b.transpose()))

    c = (sp.Matrix(m).inv()) * sp.Matrix(b.transpose())
    # pprint(c)
    b = []

    for i in range(0, len(hi)):
        b.append(
            ((fx[i + 1] - fx[i]) / hi[i]) - ((((2 * c[i]) + c[i + 1]) * hi[i]) / 3)
        )

    # pprint(Matrix(b))

    d = []

    for i in range(0, len(hi)):
        d.append((c[i + 1] - c[i]) / (3 * hi[i]))

    # pprint(Matrix(d))

    x = sp.symbols("x")
    spl = []
    for i in range(0, len(inter)):
        spl.append(
            fx[i]
            + (b[i] * (x - v[i]))
            + (c[i] * ((x - v[i]) ** 2))
            + (d[i] * ((x - v[i]) ** 3))
        )

    # pprint(Matrix(spl))

    p = sp.plot(spl[0], (x, inter[0][0], inter[0][1]), show=False)

    for i in range(1, len(spl)):
        paux = sp.plot(spl[i], (x, inter[i][0], inter[i][1]), show=False)
        p.append(paux[0])

    return spl


x_k: str = st.text_input(
    "Ingrese los valores de $x_k$ (separado por comas)", value="-2, -1, 1, 3"
)

fx_k: str = st.text_input(
    "Ingrese los valores de $f_x$ (separado por comas)", value="3, 1, 2, -1"
)

dx_1: str = st.text_input(
    "Ingrese el valor de la derivada del primer termino", value="0"
)

dx_2: str = st.text_input(
    "Ingrese el valor de la derivada del segundo termino", value="0"
)

dx_1 = float(dx_1)
dx_2 = float(dx_2)
x_k = text_to_array(x_k)
fx_k = text_to_array(fx_k)
x = sp.symbols("x")

points = [(x, y) for x, y in zip(x_k, fx_k)]

s = spline(fx_k, x_k, dx_1, dx_2)

fig = go.Figure()
xx = np.linspace(x_k[0], x_k[-1], 100)


st.write("## Splines")
for i, spline in enumerate(s):
    st.write(spline)
    sp = lambdify(x, spline, modules=["numpy"])
    space = np.linspace(x_k[i], x_k[i + 1], 100)
    fig.add_trace(go.Scatter(x=space, y=sp(space), name=f"Spline {i + 1}"))
fig.add_trace(go.Scatter(x=x_k, y=fx_k, mode="markers", name="Puntos"))


st.plotly_chart(fig)
