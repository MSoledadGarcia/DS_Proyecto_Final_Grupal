USE olist_store;

-- Transformación de Id de clientes, ordenes y vendedor

alter table `clientes` add id_nuevo int(6) not null after customer_unique_id;
set @numero = 0;
update clientes
set id_nuevo = @numero:=@numero+1;

alter table `ordenes` add id_cliente_nuevo int not null default 0 after id_cliente; -- Agrego columna id_cliente_nuevo en tabla ordenes
UPDATE ordenes o JOIN clientes c
	ON (o.id_cliente = c.id)
SET o.id_cliente_nuevo = c.id_nuevo;

alter table `ordenes` add id_orden_nuevo int not null default 0 after id_orden;  -- transformacion de id de ordenes
set @numero = 100000;
update ordenes
set id_orden_nuevo = @numero:=@numero+1 order by fecha_compra;
select * from ordenes;

select * from opiniones;
alter table `opiniones` add id_orden_nuevo int not null default 0 after id_orden;    -- agrego id de ordenes nuevo a la tabla opiniones
UPDATE opiniones o JOIN ordenes r
	ON (o.id_orden = r.id_orden)
SET o.id_orden_nuevo = r.id_orden_nuevo;

alter table `order_items` add id_orden_nuevo int not null default 0 after id_orden;   -- agrego id de ordenes nuevo a la tabla order_items
UPDATE order_items o JOIN ordenes r
	ON (o.id_orden = r.id_orden)
SET o.id_orden_nuevo = r.id_orden_nuevo;


alter table `pagos` add id_orden_nuevo int not null default 0 after id_orden;     -- agrego id de ordenes nuevo a la tabla pagos
UPDATE pagos p JOIN ordenes r
	ON (p.id_orden = r.id_orden)
SET p.id_orden_nuevo = r.id_orden_nuevo;

select count(distinct id_orden_nuevo) from pagos;
select o.id_orden_nuevo, p.id_orden_nuevo, o.id_orden, p.id_orden from ordenes o  join pagos p on (o.id_orden_nuevo = p.id_orden_nuevo);


alter table `vendedor` add IdVendedor int not null default 0 after id_vendedor;
set @numero = 200000000;
update `vendedor`
set IdVendedor = @numero:=@numero+1 order by id_vendedor;


select count(*)from order_items;
alter table `order_items` add IdVendedor int not null default 0 after id_vendedor;
UPDATE order_items o JOIN vendedor v
	ON (o.id_vendedor = v.id_vendedor)
SET o.IdVendedor = v.IdVendedor;

alter table `order_items` drop id_vendedor;
alter table `vendedor` drop id_vendedor;


-- Cambio nombres de columnas y elimino columnas que ya no necesito

ALTER TABLE `clientes` CHANGE `id_nuevo` `IdCliente` INT(11) NULL DEFAULT NULL;   -- elimino id viejo de tabla clientes
ALTER TABLE `clientes` drop id;

select * from opiniones;
ALTER TABLE `opiniones` CHANGE `id_orden_nuevo` `IdOrden` INT(11) NULL DEFAULT NULL;   
ALTER TABLE `opiniones` CHANGE `id_opinion` `IdOpinion` varchar (80) NULL DEFAULT NULL;
ALTER TABLE `opiniones` drop id_orden;

select * from ordenes ;
ALTER TABLE `ordenes` CHANGE `id_orden_nuevo` `IdOrden` INT(11) NULL DEFAULT NULL;
ALTER TABLE `ordenes` CHANGE `id_cliente_nuevo` `IdCliente` INT(11) NULL DEFAULT NULL;
ALTER TABLE `ordenes` drop id_orden;
ALTER TABLE `ordenes` drop id_cliente;

select * from order_items;
ALTER TABLE `order_items` CHANGE `id_orden_nuevo` `IdOrden` INT(11) NULL DEFAULT NULL;
ALTER TABLE `order_items` CHANGE `id_orden_item` `articulo` INT(5) NULL DEFAULT NULL;
ALTER TABLE `order_items` drop id_orden;

select * from pagos;
ALTER TABLE `pagos` CHANGE `id_orden_nuevo` `IdOrden` INT(11) NULL DEFAULT NULL;
ALTER TABLE `pagos` drop id_orden;
ALTER TABLE `pagos` drop payment_sequential;


-- Transformacion de tabla categorias -> Ordeno y agrego Id de cada categoría y elimino columna 'product_category_name_english' 
alter table `categorias` add column IdCategorias int(6) not null;
select * from categorias;
set @numero = 0;
update categorias
set IdCategorias = @numero:=@numero+1;

ALTER TABLE `categorias`
MODIFY COLUMN `categoria` varchar (80) -- especifica el tipo de dato y otras restricciones si es necesario
AFTER `IdCategorias`; -- especifica la columna después de la cual deseas ubicar la columna modificada

