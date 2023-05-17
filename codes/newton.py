import sympy as sp
import numpy as np
from sympy import lambdify


def newton(
    ecuaciones: list, symbols: list, x_0: np.array, max_iter=100, error=0.000001
):
    system = sp.Matrix(ecuaciones)
    jaco = system.jacobian(symbols)
    jaco_inv = jaco.inv()

    lamb_system = lambdify([symbols], system, modules=["numpy"])
    lamb_jaco = lambdify([symbols], jaco_inv, modules=["numpy"])

    for i in range(max_iter):
        delta = np.matmul(lamb_jaco(x_0), lamb_system(x_0))
        x_n = x_0.reshape(delta.shape) - delta

        # Check error
        if np.abs(np.linalg.norm(x_n - x_0.reshape(x_n.shape))) <= error:
            break
        x_0 = x_n.reshape(x_0.shape)
    return x_0


# Ejemplo aplicado
x, y = sp.symbols("x,y")
f_xy = x**2 + x * y - 10
g_xy = y + 3 * x * y**2 - 57
x0 = np.array([1.5, 3.5])

sol = newton(ecuaciones=[f_xy, g_xy], symbols=[x, y], x_0=x0)
