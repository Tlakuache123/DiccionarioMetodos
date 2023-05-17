import streamlit as st
import sympy as sp
import numpy as np
from sympy import lambdify

st.set_page_config(page_title="Newton", page_icon="🍎")

st.write("# Newton")

st.write(
    r"""
## Metodo Newton-Multivariable
$f:D\subseteq R^n \rightarrow R^n$ que sea de clase $C^{(2)}$ y continua.

$Jf(x)=\{ \frac{df_i}{dx_i}\}^n_{i=1}\in Mat_{n\times n}(R)$

$Hf(x)=\{ \frac{d^2f_i}{dx_jdx_i}\}^n_{i*j=1}$

El teorema de la funcion inversa, nos dice que bajo hipotesis sobre

$f:$\{Inyectiva, Inversa Diferenciable\}, $f:D\subseteq R^n \rightarrow R^n$, $D\leftrightarrow f^{-1}:f^{-1}$

$D$ y $Df$ son conjuntos abiertos.

Si llamamos a $y=f(x)$, entonces:

$det$ $Jf(x) \neq 0$(la jacobiana es invertible) y $Jf(x)^{-1}(y)=\{ \frac{df_i}{dx_i}(y)\}^{-1}$

## Metodo Newton
Para sistemas de ecuaciones no líneales es el sig:

$x^{(k)}=x^{(k-1)}-Jf^{-1}(y^{(k-1)})f(x^{(k-n)})$

### Forma Recursiva

Basta dar condiciones iniciales.

$x^{(0)}=(x_1^{(0)}, x_2^{(0)},...,x_n^{(0)})$

**Teorema**: Si un sistema de ecuaciones no-líneales tiene una cantidad inicial(suficientemente cerca de la solución $f(x)=0$), entonces la convergencia en el método de Newton es de tipo cuadratica.
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
  &x^2 + xy - 10 = 0 \\
  &y + 3xy^2 - 57 = 0
\end{split}
\end{cases}
\end{equation*}
"""
)

## Code
max_iteraciones = 100
error = 0.00001
x, y = sp.symbols("x,y")
f_xy = x**2 + x * y - 10
g_xy = y + 3 * x * y**2 - 57
x_0 = np.array([1.5, 3.5])

system = sp.Matrix([f_xy, g_xy])
jaco = system.jacobian([x, y])
jaco_inv = jaco.inv()

lamb_system = lambdify([[x, y]], system, modules=["numpy"])
lamb_jaco = lambdify([[x, y]], jaco_inv, modules=["numpy"])

# st.write(system)
# st.write(jaco)
# st.write(jaco_inv)

iteraciones_container = st.expander(label="Iteraciones")
with iteraciones_container:
    for i in range(max_iteraciones):
        st.write(f"### Iteracion {i}")
        delta = np.matmul(lamb_jaco(x_0), lamb_system(x_0))
        x_n = x_0.reshape(delta.shape) - delta

        st.latex("x_n")
        st.write(x_0)
        st.latex(r"x_{n+1}")
        st.write(x_n)

        if np.abs(np.linalg.norm(x_n - x_0.reshape(x_n.shape))) <= error:
            break
        x_0 = x_n.reshape(x_0.shape)
