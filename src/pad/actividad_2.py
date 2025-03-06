import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import seaborn as sns  # Necesario para estilos
import os
import sys
import json



# Configuración inicial
np.random.seed(42)  
plt.style.use('seaborn-v0_8')  # 🚨 Nombre actualizado

# ----------------------------
# 1. Ejercicios con Arrays NumPy
# ----------------------------
# 1. Array de 10 a 29
array_10_29 = np.arange(10, 30)
print("Array 10-29:\n", array_10_29)

directorio = os.path.join("src", "pad", "static", "json")  # 🛑 Usa os.path.join
os.makedirs(directorio, exist_ok=True)

# Ruta completa del archivo
ruta_archivo = os.path.join(directorio, "array_10_29.json")  # ✅ Ruta válida

# Guardar el JSON
with open(ruta_archivo, "w", encoding="utf-8") as archivo:
    json.dump({"array": array_10_29.tolist()}, archivo, indent=4)

print(f"Archivo guardado en: {ruta_archivo}")


# 2. Suma de array 10x10 de unos
array_10x10 = np.ones((10, 10))
suma_10x10 = array_10x10.sum()
print("\nSuma de 10x10 de unos:", suma_10x10)

# 3. Producto elemento a elemento de dos arrays
arr1 = np.random.randint(1, 11, 5)
arr2 = np.random.randint(1, 11, 5)
producto = arr1 * arr2
print("\nProducto elemento a elemento:\n", arr1, "*", arr2, "=", producto)

# 4. Matriz 4x4 invertible (i*2 + j)
matriz_4x4 = np.fromfunction(lambda i, j: i*2 + j, (4,4), dtype=int)  # ✅ Matriz invertible
inversa_4x4 = np.linalg.inv(matriz_4x4)
print("\nMatriz 4x4 (i*2 + j):\n", matriz_4x4)
print("\nInversa:\n", inversa_4x4)

# 5. Máximo y mínimo con índices
array_100 = np.random.rand(100)
maximo, minimo = array_100.max(), array_100.min()
idx_max, idx_min = array_100.argmax(), array_100.argmin()
print(f"\nMáximo: {maximo:.3f} (índice {idx_max})")
print(f"Mínimo: {minimo:.3f} (índice {idx_min})")

# 6. Broadcasting 3x1 + 1x3 (explicito)
a = np.array([2, 3, 4])  # Columna 3x1 (valores 2, 3, 4)
b = np.array([[4, 5, 6]])       # Fila 1x3
resultado = a + b  # Broadcasting a 3x3
print("\nResultado Broadcasting:\n", resultado)

# 7. Submatriz 2x2 desde fila 2, columna 2 (índices 1)
matriz_5x5 = np.random.randint(1, 10, (5,5))
submatriz = matriz_5x5[1:3, 1:3]
print("\nSubmatriz 2x2:\n", submatriz)

# 8. Array de ceros modificado
zeros_mod = np.zeros(10)
zeros_mod[3:7] = 5
print("\nArray de ceros modificado:\n", zeros_mod)

# 9. Invertir filas de matriz 3x3
matriz_3x3 = np.array([[1,2,3], [4,5,6], [7,8,9]])
matriz_invertida = matriz_3x3[::-1]
print("\nMatriz invertida:\n", matriz_invertida)

# 10. Seleccionar elementos >0.5
arr_rand = np.random.rand(10)
selected = arr_rand[arr_rand > 0.5]
print("\nElementos >0.5:\n", selected)

# ----------------------------
# 2. Gráficos de Dispersión/Densidad
# ----------------------------
# 11. Scatter plot básico
plt.figure(figsize=(10, 6))
x1, y1 = np.random.rand(100), np.random.rand(100)
plt.scatter(x1, y1, alpha=0.7, edgecolor='k')
plt.title("Gráfico de Dispersión Aleatorio")
plt.xlabel("X"), plt.ylabel("Y")
print("x1:", x1)
print("y1:", y1)
plt.savefig("graficas_generadas1.jpg", dpi=300)  # Alta resolución

