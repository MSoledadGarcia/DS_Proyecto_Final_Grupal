# ETL para  Proyecto  Olist Store

Este repositorio contiene scripts y documentación para el proceso de Extract, Transform, Load (ETL) de datos, 
como parte de éste proyecto de Business Intelligence.

## Extracción de datos:
Se descargaron los datos en archivos con formato CSV del repositorio proporcionado por la empresa https://github.com/soyHenry/DS-Proyecto_Grupal_Olist/tree/main/data 

## Transformación de datos
Se armó una base de datos SQL para analizar y transformar las tablas proporcionadas.

## Archivos SQL

El script SQL utilizado en el proceso de carga se encuentra en el archivo [base_de_datos.sql](ETL/base_de_datos.sql). 
Este script realiza las siguientes operaciones:

- Creacion de la base de datos olist_store
- Creación de tablas 
- Carga de datos 


Para el proceso de transformación de utilizó el script [limpieza_de_datos_1.sql](ETL/limpieza_de_datos_1.sql) en el cual se realizaron las siguientes transformaciones:

- Transformación de Id de clientes, ordenes y vendedor.
- Transformación de nombres de columnas.
- Limpieza de columnas que no se necesitaban para el análisis. 
- Transformacion de tabla categorías (se agregó el Id de cada categoría de productos).
- Transformación de tabla productos, se agregó el Id de categorías y se eliminaron nombres de categorías.
- Transformación de tabla de localizaciones (Normalización de nombres de ciudades que estaban mal escritas)
- Creación de tabla de dimensión ciudades con sus Id
- Transformación de tablas donde estaban los nombres de ciudades y estados, se reemplazaron por Id de Ciudades. 

Además se utilizó el siguiente script .py [limpieza_de_datos_2.py](ETL/limpieza_de_datos_2.py)
en el que se ralizó la conexión con la base de datos para hacer un segundo proceso de ETL en el que se analizaron y trataron los datos faltantes para luego poder trabajar en el análisis final  y dashboard. 

## Carga de datos
Los datos están disponibles en la base de datos olist_store en MySql que por medio de un conector los podemos visualizar en PowerBI. Además se realizó la descarga de cada tabla en nuevos archivos .csv para su almacenamiento local. 


# Recomendación para la empresa Olist Store

Se recomienda implementar un sistema de automatización de la extracción de datos para respaldar el análisis continuo y la predicción de las ventas de la empresa durante su expansión. Esta iniciativa busca optimizar la eficiencia operativa y asegurar un flujo de datos oportuno y preciso para la toma de decisiones informada.

Se sugiere explorar plataformas de extracción de datos especializadas y de pago que se adapten a las necesidades específicas de la empresa. Estas plataformas pueden ofrecer capacidades avanzadas de integración con diversas fuentes de datos, facilitando la recopilación de información clave relacionada con órdenes, clientes, envíos y precios.

Además, se propone la implementación de aplicaciones diseñadas para cargar información de manera eficiente en la base de datos, asegurando una estructura de datos coherente y fácilmente analizable. Este enfoque garantiza la consistencia en la gestión de datos y facilita la adaptación de la arquitectura de tablas y datos utilizada en el proyecto actual para dar soporte a las nuevas exigencias derivadas de la expansión.

Para obtener valiosos insights sobre la satisfacción del cliente, se sugiere la incorporación de un formulario automatizado que se envíe a los clientes por correo electrónico después de recibir su compra. Este formulario, vinculado a la encuesta de satisfacción, permitirá recopilar datos valiosos sobre la experiencia del cliente y contribuirá a la mejora continua de los servicios ofrecidos.

