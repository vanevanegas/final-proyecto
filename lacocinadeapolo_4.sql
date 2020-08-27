CREATE DATABASE  IF NOT EXISTS `lacocinadeapolo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lacocinadeapolo`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: lacocinadeapolo
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carrito`
--

DROP TABLE IF EXISTS `carrito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_receta` int DEFAULT NULL,
  `id_ingrediente` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito`
--

LOCK TABLES `carrito` WRITE;
/*!40000 ALTER TABLE `carrito` DISABLE KEYS */;
INSERT INTO `carrito` VALUES (1,1,1,1),(3,4,2,1),(4,1,NULL,2),(5,1,NULL,3),(8,1,NULL,6),(9,1,NULL,7),(10,1,NULL,6),(11,1,NULL,7),(12,1,NULL,4),(13,1,NULL,5),(14,2,NULL,1),(15,2,NULL,2),(16,2,NULL,0),(17,2,NULL,0),(18,2,NULL,1),(19,2,NULL,2),(20,2,NULL,0),(21,2,NULL,0),(22,2,NULL,1),(23,2,NULL,2),(24,2,NULL,3),(25,2,NULL,4),(26,2,NULL,5),(27,2,NULL,1),(28,2,NULL,2),(29,2,NULL,0),(30,2,NULL,9),(31,2,NULL,10),(32,2,NULL,11),(33,2,NULL,12);
/*!40000 ALTER TABLE `carrito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalles_venta`
--

DROP TABLE IF EXISTS `detalles_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalles_venta` (
  `id` int NOT NULL,
  `id_venta` int NOT NULL,
  `nombre_prod` varchar(45) NOT NULL,
  `precio` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalles_venta`
--

LOCK TABLES `detalles_venta` WRITE;
/*!40000 ALTER TABLE `detalles_venta` DISABLE KEYS */;
INSERT INTO `detalles_venta` VALUES (1,2,'Lechuga','4'),(2,2,'Pepino','8');
/*!40000 ALTER TABLE `detalles_venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(45) NOT NULL,
  `precio` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Pan para Hamburguesa','Pan balnco para hamburguesa',1),(2,'Carne Molida','Carne Molida ',1.5),(3,'Lechuga','Lechuga fresca',0.3),(4,'Tomate','Tomate fresco',0.3),(5,'Mayonesa','Mayonesa',0.3),(6,'Mostaza','Mostaza',0.3),(7,'Salsa de Tomate','Salsa de tomate',0.3),(8,'Aceite','Aceite para cocinar',0.75),(9,'Sal','Sal',0.3),(10,'Pimienta','Pimienta',0.3),(11,'Aguacate','Aguacate',0.5),(12,'Queso Blanco','Queso Blanco',0.5),(17,'sdf','sdf',456),(18,'Carne de res','Rica',4.5),(19,'cebolla','asdasdasdasdasd',0.2);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientes_por_receta`
--

DROP TABLE IF EXISTS `ingredientes_por_receta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes_por_receta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ingredientes_id` int NOT NULL,
  `recetas_id` int NOT NULL,
  `cantidad` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_usar_ingredientes_idx` (`ingredientes_id`),
  KEY `fk_usar_recetas1_idx` (`recetas_id`),
  CONSTRAINT `fk_usar_ingredientes` FOREIGN KEY (`ingredientes_id`) REFERENCES `ingredientes` (`id`),
  CONSTRAINT `fk_usar_recetas1` FOREIGN KEY (`recetas_id`) REFERENCES `recetas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes_por_receta`
--

LOCK TABLES `ingredientes_por_receta` WRITE;
/*!40000 ALTER TABLE `ingredientes_por_receta` DISABLE KEYS */;
INSERT INTO `ingredientes_por_receta` VALUES (1,1,1,1),(2,2,1,1),(3,3,1,1),(4,4,1,1),(5,5,1,1),(6,6,1,1),(7,7,1,1),(8,8,1,1),(9,9,1,1),(10,10,1,1),(11,11,1,1),(12,12,1,1);
/*!40000 ALTER TABLE `ingredientes_por_receta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `precio_envio`
--

DROP TABLE IF EXISTS `precio_envio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `precio_envio` (
  `id` int NOT NULL,
  `departamento` varchar(45) NOT NULL,
  `precio` double(3,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `precio_envio`
--

LOCK TABLES `precio_envio` WRITE;
/*!40000 ALTER TABLE `precio_envio` DISABLE KEYS */;
INSERT INTO `precio_envio` VALUES (1,'San Salvador',2.00),(2,'Chalatenango',3.00),(3,'Ahuachapan',3.00),(4,'Sonsonate',4.50),(5,'Santa Ana',3.00),(6,'San Miguel',4.00),(7,'La Union',4.50),(8,'Cabañas',3.50),(9,'La Paz',3.50),(10,'La Libertad',2.00),(11,'Morazán',2.50),(12,'San Vicente',2.50),(13,'Usulután',3.00),(14,'Cuscatlán',2.50);
/*!40000 ALTER TABLE `precio_envio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  `Tipo` varchar(45) NOT NULL,
  `video` varchar(1200) DEFAULT NULL,
  `imagen` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (1,'Cheeseburger','Deliciosa torta de brisket y short rib molida, acompañada con el fiel','Casero',' https://www.youtube.com/watch?v=gi1ZyNEcShM','hamburguesa.jpg'),(2,'Club Sandwich','Deliciosa Texas toast con lechuga, tomate, tocino, jamon, huevo y','Casero','https://www.youtube.com/watch?v=wjPWrA4cbRk','club_sandwich.jpg'),(3,'Poke bowl','No se que lleva brother pero fijo es algo rico, a pues lleva garbazos y','Casero','https://www.youtube.com/watch?v=jsWK0skZ0S8','poke_bowl.jpg'),(4,'Pizza','Deliciosa masa de la casa, con la salsa especial de tomates del','Casero','https://www.youtube.com/watch?v=sv3TXMSv6Lw','pizza.jpg'),(16,'tre','tre','tre','tre','DJI_0054.JPG'),(17,'DJI_0001.JPG','DJI_0001.JPG','DJI_0001.JPG','DJI_0001.JPG','DJI_0001.JPG'),(18,'qwerty','qwerty','qwerty','qwerty','DJI_0027.JPG'),(19,'qwe','asdasdasdasdasd','cena','https://www.youtube.com/watch?v=FNELyYijVMA','DJI_0002.JPG'),(20,'45','45','45','45','DJI_0019.JPG');
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(20) NOT NULL,
  `contrasenna` varchar(45) NOT NULL,
  `tipo` varchar(12) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `apellido` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `nombre_tarjeta` varchar(45) DEFAULT NULL,
  `numero_tarjeta` varchar(12) DEFAULT NULL,
  `mes_vencimiento` varchar(2) DEFAULT NULL,
  `anno_vencimiento` varchar(2) DEFAULT NULL,
  `cvv` varchar(3) DEFAULT NULL,
  `direccion` varchar(500) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `departamento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Juan','Juan','Admin','Saul','Saul','Juan@hotmail.com','diego','123456789111','11','22','122','Colonia San Juan,casa#3,San Salvador,El Salvador','San Salvador','Cuscatlán'),(2,'Lucas','Lucas','Miembro','2','2','Lucas@hotmail.com','2','2','01','25','2','2','2','La Libertad');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuarios_id` int NOT NULL,
  `fecha` varchar(45) NOT NULL,
  `cantidad` int DEFAULT NULL,
  `total` double(4,2) DEFAULT NULL,
  `direccion` varchar(305) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_venta_usuarios1_idx` (`usuarios_id`),
  CONSTRAINT `fk_venta_usuarios1` FOREIGN KEY (`usuarios_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,1,'26/junio/2020',2,10.00,NULL),(2,2,'27/Junio/2020',5,15.00,'Colonia San Juan,casa#3,San Salvador,El Salvador');
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-27  0:32:19
