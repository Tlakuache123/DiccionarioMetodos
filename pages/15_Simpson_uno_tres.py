import streamlit as st
import sympy as sp

st.write(r"# Simpson $\frac{1}{3}$")

st.write(
    r"""
$\frac{1}{3}$ Simpson, sobre una partición.

$\int_a^b f(x)dx\approx \frac{b-a}{6}\{f(a)+4f(\frac{a+b}{2})\}+f(b)$

$\frac{1}{3}$ Simpson, para $n$ = par.

$\int_a^b f(x)dx\approx \frac{h}{3} \sum_{j=1}^{\frac{n}{2}}\{f(x_{2j-2})+4f(x_{2j-1})+f(x_j)\}$

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
n = 20

h = (b - a) / n
# Creamos los intervalos del trapecio
for i in range(n + 1):
    puntos.append(a + i * h)
# Sumatoria
for i in range(1, n // 2):
    total += (
        fx.subs({x: puntos[2 * i - 2]})
        + 4 * fx.subs({x: puntos[2 * i - 1]})
        + fx.subs({x: puntos[2 * i]})
    )
total *= h / 3
    """
)

st.write("# Ejemplo")
# Codigo
x = sp.symbols("x")
fx = x * sp.E ** (2 * x)
a = 0
b = 3
n = 20

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

n = st.number_input("Inserta N", step=2, min_value=2, value=20)
if n % 2 != 0:
    n -= 1

h = (b - a) / n
for i in range(n + 1):
    puntos.append(a + i * h)

for i in range(1, n // 2):
    total += (
        fx.subs({x: puntos[2 * i - 2]})
        + 4 * fx.subs({x: puntos[2 * i - 1]})
        + fx.subs({x: puntos[2 * i]})
    )
total *= h / 3

st.write(puntos)


st.write("Tomar en cuenta que entre mas grande sea N, mas preciso sera el resultado")
st.write(total)
