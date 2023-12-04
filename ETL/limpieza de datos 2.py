import pymysql
import pandas as pd

# Parámetros de conexión a MySQL
host = 'localhost'
usuario = 'root'
contraseña = 'root1234'
base_de_datos= 'olist_store'


# Crea la conexión a MySQL
connection = pymysql.connect(
    host=host,
    user=usuario,
    password=contraseña,
    database = base_de_datos
)

#crea un cursor
cursor = connection.cursor()

query = "SELECT * FROM vendedor"
cursor.execute(query)



# Obtiene los resultados y crea un DataFrame de Pandas
vendedor= pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])


# Guarda el DataFrame en un archivo CSV
vendedor.to_csv('vendedor.csv', index=False)

vendedor= pd.read_csv('vendedor.csv')
print(vendedor)

# Cierra la conexión
connection.close()

####################

articulos_orden= pd.read_csv('Olist limpio\\articulos_orden.csv')
print(articulos_orden)
articulos_orden.describe()
articulos_orden.info()

opiniones= pd.read_csv('Olist limpio\\opiniones.csv')
print(opiniones)
opiniones.describe()
opiniones.info()


ciudad= pd.read_csv('Olist limpio\\ciudad.csv')
ciudad.describe()
ciudad.info()

clientes= pd.read_csv('Olist limpio\\clientes.csv')
clientes.describe()
clientes.info()

localizacion= pd.read_csv('Olist limpio\\localizacion.csv')
localizacion.describe()
localizacion.info()

ordenes= pd.read_csv('Olist limpio\\ordenes.csv')
ordenes.describe()
ordenes.info()

ordenes['fecha_recepcion'].unique()

pagos= pd.read_csv('Olist limpio\\pagos.csv')
pagos.describe()
pagos.info()

productos= pd.read_csv('Olist limpio\\productos.csv')
productos.describe()
productos.info()   # hay nulls

####################### COMPLETO VALORES FALTANTES
mediana=productos["product_name_lenght"].median()
print(mediana)
productos["product_name_lenght"].fillna(productos["product_name_lenght"].median(),inplace=True)
productos["product_description_lenght"].fillna(productos["product_description_lenght"].median(),inplace=True)

productos.to_csv('Olist limpio\\productos.csv', index=False)

productos= pd.read_csv('Olist limpio\\productos.csv')
print(productos)

# Eliminar la columnas
productos = productos.drop('product_photos_qty', axis=1)
productos = productos.drop('product_weight_g', axis=1)
productos = productos.drop('product_length_cm', axis=1)
productos = productos.drop('product_height_cm', axis=1)
productos = productos.drop('product_width_cm', axis=1)



vendedor= pd.read_csv('Olist limpio\\clientes.csv')
vendedor.describe()
vendedor.info()

len(ciudad['estado']. unique())


