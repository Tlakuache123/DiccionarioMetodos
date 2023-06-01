import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


st.markdown("# Decenso por Gradiente")

st.write(
    r"""
El descenso de gradiente es un algoritmo que estima numéricamente dónde una función genera sus valores más bajos. Eso significa que encuentra mínimos locales, pero no al establecer $\bigtriangledown f=0$ como hemos visto antes. En lugar de encontrar mínimos manipulando símbolos, el descenso de gradiente aproxima la solución con números. Además, todo lo que necesita para ejecutarse es la salida numérica de una función, no requiere ninguna fórmula.

Si tuviéramos una fórmula simple como $f(x)=x^2-4x$, entonces podríamos calcular fácilmente $\bigtriangledown f=0$ para determinar que $x=2$ minimiza $f(x)$. O podríamos usar el descenso de gradiente para obtener una aproximación numérica, algo así como $x\approx 1.99999967$

La forma en la que el descenso de gradiente logra encontrar el mínimo de funciones es más fácil de imaginar en tres dimensiones.

Piensa en una función $f(x,y)$ que define algún terreno montañoso cuando se grafica como un mapa de altura. Aprendimos que el gradiente evaluado en cualquier punto representa la dirección del ascenso más pronunciado por este terreno montañoso. Eso podría darte una idea de cómo maximizar la función: comenzar con una entrada aleatoria, y tantas veces como podamos, dar un pequeño paso en la dirección del gradiente para movernos cuesta arriba. En otras palabras, subir la colina.
Por el contrario, para minimizar la función, podemos seguir el negativo del gradiente, y así ir en la dirección del descenso más pronunciado. Este es el descenso de gradiente. Formalmente, si comenzamos en un punto $x_0$ y nos movemos una distancia positiva $\alpha$ en la dirección del gradiente negativo, entonces nuestro nuevo y mejorado $x_1$ se verá así:

$x_1=x_0-\alpha \bigtriangledown f(x_0)$

Más generalmente, podemos escribir una fórmula para convertir $x_n$ en $x_{n+1}$:

$x_{n+1}=x_n - \alpha \bigtriangledown f(x_n)$

A partir de una conjetura inicial $x_0  $, la seguimos mejorando poco a poco hasta encontrar un mínimo local. Este proceso puede tomar miles de iteraciones, por lo que normalmente implementamos un gradiente de descenso con una computadora.
"""
)

st.write("# Codigo")

st.code(
    """
    import numpy as np

    def decenso_gradiente(gradiente, x_0, alpha, n_iteraciones=50, error=1e-06):
    vector = x_0
    for _ in range(n_iteraciones):
        diff = -alpha * gradiente(vector)
        if np.all(np.abs(diff) <= error):
            break
        vector += diff
    return vector
    """,
    language="python",
)

st.write(
    """
# Ejemplo
Sea la siguiente funcion
"""
)
st.latex(r"x_{n+1} = x_n - \alpha * \nabla f(x)")


def decenso_gradiente(gradiente, x_0, alpha, n_iteraciones=50, error=1e-06):
    vector = x_0
    vector_history = []
    gradient_history = []
    for _ in range(n_iteraciones):
        vector_history.append(vector)
        grad = gradiente(vector)
        diff = -alpha * grad
        gradient_history.append(np.abs(alpha * grad))
        if np.all(np.abs(diff) <= error):
            break
        vector += diff
    return vector, vector_history, gradient_history


x, y = sp.symbols("x, y")
f = x**4 - 5 * x**2 - 3 * x
df = f.diff(x)

x_0 = st.number_input("Inserta $x_0$", value=0)
alpha = st.number_input(r"Inserta $\alpha$", value=0.05)

lamb_fx = sp.lambdify(x, f, modules=["numpy"])
lamb_dfx = sp.lambdify(x, df, modules=["numpy"])

v, v_h, g_h = decenso_gradiente(gradiente=lamb_dfx, x_0=x_0, alpha=alpha)

vals_x = np.linspace(-3, 3, 100)
fx = lamb_fx(vals_x)
vfx = lamb_fx(np.array(v_h))

st.write("Nuestra funcion a evaluar")
st.latex(f)

st.write("Su derivada")
st.latex(df)

# Plotting function
fig1 = px.line(x=vals_x, y=fx)
fig1.update_traces(line=dict(color="rgba(125,125,125,0.6)"))

fig2 = px.line(x=v_h, y=vfx, markers=True)

fig = go.Figure(data=fig1.data + fig2.data)

st.write(
    r"""
### Caracteristicas
- Maximo de iteraciones: 100
- Error: 1e-06
"""
)
st.plotly_chart(fig, use_container_width=True)
st.write(f"Minimo calculado f({v}) = {lamb_fx(v)}")
