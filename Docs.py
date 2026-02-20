import numpy as np

# Creación básica
a = np.array([1, 2, 3])              # Array 1D
b = np.array([(1, 2, 3), (4, 5, 6)]) # Array 2D (Matriz)

# Placeholders (Rellenos)
np.zeros(5)               # Array de 5 ceros
np.ones((2, 3))           # Matriz 2x3 de unos
np.eye(4)                 # Matriz identidad de 4x4
np.linspace(0, 10, 5)     # 5 valores equiespaciados entre 0 y 10
np.arange(0, 10, 2)       # Rango de 0 a 10 con paso de 2
np.full((2, 2), 7)        # Matriz 2x2 llena de sietes

2. Inspección del Array
Útil para saber con qué tipo de datos estás trabajando.
a.shape : Dimensiones (filas, columnas).
len(a) : Longitud del array.
a.ndim : Número de dimensiones.
a.size : Número total de elementos.
a.dtype : Tipo de datos de los elementos.
a.astype(int) : Convertir a un tipo de dato específico.
3. Operaciones Matemáticas (Element-wise)
NumPy aplica la operación a cada elemento individualmente.
np.add(a, b) o a + b : Suma.
np.subtract(a, b) o a - b : Resta.
np.multiply(a, b) o a * b : Multiplicación.
np.divide(a, b) o a / b : División.
np.exp(a) : Exponencial.
np.sqrt(a) : Raíz cuadrada.
np.dot(a, b) : Producto punto (álgebra lineal).
4. Estadística Descriptiva
Los métodos que más usarás en tu especialización:
np.mean(a, axis=0) : Media (axis=0 columnas, axis=1 filas).
np.median(a) : Mediana.
np.std(a) : Desviación estándar.
np.var(a) : Varianza.
np.corrcoef(a) : Coeficiente de correlación.
a.min() / a.max() : Valores mínimo y máximo.
a.sum() : Suma total de los elementos.
5. Selección y Slicing (Rebanado)
a[5] : El elemento en el índice 5.
b[1, 2] : Elemento en fila 1, columna 2.
a[0:2] : Elementos del índice 0 al 1.
b[:, 1] : Todos los elementos de la columna 1.
a[a < 5] : Filtro booleano (trae elementos menores a 5).
6. Manipulación de Forma
a.reshape(3, -2) : Cambia la forma (ej. de 1x6 a 3x2).
a.flatten() : Colapsa un array 2D a 1D.
np.transpose(a) o a.T : Transponer la matriz (filas por columnas).
np.concatenate((a, b)) : Une dos arrays.
np.vstack((a, b)) : Apila verticalmente.
np.hstack((a, b)) : Apila horizontalmente.
7. Generación Aleatoria (np.random)
np.random.rand(5) : 5 números aleatorios entre 0 y 1.
np.random.randn(5) : 5 números de una distribución normal estándar.
np.random.randint(0, 10, 5) : 5 enteros aleatorios entre 0 y 9.
np.random.seed(42) : Fija la semilla para que los resultados sean repetibles.
Tip de oro: Casi todas las funciones de NumPy tienen un parámetro llamado out. Si quieres ahorrar memoria en datasets gigantes, puedes decirle a NumPy dónde guardar el resultado directamente: np.add(a, b, out=a).
