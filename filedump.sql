-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: e_commerce
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `package_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `nama_package` varchar(200) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `created_at` varchar(200) DEFAULT NULL,
  `updated_at` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,1,2,1,'silver',1,50000,'2019-03-23 19:33:32.231988','2019-03-23 19:33:32.232000');
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kategori` varchar(200) DEFAULT NULL,
  `nama` varchar(200) DEFAULT NULL,
  `deskripsi` varchar(200) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `lokasi` varchar(200) DEFAULT NULL,
  `url_foto` varchar(200) DEFAULT NULL,
  `status_item` varchar(200) DEFAULT NULL,
  `post_by` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'rumah','Rumah Malang Murah','Rumah daerah malang, lokasi strategis. Dekat dengan masjid, sekolahan, pusat perbelanjaan, dan taman bermain. Dijual cepat',50000000,'malang','https://rumahpedia.info/wp-content/uploads/2018/10/Rumah-Minimalis-Tampak-Depan-Batu-Alam.jpg','regular','2'),(2,'apartemen','Apartemen Murah Sederhana Jakarta','Apartemen full furniture, tinggal tempati. Parkir automatis, kolam renang, mall, security 24 jam.',2000000000,'jakarta','https://d1nabgopwop1kh.cloudfront.net/hotel-asset/30000002000025383_wh_4','regular','2'),(3,'tanah','Tanah Lapang dan Luas','Tanah lapang dan luas bisa digunakan untuk membangun rumah, lapangan, masjid, sawah, kebun, dll.',200000000,'malang','https://s3-ap-southeast-1.amazonaws.com/jualo/original/11526529/tanah-kosong-lokasi-s-properti-11526529.jpg','regular','2'),(4,'rumah','Rumah Sidoarjo Murah','Rumah daerah sidoarjo, lokasi strategis. Dekat dengan masjid, sekolahan, pusat perbelanjaan, dan taman bermain. Dijual cepat.',1000000000,'sidoarjo','http://rumahpantura.com/wp-content/uploads/2016/11/1480320715_615_23-Model-Rumah-Terbaru-Keren.jpg','regular','3'),(5,'tanah','Tanah Untuk Apa Saja','Tanah lapang dan luas bisa digunakan untuk membangun rumah, sawah, dan sebagainya.',100000000,'purwodadi','https://media.suara.com/pictures/653x366/2017/01/26/o_1b7cf35hm13ql1dohv041fnm1auoc.jpg','regular','3'),(6,'rumah','Rumah Dekat Pantai','Rumah daerah pantai, pagi hari bisa lihat sunrise, malam hari bisa lihat sunset.',2000000000,'tuban','https://hello-pet.com/assets/uploads/2015/09/14-e1441263850719.jpg','regular','4'),(7,'rumah','Rumah Desa','Rumah desa sejuk dan bersih, suasana nyaman dan tenang di desa bisa anda nikmati sekarang juga.',1000000000,'tuban','https://s-ec.bstatic.com/images/hotel/max1024x768/100/100082178.jpg','regular','4'),(8,'apartemen','Apartemen Dekat Pantai','Apartemen lantai 20 dekat pantai sehingga sunrise dan sunset terlihat jelas.',2000000000,'jakarta','https://d1pr4bk5d0i5im.cloudfront.net/images/18/c0/360006666_69_1.jpg','regular','4'),(9,'rumah','Rumah Salju','Rumah di daerah bersalju, ada perapian yang siap menghangatkan ruangan.',2000000000,'papua','https://parade.com/wp-content/uploads/2017/01/iStock-162264365.jpg','regular','5'),(10,'rumah','Rumah Musim Semi','Rumah musim semi dengan halaman yang luas, pemukiman yang tenang dan nyaman.',1500000000,'surabaya','https://images.unsplash.com/photo-1475855581690-80accde3ae2b?ixlib=rb-1.2.1&auto=format&fit=crop&w=1500&q=80','premium','5'),(11,'apartemen','Apartemen Hijau','Apartemen dengan pohon disekelilingnya sehingga membuat suasana menjadi tenang.',2000000000,'jakarta','https://images.unsplash.com/photo-1527030280862-64139fba04ca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1506&q=80','premium','5'),(12,'tanah','Tanah Dekat Gunung','Tanah luas dekat gunung, setiap hari adalah petualangan.',120000000,'bromo','https://images.unsplash.com/photo-1434048230393-5d8c92b31587?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1381&q=80','premium','3');
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package`
--

DROP TABLE IF EXISTS `package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(200) DEFAULT NULL,
  `jumlah_iklan` int(11) DEFAULT NULL,
  `jumlah_iklan_premium` int(11) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package`
--

LOCK TABLES `package` WRITE;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
INSERT INTO `package` VALUES (1,'regular',1,0,25000),(2,'silver',3,1,50000),(3,'gold',8,3,100000);
/*!40000 ALTER TABLE `package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total_quantity` int(11) DEFAULT NULL,
  `total_harga` int(11) DEFAULT NULL,
  `payment_method` varchar(200) DEFAULT NULL,
  `payment_status` varchar(200) DEFAULT NULL,
  `created_at` varchar(200) DEFAULT NULL,
  `updated_at` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,1,1,50000,'Transfer ATM','paid','2019-03-23 19:34:45.507179','2019-03-23 19:34:45.507190');
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `first_name` varchar(200) DEFAULT NULL,
  `last_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `jumlah_iklan` varchar(200) DEFAULT NULL,
  `jumlah_iklan_premium` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'USERNAME-01','PASSWORD-01','dummy','user1','dummyuser1@gmail.com','085725756222','0','0','admin'),(2,'USERNAME-02','PASSWORD-02','dummy','user2','dummyuser2@gmail.com','085725756222','0','0','user'),(3,'USERNAME-03','PASSWORD-03','dummy','user3','dummyuser3@gmail.com','085725756222','0','0','user'),(4,'USERNAME-04','PASSWORD-04','dummy','user4','dummyuser4@gmail.com','085725756222','0','0','user'),(5,'USERNAME-05','PASSWORD-05','dummy','user5','dummyuser5@gmail.com','085725756222','0','0','user');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-23 20:31:22
