import streamlit as st

st.write("# Interpolacion")

st.write(
    r"""
## Interpolacion de Lagrange, Polinomial y Cubica
Apartir de un conjunto finito de puntos $n+1$, ${x_1, x_2, x_3,...,x_n}$ dsitintos entre ellos y expondremos de manera explicita polinomios que pasen por los puntos dados.


### Teoría de la aproximacion
Dada una funcion uniformemente continua, podemos aproximar tal funcion por una familia de polinomios.


Se trabaja con 3 tipos de polinomios:

- Berstein.

- Chebysher(Tipo 1 y 2).

- Lagrange(*)


Estos ultimos son faciles de construir y programar, ademas son la familia de polinomios cuya convergencia es cuadratica y Superlíneal.


Seguiremos la siguiente notacion.


$P(x)\in P_n(R) \rightarrow grado(P)\leq n$, $P_n(R =\{Polinomios de grado a lo mas n\})$


$P(x) = a_n x^n + a_{n-1} x^{n-1} + a_1 x + a_0$.


**Nota 1**

Todo polinomio en $P_n(R)$, esta caracterizado por sus coeficientes en $\{a_0, a_1, a_2,...,a_n\}$.


**Nota 2**

$P_n(R)$ es un espacio vectorial sobre $R$


$dim_R P_n(R)=n+1 < \infty$ $\beta = \{1, x, x^2,...,x^n\}$ Base de $P_n(R)$


Sea $\{x_0, x_1, x_2, x_3,...,x_n\}$ $n+1$ puntos distintos.
"""
)
