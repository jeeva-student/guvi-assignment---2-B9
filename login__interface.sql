-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2021 at 07:40 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login_interface`
--

-- --------------------------------------------------------

--
-- Table structure for table `login__interface`
--

CREATE TABLE `login__interface` (
  `Id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login__interface`
--

INSERT INTO `login__interface` (`Id`, `user_name`, `password`) VALUES
(1, 'ram@gmail.com', 'Ram@2020'),
(2, 'kumar@gmail.com', 'Pass@2020'),
(3, 'friend@gmail.com', 'Friend@2020'),
(4, 'friend@gmail.com', 'Friend@2020'),
(5, 'hari@gmail.com', 'Hari@1999'),
(6, 'Jeeva@gmail.com', 'Jeeva@2021'),
(7, 'briyani@gmail.com', 'Briyani@124'),
(8, 'karthick@gmail.com', 'Karthick@2021'),
(9, 'ajeeva@gmail.com', 'Jeeva@10'),
(10, 'kumari@gmail.com', 'Kumari@123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login__interface`
--
ALTER TABLE `login__interface`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login__interface`
--
ALTER TABLE `login__interface`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
