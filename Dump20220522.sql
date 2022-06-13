-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: shws
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add health worker',7,'add_healthworker'),(26,'Can change health worker',7,'change_healthworker'),(27,'Can delete health worker',7,'delete_healthworker'),(28,'Can view health worker',7,'view_healthworker'),(29,'Users Can view Health Worker Table',7,'can_view_healthwoker'),(30,'Can add district',8,'add_district'),(31,'Can change district',8,'change_district'),(32,'Can delete district',8,'delete_district'),(33,'Can view district',8,'view_district'),(34,'Can add report',9,'add_report'),(35,'Can change report',9,'change_report'),(36,'Can delete report',9,'delete_report'),(37,'Can view report',9,'view_report');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (3,'pbkdf2_sha256$260000$LrTzMIeYbfVQlAVxoXOdj0$PAJEIq/jTQOnnzAlBNh3+9cTDdrzXXjYkoi4G7C95c8=','2022-04-11 13:06:21.985666',0,'huzaifa786','','','',1,1,'2022-04-11 13:01:32.000000'),(5,'pbkdf2_sha256$260000$9a2ZmViUPFkvkibG4r2475$AOJMV1MoPZHq5vfzXSjOtGHkhDrg01gs0qKLARrHjRg=','2022-04-15 09:45:40.030892',1,'humayun786','','','',1,1,'2022-04-11 15:14:56.000000'),(18,'pbkdf2_sha256$260000$1mAfG6Nbjc5Vu9ZRFcXNAq$hllISCrZPPH5SY23SPLLiJIN2P1nOVYwreh2Sc8brxw=','2022-05-12 14:58:02.233925',1,'m.humayunabid','','','humayunabid986@gmail.com',1,1,'2022-05-12 14:56:25.164394'),(19,'pbkdf2_sha256$260000$dpieprgL2sRtG85iqgLsaq$EVVms5CzKYL9Ui6NE9ni66hRxvbN+gxwB2lLITyN5E0=','2022-05-13 10:50:39.290848',1,'nauman12175','','','',1,1,'2022-05-12 16:30:54.000000'),(20,'pbkdf2_sha256$260000$bnkISYEcvHWGyT0H5JxZvO$dlolAc5dzvb4zGBU33ar3aQzAYPsmwLZVyAiYsoZB+o=','2022-05-13 13:57:42.571414',1,'humayun789','','','n@n.com',1,1,'2022-05-13 13:56:08.558854');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (15,'2022-04-11 21:49:13.367952','11','user3',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',4,5),(16,'2022-04-11 21:49:15.619910','8','user3',2,'[]',7,5),(17,'2022-04-11 21:50:28.794068','11','user3',2,'[{\"changed\": {\"fields\": [\"Active\"]}}]',4,5),(18,'2022-04-11 21:53:16.696451','11','user3',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,5),(19,'2022-04-11 21:53:18.870431','8','user3',2,'[]',7,5),(20,'2022-04-12 05:44:24.694897','12','user8',2,'[]',7,5),(21,'2022-05-12 14:57:44.414053','6','user1',3,'',4,18),(22,'2022-05-12 14:57:44.431015','17','user10',3,'',4,18),(23,'2022-05-12 14:57:44.436893','11','user3',3,'',4,18),(24,'2022-05-12 14:57:44.444521','10','user4',3,'',4,18),(25,'2022-05-12 14:57:44.451713','12','user5',3,'',4,18),(26,'2022-05-12 14:57:44.457416','13','user6',3,'',4,18),(27,'2022-05-12 14:57:44.462369','14','user7',3,'',4,18),(28,'2022-05-12 14:57:44.468212','15','user8',3,'',4,18),(29,'2022-05-12 14:57:44.474259','16','user9',3,'',4,18),(30,'2022-05-12 16:30:54.439266','19','nauman12175',1,'[{\"added\": {}}]',4,18),(31,'2022-05-12 16:31:48.125289','15','nauman12175',1,'[{\"added\": {}}]',7,18),(32,'2022-05-12 16:32:10.866669','19','nauman12175',2,'[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]',4,18),(33,'2022-05-12 16:32:12.620477','15','nauman12175',2,'[]',7,18);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'health_worker','district'),(7,'health_worker','healthworker'),(9,'health_worker','report'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-11 11:47:54.348888'),(2,'auth','0001_initial','2022-04-11 11:47:55.504541'),(3,'admin','0001_initial','2022-04-11 11:47:55.929284'),(4,'admin','0002_logentry_remove_auto_add','2022-04-11 11:47:55.945180'),(5,'admin','0003_logentry_add_action_flag_choices','2022-04-11 11:47:55.962133'),(6,'app','0001_initial','2022-04-11 11:47:56.004394'),(7,'app','0002_rename_profile_healthworker','2022-04-11 11:47:56.052367'),(8,'app','0003_delete_healthworker','2022-04-11 11:47:56.087573'),(9,'contenttypes','0002_remove_content_type_name','2022-04-11 11:47:56.285664'),(10,'auth','0002_alter_permission_name_max_length','2022-04-11 11:47:56.402509'),(11,'auth','0003_alter_user_email_max_length','2022-04-11 11:47:56.449348'),(12,'auth','0004_alter_user_username_opts','2022-04-11 11:47:56.468461'),(13,'auth','0005_alter_user_last_login_null','2022-04-11 11:47:56.583405'),(14,'auth','0006_require_contenttypes_0002','2022-04-11 11:47:56.594375'),(15,'auth','0007_alter_validators_add_error_messages','2022-04-11 11:47:56.614426'),(16,'auth','0008_alter_user_username_max_length','2022-04-11 11:47:56.842287'),(17,'auth','0009_alter_user_last_name_max_length','2022-04-11 11:47:56.964688'),(18,'auth','0010_alter_group_name_max_length','2022-04-11 11:47:57.003899'),(19,'auth','0011_update_proxy_permissions','2022-04-11 11:47:57.023738'),(20,'auth','0012_alter_user_first_name_max_length','2022-04-11 11:47:57.171205'),(21,'health_worker','0001_initial','2022-04-11 11:47:57.219316'),(22,'health_worker','0002_auto_20220321_2141','2022-04-11 11:47:57.941824'),(23,'health_worker','0003_alter_healthworker_options','2022-04-11 11:47:57.958316'),(24,'health_worker','0004_auto_20220324_0830','2022-04-11 11:47:58.009057'),(25,'health_worker','0005_alter_healthworker_district','2022-04-11 11:47:58.355111'),(26,'health_worker','0006_healthworker_thumbnail','2022-04-11 11:47:58.402927'),(27,'health_worker','0007_healthworker_father_or_husband_name','2022-04-11 11:47:58.510605'),(28,'health_worker','0008_report','2022-04-11 11:47:58.553338'),(29,'health_worker','0009_alter_healthworker_thumbnail','2022-04-11 11:47:58.573566'),(30,'health_worker','0010_auto_20220329_1119','2022-04-11 11:48:09.227414'),(31,'health_worker','0011_auto_20220329_1222','2022-04-11 11:48:09.550909'),(32,'health_worker','0012_auto_20220330_2049','2022-04-11 11:48:11.205340'),(33,'health_worker','0013_auto_20220330_2058','2022-04-11 11:48:11.636367'),(34,'health_worker','0014_auto_20220330_2105','2022-04-11 11:48:12.143425'),(35,'health_worker','0015_alter_report_otherfunction','2022-04-11 11:48:12.209037'),(36,'health_worker','0016_auto_20220330_2141','2022-04-11 11:48:12.480814'),(37,'health_worker','0017_auto_20220404_2103','2022-04-11 11:48:12.746158'),(38,'health_worker','0018_auto_20220405_0918','2022-04-11 11:48:13.183574'),(39,'health_worker','0019_auto_20220405_0934','2022-04-11 11:48:13.229003'),(40,'health_worker','0020_auto_20220410_1206','2022-04-11 11:48:30.813746'),(41,'sessions','0001_initial','2022-04-11 11:48:30.879514');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3fu50paruf565pbwy56bwv01xv35dngp','.eJxVjMsOwiAUBf-FtSFAC4hL9_0GcrhcpGpo0sfK-O_apAvdnpk5LxGxrTVuC89xzOIijBKn3zGBHtx2ku9ot0nS1NZ5THJX5EEXOUyZn9fD_TuoWOq3Bki5or2l0hnqs9NsVPAayI6hk8vnwL03INjUuw4mdESuWB-sAifx_gAemjiy:1npVna:dm2BlR-nhJeJbdtyIk8Bxd_6s8flXIQ_aRJ8xfW1-1A','2022-05-27 13:57:42.579282'),('5cukbyx1mmdll6afl8o4p62sofcxc0bt','.eJxVjMEOwiAQRP-FsyEgFIJH734D2V12pWpoUtqT8d9tkx70OPPezFtlWJea185zHou6KKtOvx0CPbntoDyg3SdNU1vmEfWu6IN2fZsKv66H-3dQoddtDSF4Ml4ExZCBgmd26Ae0ZiicxERvBdGFSMkmCi4w2rhFiQJenKjPFwEtOIw:1ndvDu:wMVQlIVCkR6AI3aYVf9qBKSVucYt5WmeFkQGABm-WWk','2022-04-25 14:40:58.892011'),('d8pct9c92urw4alwd9u2glt8agjs0f0c','.eJxVjEEOwiAQRe_C2pCBoRRcuvcMZIBBqoYmpV0Z765NutDtf-_9lwi0rTVsnZcwZXEWyovT7xgpPbjtJN-p3WaZ5rYuU5S7Ig_a5XXO_Lwc7t9BpV6_dQGnB2fQWpsgGtQRi7WUNRI6rdxggHFMDFEBOkMjOojMSulUyHst3h_afjcF:1npSsZ:BdpJbKzFvoLb39DZ-JBY8hS--zZB8_GkFrqSPdt-zQQ','2022-05-27 10:50:39.299824'),('rxo70of4v8n0nrkp1j1as0129wh1h9ea','.eJxVjEEOwiAQRe_C2pCBoRRcuvcMZIBBqoYmpV0Z765NutDtf-_9lwi0rTVsnZcwZXEWyovT7xgpPbjtJN-p3WaZ5rYuU5S7Ig_a5XXO_Lwc7t9BpV6_dQGnB2fQWpsgGtQRi7WUNRI6rdxggHFMDFEBOkMjOojMSulUyHst3h_afjcF:1npBjs:jK4nQNyKR5VQLEihVP2G3wG3Ux_Zhytj0CUQ92lNCOg','2022-05-26 16:32:32.193893'),('z8oqz0jlai86rvde6pk6q7246doa47eb','.eJxVjEEOwiAQRe_C2pAiA1Ncuu8ZyDBMpWpoUtqV8e7apAvd_vfef6lI21ri1mSJU1YX5dTpd0vED6k7yHeqt1nzXNdlSnpX9EGbHuYsz-vh_h0UauVb970RKxDwHDybZGjE4EE4OfEM0AXLFhGlyyOjcQQuBEIw7MBJtla9P9RqN2A:1ndvo6:Ck4i4K_pDxFazW1zJPxjSQtVwlRzmk56FCWgJzdiPt8','2022-04-25 15:18:22.212177');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_worker_district`
--

DROP TABLE IF EXISTS `health_worker_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_worker_district` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `district` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_worker_district`
--

