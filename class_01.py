# 📘 Guía : Estadística Descriptiva y Modelado con Python

## 1. Manipulación de Datos (Pandas & NumPy)

Antes de modelar, debemos entender y limpiar la estructura de la información.

* **Inspección:** Usa `df.describe()` para obtener una visión global (media, desviación, cuartiles).
* **Limpieza:** El método `df.fillna()` es vital para tratar valores nulos que podrían romper tus modelos matemáticos.
* **Transformación:** Los modelos de Machine Learning requieren que los datos estén en formato de matriz (NumPy). Usa `df['columna'].values.reshape(-1, 1)` para preparar tus variables independientes ().

---

## 2. Regresión Lineal: Predicción de Continuos

Se utiliza cuando queremos predecir un valor numérico específico basado en una relación lineal.

### Conceptos Clave:

* **Variable Independiente ():** La causa (ej. Horas de estudio).
* **Variable Dependiente ():** El efecto (ej. Nota final).
* **Ecuación:**  (donde  es la pendiente).

### Pasos en Código:

1. **Instanciar:** `modelo = LinearRegression()`
2. **Entrenar:** `modelo.fit(X, y)`
3. **Predecir:** `y_pred = modelo.predict(nuevos_datos)`

---

## 3. Regresión Logística: Clasificación Binaria

A pesar de su nombre, es un algoritmo de **clasificación**. Se usa para predecir la probabilidad de que algo pertenezca a una categoría (Sí/No).

### Conceptos Clave:

* **Función Sigmoide:** Transforma cualquier valor real en un rango entre **0 y 1**.
* **Umbral (Threshold):** Por defecto es **0.5**. Si la probabilidad es mayor, se clasifica como 1 (Positivo).

### Pasos en Código:

1. **Entrenar:** `log_reg.fit(X, y_binario)`
2. **Probabilidades:** `log_reg.predict_proba(X)` (Devuelve la certeza del modelo para cada clase).

---

## 4. Procesamiento de Imágenes (Lena y Matrices)

Las imágenes son, en esencia, **tensores** o arreglos de NumPy. En estadística descriptiva, las tratamos como distribuciones de frecuencias de píxeles.

### Operaciones Fundamentales:

* **Normalización:** Dividir los valores de los píxeles (0-255) entre 255 para escalarlos de **0 a 1**. Esto ayuda a que los modelos converjan más rápido.
* **Umbralización (Thresholding):** Aplicar la media o mediana para binarizar una imagen.
* *Fórmula:* Si , entonces  (Blanco), de lo contrario  (Negro).



### Visualización:

Usa un **Histograma de Intensidad** para ver si una imagen está sobreexpuesta (sesgada a la derecha) o subexpuesta (sesgada a la izquierda).

---

## 5. Glosario de Métodos Imprescindibles

| Herramienta | Método | Uso Principal |
| --- | --- | --- |
| **NumPy** | `np.mean()` | Calcular el centro de los datos (o brillo de imagen). |
| **NumPy** | `np.std()` | Medir la dispersión o "ruido" en los datos. |
| **Pandas** | `df.groupby()` | Segmentar estadísticas por categorías. |
| **Scikit-Learn** | Es imperativo que utilcen esta libreria me gustaria ver que conocimiento tienen de ella

---

### para la Tarea:

Al trabajar con **Regresión Lineal**, siempre grafica los residuos (la diferencia entre el valor real y la predicción).
