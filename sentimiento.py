import pyprind
import pandas as pd
import os
import numpy as np

# Establecer la ruta base de manera absoluta
basepath = r'C:\Users\liuph\Documents\MachineLearning\AnalisisSentimientosPython\aclimdb'

# Definir las etiquetas para las clases positivas y negativas
labels = {'pos': 1, 'neg': 0}

# Crear una barra de progreso para seguir el progreso del procesamiento
pbar = pyprind.ProgBar(50000)

# Crear un DataFrame vacío con columnas 'review' y 'sentiment'
df_reviews = pd.DataFrame(columns=['review', 'sentiment'])

# Iterar sobre los conjuntos de datos 'test' y 'train' y las clases 'pos' y 'neg'
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        # Construir la ruta completa utilizando os.path.join
        path = os.path.join(basepath, s, l)
        
        # Iterar sobre los archivos en la carpeta actual
        for file in os.listdir(path):
            # Abrir cada archivo y leer su contenido
            with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                txt = infile.read()
                
                # Agregar una fila al DataFrame con el texto y la etiqueta
                df_reviews = df_reviews._append({'review': txt, 'sentiment': labels[l]}, ignore_index=True)
                
                # Actualizar la barra de progreso
                pbar.update()

# Convertir la columna 'sentiment' a tipo entero
df_reviews['sentiment'] = df_reviews['sentiment'].astype(int)

# Permutar aleatoriamente el DataFrame y guardarlo en un nuevo DataFrame llamado 'df'
np.random.seed(0)
df = df_reviews.reindex(np.random.permutation(df_reviews.index))

# Guardar el DataFrame en un archivo CSV llamado 'movie_data.csv'
df.to_csv(os.path.join(basepath, 'movie_data.csv'), index=False, encoding='utf-8')

csv_path = os.path.join(basepath, 'movie_data.csv')

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path, encoding='utf-8')
    print(df.head(3))
else:
    print(f"El archivo {csv_path} no existe.")




