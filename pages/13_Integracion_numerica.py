import streamlit as st

st.write("# Integracion Numerica")

st.write(
    r"""
Dada una función $f:[a,b]\rightarrow R$ continua, queremos calcular la integral definida de $f$ en $[a,b]$.


$\int_a^b f(x)dx$


Por el teorema fundamental del cálculo, si $F$ es primitiva de $f$, entonces:


$\int_a^b f(x)dx = F(b) - F(a)$


- No siempre se conoce una primitiva de $f$.

- De hecho, puede ser primitiva de F no se pueda expresar mediante   funciones elementales.

- La alternativa es realizar la estimacion del valor de la integral.

- En la practica, solo se usan algunos valores de la funcion f en ciertos puntos del intervalo $[a,b]$ para realizar la estimacion númerica.


El problema de usar este enfoque es que necesitamos calcular el maximo y el minimo de la funcion en cada subintervalo $[x_i, x_{i+1}]$, lo cual no es practico.

"""
)
