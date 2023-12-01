import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
from unidecode import unidecode
from nltk.probability import FreqDist
from wordcloud import WordCloud

# Descargar recursos adicionales de NLTK (puedes hacerlo una vez)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

df= pd.read_csv('opiniones_traducido - opiniones.csv')
columnas_seleccionadas = df.columns[1:]  # Excluye la primera columna

# Crear un nuevo DataFrame con las columnas seleccionadas
df_recortado = df[columnas_seleccionadas]

# Guardar el DataFrame recortado en un nuevo archivo CSV
df_recortado.to_csv('archivo_recortado.csv', index=False)

def condicional(row):
    if pd.notnull(row['puntaje']) and ((pd.notnull(row['titulo']) and row['titulo'] != '') or (pd.notnull(row['mensaje']) and row['mensaje'] != '')):
        return 1 if row['puntaje'] >= 3 else 0
    else:
        return None  # Si ambos campos de título y mensaje son nulos, no asignar un valor

# Aplicar la función condicional a cada fila
df_recortado['review_positiva'] = df_recortado.apply(lambda row: condicional(row), axis=1)

# Guardar el DataFrame con la nueva columna en un nuevo archivo CSV
df_recortado.to_csv('opiniones_cond.csv', index=False)

# Crear el histograma de la columna "puntaje"
plt.figure(figsize=(7, 6))
sns.histplot(df_recortado['puntaje'], discrete=True, edgecolor='black', color='orange')

# Personalizar el gráfico
plt.title('Distribución de frecuencias I')
plt.xlabel('Puntaje')
plt.ylabel('Frecuencia')

# Mostrar el histograma
#plt.show()

#Crear el histograma de la columna "review_positiva" para ver la distribución de las opiniones.
plt.figure(figsize=(7, 6))
sns.histplot(data=df_recortado, x='review_positiva', discrete=True, edgecolor='black', hue='review_positiva', multiple='stack')

# Personalizar el gráfico
plt.title('Distribución de frecuencias II')
plt.xlabel('Tipo de review')
plt.ylabel('Frecuencia')

# Cambiar las etiquetas del eje x
plt.xticks([0, 1], ['Negativa', 'Positiva'])

# Mostrar el histograma
#plt.show()

df_token = pd.read_csv('opiniones_cond.csv')
# Definir la expresión regular para filtrar solo letras
regex_letters = re.compile('[^a-zA-Z]')

# Tokenizar y lematizar la columna 'titulo'
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('spanish'))  # Puedes personalizar las stopwords según tu idioma

def tokenize_and_lemmatize(text):
    text = unidecode(str(text))  # Quitar acentos
    text = regex_letters.sub(' ', text)
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(text) if word.lower() not in stop_words]

# Crear dos DataFrames separados para opiniones positivas y negativas manteniendo todas las columnas
df_positivas = df_recortado[df_recortado['review_positiva'] == 1].copy()
df_negativas = df_recortado[df_recortado['review_positiva'] == 0].copy()

# Aplicar la función a las columnas 'titulo' y 'mensaje' del DataFrame con opiniones positivas
df_positivas['titulo_tokenizado'] = df_positivas['titulo'].apply(tokenize_and_lemmatize)
df_positivas['mensaje_tokenizado'] = df_positivas['mensaje'].apply(tokenize_and_lemmatize)
#print(df_positivas[['puntaje', 'titulo_tokenizado', 'mensaje_tokenizado']].head())

# Aplicar la función a las columnas 'titulo' y 'mensaje' del DataFrame con opiniones positivas
df_negativas['titulo_tokenizado'] = df_negativas['titulo'].apply(tokenize_and_lemmatize)
df_negativas['mensaje_tokenizado'] = df_negativas['mensaje'].apply(tokenize_and_lemmatize)
#print(df_negativas[['puntaje', 'titulo_tokenizado', 'mensaje_tokenizado']].head())

#Distribución de palabras en la columna 'titulo_tokenizado' del DF de opiniones positivas:
fd_titulo_positivas = FreqDist(token for tokens in df_positivas['titulo_tokenizado'] for token in tokens)
del fd_titulo_positivas['nan']
if 'otimo' in fd_titulo_positivas:
    fd_titulo_positivas['optimo'] = fd_titulo_positivas.pop('otimo')


df_titulo_positivo = pd.DataFrame(list(fd_titulo_positivas.items()), columns = ["Word","Frequency"])
#print(df_titulo_positivo)
df_titulo_positivo.sort_values('Frequency',ascending=False, inplace = True)
print(df_titulo_positivo.head(10))

#Graficar histograma del df_titulo_positivo :
colores = sns.color_palette("rocket")
plt.figure(figsize = (15,8))
plot = sns.barplot(x  = df_titulo_positivo.iloc[:10].Word, y = df_titulo_positivo.iloc[:10].Frequency, palette=colores)
for item in plot.get_xticklabels():
    item.set_rotation(90)
#plt.show()

#Graficar nube de palabras del df_titulo_positivo :
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(fd_titulo_positivas)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
#plt.show()

#Distribución de palabras en la columna 'mensaje_tokenizado' del DF de opiniones positivas
fd_mensaje_positivas = FreqDist(token for tokens in df_positivas['mensaje_tokenizado'] for token in tokens)
del fd_mensaje_positivas['nan']

df_mensaje_positivo = pd.DataFrame(list(fd_mensaje_positivas.items()), columns = ["Word","Frequency"])
df_mensaje_positivo.sort_values('Frequency',ascending=False, inplace = True)
print(df_mensaje_positivo.head(10))

#Graficar histograma del df_mensaje_positivo :
colores = sns.color_palette("cubehelix")
plt.figure(figsize = (15,8))
plot = sns.barplot(x  = df_mensaje_positivo.iloc[:10].Word, y = df_mensaje_positivo.iloc[:10].Frequency, palette=colores)
for item in plot.get_xticklabels():
    item.set_rotation(90)
#plt.show()

#Graficar nube de palabras del df_mensaje_positivo :
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(fd_mensaje_positivas)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
#plt.show()

