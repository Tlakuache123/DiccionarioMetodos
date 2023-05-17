import sympy as sp
import numpy as np
from sympy import lambdify


# Retorna la solucion junto a una lista de las iteraciones
def cuasi_newton(
    ecuaciones: list, symbols: list, x_0: np.array, max_iter=100, error=0.0000001
):
    # Transformar np.matrix a np.array
    def mat_to_arr(matrix):
        return np.squeeze(np.asarray(matrix))

    soluciones = []
    soluciones.append(x_0)

    system = sp.Matrix(ecuaciones)
    jaco = system.jacobian(symbols)

    np_system = lambdify([symbols], system, modules=["numpy"])
    np_jaco = lambdify([symbols], jaco, modules=["numpy"])

    # Primer iteracion
    A = np.linalg.inv(np_jaco(x_0))
    v = np_system(x_0)
    s = -np.matrix(A) * v
    x0 = np.matrix(x_0).T + s

    # N iteraciones
    for i in range(max_iter):
        w = v
        v = np_system(mat_to_arr(x0))
        y = v - w
        k = -np.matrix(A) * y
        p = float(s.T * A * y)
        A = A + 1 / p * (s + k) * s.T * A
        s = -A * v
        x0 = x0 + s

        soluciones.append(mat_to_arr(x0))
        if np.linalg.norm(mat_to_arr(s)) <= error:
            break

    solucion = mat_to_arr(x0)
    return solucion, soluciones


# Ejemplo aplicado
x, y, z = sp.symbols("x,y,z")
x_0 = np.array([0.1, 0.1, 0.1])
f1 = 3 * x - sp.cos(y * z) - 1 / 2
f2 = x**2 - 81 * (y + 0.1) ** 2 + sp.sin(z) + 1.06
f3 = sp.exp(-x * y) + 20 * z + (10 * sp.pi - 3) / 3

solucion, iteraciones = cuasi_newton(
    ecuaciones=[f1, f2, f3], symbols=[x, y, z], x_0=x_0
)
