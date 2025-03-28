# Cargar el archivo CSV
file_path = 'C:\winemag-data-130k-v2.csv'  # Asegúrate de cambiar esto a la ruta correcta
review = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print(review.head())

