import streamlit as st
import sympy as sp

st.write(r"# Simpson $\frac{3}{8}$")

st.write(
    r"""
$\frac{3}{8}$ Simpson, para $n$ = impar
\vspace{0.5cm}

$\int_a^b f(x)dx\approx \frac{3h}{8} \sum_{j=1}^{\frac{n}{3}}\{f(x_{3j-3})+3f(x_{3j-1})+f(x_j)\}$
"""
)

st.write("# Codigo")

st.code(
    r"""
# Inicializamos funcion, a, b y partes a dividir    
x = sp.symbols("x")
fx = x * sp.E ** (2 * x)
a = 0
b = 3
n = 15

h = (b - a) / n
# Creamos los intervalos del trapecio
for i in range(n + 1):
    puntos.append(a + i * h)
# Sumatoria
for i in range(1, n // 3):
    total += (
        fx.subs({x: puntos[3 * i - 3]})
        + 3 * fx.subs({x: puntos[3 * i - 2]})
        + 3 * fx.subs({x: puntos[3 * i - 1]})
        + fx.subs({x: puntos[3 * i]})
    )
total *= 3 * h / 8
"""
)

st.write("# Ejemplo")
# Codigo
x = sp.symbols("x")
fx = x * sp.E ** (2 * x)
a = 0
b = 3
n = 15

puntos = []
evaluaciones = []
total = 0
result = sp.integrate(fx, (x, a, b))


# Texto
st.latex(r"\int_{0}^{3} xe^{2x} dx")
st.write("Evaluando la integral de forma directa con sympy")
st.write(result.evalf())

st.write(r"### Obteniendo la integral por medio de simpson $\frac{1}{3}$")
st.write("Intervalos")

n = st.number_input("Inserta N", step=3, min_value=3, value=30)

h = (b - a) / n
for i in range(n + 1):
    puntos.append(a + i * h)

for i in range(1, n // 3):
    total += (
        fx.subs({x: puntos[3 * i - 3]})
        + 3 * fx.subs({x: puntos[3 * i - 2]})
        + 3 * fx.subs({x: puntos[3 * i - 1]})
        + fx.subs({x: puntos[3 * i]})
    )
total *= 3 * h / 8

st.write(puntos)


st.write("Tomar en cuenta que entre mas grande sea N, mas preciso sera el resultado")
st.write(total)