LOCK TABLES `health_worker_district` WRITE;
/*!40000 ALTER TABLE `health_worker_district` DISABLE KEYS */;
INSERT INTO `health_worker_district` VALUES (50,'Badin'),(51,'Dadu'),(52,'Ghotki'),(53,'Hyderabad'),(54,'Jacobabad'),(55,'Jamshoro'),(56,'Karachi Central'),(57,'Kashmore'),(58,'Khairpur'),(59,'Larkana'),(60,'Matiari'),(61,'Mirpur Khas'),(62,'Naushahro Feroze'),(63,'Shaheed Benazirabad'),(64,'Qambar Shahdadkot'),(65,'Sanghar'),(66,'Shikarpur'),(67,'Sukkur'),(68,'Tando Allahyar'),(69,'Tando Muhammad Khan'),(70,'Tharparkar'),(71,'Thatta'),(72,'Umerkot'),(73,'Sujawal'),(74,'Karachi East'),(75,'Karachi South'),(76,'Karachi West'),(77,'Korangi'),(78,'Malir');
/*!40000 ALTER TABLE `health_worker_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_worker_healthworker`
--

DROP TABLE IF EXISTS `health_worker_healthworker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_worker_healthworker` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `attached_facility` varchar(50) NOT NULL,
  `catchment_of_population_of_flcf` varchar(50) NOT NULL,
  `cnic` varchar(50) NOT NULL,
  `code` varchar(50) NOT NULL,
  `district_id` bigint DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `population_registered_by_lhws` varchar(50) NOT NULL,
  `tehsil` varchar(50) NOT NULL,
  `union_council` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `father_or_husband_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `health_worker_healthworker_district_id_d2482c26` (`district_id`),
  CONSTRAINT `health_worker_health_district_id_d2482c26_fk_health_wo` FOREIGN KEY (`district_id`) REFERENCES `health_worker_district` (`id`),
  CONSTRAINT `health_worker_healthworker_user_id_ffe1bc0d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_worker_healthworker`
--

LOCK TABLES `health_worker_healthworker` WRITE;
/*!40000 ALTER TABLE `health_worker_healthworker` DISABLE KEYS */;
INSERT INTO `health_worker_healthworker` VALUES (2,'first Aid','hiopll','6110178945612','52000',61,'Huzaifa Khan','12000','dfre','NA-112',3,'healthworker/thumbnail/2022/04/11/landscape-g5cb84be8d_1920_nybqYOk.jpg','Zahid Khan'),(3,'first Aid','hjuy','611014569875-9','hum786',59,'Humayun Chaudhry','25000','sad','NA-98',5,'healthworker/thumbnail/2022/04/11/cv_photo11.jpeg','Muhammad Abid'),(15,'masdn','ekwlje','2545485','12568',51,'Nauman Iftikhar','sdksj','wjewkql','wwmsnd',19,'healthworker/thumbnail/2022/05/12/cv_photo11.jpeg','njas');
/*!40000 ALTER TABLE `health_worker_healthworker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health_worker_report`
--

DROP TABLE IF EXISTS `health_worker_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `health_worker_report` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `administeredwithinjectablecontraceptive` decimal(20,10) NOT NULL,
  `alldeaths` decimal(20,10) NOT NULL,
  `anameia` decimal(20,10) NOT NULL,
  `ari` decimal(20,10) NOT NULL,
  `aritimeravailable` varchar(50) NOT NULL,
  `aritimerfunction` varchar(50) NOT NULL,
  `bloodpressureavailable` varchar(50) NOT NULL,
  `bloodpressurefunction` varchar(50) NOT NULL,
  `canal` decimal(20,10) NOT NULL,
  `clientsreferred` decimal(20,10) NOT NULL,
  `cocusers` decimal(20,10) NOT NULL,
  `comments` longtext NOT NULL,
  `condomusers` decimal(20,10) NOT NULL,
  `contraceptiveusers` decimal(20,10) NOT NULL,
  `deathmorethanoneweek` decimal(20,10) NOT NULL,
  `deathsofchildren` decimal(20,10) NOT NULL,
  `deliveredbyskilledattendants` decimal(20,10) NOT NULL,
  `diarrhoea` decimal(20,10) NOT NULL,
  `district_id` bigint DEFAULT NULL,
  `ecpusers` decimal(20,10) NOT NULL,
  `eligiblecouples` decimal(20,10) NOT NULL,
  `eyeinfection` decimal(20,10) NOT NULL,
  `fever` decimal(20,10) NOT NULL,
  `fistulacases` decimal(20,10) NOT NULL,
  `flush` decimal(20,10) NOT NULL,
  `followupcases` decimal(20,10) NOT NULL,
  `followupcasesforfamilyplanning` decimal(20,10) NOT NULL,
  `handpump` decimal(20,10) NOT NULL,
  `healtboardfunction` varchar(50) NOT NULL,
  `healthboardavailable` varchar(50) NOT NULL,
  `hepatitas` decimal(20,10) NOT NULL,
  `householdregisteredbyhw` decimal(20,10) NOT NULL,
  `householdusingiodine` decimal(20,10) NOT NULL,
  `infantsdeaths` decimal(20,10) NOT NULL,
  `injuries` decimal(20,10) NOT NULL,
  `ironsuppliedpregnantwomen` decimal(20,10) NOT NULL,
  `isheathcommittesformulated` varchar(50) NOT NULL,
  `iswomensupportgroupformulated` varchar(50) NOT NULL,
  `iucdclient` decimal(20,10) NOT NULL,
  `kitbagavailability` varchar(50) NOT NULL,
  `kitbagfunctional` varchar(50) NOT NULL,
  `lessthanfiveyearchildren` decimal(20,10) NOT NULL,
  `lessthanfiveyearchildrengmdone` decimal(20,10) NOT NULL,
  `lessthanfiveyearchildrenlowweight` decimal(20,10) NOT NULL,
  `lessthanfiveyearchildrenprovidedsachet` decimal(20,10) NOT NULL,
  `livebirths` decimal(20,10) NOT NULL,
  `malaria` decimal(20,10) NOT NULL,
  `malnutritionchildren` decimal(20,10) NOT NULL,
  `maternaldeaths` decimal(20,10) NOT NULL,
  `maucforchildrenavailable` varchar(50) NOT NULL,
  `maucforchildrenfunction` varchar(50) NOT NULL,
  `maucformotheravailable` varchar(50) NOT NULL,
  `maucformotherfunction` varchar(50) NOT NULL,
  `visitsbyadc` decimal(20,10) NOT NULL,
  `modernmethodusers` decimal(20,10) NOT NULL,
  `newfamilyplanningclients` decimal(20,10) NOT NULL,
  `newnataldeaths` decimal(20,10) NOT NULL,
  `noofabortions` decimal(20,10) NOT NULL,
  `noofhealthcommitteemeeting` decimal(20,10) NOT NULL,
  `noofhealtheducationsessionsheld` decimal(20,10) NOT NULL,
  `nooflowbirthweighted` decimal(20,10) NOT NULL,
  `noofnewbirthstartedbreastfeeding` decimal(20,10) NOT NULL,
  `noofnewbornappliedchx` decimal(20,10) NOT NULL,
  `noofnewbornimmunestarted` decimal(20,10) NOT NULL,
  `noofnewbornsweighted` decimal(20,10) NOT NULL,
  `noofpregnantandbreastfeddingwomen` decimal(20,10) NOT NULL,
  `openfields` decimal(20,10) NOT NULL,
  `oralpillusers` decimal(20,10) NOT NULL,
  `otheravailable` varchar(50) NOT NULL,
  `otherdiseases` decimal(20,10) NOT NULL,
  `otherdrinkingsource` decimal(20,10) NOT NULL,
  `otherfunction` varchar(55) NOT NULL,
  `othermoderncontraceptiveusers` decimal(20,10) NOT NULL,
  `pit` decimal(20,10) NOT NULL,
  `postnatalcasevisited` decimal(20,10) NOT NULL,
  `referalcasestohealthfacility` decimal(20,10) NOT NULL,
  `scabies` decimal(20,10) NOT NULL,
  `scissorsavailable` varchar(50) NOT NULL,
  `scissorsfunction` varchar(50) NOT NULL,
  `sixmontholdchildren` decimal(20,10) NOT NULL,
  `sixmontholdchildrenhavingbreastfeed` decimal(20,10) NOT NULL,
  `sixtofiveninechildrenhavingmaucdone` decimal(20,10) NOT NULL,
  `sixtofiveninemalnutritionchildren` decimal(20,10) NOT NULL,
  `sixtofiveninemonthchildren` decimal(20,10) NOT NULL,
  `stethoscopeavailable` varchar(50) NOT NULL,
  `stethoscopefunction` varchar(50) NOT NULL,
  `stillbirths` decimal(20,10) NOT NULL,
  `suppliedwithcondoms` decimal(20,10) NOT NULL,
  `suppliedwithoral` decimal(20,10) NOT NULL,
  `surgicalclient` decimal(20,10) NOT NULL,
  `tap` decimal(20,10) NOT NULL,
  `tbcases` decimal(20,10) NOT NULL,
  `thermometeravailable` varchar(50) NOT NULL,
  `thermometerfunction` varchar(50) NOT NULL,
  `threemonthinjection` decimal(20,10) NOT NULL,
  `torchavailable` varchar(50) NOT NULL,
  `torchfunction` varchar(50) NOT NULL,
  `total` decimal(20,10) NOT NULL,
  `totalhouseholdwithdrinkingwatersource` decimal(20,10) NOT NULL,
  `totalofdeliveries` decimal(20,10) NOT NULL,
  `totalpregnantwomen` decimal(20,10) NOT NULL,
  `totalpregnantwomenvisited` decimal(20,10) NOT NULL,
  `tractinfection` decimal(20,10) NOT NULL,
  `traditionalmethodusers` decimal(20,10) NOT NULL,
  `twelvetotwentythreechildrenfullyimmunized` decimal(20,10) NOT NULL,
  `twelvetotwentythreemonthchildren` decimal(20,10) NOT NULL,
  `twomonthinjection` decimal(20,10) NOT NULL,
  `user_id` int DEFAULT NULL,
  `visitsbydco` decimal(20,10) NOT NULL,
  `visitsbylhs` decimal(20,10) NOT NULL,
  `womendeliveredancvisits` decimal(20,10) NOT NULL,
  `visitsbyfpo` decimal(20,10) NOT NULL,
  `visitsbyppiu` decimal(20,10) NOT NULL,
  `weighingmachineavailability` varchar(50) NOT NULL,
  `weighingmachinefunction` varchar(50) NOT NULL,
  `well` decimal(20,10) NOT NULL,
  `womendeliveredtabprovided` decimal(20,10) NOT NULL,
  `womendeliveredwithttcompleted` decimal(20,10) NOT NULL,
  `worminfection` decimal(20,10) NOT NULL,
  `datesubmitted` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `health_worker_report_district_id_8dcedaed_fk_health_wo` (`district_id`),
  KEY `health_worker_report_user_id_1f0c2129_fk_auth_user_id` (`user_id`),
  CONSTRAINT `health_worker_report_district_id_8dcedaed_fk_health_wo` FOREIGN KEY (`district_id`) REFERENCES `health_worker_district` (`id`),
  CONSTRAINT `health_worker_report_user_id_1f0c2129_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health_worker_report`
--

LOCK TABLES `health_worker_report` WRITE;
/*!40000 ALTER TABLE `health_worker_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `health_worker_report` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-22 13:02:11
