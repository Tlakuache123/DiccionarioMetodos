import streamlit as st

st.set_page_config(page_title="Sistemas no lineales")

st.write("# Sistemas no lineales")

st.write(
    r"""
Una funcion $f:D \subseteq R^n \rightarrow R^n$ no es líneal si:


$\forall x,y \in D$ $f(x+y)\neq f(x)+f(y)$


Ejemplos:


$f(x)=x$ sí es líneal


$f(x)=x \rightarrow (x+y)² \neq x²+y²$


$R^n$ es un espacio vectorial sobre $R$ si:


$\dim_R R^n = n$


Un sistema de ecuaciones no líneales es un sistema:


$(s): f_1(x_1,...,x_n)=0, f_2(x_1,...,x_n)=0, f_n(x_1,...,x_n)=0$


Donde cada $f_i(x_1,...,x_n$ no-líneales $f_i:D \subseteq R^n \rightarrow R^n$.


Una solucion a un sistema de $e.c.s$ no líneales, sera un punto en $R^n$ $(x_1,...,x_n)\in R^n$ que satisface $(s)$ de manera simultanea.


$(1)$ Tal punto puede existir o no existir.


Para resolver este tipo de ecuacuiones vamos a necesitar métodos de aproximacion como la derivada de $f$.


### Recordemos lo siguiente


Supongamos que tenemos una sucesion ${x_n}\subseteq R$ decimos que la sucesion converge si:


Si $\exists x \neq x_n, \forall n$ tal que:


$\lim_{n \to \infty} x_n = x$ (Ademas, si esto sucede, tal límite es unico).


Decimos que la sucesión ${x_n}\subseteq R$ converge a $x$ con orden $\alpha$.


Si $\exists \lambda \in R$ tal que:


$\lim_{n \to \infty} \frac{|x_n-x|}{|x_n-x|\alpha}=\lambda$.
\

Esta notación, medira la velocidad de convergencia con los métodos iterativos.


Cuando:


$\alpha = 1 \rightarrow$ sera convergencia líneal.


$\alpha = 2 \rightarrow$ sera convergencia cuadratica.


### Caso Espacila


$\alpha=1$ y $\lambda<1\rightarrow$ sera convergencia super líneal.


Sea $f:D\subseteq R \rightarrow R$ derivable hasta orden $n\in N$ y no constante.


Por $Taylor$, tal funcion se puede escribir de la siguiente forma:


Si se expande la función al rededor de un punto, sí $x_1 \in R$.


$f(x)=f(x_1)+f^{(1)}(x_1)(x-x_1)+\frac{f^{(2)}(x_1)(x-x_1)²}{2!}+...+R_n(f)$ (Se puede controlar la velocidad de convergencia).


Reescribimos:


$f(x)\approx f(x_1)+f^{(1)}(x_1)(x-x_1)$


Si ponemos $f(x)=0$

$\Rightarrow f(x_1)+f^{(1)}(x_1)(x-x_1) \approx 0$

Despejamos a $x$


$x\approx x_1 - \frac{f(x_1)}{f^{(1)(x_1)}}$


(Iterando el despeje que acabamos de hacer).


$x_{i+1} \approx x_i - \frac{f(x_i)}{f'(x_i)}$


Recordatorio de derivadas en el caso multidimensional.


Sea $f:D\subseteq R^n \rightarrow R^n$

$f$ es derivable si


$\forall x,h \in D^{o}$

$D$ es abierto, $D=D^{o}$


$f(x+h)-f(x) = L(x)(n)+\alpha(x,h)$, donde:


$x=(x_1,...,x_n)$ y $h=(h_1,...,h_n)$, y:


$L(x):R^n \rightarrow R^n$ es una transformacion líneal y $\alpha(x,h) \rightarrow 0\in R$ y $h \to 0$.


A tal transformacion líneal se llama la derivada de $f$ y se denota por $Df(x)$.


Si $f:D\subseteq R^n \rightarrow R^n$ es derivable, a la matríz A de álgebra líneal, se le llama la matríz jacobiana(Jacobi).


$J(x)=
\begin{pmatrix}
\frac{df_1}{dx_1}(x) & \frac{df_1}{dx_2}(x) & \frac{df_1}{dx_n}(x)\\
\frac{df_2}{dx_1}(x) & \frac{df_2}{dx_2}(x) & \frac{df_2}{dx_n}(x)\\
\frac{df_n}{dx_1}(x) & \frac{df_n}{dx_2}(x) & \frac{df_n}{dx_n}(x)
\end{pmatrix}$

$\in Mat_{n\times n}(R)$.


$x\in R$

$f(x)=(f_1(x),...,f_n(x))$

$f_i:D \rightarrow R$ componentes.


Ademas, así $f$ tiene derivadas parciales continuas hasta orden 2.


$H_f(x)
 \begin{pmatrix}
  \frac{d^2f_1}{dx_1^2}(x) & \frac{d^2f_1}{dx_1 dx_2}(x) & \frac{d^2f_1}{dx_1 dx_2}(x)\\
  \frac{d^2f_2}{dx_1^2 dx_1}(x) & \frac{d^2f_2}{dx_2}(x) & \frac{d^2f_2}{dx_2 dx_n^2}(x)\\
  \frac{d^2f_n}{dx_n dx_1}(x) & \frac{d^2f_n}{dx_n dx_2}(x) & \frac{d^2f_n}{dx_n^2}(x)\\
 \end{pmatrix}
$



Con $\frac{d^2f}{dx_i dx_j} = \frac{d^2f}{dx_j dx_i}$.
\
"""
)

