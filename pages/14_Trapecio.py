import streamlit as st
import sympy as sp
import pandas as pd


st.markdown("# Trapecio")

st.write(
    r"""

### La regla del Trapecio aproxima la integral:


$\int_{x_i}^{x_{i+1}f(x)dx}$


$\parallel f(x)- P(x)\parallel_{\infty}^{n\rightarrow \infty}$


$\lim_{n\rightarrow \infty} \parallel P(x)\parallel = f(x)$


Si tenemos la partición equidistante $\{a=x_0, x_1, x_2,...,x_n=b\}$, $x_i = a+\frac{b-a}{n} i$ para $i=0,1,...,n$.


$d(x_0, x_1)=d(x_i, x_j), \forall i\neq j$, $\frac{b-a}{n}$


Por el area del trapecio.


$\int_a^bf(x)dx \approx \frac{b-a}{2n} \{f(x_0)+2f(x_1)+2f(x_3)+f(x_n)\}$
"""
)

st.write("# Codigo")

st.code(
    """
# Inicializamos funcion, a, b y partes a dividir
x = sp.symbols("x")
n = 6
a = 0
b = sp.pi
# Variable acomuladora
c = 0

puntos = []
h = (b - a) / (n * 2)
fx = sp.sin(x) ** 2

# Creamos los intervalos del trapecio
for i in range(n + 1):
    puntos.append(c)
    c += b / n

total = 0
for i, v in enumerate(puntos):
    # Evaluamos la funcion y multiplicamos por 2 si no son extremos
    multi = 1 if i == 0 or i == len(puntos) - 1 else 2
    
    evaluacion = fx.subs({x: v}) * multi
    total += evaluacion
total *= (b - a) / (2 * n)
"""
)

st.write("# Ejemplo")

x = sp.symbols("x")
n = 6
a = 0
b = sp.pi

c = 0
puntos = []
h = (b - a) / (n * 2)
fx = sp.sin(x) ** 2

st.latex(r"\int_{0}^{\pi} \sin(x)^2 dx")
st.write("Evaluando la integral de forma directa usando sympy")
result = sp.integrate(fx, (x, a, b))
st.write(result)

st.write("### Obteniendo la integral por medio del trapecio")

for i in range(n + 1):
    puntos.append(c)
    c += b / n

total = 0
evaluaciones = []
for i, v in enumerate(puntos):
    multi = 1 if i == 0 or i == len(puntos) - 1 else 2
    # Evaluamos la funcion y multiplicamos por 2 si no son extremos
    evaluacion = fx.subs({x: v}) * multi
    total += evaluacion
    evaluaciones.append(evaluacion)
total *= (b - a) / (2 * n)

st.write("Funcion")
st.write(fx)

st.write("**Puntos** del intervalo junto a sus **evaluaciones en la funcion**   ")
dataframe = pd.DataFrame({"Puntos": puntos, "F(x)": evaluaciones})
st.dataframe(dataframe)

st.write("### Resultado final usando el metodo del trapecio")
st.write(total)
