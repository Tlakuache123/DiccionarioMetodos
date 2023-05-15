import streamlit as st
import sympy as sp
import numpy as np
from sympy import lambdify

st.set_page_config(page_title="Newton", page_icon="🍎")

st.write("# Newton")

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
