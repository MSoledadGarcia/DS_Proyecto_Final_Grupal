import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import re
from unidecode import unidecode
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, roc_curve, auc, roc_auc_score, confusion_matrix
import xgboost as xgb
from xgboost import XGBClassifier



# Descargar recursos adicionales de NLTK 
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

df= pd.read_csv('opiniones_traducido - opiniones.csv')
columnas_seleccionadas = df.columns[1:5]  # Excluye la primera columna

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
#plt.show()

#Crear el histograma de la columna "review_positiva" para ver la distribución de las opiniones.
plt.figure(figsize=(7, 6))
sns.histplot(data=df_recortado, x='review_positiva', discrete=True, edgecolor='black', hue='review_positiva', multiple='stack')

# Personalizar el gráfico
plt.title('Distribución de frecuencias II')
plt.xlabel('Tipo de review')
plt.ylabel('Frecuencia')
plt.xticks([0, 1], ['Negativa', 'Positiva'])
plt.show()

df_token = pd.read_csv('opiniones_cond.csv')
# Definir la expresión regular para filtrar solo letras
regex_letters = re.compile('[^a-zA-Z]')

# Tokenizar y lematizar la columna 'titulo'
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('spanish')) 

def tokenize_and_lemmatize(text):
    text = unidecode(str(text))  
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
plt.show()

#Graficar nube de palabras del df_titulo_positivo :
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(fd_titulo_positivas)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.show()

#Distribución de palabras en la columna 'mensaje_tokenizado' del DF de opiniones positivas
fd_mensaje_positivas = FreqDist(token for tokens in df_positivas['mensaje_tokenizado'] for token in tokens)
del fd_mensaje_positivas['nan']

df_mensaje_positivo = pd.DataFrame(list(fd_mensaje_positivas.items()), columns = ["Word","Frequency"])
df_mensaje_positivo.sort_values('Frequency',ascending=False, inplace = True)
print(df_mensaje_positivo.head(10))

#---------XGBoost---------#
df_recortado['texto'] = df_recortado['titulo'] + ' ' + df_recortado['mensaje']
df_recortado= df_recortado.drop(['titulo', 'mensaje'], axis=1)
df_recortado= df_recortado.dropna(subset=['texto'])

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(df_recortado['texto'])


X = df_recortado.drop(['review_positiva'], axis=1)
y = df_recortado['review_positiva']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train['texto'])
X_test_tfidf = tfidf_vectorizer.transform(X_test['texto'])

model_xgboost= xgb.XGBClassifier(learning_rate = 0.1,
                                 max_depth = 5,
                                 n_estimators=5000,
                                 subsample=0.5,
                                 colsample_bytree=0.5,
                                 eval_metric = 'auc',
                                 verbosity=1
                                )

eval_set= [(X_test_tfidf, y_test)]

model_xgboost.fit(X_train_tfidf,
                  y_train,
                  early_stopping_rounds=10,
                  eval_set=eval_set,
                  verbose=True)

y_train_pred= model_xgboost.predict_proba(X_train_tfidf)[:,1]
y_test_pred= model_xgboost.predict_proba(X_test_tfidf)[:,1]

print("AUC Train: {:.4f}\nAUC Test: {:.4f}".format(roc_auc_score(y_train, y_train_pred),
                                                   roc_auc_score(y_test, y_test_pred)))

#Matriz de confusión:
conf_matrix = confusion_matrix(y_test, model_xgboost.predict(X_test_tfidf))

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Matriz de Confusión")
plt.xlabel("Predicciones")
plt.ylabel("Valores Verdaderos")
#plt.show()

#Informe de clasificación.
print(classification_report(y_test, model_xgboost.predict(X_test_tfidf)))

#----------------------------------Optimización de hiperparámetros-----------------------------------#
param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [3, 5, 7],
    'n_estimators': [100, 500, 1000],
    'subsample': [0.5, 0.7, 1],
    'colsample_bytree': [0.5, 0.7, 1]
}

model_xgboost = xgb.XGBClassifier(eval_metric='auc')
grid_search = GridSearchCV(model_xgboost, param_grid, scoring='roc_auc', cv=3, verbose=1)

# Ejecutar la búsqueda
grid_search.fit(X_train_tfidf, y_train)

# Mejores hiperparámetros
print("Mejores hiperparámetros:", grid_search.best_params_)

# Evaluar el modelo optimizado
best_model = grid_search.best_estimator_
y_train_pred = best_model.predict_proba(X_train_tfidf)[:,1]
y_test_pred = best_model.predict_proba(X_test_tfidf)[:,1]

print("AUC Train: {:.4f}\nAUC Test: {:.4f}".format(roc_auc_score(y_train, y_train_pred),
                                                   roc_auc_score(y_test, y_test_pred)))

# Matriz de confusión y reporte de clasificación
conf_matrix = confusion_matrix(y_test, best_model.predict(X_test_tfidf))
print(classification_report(y_test, best_model.predict(X_test_tfidf)))

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("Matriz de Confusión")
plt.xlabel("Predicciones")
plt.ylabel("Valores Verdaderos")
plt.show()

# Graficar la Curva ROC y calcular el AUC para el modelo optimizado
fpr, tpr, thresholds = roc_curve(y_test, y_test_pred)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='Curva ROC (área = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Característica Operativa del Receptor - XGBoost Optimizado')
plt.legend(loc="lower right")
plt.show()
