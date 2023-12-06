## Proyecto final - Consultor BI - HENRY Labs


# Índice

1. [Acerca de nosotros](#acerca-de-nosotros)
2. [Equipo de trabajo](#equipo-de-trabajo)
3. [Proyecto](#proyecto)
4. [Introducción](#introducción)
5. [Descripción del problema](#descripción-del-problema)
6. [Objetivo General](#objetivo-general)
7. [Objetivos Específicos](#objetivos-específicos)
8. [Indicadores de rendimiento KPI's](#indicadores-de-rendimiento-kpis)
9. [Alcance del proyecto](#alcance-del-proyecto)
10. [Metodología de trabajo](#metodología-de-trabajo)
11. [Stack tecnológico](#stack-tecnológico)
12. [Diagrama de Gantt](#diagrama-de-gantt)
13. [Análisis preliminar de datos](#análisis-preliminar-de-datos)




# Acerca de nosotros

![Logo del equipo](https://github.com/ji-berti/DS_Proyecto_Final_Grupal/blob/main/images/logo_G4.jpg)  
<img src="/images/logo_G4.jpeg" alt="G4" width="300" height="300">

G4 Business Intelligence es una  empresa dedicada a potenciar el éxito de otras organizaciones al colaborar estrechamente con aquellas que buscan maximizar su rendimiento a través de la implementación efectiva de estrategias basadas en datos. En un mundo cada vez más impulsado por la información, G4 se destaca como un aliado confiable para empresas data-driven que buscan obtener un valor significativo de sus activos de datos.

Nuestra misión en G4 es proporcionar soluciones integrales de business intelligence que abarcan desde la obtención hasta el análisis y las predicciones de datos, permitiendo a nuestros clientes tomar decisiones informadas y estratégicas en todos los aspectos de sus operaciones. Nos enorgullece ofrecer servicios personalizados que se adaptan a las necesidades específicas de cada empresa con la que colaboramos, impulsando así la eficiencia, la productividad y la rentabilidad.

Trabajamos en estrecha colaboración con los equipos internos, aprovechando tecnologías de vanguardia y metodologías avanzadas para garantizar que nuestros clientes no solo recopilen datos, sino que los transformen en información valiosa y accionable.

En G4 Business Intelligence, reconocemos la importancia de la agilidad y la innovación en el entorno empresarial actual. 
Nuestro equipo está comprometido con la excelencia y se esfuerza por mantenerse a la vanguardia de las tendencias emergentes en el mundo del análisis de datos.



# Equipo de trabajo

- Mario Suaza - Mentor
- María Soledad García Ortiz - Ingeniería de Datos
- Agustín Chianello - Análisis de Datos
- Juan Ignacio Berti - Ciencia de Datos

# Proyecto 

EXPANSIÓN DE LA EMPRESA OLIST - ANÁLISIS DE LA TENDENCIA DE VENTA
![Logo del proyecto](https://github.com/ji-berti/DS_Proyecto_Final_Grupal/blob/main/images/68747470733a2f2f706c61792d6c682e676f6f676c6575736572636f6e74656e742e636f6d2f65714c545857647979674b556638354a7343586d634c537231476e6f594e4c4a664656436d592d4e38784746723254335057774e6346644a325378374d77634f366163.png)


# Introducción

En este proyecto, se llevará a cabo un análisis de datos de e-commerce en Brasil con el objetivo de entender el mercado y realizar una predicción de ventas. El cliente, "Olist Store", tiene la intención de expandirse a este país, y contamos con información detallada sobre órdenes, precios, pagos, envíos, satisfacción del cliente y ubicación de puntos de venta.

# Descripción del problema

La entrada exitosa en un nuevo mercado de e-commerce implica satisfacer eficazmente a los clientes y seleccionar cuidadosamente los productos a ofrecer. En este proyecto, se analizarán los tiempos de envío, los métodos de promoción más efectivos y los productos más populares.

# Objetivo General

Realizar una predicción de ventas y analizar los medios de pago más utilizados por los clientes, así como la distribución geográfica de los vendedores para garantizar tiempos de entrega esperados.

# Objetivos Específicos

1. Predicción de los productos más vendidos.
2. Análisis de los estados con mayores ventas.
3. Análisis de los métodos de pago más utilizados.

# Indicadores de rendimiento KPI's

1. Análisis de Productos Más y Menos Vendidos

Objetivo: Identificar los productos con mayores y menores niveles de ventas.

KPI: Porcentaje de participación en ventas para los productos más y menos vendidos.

Fórmula: (Ventas de Producto específico / Ventas Totales) * 100

Descripción: Este KPI evalúa la contribución de cada producto al total de las ventas. Al identificar los productos con mayores y menores porcentajes de participación, se puede focalizar estrategias específicas para impulsar la venta de productos populares o mejorar la promoción de aquellos con menor rendimiento. Este enfoque proporciona una visión más detallada sobre qué productos están influyendo más en las ventas generales.

2. Análisis de Medios de Pago Más Utilizados

Objetivo: Identificar los métodos de pago preferidos por los clientes.

KPI: Porcentaje de transacciones utilizando métodos de pago específicos.

Fórmula: (Transacciones con Método Específico / Total de Transacciones) * 100

Descripción: Este KPI mide la proporción de transacciones que utilizan métodos de pago específicos, proporcionando información sobre las preferencias de los clientes en cuanto a métodos de pago.

3. Análisis de Distribución Geográfica de Ventas

Objetivo: Evaluar la distribución de las ventas en diferentes regiones.

KPI: Porcentaje de participación de ventas en cada región.

Fórmula: (Ventas en Región Específica / Ventas Totales) * 100

Descripción: Este KPI ayuda a comprender cómo se distribuyen las ventas en diferentes regiones, lo que puede ser crucial para desarrollar estrategias de marketing y logística específicas.

4. Tiempo de Envío Promedio

Objetivo: Garantizar tiempos de entrega esperados.

KPI: Promedio del tiempo de envío.

Fórmula: Suma de Tiempos de Envío / Número de Envíos

Descripción: Este KPI proporciona una medida simple y directa del tiempo promedio que transcurre desde la realización del pedido hasta la entrega.

5. Satisfacción del Cliente

Objetivo: Evaluar la satisfacción del cliente.

KPI: Puntuación promedio de satisfacción del cliente.

Fórmula: Suma de Puntuaciones de Satisfacción / Número de Clientes Encuestados

Descripción: Este KPI mide la satisfacción del cliente mediante la recopilación y análisis de las puntuaciones proporcionadas por los clientes encuestados.

# Alcance del proyecto

El proyecto cuenta con un objetivo claro, realizar una predicción sobre las potenciales ventas una vez se consolide la expansión de la empresa a Brasil. Sin embargo, para lograrlo es menester abordar diferentes aristas. 
- Análisis Preliminar de Datos:

Exploración y limpieza de datos para prepararlos para el análisis.
Identificación de patrones y tendencias iniciales en el comportamiento de compra.

- Predicción de Ventas:

Análisis histórico de ventas en otros mercados.
Implementación de modelos predictivos para estimar las ventas futuras.
Evaluación de la precisión de las predicciones mediante indicadores de rendimiento.

- Análisis de Medios de Pago:

Recopilación de datos sobre los medios de pago utilizados en transacciones anteriores.
Evaluación de la preferencia de los clientes por diferentes métodos de pago.
Identificación de oportunidades para optimizar la oferta de medios de pago.

- Distribución de Vendedores:

Localización de los puntos de venta existentes en Brasil.
Análisis de la dispersión geográfica de vendedores.
Recomendaciones para la expansión de puntos de venta basadas en el análisis de datos.

# Metodología de trabajo

Hemos decidido adoptar Scrum como metodología de trabajo. La estructura del proyecto se organizará en un equipo pequeño, facilitando la colaboración y maximizando la eficiencia. Ésta metodología se caracteriza por su flexibilidad y capacidad de adaptación, lo que permitirá al equipo ajustar las tareas y metas según sea necesario durante cada sprint.

# Stack tecnológico

<div class="stack-tech-images">
  <img src="/images/vscode.jpeg" alt="VS Code" width="180" height="80">
  <img src="/images/github1.jpg" alt="GitHub" width="180" height="80">
  <img src="/images/Google-Cloud-Logo.jpeg" alt="Google Cloud" width="180" height="auto">
  <img src="/images/python.png" alt="Python" width="180" height="80">
  <img src="/images/pandas1.jpeg" alt="Pandas" width="180" height="80">
  <img src="/images/id0B3_53hD.jpeg" alt="Matplotlib" width="180" height="90">
  <img src="/images/Tutorial-Sklearn.jpg" alt="Scikit-Learn" width="180" height="90">
   <img src="/images/sql.png" alt="SQL Workbench" width="180" height="90">
</div>


# Diagrama de Gantt

![image](https://github.com/ji-berti/DS_Proyecto_Final_Grupal/assets/142271064/3d583eea-516f-4192-a029-58b709aca000)


# Análisis preliminar de datos

1. Objetivo del Análisis Preliminar de Datos:
Se realizó un análisis preliminar de datos sobre  100 mil  ordenes de compras que se realizaron en Brasil en distintos puntos de venta desde el 2016 hasta el 2018 con el objetivo de identificar y conocer la calidad de los datos e  identificar patrones. 

2. Fuentes de Datos Utilizadas:

         Dataset e-commerce_Olist_dataset:
   
        1. olist_customers_dataset.csv
        2. olist_geolocation_dataset.csv
        3. olist_order_items_dataset.csv
        4. olist_order_payments_dataset.csv
        5. olist_order_reviews_dataset.csv
        6. olist_orders_dataset.csv
        7. olist_products_dataset.csv
        8. olist_sellers_dataset.csv
        9. product_category_name_translation.csv

Se pueden obtener de https://github.com/soyHenry/DS-Proyecto_Grupal_Olist/tree/main/data 

3. Proceso de Extracción y Carga (ETL):
El proceso de Extracción, Transformación y Carga (ETL) se llevó a cabo para preparar los datos para su análisis. 
Los datos fueron extraídos de los archivos CSV detallados anteriormente, utilizando sentencias SQL específicas para cargarlos en la base de datos MySQL. Las fuentes abarcan información detallada sobre clientes, ubicaciones geográficas, productos, órdenes, pagos, opiniones, vendedores, categorías, acuerdos cerrados y lideres de marketing.
Durante la etapa de transformación, se crearon nuevas columnas y se ajustaron los tipos de datos para asegurar la coherencia en la base de datos. Por ejemplo, se agregó la columna id_nuevo a la tabla clientes y se actualizó con identificadores únicos incrementales. Además, se realizaron correcciones en la nomenclatura de las ciudades en la tabla localizacion para garantizar consistencia.
Se establecieron relaciones lógicas entre las tablas, garantizando la integridad referencial. Este proceso facilitará consultas más complejas y análisis más profundos en etapas posteriores del proyecto.
Este proceso de ETL no solo facilita la manipulación eficiente de los datos, sino que también sienta las bases para un análisis más significativo en las etapas subsiguientes del proyecto. Cabe destacar que se implementaron medidas para garantizar la calidad y consistencia de los datos en todas las tablas.

Mas detalles sobre este proceso en [ETL](ETL)  

4. Calidad de Datos:
   
La calidad de los datos analizados en el informe es en su mayoría alta, ya que la mayoría de la información se presenta de manera legible. Sin embargo, se observaron algunos desafíos relacionados con los nombres propios, donde se detectaron errores tipográficos y variaciones en la escritura. Además, se identificaron inconsistencias en la estructura de los identificadores alfanuméricos, ya que no seguían un formato incremental. Estos aspectos pueden requerir una atención específica para garantizar la coherencia y precisión de los datos, pero en general, la calidad es sólida con la necesidad de abordar ciertas áreas específicas.

5. Primeras observaciones:
  <img src="/images/Analisis%20preliminar%20productos.png" alt="Productos" width="auto" height="auto">
  <img src="/images/Analisis%20preliminar%20vendedores.png" alt="Vendedores" width="auto" height="auto">
  <img src="/images/Analisis%20preliminar%20medios%20de%20pago.png" alt="medios pago" width="auto" height="auto">
