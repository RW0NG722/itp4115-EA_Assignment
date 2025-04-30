/*
 Navicat Premium Dump SQL

 Source Server         : DEDE
 Source Server Type    : MySQL
 Source Server Version : 50743 (5.7.43-log)
 Source Host           : localhost:3306
 Source Schema         : hkcinema

 Target Server Type    : MySQL
 Target Server Version : 50743 (5.7.43-log)
 File Encoding         : 65001

 Date: 11/04/2025 23:49:36
*/

use cinema;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `birth_date` date,
  `phone` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email_subscription` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `occupation` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `income_level` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `work_location` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `residence_location` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cinema
-- ----------------------------
DROP TABLE IF EXISTS `cinemas`;
CREATE TABLE `cinemas`  (
  `cinema_id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `capacity` int(11) NOT NULL,
  `house` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sent` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `format` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ticket information` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`cinema_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cinema
-- ----------------------------

-- ----------------------------
-- Table structure for houses
-- ----------------------------
DROP TABLE IF EXISTS `houses`;
CREATE TABLE `houses` (
  `house_id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_id` int NOT NULL,
  `house_name` VARCHAR(100) NOT NULL,
  `house_type` int NOT NULL,
  `house_available` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`house_id`) USING BTREE,
  FOREIGN KEY (`cinema_id`) REFERENCES `cinemas`(`cinema_id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of houses
-- ----------------------------

-- ----------------------------
-- Table structure for seats
-- ----------------------------
DROP TABLE IF EXISTS `seats`;
CREATE TABLE `seats` (
  `seat_id` int(11) NOT NULL AUTO_INCREMENT,
  `house_id` int NOT NULL,
  `seat_name` VARCHAR(100) NOT NULL,
  `seat_type` VARCHAR(10) NOT NULL,
  `seat_available` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`seat_id`) USING BTREE,
  FOREIGN KEY (`house_id`) REFERENCES `houses`(`house_id`)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of seats
-- ----------------------------

-- ----------------------------
-- Table structure for movies
-- ----------------------------
DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies`  (
  `movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `release_date` date NOT NULL,
  `duration` int(11) NOT NULL,
  `language` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `synopsis` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `director` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cast` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `movie_type` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`movie_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movies
-- ----------------------------

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `showtime_id` int(11) NOT NULL,
  `order_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `seat_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ticket_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `service_fee` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `total_amount` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`order_id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE,
  INDEX `showtime_id`(`showtime_id`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`showtime_id`) REFERENCES `showtimes` (`showtime_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------

-- ----------------------------
-- Table structure for showtimes
-- ----------------------------
DROP TABLE IF EXISTS `showtimes`;
CREATE TABLE `showtimes`  (
  `showtime_id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NOT NULL,
  `cinema_id` int(11) NOT NULL,
  `show_date` date NOT NULL,
  `show_time` time NOT NULL,
  `house_number` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`showtime_id`) USING BTREE,
  INDEX `movie_id`(`movie_id`) USING BTREE,
  INDEX `cinema_id`(`cinema_id`) USING BTREE,
  CONSTRAINT `showtimes_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `showtimes_ibfk_2` FOREIGN KEY (`cinema_id`) REFERENCES `cinemas` (`cinema_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for members
-- ----------------------------
DROP TABLE IF EXISTS `members`;
CREATE TABLE `members`  (
  `member_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `member_price` int(10) NOT NULL,
  PRIMARY KEY (`member_type`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of members
-- ----------------------------

-- ----------------------------
-- Table structure for advertisements
-- ----------------------------
DROP TABLE IF EXISTS `advertisements`;
CREATE TABLE `advertisements`  (
  `ad_id` int(50) NOT NULL AUTO_INCREMENT,
  `ad_title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ad_content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `member_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ad_id`) USING BTREE,
  INDEX `member_type`(`member_type`) USING BTREE,
  CONSTRAINT `advertisements_ibfk_1` FOREIGN KEY (`member_type`) REFERENCES `members` (`member_type`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of advertisements
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