ALTER TABLE `categorias`
MODIFY COLUMN `categoria_ingles` varchar (80) -- especifica el tipo de dato y otras restricciones si es necesario
AFTER `categoria`; -- especifica la columna después de la cual deseas ubicar la columna modificada


-- Transformo tabla productos, cambio nombre de categorías por id de categorías.

alter table `productos` add IdCategorias int not null default 0 after id_producto;
select * from productos;
UPDATE productos p JOIN categorias c
	ON (p.categoria = c.categoria)
SET p.IdCategorias = c.IdCategorias;
ALTER TABLE `productos` DROP `categoria`;


-- Transformación de tabla localizacion, normalizacion de nombres de ciudades. 


update `localizacion` set ciudad = 'sao paulo' where ciudad = 'sãopaulo';
update `localizacion` set ciudad = 'sao paulo' where ciudad = 'são paulo';
update `localizacion` set ciudad = 'sao paulo' where ciudad = 'sa£o paulo';
update `localizacion` set ciudad = 'sao paulo' where ciudad = 'sp';
update `localizacion` set ciudad = 'embu guaçu' where ciudad = 'embu-guacu';
update `localizacion` set ciudad = 'guarulhos' where ciudad = 'guarulhos-sp';
update `localizacion` set ciudad = 'mogi das cruzes' where ciudad = 'mogidascruzes';
update `localizacion` set ciudad = 'sao luis do paraitinga' where ciudad = 'sao luiz do paraitinga';
update `localizacion` set ciudad = '4º centenario' where ciudad = '4o. centenario';
update `localizacion` set ciudad = 'arraial do cabo' where ciudad = '...arraial do cabo';
update `localizacion` set ciudad = 'rio branco' where ciudad = 'rio bracnco';
update `localizacion` set ciudad = 'barra de santo antonio' where ciudad = 'barra de  santo antônio';
update `localizacion` set ciudad = 'maceio' where ciudad = 'maceia³';
update `localizacion` set ciudad = "olho d'agua das flores" where ciudad = 'olho d agua das flores';
update `localizacion` set ciudad = "olho d'agua grande" where ciudad = 'olho dágua grande';
update `localizacion` set ciudad = "cidade gaucha" where ciudad = '* cidade';
update `localizacion` set ciudad = "teresopolis" where ciudad = '´teresopolis';


select distinct estado, ciudad from localizacion  order by estado;

select * from localizacion;
select * from opiniones;

-- Analizo columna customer_unique_id de tabla clientes

select count(*) from clientes ;
select count(distinct customer_unique_id) from clientes;
select count(distinct id) from clientes;

SELECT customer_unique_id, COUNT(*) as cantidad
FROM clientes
GROUP BY customer_unique_id
HAVING COUNT(*) > 1;

select * from clientes c join ordenes o 
on (c.customer_unique_id = o.id_cliente);

select count(*) from clientes;


-- Creo tabla de dimension 'ciudad'

drop table if exists ciudad;
create table if not exists ciudad (
idCiudad int not null auto_increment,
ciudad varchar (80),
estado varchar (5),
primary key (idCiudad)
); 
INSERT INTO ciudad (ciudad, estado)
(SELECT DISTINCT ciudad, estado FROM localizacion ORDER BY ciudad);

select count(*) from ciudad;
select count(distinct ciudad) from ciudad;


-- Agrego ID de ciudades y elimino columnas con nombres de ciudad y estado

alter table `localizacion` add idCiudad int not null default 0 after longitud;
UPDATE localizacion l JOIN ciudad ci
	ON (l.ciudad = ci.ciudad and l.estado = ci.estado)
SET l.idCiudad = ci.idCiudad;
select * from localizacion;
ALTER TABLE `localizacion` DROP `ciudad`;
ALTER TABLE `localizacion` DROP `estado`;


alter table `clientes` add idCiudad int not null default 0 after codigo_postal;
UPDATE clientes c JOIN ciudad ci
	ON (c.ciudad = ci.ciudad and c.estado = ci.estado)
SET c.idCiudad = ci.idCiudad;
select * from clientes;
ALTER TABLE `clientes` DROP `ciudad`;
ALTER TABLE `clientes` DROP `estado`;
ALTER TABLE `clientes` DROP `customer_unique_id`;



alter table `vendedor` add idCiudad int not null default 0 after codigo_postal;
select * from vendedor;
UPDATE vendedor v JOIN ciudad ci
	ON (v.ciudad = ci.ciudad and v.estado = ci.estado)
SET v.idCiudad = ci.idCiudad;
ALTER TABLE `vendedor` DROP `ciudad`;
ALTER TABLE `vendedor` DROP `estado`;

-- cambio nombre a tabla order_item por articulo_orden

drop table if exists articulo_orden;
create table if not exists articulo_orden(
IdOrden int not null default 0,
articulo int not null default 0,
id_producto varchar (80),
IdVendedor int (30) not null default 0,
fecha_limite_entrega date,
precio double,
gasto_envio double
);

insert into articulo_orden
select * from order_items;
select count(*) from articulo_orden;

drop table if exists order_items;

