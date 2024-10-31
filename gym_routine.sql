-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2024 at 09:13 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gym_routine`
--

-- --------------------------------------------------------

--
-- Table structure for table `exercise_tbl`
--

CREATE TABLE `exercise_tbl` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `target_muscle` varchar(100) NOT NULL,
  `equipment_needed` varchar(100) NOT NULL,
  `reps` int(100) NOT NULL,
  `sets` int(100) NOT NULL,
  `rest_time` time(6) NOT NULL,
  `exercise_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nutrition_tbl`
--

CREATE TABLE `nutrition_tbl` (
  `id` int(10) NOT NULL,
  `user_id` text NOT NULL,
  `date` date NOT NULL,
  `meal_type` varchar(100) NOT NULL,
  `calories` int(100) NOT NULL,
  `protein` float NOT NULL,
  `carbs` float NOT NULL,
  `fats` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `progress_tbl`
--

CREATE TABLE `progress_tbl` (
  `id` int(10) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `weight` float NOT NULL,
  `bodyfat_percentage` decimal(65,0) NOT NULL,
  `muscle_mass` float NOT NULL,
  `workout_id` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_tbl`
--

CREATE TABLE `user_tbl` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `age` int(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `height` int(10) NOT NULL,
  `weight` int(100) NOT NULL,
  `fitness_lvl` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `workout_schedule_tbl`
--

CREATE TABLE `workout_schedule_tbl` (
  `id` int(10) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `workout_id` varchar(100) NOT NULL,
  `day_of_week` varchar(100) NOT NULL,
  `time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `workout_tbl`
--

CREATE TABLE `workout_tbl` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `discription` varchar(100) NOT NULL,
  `target_muscle` varchar(100) NOT NULL,
  `level` int(100) NOT NULL,
  `duration` time(6) NOT NULL,
  `calories_burned` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `exercise_tbl`
--
ALTER TABLE `exercise_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nutrition_tbl`
--
ALTER TABLE `nutrition_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `progress_tbl`
--
ALTER TABLE `progress_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_tbl`
--
ALTER TABLE `user_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `workout_schedule_tbl`
--
ALTER TABLE `workout_schedule_tbl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `workout_tbl`
--
ALTER TABLE `workout_tbl`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `exercise_tbl`
--
ALTER TABLE `exercise_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nutrition_tbl`
--
ALTER TABLE `nutrition_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `progress_tbl`
--
ALTER TABLE `progress_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_tbl`
--
ALTER TABLE `user_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `workout_schedule_tbl`
--
ALTER TABLE `workout_schedule_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `workout_tbl`
--
ALTER TABLE `workout_tbl`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
