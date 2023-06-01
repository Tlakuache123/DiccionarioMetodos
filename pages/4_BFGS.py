import streamlit as st
import pandas as pd
import numpy as np
import sympy as sy
from matplotlib import pyplot as plt
from sympy.plotting.plot import MatplotlibBackend, Plot
from sympy.plotting import plot3d, plot3d_parametric_line
import plotly as ply
import plotly.express as ex
import plotly.graph_objects as gro
from plotly.subplots import make_subplots


def get_sympy_subplots(plot: Plot):
    backend = MatplotlibBackend(plot)

    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt


st.write("# Método de Quasi-Newton(BFGS)")

st.write(
    r"""
## Método Broyden-Fletcher-Goldfard-Sabanno


$1.-$ Elegimos una suposicion líneal $x_0$


$2.-$ Elegimos un Hessiano inicial $B_0$

Por ejemplo: $B_0=1$


$3.-$ $For = (1,2,3...)$ solve...


$4.-$ $B_k*S_k=\bigtriangledown f(x_k)$


$5.-$ $x_{k+1}=x_k+s_k$


$6.-$ $y_k=\bigtriangledown f(x_{k+1})-\bigtriangledown f(x_k)$


## Método de busqueda de raices de Broyden
Una froma de encontrar $f(x)=0$ a ecuaciones no-líneales  sin encontrar el Jacobiano.


Dada $f:R\rightarrow R$, encontramos $f(x)=0$ sin calcular la derivada.

Esto se puede hacer utiliando el método de la secante.


Para el paso $k$:


$[f'(x_k) ]_{aprox}=\frac{f(x_k)-f(x_{k+1})}{x_k-x_{k-1}}$


Entonces $x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}$


Pretendiendo generalizar para $f:R^n \rightarrow R^n$


$J_k(x_k - x_{k-1})=F(x_k)-F(x_{k-1})$ aproximacion al Jacobiano


$x_k = x_k-J_k^{-1}$ $F(x_k)$ $\leftarrow$ el siguiente paso.


Ahora queremos un sistema indeterminado para $J_k$, para ello definimos $\Delta x_1 = x_k -x_{k-1}$ y $\Delta F_k = F(k)-F(k-1)$ y asi obtenemos $J_k \Delta x_k = \Delta F_k....(*)$


Una forma de hacer esto es:
$J_k = J_{k-1}+\frac{\Delta F(k)-J_{k-1}\Delta x_k}{(\parallel \Delta x_k\parallel)^2} \Delta x_k^T$


y que ademas minimiza la forma de Frobenus $\parallel J_k - J_{k-1}\parallel$.

"""
)

st.write("# Ejemplo")

xxs = st.text_input("Ingrese la función $f(x)$: ", value="(x - 1)**2 + (y - 2.5)**2")


fx = sy.parse_expr(xxs)
intstrr = ""


st.latex("f" + str(tuple(fx.free_symbols)) + " = " + sy.latex(fx))
if len(fx.free_symbols) <= 2:
    if len(fx.free_symbols) == 1:
        func = sy.lambdify(list(fx.free_symbols), fx)
        plo = gro.Figure()
        plo.add_trace(
            gro.Scatter(
                x=np.linspace(-10, 10, 1000), y=func(np.linspace(-10, 10, 1000))
            )
        )
        st.plotly_chart(plo)
        p = sy.plot(fx, show=False)
        pl = get_sympy_subplots(p)

        st.pyplot(pl)

    if len(fx.free_symbols) == 2:
        func = sy.lambdify(list(fx.free_symbols), fx)
        plo = gro.Figure()
        ran = np.linspace(-10, 10, 100)
        su = [
            [func(ran[xs], ran[ys]) for xs in range(0, len(ran))]
            for ys in range(0, len(ran))
        ]
        plo.add_trace(gro.Surface(z=su))
        st.plotly_chart(plo)
        p = plot3d(fx, show=False)
        pl = get_sympy_subplots(p)

        st.pyplot(pl)


initaprx = st.text_input("Ingrese una aproximacion inicial $x_0$: ", value="[0,0]")

intaprox = []
intstr = ""


for i in initaprx:
    if i not in "()[]{} ":
        intstr = intstr + i

try:
    st.write("La aproximacion inicial es: ")
    intaprox = list(map(int, intstr.split(",")))
    st.latex(sy.latex(sy.Matrix(list(intaprox))))
except:
    st.error("Error al introducir la aproximación inicial", icon="🚨")

err = st.text_input("Ingrese el error de tolerancia: ", value="0.00001")
try:
    st.write("El error de tolerancia es:", float(err))
except:
    st.error("Error al introducir el error de tolerancia", icon="🚨")


maxiter = st.slider("Maximo de Iteraciones", 10, 1000, 10)


# COLOCA TU METODO AQUI y PASA LA  FUNCION ALOJADA EN fx