# 12. Scatter plot con y = sin(x) + ruido
plt.figure(figsize=(10, 6))
x2 = np.linspace(-2*np.pi, 2*np.pi, 100)
y2 = np.sin(x2) + np.random.normal(0, 0.2, 100)
plt.scatter(x2, y2, label=r"$y = \sin(x) + \mathcal{N}(0,0.2)$")
plt.plot(x2, np.sin(x2), color='red', linewidth=2, label=r"$y = \sin(x)$")
plt.title("Función Seno con Ruido Gaussiano")
plt.legend()
print("x2:", x2)
print("y2:", y2)
plt.savefig("graficas_generadas2.jpg", dpi=300)  # Alta resolución


# 13. Gráfico de contorno con meshgrid
plt.figure(figsize=(10, 6))
x3 = np.linspace(-5, 5, 100)
y3 = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x3, y3)
Z = np.cos(X) + np.sin(Y)
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.title(r"Gráfico de Contorno: $z = \cos(x) + \sin(y)$")
print("x3:", x3)
print("y3:", y3)
print("X:", X)
print("Y:", Y)
print("Z:", Z)
plt.savefig("graficas_generadas3.jpg", dpi=300)  # Alta resolución


# 14. Scatter con densidad de color
plt.figure(figsize=(10, 6))
x4, y4 = np.random.randn(1000), np.random.randn(1000)
plt.scatter(x4, y4, c=np.hypot(x4, y4), cmap='plasma', alpha=0.6, edgecolor='w', linewidth=0.3)
plt.colorbar(label="Distancia al origen")
plt.title("Dispersión con Densidad")
print("x4:", x4)
print("y4:", y4)     
plt.savefig("graficas_generadas4.jpg", dpi=300)  # Alta resolución   


# 15. Gráfico de contorno lleno
plt.figure(figsize=(10, 6))
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label="Valor de Z")
plt.title(r"Contorno Lleno: $z = \cos(x) + \sin(y)$")
print("X:", X)
print("Y:", Y)  
plt.savefig("graficas_generadas5.jpg", dpi=300)  # Alta resolución

# ----------------------------
# 3. Histogramas
# ----------------------------
# 16. Histograma normal (con densidad)
plt.figure(figsize=(10, 6))
data_norm = np.random.normal(0, 1, 1000)
plt.hist(data_norm, bins=30, density=True, alpha=0.7, edgecolor='black', color='skyblue')
plt.axvline(data_norm.mean(), color='red', linestyle='--', label=f"Media: {data_norm.mean():.2f}")
plt.title("Histograma Distribución Normal")
plt.legend()
print("data_norm:", data_norm)
plt.savefig("graficas_generadas6.jpg", dpi=300)  # Alta resolución


# 17. Dos distribuciones superpuestas (con densidad)
plt.figure(figsize=(10, 6))
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(3, 1.5, 1000)
plt.hist(data1, bins=30, alpha=0.5, label=r"$\mu=0, \sigma=1$", density=True)
plt.hist(data2, bins=30, alpha=0.5, label=r"$\mu=3, \sigma=1.5$", density=True)
plt.title("Histogramas Superpuestos (Normalizados)")
plt.legend()
print("data1:", data1)
print("data2:", data2)  
plt.savefig("graficas_generadas7.jpg", dpi=300)  # Alta resolución


# 18. Experimentar con bins
plt.figure(figsize=(15, 5))
bins_list = [10, 30, 50]
for i, bins in enumerate(bins_list, 1):
    plt.subplot(1, 3, i)
    plt.hist(data_norm, bins=bins, density=True, alpha=0.7, color='green')
    plt.title(f"{bins} bins")
plt.suptitle("Efecto de Número de Bins")
print("data_norm:", data_norm)  
plt.savefig("graficas_generadas8.jpg", dpi=300)  # Alta resolución

# ----------------------------
# Mostrar todos los gráficos

# ----------------------------
plt.tight_layout()
plt.show()

# 1. Crear carpeta para gráficas
carpeta = "graficas_generadas"
os.makedirs(carpeta, exist_ok=True)

# 2. Generar y guardar gráficos
x = np.linspace(0, 2*np.pi, 100)

plt.figure(figsize=(10, 6))
x1, y1 = np.random.rand(100), np.random.rand(100)
plt.scatter(x1, y1, alpha=0.7, edgecolor='k')
plt.title("Graficas_generadas")
plt.xlabel("X"), plt.ylabel("Y")
print("x1:", x1)
print("y1:", y1)

plt.savefig("graficas_generadas.jpg", dpi=300)  # Alta resolución