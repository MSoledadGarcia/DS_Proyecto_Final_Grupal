DROP DATABASE olist_store;
CREATE DATABASE  IF NOT EXISTS olist_store;

use olist_store;
SELECT @@global.secure_file_priv;


drop table if exists clientes;
CREATE TABLE clientes(
id VARCHAR (50),
customer_unique_id varchar(50),
codigo_postal int,
ciudad varchar (50),
estado varchar(5),
primary key(id)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_customers_dataset.csv' 
INTO TABLE `clientes` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;



drop table if exists localizacion;
create table if not exists localizacion(
codigo_postal int(10),
latitud double,
longitud double,
ciudad varchar (50),
estado varchar(5)
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_geolocation_dataset.csv' 
INTO TABLE `localizacion` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


drop table if exists order_items;
create table if not exists order_items(
id_orden VARCHAR (50),
id_orden_item varchar (50),
id_producto varchar (50),
id_vendedor varchar (50),
fecha_limite_entrega date,
precio double,
gasto_envio double
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_order_items_dataset.csv' 
INTO TABLE `order_items` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;



drop table if exists pagos;
create table if not exists pagos(
id_orden VARCHAR (50),
payment_sequential int,
medio_de_pago varchar (30),
cuotas int,
payment_value double
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_order_payments_dataset.csv' 
INTO TABLE `pagos` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

drop table if exists opiniones;
create table if not exists opiniones(
id_opinion varchar(50),
id_orden VARCHAR (50),
puntaje int,
titulo varchar (100),
mensaje varchar(250),
fecha_opinion date,
fecha_respuesta date
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_order_reviews_dataset.csv' 
INTO TABLE `opiniones` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;




drop table if exists ordenes;
create table if not exists ordenes(
id_orden VARCHAR (50),
id_cliente VARCHAR (50),
estado VARCHAR (50),
fecha_compra date,
fecha_aprobacion varchar (100),
fecha_envio  varchar(100),
fecha_recepcion varchar (100),
fecha_recepcion_estimada date,
primary key (id_orden)
);


LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_orders_dataset.csv' 
INTO TABLE `ordenes` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


drop table if exists productos;
create table if not exists productos(
id_producto varchar (50),
categoria varchar (50),
product_name_lenght varchar (20),
product_description_lenght varchar(20),
product_photos_qty  varchar(20),
product_weight_g varchar(20),
product_length_cm  varchar(20),
product_height_cm  varchar(20),
product_width_cm  varchar(20),
primary key(id_producto)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_products_dataset.csv' 
INTO TABLE `productos` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


drop table if exists vendedor;
create table if not exists vendedor(
id_vendedor varchar(50),
codigo_postal int,
ciudad varchar (100),
estado varchar (5),
primary key  (id_vendedor)
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_sellers_dataset.csv' 
INTO TABLE `vendedor` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;



drop table if exists categorias;
create table if not exists categorias(
categoria varchar(100),
categoria_ingles varchar(100),
primary key(categoria)
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\product_category_name_translation.csv' 
INTO TABLE `categorias` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;


drop table if exists closed_deals;
create table if not exists closed_deals(
id_lideres varchar(50),
id_vendedor varchar(50),
sdr_id varchar (50),
sr_id varchar(50),
won_date date,
business_segment varchar(50),
lead_type varchar (80),
lead_behaviour_profile varchar (50),
has_company varchar (50),
has_gtin varchar (50),
average_stock varchar (50),
business_type varchar (100),
declared_product_catalog_size varchar(10),
declared_monthly_revenue double
);
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_closed_deals_dataset.csv' 
INTO TABLE `closed_deals` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;




drop table if exists lideres_marketing;
create table if not exists lideres_marketing(
id_lideres varchar (50),
fecha_contacto date,
landing_page_id varchar (50),
origen varchar (50)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\olist_marketing_qualified_leads_dataset.csv' 
INTO TABLE `lideres_marketing` 
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '' 
LINES TERMINATED BY '\n' IGNORE 1 LINES;

select * from vendedor;
select * from ordenes;