st.write(
    r"""
# Sistemas de ecuaciones (en varias variables) no líneales.


Método de $Newton$

Método de $quasi-newton$


Ambos son métodos Iterativos(Número finito de pasos hasta obtener convergencia).


En una variable, se obtiene una funcion(continua)

$f:D\subseteq R \rightarrow R$, bajos ciertas hipotesis, derivable hasta orden 2, podemos expandir a $f$ al rededor de un punto dado $x_i\in R$, atravez de uns serie de polinomios cuando el resultado es de orden que se pueda anular.


Entonces se obtiene el polinomio de $Taylor$.


$f(x)=f(x_1)+f^{(1)}(x_1)(x-x_1)+ \frac{f^{(2)}(x_1)(x-x_1)}{2!}$

$\rightarrow f(x)\approx f(x_1)+f^{(1)}(x_1)(x-x_1)$


Si $x$ es una raíz de $f$

$f(x_1)+f^{(1)(x_1)(x-x_1)}\approx 0$

$\Rightarrow x = x_1-\frac{f(x_1)}{f´(x_1)}$



## Convergencia

Si $\{x_n\}\subseteq R$ tales que:´


$x_n \to x$ si $n\to \infty$, podemos comprobar la velocidad de convergencia.


Como sigue:

Sean $\alpha, \lambda >0$


$\lim_{n\to \infty}\frac{|x_{n+1}-x|}{|x_n-x|\alpha}=\lambda >0$

Decimos que la convergencia es de tipo $\alpha$.


$(1)$ Si $\alpha =1 \rightarrow$ Líneal.

$(2)$ Si $\alpha =2 \rightarrow$ Cuadratica.

$(3)$ Si $\alpha =1$ y $\lambda<1 \rightarrow$ Superlíneal.

## Convergencia en varias variables
En cálculo 3, $(R^n, \parallel * \parallel)$, espacio vectorial sobre $R$; Es un espacio vectorial normado.


$x\in R^n, x=(x_1,x_2,...,x_n)$ y $y=(y_1,y_2,...,y_n)\in R^n$


$x*y=x_1y_1+x_2y_2+...+x_ny_n \in R^n$


$x*x=x_1^2+x_2^2+...+x_n^2$


$\parallel x \parallel = \sqrt{x*x}=\sqrt{x_1^2+...+x_n^2}$
\vspace{0.5cm}

$(R^n,d)$, $d:R^n\times R^n \rightarrow R$

$d(x,y)=\parallel x-y \parallel$


$(1)$ $\parallel x \parallel \geq 0$


$(2)$ $\parallel x \parallel = 0 \Leftrightarrow x = 0.$


$(3)$ $\parallel x*y\parallel \leq \parallel x\parallel * \parallel y\parallel.$


$(4)$ $\parallel x+y\parallel \leq \parallel x\parallel +\parallel y \parallel.$


Hay mas normas en $R^n$


$\parallel x\parallel = max\{|x_i|\}, con i\leq n.$

"""
)
