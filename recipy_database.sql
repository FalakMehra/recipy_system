-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: project_july
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `password` varchar(265) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'ADMIN','admin@gmail.com','987654321','12345','SUPER ADMIN'),(3,'aakash','aakash@gmail.com','987654321','12345','admin'),(4,'falak','falak@gmail.com','98765432','flk03','admin'),(5,'SAMRITI','SAMRITI@gmail.com','987654321','samriti','Admin'),(6,'falak mehra','falak@gmail.com','9876543210','falak','Super admin'),(7,'priyanshu','priyansh@gmail.com','8877665531','priyanshu90','Admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES ('Italian','The Mediterranean diet forms the basis of Italian cuisine, rich in pasta, fish, fruits and vegetables. Cheese, cold cuts and wine are central to Italian cuisine, and along with pizza and coffee (especially espresso) form part of Italian gastronomic culture.'),('KASHISH','SMART'),('tanisha','brilliant');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipy`
--

DROP TABLE IF EXISTS `recipy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipy` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `duration` int NOT NULL,
  `ingredients` text NOT NULL,
  `category` varchar(255) NOT NULL,
  `user` int NOT NULL,
  `image` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `value2_idx` (`user`),
  KEY `value1_idx` (`category`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipy`
--

LOCK TABLES `recipy` WRITE;
/*!40000 ALTER TABLE `recipy` DISABLE KEYS */;
INSERT INTO `recipy` VALUES (1,'adsfg','sdfgsdf\ndsf\nds\nfdsfdsfdsfdsf\n',289,'fdsfsd,fsdfds,fdsfdsf','Italian',2,''),(5,'hghkhh','fdfdffgg',240,'rfb','tanisha',2,''),(6,'fgghhh','gfdsfhjhtdcd',345,'dfdhj','KASHISH',2,''),(7,'maggie','boil it add water',10,'maggie,water','tanisha',2,''),(12,'Pizza','Start with a solid pizza dough recipe.Make the dough.Proof the dough.Prepare the sauce and toppings.Shape the dough.Bake the pizza.Cool the pizza.',100,'olive oil. Flour, yeast, mozzarella cheese, white sugar, tomatoes and onion are also common ingredients in pizza recipes. Variations include: brown sugar in place of white sugar.','Italian',2,'recipy_images/12.png'),(13,'Burger','Divide the ground beef.Shape the patties.Warm the pan.Toast the buns.Increase the heat to medium-high.Cook the burgers for 3 to 5 minutes.Flip the burgers and cook another 3 to 5 minutes.To make cheeseburgers.',90,'1 sliced onion\n4 slices cheese slices\n1 teaspoon powdered garam masala powder\n2 teaspoon refined oil\n1/2 gm ginger paste\n4 halved burger buns\n2 tablespoon tomato ketchup\n1/2 teaspoon garlic paste\n','Italian',2,'recipy_images/13.png'),(14,'Pasta','Boil Water. Start with a very large pot of water, about 6 quarts per pound of pasta. Add Salt. Put in a lot of salt, about 3 tablespoons.Add the Pasta Stir.Taste the Pasta.\nDrain.Removing Ravioli.Stir In the Sauce.',50,'225 gm pasta penne\n4 cloves garlic\n2 teaspoon basil\nsalt as required\n2 pinches powdered black pepper\n2 red chilli\n','Italian',2,'recipy_images/14.png'),(15,'Cake','Cream together oil and sugar and then blend with beaten eggs\nMaking a homemade sponge cake was never so easy. Begin by mixing sugar and olive oil together. Whisk well until light and fluffy with a manual whisker or a fork. Once done, add the beaten eggs and blend well. Beat further so that the mixture turns white and creamy.',30,'3 cup all purpose flour\n4 egg\n2 teaspoon baking soda\n2 teaspoon vanilla essence\n1 1/2 cup powdered sugar\n1/2 cup virgin olive oil\n1 cup milk\n','Italian',2,'recipy_images/15.png'),(16,'French Fries','I just chopped the potatoes, rubbed them with some salt and directly fried them.',30,'Potatoes, Vegetable Oil (canola Oil, Corn Oil, Soybean Oil, Hydrogenated Soybean Oil, Natural Beef Flavor [wheat And Milk Derivatives]*), Dextrose, Sodium Acid Pyrophosphate (maintain Color), Salt.','Italian',2,'recipy_images/16.png');
/*!40000 ALTER TABLE `recipy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` int DEFAULT NULL,
  `recipy_id` int DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `view` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dscd_idx` (`userid`),
  KEY `dsd_idx` (`recipy_id`),
  CONSTRAINT `dscd` FOREIGN KEY (`userid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dsd` FOREIGN KEY (`recipy_id`) REFERENCES `recipy` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,3,12,7,'it was good'),(2,3,12,9,'good');
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'FALAK','falak@gmail.com','987654321','falak','FEMALE','#1234,GT ROAD,ASR'),(2,'SAMRITI','samriti','8654322122','samriti1234','FEMALE','#1297,MEDICAL ENCLAVE,ASR'),(3,'Priyanshu','priyansh@gmail.com','8877665432','priyansh','MALE','#`1235,GT ROAD,ASR');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-04 11:23:38
