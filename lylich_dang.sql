-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2026 at 02:22 AM
-- Server version: 10.11.16-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lylich_dang`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_requests`
--

CREATE TABLE `account_requests` (
  `id` bigint(20) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `cccd` varchar(12) NOT NULL,
  `dob` date NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `notify_sms` tinyint(1) NOT NULL,
  `notify_email` tinyint(1) NOT NULL,
  `notify_zalo` tinyint(1) NOT NULL,
  `status` varchar(20) NOT NULL,
  `fail_reason` varchar(500) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `processed_at` datetime(6) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `officer_in_charge` bigint(20) DEFAULT NULL,
  `requested_by_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `account_requests`
--

INSERT INTO `account_requests` (`id`, `full_name`, `cccd`, `dob`, `phone`, `email`, `notify_sms`, `notify_email`, `notify_zalo`, `status`, `fail_reason`, `notes`, `created_at`, `processed_at`, `user_id`, `officer_in_charge`, `requested_by_id`) VALUES
(1, 'eeeeeee', '05456453535', '2000-01-01', '0978765432', 'linh@gmail.comd', 1, 0, 0, 'failed', 'log_activity() got an unexpected keyword argument \'target_type\'. Did you mean \'target_model\'?', NULL, '2026-05-12 12:46:39.262695', '2026-05-12 12:46:39.946425', 54, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `activity_logs`
--

CREATE TABLE `activity_logs` (
  `id` bigint(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `target_model` varchar(80) DEFAULT NULL,
  `target_id` bigint(20) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(500) DEFAULT NULL,
  `extra` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`extra`)),
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `activity_logs`
--

INSERT INTO `activity_logs` (`id`, `action`, `target_model`, `target_id`, `description`, `ip_address`, `user_agent`, `extra`, `created_at`, `user_id`) VALUES
(1, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 04:11:25.369041', 1),
(2, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 04:21:53.087490', 1),
(3, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 04:21:53.089519', 1),
(4, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 05:06:12.633879', 1),
(5, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 05:06:12.636198', 1),
(6, 'create', NULL, NULL, 'POST /api/v1/notifications/bulk-send/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 07:40:29.027551', 1),
(7, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 07:40:34.896056', 1),
(8, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 07:40:34.898004', 1),
(9, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 07:55:35.935730', 1),
(10, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 07:55:35.938135', 1),
(11, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 09:58:30.404784', 1),
(12, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 09:58:30.406479', 1),
(13, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 10:08:44.692611', 1),
(14, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 10:08:44.694416', 1),
(15, 'export', 'Profile', 10, 'Xuất Word hồ sơ Nguyễn Thị Bình An', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 10:34:01.324892', 1),
(16, 'create', NULL, NULL, 'POST /api/v1/exports/word/10/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 10:34:01.326746', 1),
(17, 'export', 'Profile', 11, 'Xuất Word hồ sơ Lê Thị Mai', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 11:08:20.390597', 1),
(18, 'create', NULL, NULL, 'POST /api/v1/exports/word/11/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 11:08:20.393331', 1),
(19, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 11:41:09.203743', 1),
(20, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:51:15.244311', NULL),
(21, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:51:24.811195', NULL),
(22, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:52:09.276137', NULL),
(23, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:52:23.719786', NULL),
(24, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:52:35.964900', NULL),
(25, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:52:42.562340', NULL),
(26, 'update', NULL, NULL, 'PATCH /api/v1/profiles/my/', '127.0.0.1', 'curl/8.12.1', NULL, '2026-05-12 11:52:56.401897', NULL),
(27, 'export', 'Profile', 11, 'Xuất Word hồ sơ NGO DINH HOANG', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 11:57:38.471241', 1),
(28, 'create', NULL, NULL, 'POST /api/v1/exports/word/11/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 11:57:38.472839', 1),
(29, 'export', 'Profile', 40, 'Xuất Word hồ sơ Trương Thị Hằng', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 12:36:43.574464', 1),
(30, 'create', NULL, NULL, 'POST /api/v1/exports/word/40/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 12:36:43.576743', 1),
(31, 'create', NULL, NULL, 'POST /api/v1/auth/account-requests/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 12:46:39.953739', 1),
(32, 'export', NULL, NULL, 'Xuất báo cáo Excel BaoCao_2026.xlsx', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 12:53:50.418212', 1),
(33, 'create', NULL, NULL, 'POST /api/v1/reports/export/excel/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 12:53:50.424074', 1),
(34, 'export', 'Profile', 40, 'Xuất Word hồ sơ Trương Thị Hằng', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:17:36.014429', 1),
(35, 'create', NULL, NULL, 'POST /api/v1/exports/word/40/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:17:36.016395', 1),
(36, 'export', 'Profile', 39, 'Xuất Word hồ sơ Trần Thị Hoa', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:17:46.677463', 1),
(37, 'create', NULL, NULL, 'POST /api/v1/exports/word/39/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:17:46.679522', 1),
(38, 'export', 'Profile', 31, 'Xuất Word hồ sơ Lê Thị Mai', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:18:01.818737', 1),
(39, 'create', NULL, NULL, 'POST /api/v1/exports/word/31/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:18:01.820586', 1),
(40, 'export', 'Profile', 51, 'Xuất Word hồ sơ Ngô Đình Hoàng', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:27:22.284876', 1),
(41, 'create', NULL, NULL, 'POST /api/v1/exports/word/51/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 14:27:22.287413', 1),
(42, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 16:51:07.499728', 1),
(43, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Edg/148.0.0.0', NULL, '2026-05-12 16:51:29.087269', 1),
(44, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 16:58:38.782350', 1),
(45, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:01:24.482037', 1),
(46, 'create', NULL, NULL, 'POST /api/v1/profiles/my/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:02:42.217472', 1),
(47, 'create', NULL, NULL, 'POST /api/v1/profiles/45/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:04:56.656260', 1),
(48, 'create', NULL, NULL, 'POST /api/v1/profiles/45/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:05:00.690687', 1),
(49, 'logout', NULL, NULL, 'Đăng xuất', NULL, NULL, NULL, '2026-05-12 17:16:41.557877', 1),
(50, 'create', NULL, NULL, 'POST /api/v1/auth/logout/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:16:41.559805', 1),
(51, 'profile_create', 'Profile', 53, 'Tạo hồ sơ nháp: Test Tao Nhanh 2', NULL, NULL, NULL, '2026-05-12 17:25:09.442770', 56),
(52, 'logout', NULL, NULL, 'Đăng xuất', NULL, NULL, NULL, '2026-05-12 17:25:40.577551', 68),
(53, 'create', NULL, NULL, 'POST /api/v1/auth/logout/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:25:40.579320', 68),
(54, 'create', NULL, NULL, 'POST /api/v1/profiles/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:26:50.007596', 1),
(55, 'profile_create', 'Profile', 54, 'Tạo hồ sơ nháp: Hồ sơ mới 12/05/2026 17:27', NULL, NULL, NULL, '2026-05-12 17:27:38.280101', 56),
(56, 'create', NULL, NULL, 'POST /api/v1/profiles/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Code/1.119.0 Chrome/142.0.7444.265 Electron/39.8.8 Safari/537.36', NULL, '2026-05-12 17:27:38.289127', 56),
(57, 'profile_create', 'Profile', 55, 'Tạo hồ sơ nháp: Hồ sơ mới 12/05/2026 17:28', NULL, NULL, NULL, '2026-05-12 17:28:42.211112', 56),
(58, 'profile_create', 'Profile', 56, 'Tạo hồ sơ nháp: NGUYEN THI LIMH', NULL, NULL, NULL, '2026-05-12 17:29:23.201966', 1),
(59, 'create', NULL, NULL, 'POST /api/v1/profiles/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:29:23.213811', 1),
(60, 'create', NULL, NULL, 'POST /api/v1/profiles/55/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:29:51.220356', 1),
(61, 'create', NULL, NULL, 'POST /api/v1/profiles/55/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:29:58.455902', 1),
(62, 'create', NULL, NULL, 'POST /api/v1/profiles/55/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:30:10.788915', 1),
(63, 'create', NULL, NULL, 'POST /api/v1/profiles/56/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:33:46.920850', 1),
(64, 'create', NULL, NULL, 'POST /api/v1/profiles/56/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:33:50.431304', 1),
(65, 'export', 'Profile', 56, 'Xuất Word hồ sơ NGUYEN THI LIMH', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:33:56.992567', 1),
(66, 'create', NULL, NULL, 'POST /api/v1/exports/word/56/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:33:56.994252', 1),
(67, 'export', 'Profile', 56, 'Xuất Word hồ sơ NGUYEN THI LIMH', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:58:10.294527', 1),
(68, 'create', NULL, NULL, 'POST /api/v1/exports/word/56/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:58:10.297880', 1),
(69, 'export', 'Profile', 41, 'Xuất Word hồ sơ Lê Thị Mai', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:58:33.815062', 1),
(70, 'create', NULL, NULL, 'POST /api/v1/exports/word/41/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 17:58:33.817030', 1),
(71, 'return', 'Profile', 45, 'Đinh Thị Nhung: submitted → returned', NULL, NULL, NULL, '2026-05-12 18:47:14.352221', 1),
(72, 'create', NULL, NULL, 'POST /api/v1/profiles/45/workflow/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 18:47:14.362491', 1),
(73, 'export', 'Profile', 51, 'Xuất Word hồ sơ Ngô Đình Hoàng', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 18:48:02.270077', 1),
(74, 'create', NULL, NULL, 'POST /api/v1/exports/word/51/', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0', NULL, '2026-05-12 18:48:02.273086', 1);

-- --------------------------------------------------------

--
-- Table structure for table `ai_scan_results`
--

CREATE TABLE `ai_scan_results` (
  `id` bigint(20) NOT NULL,
  `section` varchar(80) NOT NULL,
  `field_name` varchar(120) DEFAULT NULL,
  `issue_type` varchar(80) NOT NULL,
  `description` longtext NOT NULL,
  `severity` varchar(10) NOT NULL,
  `status` varchar(10) NOT NULL,
  `resolved_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL,
  `resolved_by` bigint(20) DEFAULT NULL,
  `scanned_by_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 3, 'add_permission'),
(6, 'Can change permission', 3, 'change_permission'),
(7, 'Can delete permission', 3, 'delete_permission'),
(8, 'Can view permission', 3, 'view_permission'),
(9, 'Can add group', 2, 'add_group'),
(10, 'Can change group', 2, 'change_group'),
(11, 'Can delete group', 2, 'delete_group'),
(12, 'Can view group', 2, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Blacklisted Token', 6, 'add_blacklistedtoken'),
(22, 'Can change Blacklisted Token', 6, 'change_blacklistedtoken'),
(23, 'Can delete Blacklisted Token', 6, 'delete_blacklistedtoken'),
(24, 'Can view Blacklisted Token', 6, 'view_blacklistedtoken'),
(25, 'Can add Outstanding Token', 7, 'add_outstandingtoken'),
(26, 'Can change Outstanding Token', 7, 'change_outstandingtoken'),
(27, 'Can delete Outstanding Token', 7, 'delete_outstandingtoken'),
(28, 'Can view Outstanding Token', 7, 'view_outstandingtoken'),
(29, 'Can add crontab', 9, 'add_crontabschedule'),
(30, 'Can change crontab', 9, 'change_crontabschedule'),
(31, 'Can delete crontab', 9, 'delete_crontabschedule'),
(32, 'Can view crontab', 9, 'view_crontabschedule'),
(33, 'Can add interval', 10, 'add_intervalschedule'),
(34, 'Can change interval', 10, 'change_intervalschedule'),
(35, 'Can delete interval', 10, 'delete_intervalschedule'),
(36, 'Can view interval', 10, 'view_intervalschedule'),
(37, 'Can add periodic task', 11, 'add_periodictask'),
(38, 'Can change periodic task', 11, 'change_periodictask'),
(39, 'Can delete periodic task', 11, 'delete_periodictask'),
(40, 'Can view periodic task', 11, 'view_periodictask'),
(41, 'Can add periodic task track', 12, 'add_periodictasks'),
(42, 'Can change periodic task track', 12, 'change_periodictasks'),
(43, 'Can delete periodic task track', 12, 'delete_periodictasks'),
(44, 'Can view periodic task track', 12, 'view_periodictasks'),
(45, 'Can add solar event', 13, 'add_solarschedule'),
(46, 'Can change solar event', 13, 'change_solarschedule'),
(47, 'Can delete solar event', 13, 'delete_solarschedule'),
(48, 'Can view solar event', 13, 'view_solarschedule'),
(49, 'Can add clocked', 8, 'add_clockedschedule'),
(50, 'Can change clocked', 8, 'change_clockedschedule'),
(51, 'Can delete clocked', 8, 'delete_clockedschedule'),
(52, 'Can view clocked', 8, 'view_clockedschedule'),
(53, 'Can add task result', 16, 'add_taskresult'),
(54, 'Can change task result', 16, 'change_taskresult'),
(55, 'Can delete task result', 16, 'delete_taskresult'),
(56, 'Can view task result', 16, 'view_taskresult'),
(57, 'Can add chord counter', 14, 'add_chordcounter'),
(58, 'Can change chord counter', 14, 'change_chordcounter'),
(59, 'Can delete chord counter', 14, 'delete_chordcounter'),
(60, 'Can view chord counter', 14, 'view_chordcounter'),
(61, 'Can add group result', 15, 'add_groupresult'),
(62, 'Can change group result', 15, 'change_groupresult'),
(63, 'Can delete group result', 15, 'delete_groupresult'),
(64, 'Can view group result', 15, 'view_groupresult'),
(65, 'Can add Trình độ học vấn', 18, 'add_educationlevel'),
(66, 'Can change Trình độ học vấn', 18, 'change_educationlevel'),
(67, 'Can delete Trình độ học vấn', 18, 'delete_educationlevel'),
(68, 'Can view Trình độ học vấn', 18, 'view_educationlevel'),
(69, 'Can add Dân tộc', 19, 'add_ethnicgroup'),
(70, 'Can change Dân tộc', 19, 'change_ethnicgroup'),
(71, 'Can delete Dân tộc', 19, 'delete_ethnicgroup'),
(72, 'Can view Dân tộc', 19, 'view_ethnicgroup'),
(73, 'Can add Trình độ chính trị', 20, 'add_politicallevel'),
(74, 'Can change Trình độ chính trị', 20, 'change_politicallevel'),
(75, 'Can delete Trình độ chính trị', 20, 'delete_politicallevel'),
(76, 'Can view Trình độ chính trị', 20, 'view_politicallevel'),
(77, 'Can add Tôn giáo', 21, 'add_religion'),
(78, 'Can change Tôn giáo', 21, 'change_religion'),
(79, 'Can delete Tôn giáo', 21, 'delete_religion'),
(80, 'Can view Tôn giáo', 21, 'view_religion'),
(81, 'Can add Đơn vị hành chính', 17, 'add_administrativeunit'),
(82, 'Can change Đơn vị hành chính', 17, 'change_administrativeunit'),
(83, 'Can delete Đơn vị hành chính', 17, 'delete_administrativeunit'),
(84, 'Can view Đơn vị hành chính', 17, 'view_administrativeunit'),
(85, 'Can add Vai trò', 25, 'add_role'),
(86, 'Can change Vai trò', 25, 'change_role'),
(87, 'Can delete Vai trò', 25, 'delete_role'),
(88, 'Can view Vai trò', 25, 'view_role'),
(89, 'Can add Người dùng', 27, 'add_user'),
(90, 'Can change Người dùng', 27, 'change_user'),
(91, 'Can delete Người dùng', 27, 'delete_user'),
(92, 'Can view Người dùng', 27, 'view_user'),
(93, 'Can add Đặt lại mật khẩu', 24, 'add_passwordreset'),
(94, 'Can change Đặt lại mật khẩu', 24, 'change_passwordreset'),
(95, 'Can delete Đặt lại mật khẩu', 24, 'delete_passwordreset'),
(96, 'Can view Đặt lại mật khẩu', 24, 'view_passwordreset'),
(97, 'Can add Phiên đăng nhập', 26, 'add_session'),
(98, 'Can change Phiên đăng nhập', 26, 'change_session'),
(99, 'Can delete Phiên đăng nhập', 26, 'delete_session'),
(100, 'Can view Phiên đăng nhập', 26, 'view_session'),
(101, 'Can add Yêu cầu cấp tài khoản', 22, 'add_accountrequest'),
(102, 'Can change Yêu cầu cấp tài khoản', 22, 'change_accountrequest'),
(103, 'Can delete Yêu cầu cấp tài khoản', 22, 'delete_accountrequest'),
(104, 'Can view Yêu cầu cấp tài khoản', 22, 'view_accountrequest'),
(105, 'Can add Lịch sử đăng nhập', 23, 'add_loginhistory'),
(106, 'Can change Lịch sử đăng nhập', 23, 'change_loginhistory'),
(107, 'Can delete Lịch sử đăng nhập', 23, 'delete_loginhistory'),
(108, 'Can view Lịch sử đăng nhập', 23, 'view_loginhistory'),
(109, 'Can add File đã tải lên', 28, 'add_uploadedfile'),
(110, 'Can change File đã tải lên', 28, 'change_uploadedfile'),
(111, 'Can delete File đã tải lên', 28, 'delete_uploadedfile'),
(112, 'Can view File đã tải lên', 28, 'view_uploadedfile'),
(113, 'Can add Hồ sơ lý lịch', 30, 'add_profile'),
(114, 'Can change Hồ sơ lý lịch', 30, 'change_profile'),
(115, 'Can delete Hồ sơ lý lịch', 30, 'delete_profile'),
(116, 'Can view Hồ sơ lý lịch', 30, 'view_profile'),
(117, 'Can add Nhận xét Ủy ban', 29, 'add_committeecomment'),
(118, 'Can change Nhận xét Ủy ban', 29, 'change_committeecomment'),
(119, 'Can delete Nhận xét Ủy ban', 29, 'delete_committeecomment'),
(120, 'Can view Nhận xét Ủy ban', 29, 'view_committeecomment'),
(121, 'Can add Phân công cán bộ', 31, 'add_profileofficerassignment'),
(122, 'Can change Phân công cán bộ', 31, 'change_profileofficerassignment'),
(123, 'Can delete Phân công cán bộ', 31, 'delete_profileofficerassignment'),
(124, 'Can view Phân công cán bộ', 31, 'view_profileofficerassignment'),
(125, 'Can add Lịch sử thẩm định', 32, 'add_profilereview'),
(126, 'Can change Lịch sử thẩm định', 32, 'change_profilereview'),
(127, 'Can delete Lịch sử thẩm định', 32, 'delete_profilereview'),
(128, 'Can view Lịch sử thẩm định', 32, 'view_profilereview'),
(129, 'Can add Thành viên gia đình', 33, 'add_familymember'),
(130, 'Can change Thành viên gia đình', 33, 'change_familymember'),
(131, 'Can delete Thành viên gia đình', 33, 'delete_familymember'),
(132, 'Can view Thành viên gia đình', 33, 'view_familymember'),
(133, 'Can add Khen thưởng / Kỷ luật', 34, 'add_award'),
(134, 'Can change Khen thưởng / Kỷ luật', 34, 'change_award'),
(135, 'Can delete Khen thưởng / Kỷ luật', 34, 'delete_award'),
(136, 'Can view Khen thưởng / Kỷ luật', 34, 'view_award'),
(137, 'Can add Lịch sử học vấn', 35, 'add_educationhistory'),
(138, 'Can change Lịch sử học vấn', 35, 'change_educationhistory'),
(139, 'Can delete Lịch sử học vấn', 35, 'delete_educationhistory'),
(140, 'Can view Lịch sử học vấn', 35, 'view_educationhistory'),
(141, 'Can add Tham gia tổ chức', 37, 'add_orgparticipation'),
(142, 'Can change Tham gia tổ chức', 37, 'change_orgparticipation'),
(143, 'Can delete Tham gia tổ chức', 37, 'delete_orgparticipation'),
(144, 'Can view Tham gia tổ chức', 37, 'view_orgparticipation'),
(145, 'Can add Người thân ở nước ngoài', 38, 'add_overseasrelative'),
(146, 'Can change Người thân ở nước ngoài', 38, 'change_overseasrelative'),
(147, 'Can delete Người thân ở nước ngoài', 38, 'delete_overseasrelative'),
(148, 'Can view Người thân ở nước ngoài', 38, 'view_overseasrelative'),
(149, 'Can add Ra nước ngoài', 39, 'add_overseastravel'),
(150, 'Can change Ra nước ngoài', 39, 'change_overseastravel'),
(151, 'Can delete Ra nước ngoài', 39, 'delete_overseastravel'),
(152, 'Can view Ra nước ngoài', 39, 'view_overseastravel'),
(153, 'Can add Lịch sử công tác', 40, 'add_workhistory'),
(154, 'Can change Lịch sử công tác', 40, 'change_workhistory'),
(155, 'Can delete Lịch sử công tác', 40, 'delete_workhistory'),
(156, 'Can view Lịch sử công tác', 40, 'view_workhistory'),
(157, 'Can add Lịch sử bản thân', 36, 'add_historyentry'),
(158, 'Can change Lịch sử bản thân', 36, 'change_historyentry'),
(159, 'Can delete Lịch sử bản thân', 36, 'delete_historyentry'),
(160, 'Can view Lịch sử bản thân', 36, 'view_historyentry'),
(161, 'Can add Yêu cầu xác minh', 42, 'add_verificationrequest'),
(162, 'Can change Yêu cầu xác minh', 42, 'change_verificationrequest'),
(163, 'Can delete Yêu cầu xác minh', 42, 'delete_verificationrequest'),
(164, 'Can view Yêu cầu xác minh', 42, 'view_verificationrequest'),
(165, 'Can add Nhật ký nhắc xác minh', 41, 'add_verificationreminderlog'),
(166, 'Can change Nhật ký nhắc xác minh', 41, 'change_verificationreminderlog'),
(167, 'Can delete Nhật ký nhắc xác minh', 41, 'delete_verificationreminderlog'),
(168, 'Can view Nhật ký nhắc xác minh', 41, 'view_verificationreminderlog'),
(169, 'Can add Thông báo', 43, 'add_notification'),
(170, 'Can change Thông báo', 43, 'change_notification'),
(171, 'Can delete Thông báo', 43, 'delete_notification'),
(172, 'Can view Thông báo', 43, 'view_notification'),
(173, 'Can add Đợt gửi thông báo', 44, 'add_notificationbatch'),
(174, 'Can change Đợt gửi thông báo', 44, 'change_notificationbatch'),
(175, 'Can delete Đợt gửi thông báo', 44, 'delete_notificationbatch'),
(176, 'Can view Đợt gửi thông báo', 44, 'view_notificationbatch'),
(177, 'Can add Mẫu thông báo', 45, 'add_notificationtemplate'),
(178, 'Can change Mẫu thông báo', 45, 'change_notificationtemplate'),
(179, 'Can delete Mẫu thông báo', 45, 'delete_notificationtemplate'),
(180, 'Can view Mẫu thông báo', 45, 'view_notificationtemplate'),
(181, 'Can add Mục yêu cầu bổ sung', 46, 'add_profilecorrectionitem'),
(182, 'Can change Mục yêu cầu bổ sung', 46, 'change_profilecorrectionitem'),
(183, 'Can delete Mục yêu cầu bổ sung', 46, 'delete_profilecorrectionitem'),
(184, 'Can view Mục yêu cầu bổ sung', 46, 'view_profilecorrectionitem'),
(185, 'Can add Lịch sử chỉnh sửa', 48, 'add_profileedithistory'),
(186, 'Can change Lịch sử chỉnh sửa', 48, 'change_profileedithistory'),
(187, 'Can delete Lịch sử chỉnh sửa', 48, 'delete_profileedithistory'),
(188, 'Can view Lịch sử chỉnh sửa', 48, 'view_profileedithistory'),
(189, 'Can add Xuất Word', 49, 'add_wordexportlog'),
(190, 'Can change Xuất Word', 49, 'change_wordexportlog'),
(191, 'Can delete Xuất Word', 49, 'delete_wordexportlog'),
(192, 'Can view Xuất Word', 49, 'view_wordexportlog'),
(193, 'Can add Yêu cầu bổ sung', 47, 'add_profilecorrectionrequest'),
(194, 'Can change Yêu cầu bổ sung', 47, 'change_profilecorrectionrequest'),
(195, 'Can delete Yêu cầu bổ sung', 47, 'delete_profilecorrectionrequest'),
(196, 'Can view Yêu cầu bổ sung', 47, 'view_profilecorrectionrequest'),
(197, 'Can add Xuất báo cáo', 50, 'add_reportexport'),
(198, 'Can change Xuất báo cáo', 50, 'change_reportexport'),
(199, 'Can delete Xuất báo cáo', 50, 'delete_reportexport'),
(200, 'Can view Xuất báo cáo', 50, 'view_reportexport'),
(201, 'Can add Thống kê tháng', 51, 'add_statsmonthly'),
(202, 'Can change Thống kê tháng', 51, 'change_statsmonthly'),
(203, 'Can delete Thống kê tháng', 51, 'delete_statsmonthly'),
(204, 'Can view Thống kê tháng', 51, 'view_statsmonthly'),
(205, 'Can add Nhật ký hoạt động', 52, 'add_activitylog'),
(206, 'Can change Nhật ký hoạt động', 52, 'change_activitylog'),
(207, 'Can delete Nhật ký hoạt động', 52, 'delete_activitylog'),
(208, 'Can view Nhật ký hoạt động', 52, 'view_activitylog'),
(209, 'Can add Kết quả quét AI', 53, 'add_aiscanresult'),
(210, 'Can change Kết quả quét AI', 53, 'change_aiscanresult'),
(211, 'Can delete Kết quả quét AI', 53, 'delete_aiscanresult'),
(212, 'Can view Kết quả quét AI', 53, 'view_aiscanresult');

-- --------------------------------------------------------

--
-- Table structure for table `committee_comments`
--

CREATE TABLE `committee_comments` (
  `id` bigint(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `content` longtext DEFAULT NULL,
  `signed_by` varchar(255) DEFAULT NULL,
  `signed_date` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `updated_by` bigint(20) DEFAULT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_clockedschedule`
--

CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int(11) NOT NULL,
  `clocked_time` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_crontabschedule`
--

CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int(11) NOT NULL,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_intervalschedule`
--

CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int(11) NOT NULL,
  `every` int(11) NOT NULL,
  `period` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_periodictask`
--

CREATE TABLE `django_celery_beat_periodictask` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int(10) UNSIGNED NOT NULL CHECK (`total_run_count` >= 0),
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int(11) DEFAULT NULL,
  `interval_id` int(11) DEFAULT NULL,
  `solar_id` int(11) DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int(10) UNSIGNED DEFAULT NULL CHECK (`priority` >= 0),
  `headers` longtext NOT NULL,
  `clocked_id` int(11) DEFAULT NULL,
  `expire_seconds` int(10) UNSIGNED DEFAULT NULL CHECK (`expire_seconds` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_periodictasks`
--

CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint(6) NOT NULL,
  `last_update` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_beat_solarschedule`
--

CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int(11) NOT NULL,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_chordcounter`
--

CREATE TABLE `django_celery_results_chordcounter` (
  `id` int(11) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  `sub_tasks` longtext NOT NULL,
  `count` int(10) UNSIGNED NOT NULL CHECK (`count` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_groupresult`
--

CREATE TABLE `django_celery_results_groupresult` (
  `id` int(11) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_celery_results_taskresult`
--

CREATE TABLE `django_celery_results_taskresult` (
  `id` int(11) NOT NULL,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext DEFAULT NULL,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext DEFAULT NULL,
  `meta` longtext DEFAULT NULL,
  `task_args` longtext DEFAULT NULL,
  `task_kwargs` longtext DEFAULT NULL,
  `task_name` varchar(255) DEFAULT NULL,
  `worker` varchar(100) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `periodic_task_name` varchar(255) DEFAULT NULL,
  `date_started` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(22, 'accounts', 'accountrequest'),
(23, 'accounts', 'loginhistory'),
(24, 'accounts', 'passwordreset'),
(25, 'accounts', 'role'),
(26, 'accounts', 'session'),
(27, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(52, 'auditlogs', 'activitylog'),
(53, 'auditlogs', 'aiscanresult'),
(2, 'auth', 'group'),
(3, 'auth', 'permission'),
(17, 'common', 'administrativeunit'),
(18, 'common', 'educationlevel'),
(19, 'common', 'ethnicgroup'),
(20, 'common', 'politicallevel'),
(21, 'common', 'religion'),
(4, 'contenttypes', 'contenttype'),
(8, 'django_celery_beat', 'clockedschedule'),
(9, 'django_celery_beat', 'crontabschedule'),
(10, 'django_celery_beat', 'intervalschedule'),
(11, 'django_celery_beat', 'periodictask'),
(12, 'django_celery_beat', 'periodictasks'),
(13, 'django_celery_beat', 'solarschedule'),
(14, 'django_celery_results', 'chordcounter'),
(15, 'django_celery_results', 'groupresult'),
(16, 'django_celery_results', 'taskresult'),
(46, 'exports', 'profilecorrectionitem'),
(47, 'exports', 'profilecorrectionrequest'),
(48, 'exports', 'profileedithistory'),
(49, 'exports', 'wordexportlog'),
(33, 'family', 'familymember'),
(43, 'notifications', 'notification'),
(44, 'notifications', 'notificationbatch'),
(45, 'notifications', 'notificationtemplate'),
(29, 'profiles', 'committeecomment'),
(30, 'profiles', 'profile'),
(31, 'profiles', 'profileofficerassignment'),
(32, 'profiles', 'profilereview'),
(50, 'reports', 'reportexport'),
(51, 'reports', 'statsmonthly'),
(5, 'sessions', 'session'),
(34, 'timelines', 'award'),
(35, 'timelines', 'educationhistory'),
(36, 'timelines', 'historyentry'),
(37, 'timelines', 'orgparticipation'),
(38, 'timelines', 'overseasrelative'),
(39, 'timelines', 'overseastravel'),
(40, 'timelines', 'workhistory'),
(6, 'token_blacklist', 'blacklistedtoken'),
(7, 'token_blacklist', 'outstandingtoken'),
(28, 'uploads', 'uploadedfile'),
(41, 'verification', 'verificationreminderlog'),
(42, 'verification', 'verificationrequest');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-05-12 02:46:54.315397'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-05-12 02:46:54.349157'),
(3, 'auth', '0001_initial', '2026-05-12 02:46:54.491423'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-05-12 02:46:54.515176'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-05-12 02:46:54.521450'),
(6, 'auth', '0004_alter_user_username_opts', '2026-05-12 02:46:54.527406'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-05-12 02:46:54.533145'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-05-12 02:46:54.535117'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-05-12 02:46:54.541251'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-05-12 02:46:54.546727'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-05-12 02:46:54.552421'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-05-12 02:46:54.567879'),
(13, 'auth', '0011_update_proxy_permissions', '2026-05-12 02:46:54.575305'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-05-12 02:46:54.581070'),
(15, 'accounts', '0001_initial', '2026-05-12 02:46:55.360436'),
(16, 'admin', '0001_initial', '2026-05-12 02:46:55.494685'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-05-12 02:46:55.508409'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-05-12 02:46:55.523140'),
(19, 'uploads', '0001_initial', '2026-05-12 02:46:55.587535'),
(20, 'common', '0001_initial', '2026-05-12 02:46:55.683309'),
(21, 'profiles', '0001_initial', '2026-05-12 02:46:56.747900'),
(22, 'auditlogs', '0001_initial', '2026-05-12 02:46:56.949928'),
(23, 'django_celery_beat', '0001_initial', '2026-05-12 02:46:57.025831'),
(24, 'django_celery_beat', '0002_auto_20161118_0346', '2026-05-12 02:46:57.073255'),
(25, 'django_celery_beat', '0003_auto_20161209_0049', '2026-05-12 02:46:57.091104'),
(26, 'django_celery_beat', '0004_auto_20170221_0000', '2026-05-12 02:46:57.096887'),
(27, 'django_celery_beat', '0005_add_solarschedule_events_choices', '2026-05-12 02:46:57.102166'),
(28, 'django_celery_beat', '0006_auto_20180322_0932', '2026-05-12 02:46:57.221900'),
(29, 'django_celery_beat', '0007_auto_20180521_0826', '2026-05-12 02:46:57.265584'),
(30, 'django_celery_beat', '0008_auto_20180914_1922', '2026-05-12 02:46:57.298668'),
(31, 'django_celery_beat', '0006_auto_20180210_1226', '2026-05-12 02:46:57.318891'),
(32, 'django_celery_beat', '0006_periodictask_priority', '2026-05-12 02:46:57.340419'),
(33, 'django_celery_beat', '0009_periodictask_headers', '2026-05-12 02:46:57.368243'),
(34, 'django_celery_beat', '0010_auto_20190429_0326', '2026-05-12 02:46:57.551789'),
(35, 'django_celery_beat', '0011_auto_20190508_0153', '2026-05-12 02:46:57.598312'),
(36, 'django_celery_beat', '0012_periodictask_expire_seconds', '2026-05-12 02:46:57.616678'),
(37, 'django_celery_beat', '0013_auto_20200609_0727', '2026-05-12 02:46:57.627348'),
(38, 'django_celery_beat', '0014_remove_clockedschedule_enabled', '2026-05-12 02:46:57.643707'),
(39, 'django_celery_beat', '0015_edit_solarschedule_events_choices', '2026-05-12 02:46:57.648279'),
(40, 'django_celery_beat', '0016_alter_crontabschedule_timezone', '2026-05-12 02:46:57.661395'),
(41, 'django_celery_beat', '0017_alter_crontabschedule_month_of_year', '2026-05-12 02:46:57.671218'),
(42, 'django_celery_beat', '0018_improve_crontab_helptext', '2026-05-12 02:46:57.682630'),
(43, 'django_celery_beat', '0019_alter_periodictasks_options', '2026-05-12 02:46:57.687226'),
(44, 'django_celery_results', '0001_initial', '2026-05-12 02:46:57.725453'),
(45, 'django_celery_results', '0002_add_task_name_args_kwargs', '2026-05-12 02:46:57.782615'),
(46, 'django_celery_results', '0003_auto_20181106_1101', '2026-05-12 02:46:57.786340'),
(47, 'django_celery_results', '0004_auto_20190516_0412', '2026-05-12 02:46:57.849436'),
(48, 'django_celery_results', '0005_taskresult_worker', '2026-05-12 02:46:57.875579'),
(49, 'django_celery_results', '0006_taskresult_date_created', '2026-05-12 02:46:57.955922'),
(50, 'django_celery_results', '0007_remove_taskresult_hidden', '2026-05-12 02:46:57.970036'),
(51, 'django_celery_results', '0008_chordcounter', '2026-05-12 02:46:57.980347'),
(52, 'django_celery_results', '0009_groupresult', '2026-05-12 02:46:59.029916'),
(53, 'django_celery_results', '0010_remove_duplicate_indices', '2026-05-12 02:46:59.042463'),
(54, 'django_celery_results', '0011_taskresult_periodic_task_name', '2026-05-12 02:46:59.056184'),
(55, 'django_celery_results', '0012_taskresult_date_started', '2026-05-12 02:46:59.069350'),
(56, 'django_celery_results', '0013_taskresult_django_cele_periodi_1993cf_idx', '2026-05-12 02:46:59.083234'),
(57, 'django_celery_results', '0014_alter_taskresult_status', '2026-05-12 02:46:59.087186'),
(58, 'exports', '0001_initial', '2026-05-12 02:46:59.219960'),
(59, 'exports', '0002_initial', '2026-05-12 02:46:59.834540'),
(60, 'family', '0001_initial', '2026-05-12 02:46:59.847949'),
(61, 'family', '0002_initial', '2026-05-12 02:47:00.063242'),
(62, 'notifications', '0001_initial', '2026-05-12 02:47:00.096017'),
(63, 'notifications', '0002_initial', '2026-05-12 02:47:00.644865'),
(64, 'reports', '0001_initial', '2026-05-12 02:47:00.737997'),
(65, 'sessions', '0001_initial', '2026-05-12 02:47:00.825544'),
(66, 'timelines', '0001_initial', '2026-05-12 02:47:01.645998'),
(67, 'token_blacklist', '0001_initial', '2026-05-12 02:47:01.822391'),
(68, 'token_blacklist', '0002_outstandingtoken_jti_hex', '2026-05-12 02:47:01.872776'),
(69, 'token_blacklist', '0003_auto_20171017_2007', '2026-05-12 02:47:01.927463'),
(70, 'token_blacklist', '0004_auto_20171017_2013', '2026-05-12 02:47:02.013129'),
(71, 'token_blacklist', '0005_remove_outstandingtoken_jti', '2026-05-12 02:47:02.056310'),
(72, 'token_blacklist', '0006_auto_20171017_2113', '2026-05-12 02:47:02.098636'),
(73, 'token_blacklist', '0007_auto_20171017_2214', '2026-05-12 02:47:02.538705'),
(74, 'token_blacklist', '0008_migrate_to_bigautofield', '2026-05-12 02:47:02.893126'),
(75, 'token_blacklist', '0010_fix_migrate_to_bigautofield', '2026-05-12 02:47:02.941611'),
(76, 'token_blacklist', '0011_linearizes_history', '2026-05-12 02:47:02.943731'),
(77, 'token_blacklist', '0012_alter_outstandingtoken_user', '2026-05-12 02:47:02.999208'),
(78, 'token_blacklist', '0013_alter_blacklistedtoken_options_and_more', '2026-05-12 02:47:03.039088'),
(79, 'uploads', '0002_uploadedfile_add_profile_fk', '2026-05-12 02:47:03.151006'),
(80, 'verification', '0001_initial', '2026-05-12 02:47:03.675523');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ikpzlix4mmoaik7j7a168quo0dsvwwt3', '.eJxVjDsOwjAQBe_iGlnr9YeEkp4zWF7vGgdQIsVJhbg7iZQC2pl5761iWpca1yZzHFhdlFGnX0YpP2XcBT_SeJ90nsZlHkjviT5s07eJ5XU92r-Dmlrd1gS-NwUxWwHA5BxaLMbmLmAR8J1nstwXDGcCDhgcELOjDScrAkF9vshuN7E:1wMdH7:0BLDQ1fh-XyvytAOmJ4yech0CzSIkEivt3y248EBvp4', '2026-05-26 02:55:13.139701');

-- --------------------------------------------------------

--
-- Table structure for table `family_members`
--

CREATE TABLE `family_members` (
  `id` bigint(20) NOT NULL,
  `relationship` varchar(30) NOT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `full_name` varchar(255) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `birth_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`birth_year` >= 0),
  `birth_province_text` varchar(255) DEFAULT NULL,
  `birth_place` varchar(500) DEFAULT NULL,
  `hometown_province_text` varchar(255) DEFAULT NULL,
  `hometown` varchar(500) DEFAULT NULL,
  `current_address` varchar(500) DEFAULT NULL,
  `ethnic_group_text` varchar(100) DEFAULT NULL,
  `religion_text` varchar(100) DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL,
  `workplace` varchar(500) DEFAULT NULL,
  `job_title` varchar(255) DEFAULT NULL,
  `is_deceased` tinyint(1) NOT NULL,
  `deceased_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`deceased_year` >= 0),
  `deceased_cause` varchar(255) DEFAULT NULL,
  `is_party_member` tinyint(1) NOT NULL,
  `party_join_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`party_join_year` >= 0),
  `party_chi_bo` varchar(255) DEFAULT NULL,
  `party_awards_text` longtext DEFAULT NULL,
  `party_years_count` smallint(5) UNSIGNED DEFAULT NULL CHECK (`party_years_count` >= 0),
  `political_status` varchar(255) DEFAULT NULL,
  `party_join_date` date DEFAULT NULL,
  `party_join_place` varchar(255) DEFAULT NULL,
  `awards_disciplines` longtext DEFAULT NULL,
  `child_school` varchar(255) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL,
  `updated_by` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `family_members`
--

INSERT INTO `family_members` (`id`, `relationship`, `sort_order`, `full_name`, `gender`, `dob`, `birth_year`, `birth_province_text`, `birth_place`, `hometown_province_text`, `hometown`, `current_address`, `ethnic_group_text`, `religion_text`, `occupation`, `workplace`, `job_title`, `is_deceased`, `deceased_year`, `deceased_cause`, `is_party_member`, `party_join_year`, `party_chi_bo`, `party_awards_text`, `party_years_count`, `political_status`, `party_join_date`, `party_join_place`, `awards_disciplines`, `child_school`, `notes`, `deleted_at`, `created_at`, `updated_at`, `profile_id`, `updated_by`) VALUES
(19, 'cha_ruot', 0, 'Lê Văn Hùng', NULL, NULL, 1962, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Nông dân', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.519948', '2026-05-12 14:26:00.520005', 41, NULL),
(20, 'me_ruot', 1, 'Nguyễn Thị Lan', NULL, NULL, 1965, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Nội trợ', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.521406', '2026-05-12 14:26:00.521424', 41, NULL),
(21, 'ong_noi', 2, 'Lê Văn Bảy', NULL, NULL, 1935, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, 'Kinh', 'Không', 'Đã mất năm 2010', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Mất năm 2010', NULL, '2026-05-12 14:26:00.523250', '2026-05-12 14:26:00.523268', 41, NULL),
(22, 'ba_noi', 3, 'Trần Thị Bé', NULL, NULL, 1940, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, 'Kinh', 'Không', 'Đã mất năm 2018', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Mất năm 2018', NULL, '2026-05-12 14:26:00.524597', '2026-05-12 14:26:00.524616', 41, NULL),
(23, 'ong_ngoai', 4, 'Nguyễn Văn Tư', NULL, NULL, 1938, NULL, 'Xã Long Thới, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, 'Kinh', 'Không', 'Đã mất năm 2015', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Mất năm 2015', NULL, '2026-05-12 14:26:00.526096', '2026-05-12 14:26:00.526119', 41, NULL),
(24, 'ba_ngoai', 5, 'Phạm Thị Tám', NULL, NULL, 1942, NULL, 'Xã Long Thới, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Hưu trí', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.527567', '2026-05-12 14:26:00.527586', 41, NULL),
(25, 'vo_chong', 6, 'Trần Anh Minh', NULL, NULL, 1988, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Công nhân – Công ty Nhà Bè', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Kết hôn 15/06/2015', NULL, '2026-05-12 14:26:00.529027', '2026-05-12 14:26:00.529045', 41, NULL),
(26, 'con', 7, 'Trần Thị Ngọc', NULL, NULL, 2018, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Học sinh', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Đang học tiểu học', NULL, '2026-05-12 14:26:00.530480', '2026-05-12 14:26:00.530507', 41, NULL),
(27, 'anh_chi_em_ruot', 8, 'Lê Văn Nam', NULL, NULL, 1988, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Công nhân', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.532055', '2026-05-12 14:26:00.532074', 41, NULL),
(28, 'cha_ruot', 0, 'Ngô Văn Sáu', NULL, NULL, 1954, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, 'Kinh', 'Không', 'Hưu trí', NULL, NULL, 0, NULL, NULL, 1, 2000, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Mất năm 2020', NULL, '2026-05-12 14:26:00.534641', '2026-05-12 14:26:00.534659', 51, NULL),
(29, 'me_ruot', 1, 'Trần Thị Hoa', NULL, NULL, 1958, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Hưu trí', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.536007', '2026-05-12 14:26:00.536029', 51, NULL),
(30, 'vo_chong', 2, 'Phạm Thị Liên', NULL, NULL, 1987, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Giáo viên', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Kết hôn 20/08/2010', NULL, '2026-05-12 14:26:00.537575', '2026-05-12 14:26:00.537610', 51, NULL),
(31, 'con', 3, 'Ngô Minh Anh', NULL, NULL, 2012, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Học sinh', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Con trai, năm sinh 2012', NULL, '2026-05-12 14:26:00.539212', '2026-05-12 14:26:00.539232', 51, NULL),
(32, 'anh_chi_em_ruot', 4, 'Ngô Đình Hạnh', NULL, NULL, 1980, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Cán bộ xã', NULL, NULL, 0, NULL, NULL, 1, 2008, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.540681', '2026-05-12 14:26:00.540700', 51, NULL),
(33, 'anh_chi_em_ruot', 5, 'Ngô Đình Hiệp', NULL, NULL, 1983, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', 'Kinh', 'Không', 'Kỹ sư', NULL, NULL, 0, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Em trai', NULL, '2026-05-12 14:26:00.542212', '2026-05-12 14:26:00.542231', 51, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `login_history`
--

CREATE TABLE `login_history` (
  `id` bigint(20) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(500) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `fail_reason` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `login_history`
--

INSERT INTO `login_history` (`id`, `ip_address`, `user_agent`, `status`, `fail_reason`, `created_at`, `user_id`) VALUES
(1, NULL, NULL, 'success', NULL, '2026-05-12 03:05:24.384914', 1),
(2, NULL, NULL, 'success', NULL, '2026-05-12 03:05:40.283160', 1),
(3, NULL, NULL, 'success', NULL, '2026-05-12 03:13:44.471071', 1),
(4, NULL, NULL, 'success', NULL, '2026-05-12 03:15:15.851737', 1),
(5, NULL, NULL, 'success', NULL, '2026-05-12 03:18:23.129978', 1),
(11, NULL, NULL, 'success', NULL, '2026-05-12 14:39:05.270012', 56),
(12, NULL, NULL, 'success', NULL, '2026-05-12 17:17:01.007168', 68),
(13, NULL, NULL, 'success', NULL, '2026-05-12 17:25:54.031949', 1);

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` bigint(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `type` varchar(40) NOT NULL,
  `subject` varchar(500) DEFAULT NULL,
  `body` longtext NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `read_at` datetime(6) DEFAULT NULL,
  `sent_status` varchar(20) NOT NULL,
  `sent_at` datetime(6) DEFAULT NULL,
  `delivery_ref` varchar(255) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) DEFAULT NULL,
  `recipient_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) DEFAULT NULL,
  `batch_id` bigint(20) DEFAULT NULL,
  `template_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`id`, `channel`, `type`, `subject`, `body`, `is_read`, `read_at`, `sent_status`, `sent_at`, `delivery_ref`, `created_at`, `profile_id`, `recipient_id`, `sender_id`, `batch_id`, `template_id`) VALUES
(25, 'sms', 'account_created', 'Tài khoản kê khai đã được tạo', 'Kính gửi Lê Thị Mai, tài khoản kê khai lý lịch Mẫu 2-KNĐ của bạn đã được tạo. Vui lòng đăng nhập và hoàn thiện hồ sơ.', 1, '2026-03-23 16:26:00.469189', 'sent', '2026-03-23 14:26:00.469189', NULL, '2026-03-23 14:26:00.469189', 41, 58, 56, NULL, NULL),
(26, 'sms', 'profile_returned', 'Thông báo trạng thái hồ sơ', 'Kính gửi Lê Thị Mai, hồ sơ lý lịch đã được nhận. Đang trong quá trình thẩm định.', 1, '2026-04-20 16:26:00.469189', 'sent', '2026-04-20 14:26:00.469189', NULL, '2026-04-20 14:26:00.469189', 41, 58, 56, NULL, NULL),
(27, 'sms', 'profile_returned', 'Hồ sơ đang được xem xét', 'Kính gửi Trần Minh Tuấn, hồ sơ lý lịch của bạn đang được Ban Xây dựng Đảng xem xét.', 0, NULL, 'sent', '2026-04-22 14:26:00.469189', NULL, '2026-04-22 14:26:00.469189', 42, 59, 56, NULL, NULL),
(28, 'sms', 'profile_returned', 'Yêu cầu bổ sung hồ sơ', 'Kính gửi Phạm Thị Dung, hồ sơ cần bổ sung thêm thông tin. Vui lòng đăng nhập để xem chi tiết.', 0, NULL, 'sent', '2026-05-09 14:26:00.469189', NULL, '2026-05-09 14:26:00.469189', 43, 60, 56, NULL, NULL),
(29, 'sms', 'profile_returned', 'Yêu cầu bổ sung hồ sơ', 'Kính gửi Nguyễn Văn Bình, hồ sơ cần bổ sung lịch sử gia đình phía cha. Vui lòng cập nhật.', 0, NULL, 'sent', '2026-05-07 14:26:00.469189', NULL, '2026-05-07 14:26:00.469189', 44, 61, 56, NULL, NULL),
(30, 'sms', 'account_created', 'Tài khoản kê khai đã được tạo', 'Kính gửi Hoàng Văn Đức, tài khoản kê khai lý lịch của bạn đã được tạo.', 1, '2026-04-23 16:26:00.469189', 'sent', '2026-04-23 14:26:00.469189', NULL, '2026-04-23 14:26:00.469189', 46, 63, 56, NULL, NULL),
(31, 'email', 'profile_approved', 'Hồ sơ lý lịch đã hoàn thiện', 'Kính gửi Trương Thị Hằng, hồ sơ lý lịch Mẫu 2-KNĐ đã được hoàn thiện và lưu trữ.', 1, '2026-04-12 16:26:00.469189', 'sent', '2026-04-12 14:26:00.469189', NULL, '2026-04-12 14:26:00.469189', 49, 66, 56, NULL, NULL),
(32, 'sms', 'profile_approved', 'Hồ sơ đã được phê duyệt', 'Kính gửi Nguyễn Thị Bình An, hồ sơ lý lịch đã được phê duyệt. Chúc mừng bạn.', 1, '2026-04-17 16:26:00.469189', 'sent', '2026-04-17 14:26:00.469189', NULL, '2026-04-17 14:26:00.469189', 50, 67, 56, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `notification_batches`
--

CREATE TABLE `notification_batches` (
  `id` bigint(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `type` varchar(80) NOT NULL,
  `recipient_filter` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`recipient_filter`)),
  `custom_body` longtext DEFAULT NULL,
  `total_count` int(10) UNSIGNED NOT NULL CHECK (`total_count` >= 0),
  `sent_count` int(10) UNSIGNED NOT NULL CHECK (`sent_count` >= 0),
  `failed_count` int(10) UNSIGNED NOT NULL CHECK (`failed_count` >= 0),
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `completed_at` datetime(6) DEFAULT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `template_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notification_templates`
--

CREATE TABLE `notification_templates` (
  `id` bigint(20) NOT NULL,
  `code` varchar(80) NOT NULL,
  `name` varchar(255) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `subject` varchar(500) DEFAULT NULL,
  `body` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `password_resets`
--

CREATE TABLE `password_resets` (
  `id` bigint(20) NOT NULL,
  `token` varchar(255) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `used_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profiles`
--

CREATE TABLE `profiles` (
  `id` bigint(20) NOT NULL,
  `profile_number` varchar(50) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `full_name_other` varchar(255) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `birth_place_province_text` varchar(255) DEFAULT NULL,
  `birth_place_old_name` varchar(255) DEFAULT NULL,
  `birth_place_detail` varchar(500) DEFAULT NULL,
  `ethnic_group_other` varchar(100) DEFAULT NULL,
  `religion_other` varchar(100) DEFAULT NULL,
  `religious_title` varchar(100) DEFAULT NULL,
  `hometown_detail` varchar(500) DEFAULT NULL,
  `current_address_number` varchar(100) DEFAULT NULL,
  `current_address_street` varchar(255) DEFAULT NULL,
  `current_address` varchar(500) DEFAULT NULL,
  `residence_type` varchar(20) DEFAULT NULL,
  `temporary_address_number` varchar(100) DEFAULT NULL,
  `temporary_address_street` varchar(255) DEFAULT NULL,
  `temporary_address` varchar(500) DEFAULT NULL,
  `general_edu_level` varchar(120) DEFAULT NULL,
  `edu_specialization` varchar(255) DEFAULT NULL,
  `edu_school` varchar(255) DEFAULT NULL,
  `edu_major` varchar(255) DEFAULT NULL,
  `edu_graduation_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`edu_graduation_year` >= 0),
  `academic_degree_major` varchar(255) DEFAULT NULL,
  `highest_degree` varchar(120) DEFAULT NULL,
  `academic_title_level` varchar(100) DEFAULT NULL,
  `academic_title` varchar(120) DEFAULT NULL,
  `political_level_detail` varchar(255) DEFAULT NULL,
  `political_school` varchar(255) DEFAULT NULL,
  `science_tech_qualifications` longtext DEFAULT NULL,
  `foreign_language_name` varchar(120) DEFAULT NULL,
  `foreign_language_level` varchar(120) DEFAULT NULL,
  `foreign_languages` varchar(500) DEFAULT NULL,
  `it_level` varchar(120) DEFAULT NULL,
  `ethnic_language` varchar(255) DEFAULT NULL,
  `professional_certs` longtext DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL,
  `workplace` varchar(500) DEFAULT NULL,
  `workplace_address` varchar(500) DEFAULT NULL,
  `job_title` varchar(255) DEFAULT NULL,
  `youth_union_date` date DEFAULT NULL,
  `youth_union_place` varchar(255) DEFAULT NULL,
  `other_organizations` longtext DEFAULT NULL,
  `rejoin_first_party_join_date` date DEFAULT NULL,
  `rejoin_first_party_join_place` varchar(255) DEFAULT NULL,
  `rejoin_first_official_date` date DEFAULT NULL,
  `rejoin_introducer1_name` varchar(255) DEFAULT NULL,
  `rejoin_introducer1_position` varchar(255) DEFAULT NULL,
  `rejoin_introducer2_name` varchar(255) DEFAULT NULL,
  `rejoin_introducer2_position` varchar(255) DEFAULT NULL,
  `marital_status` varchar(20) DEFAULT NULL,
  `marriage_date` date DEFAULT NULL,
  `divorce_date` date DEFAULT NULL,
  `military_service` tinyint(1) NOT NULL,
  `military_start` date DEFAULT NULL,
  `military_end` date DEFAULT NULL,
  `military_rank` varchar(100) DEFAULT NULL,
  `military_unit` varchar(255) DEFAULT NULL,
  `military_discharge_reason` varchar(255) DEFAULT NULL,
  `political_history_text` longtext DEFAULT NULL,
  `awards_text` longtext DEFAULT NULL,
  `disciplines_text` longtext DEFAULT NULL,
  `self_assessment_text` longtext DEFAULT NULL,
  `self_assessment_word_count` smallint(5) UNSIGNED DEFAULT NULL CHECK (`self_assessment_word_count` >= 0),
  `declaration_name` varchar(255) DEFAULT NULL,
  `declaration_date` date DEFAULT NULL,
  `declarant_signature` varchar(255) DEFAULT NULL,
  `ai_score` smallint(5) UNSIGNED DEFAULT NULL CHECK (`ai_score` >= 0),
  `ai_last_scanned_at` datetime(6) DEFAULT NULL,
  `ai_issues_json` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`ai_issues_json`)),
  `status` varchar(20) NOT NULL,
  `submitted_at` datetime(6) DEFAULT NULL,
  `approved_at` datetime(6) DEFAULT NULL,
  `completed_at` datetime(6) DEFAULT NULL,
  `last_returned_at` datetime(6) DEFAULT NULL,
  `return_reason` longtext DEFAULT NULL,
  `rejected_at` datetime(6) DEFAULT NULL,
  `rejected_reason` longtext DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `approved_by` bigint(20) DEFAULT NULL,
  `birth_place_ward_id` bigint(20) DEFAULT NULL,
  `created_by` bigint(20) DEFAULT NULL,
  `current_ward_id` bigint(20) DEFAULT NULL,
  `edu_level_id` bigint(20) DEFAULT NULL,
  `ethnic_group_id` bigint(20) DEFAULT NULL,
  `hometown_ward_id` bigint(20) DEFAULT NULL,
  `officer_in_charge_id` bigint(20) DEFAULT NULL,
  `photo_file_id` bigint(20) DEFAULT NULL,
  `political_level_id` bigint(20) DEFAULT NULL,
  `religion_id` bigint(20) DEFAULT NULL,
  `temporary_ward_id` bigint(20) DEFAULT NULL,
  `updated_by` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profiles`
--

INSERT INTO `profiles` (`id`, `profile_number`, `full_name`, `full_name_other`, `gender`, `dob`, `birth_place_province_text`, `birth_place_old_name`, `birth_place_detail`, `ethnic_group_other`, `religion_other`, `religious_title`, `hometown_detail`, `current_address_number`, `current_address_street`, `current_address`, `residence_type`, `temporary_address_number`, `temporary_address_street`, `temporary_address`, `general_edu_level`, `edu_specialization`, `edu_school`, `edu_major`, `edu_graduation_year`, `academic_degree_major`, `highest_degree`, `academic_title_level`, `academic_title`, `political_level_detail`, `political_school`, `science_tech_qualifications`, `foreign_language_name`, `foreign_language_level`, `foreign_languages`, `it_level`, `ethnic_language`, `professional_certs`, `occupation`, `workplace`, `workplace_address`, `job_title`, `youth_union_date`, `youth_union_place`, `other_organizations`, `rejoin_first_party_join_date`, `rejoin_first_party_join_place`, `rejoin_first_official_date`, `rejoin_introducer1_name`, `rejoin_introducer1_position`, `rejoin_introducer2_name`, `rejoin_introducer2_position`, `marital_status`, `marriage_date`, `divorce_date`, `military_service`, `military_start`, `military_end`, `military_rank`, `military_unit`, `military_discharge_reason`, `political_history_text`, `awards_text`, `disciplines_text`, `self_assessment_text`, `self_assessment_word_count`, `declaration_name`, `declaration_date`, `declarant_signature`, `ai_score`, `ai_last_scanned_at`, `ai_issues_json`, `status`, `submitted_at`, `approved_at`, `completed_at`, `last_returned_at`, `return_reason`, `rejected_at`, `rejected_reason`, `deleted_at`, `created_at`, `updated_at`, `approved_by`, `birth_place_ward_id`, `created_by`, `current_ward_id`, `edu_level_id`, `ethnic_group_id`, `hometown_ward_id`, `officer_in_charge_id`, `photo_file_id`, `political_level_id`, `religion_id`, `temporary_ward_id`, `updated_by`, `user_id`) VALUES
(41, 'HS-2026-001', 'Lê Thị Mai', NULL, 'female', '1990-03-15', NULL, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Giáo viên tiểu học', 'Trường Tiểu học Nhà Bè A', NULL, 'Giáo viên', '2007-03-15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 220, 'Lê Thị Mai', '2026-04-20', NULL, 94, '2026-05-12 14:26:00.338245', NULL, 'submitted', '2026-04-20 14:26:00.338245', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.341740', '2026-05-12 14:26:00.341747', NULL, 9, 56, 9, 6, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 58),
(42, 'HS-2026-002', 'Trần Minh Tuấn', NULL, 'male', '1993-07-20', NULL, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Phước Kiển, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 3, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Nhân viên kỹ thuật', 'Công ty TNHH Xây dựng ABC', NULL, 'Nhân viên kỹ thuật', '2009-07-20', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 205, 'Trần Minh Tuấn', '2026-04-19', NULL, 87, '2026-05-12 14:26:00.338245', NULL, 'pending', '2026-04-19 14:26:00.338245', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.348067', '2026-05-12 14:26:00.348074', NULL, 4, 56, 4, 6, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 59),
(43, 'HS-2026-003', 'Phạm Thị Dung', NULL, 'female', '1997-11-05', NULL, NULL, 'Xã Long Thới, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Long Thới, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 2, Xã Long Thới, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Trung học phổ thông', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Công nhân may', 'Công ty CP Dệt May Nhà Bè', NULL, 'Công nhân', '2013-11-05', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Phạm Thị Dung', '2026-04-17', NULL, 61, '2026-05-12 14:26:00.338245', NULL, 'returned', '2026-04-17 14:26:00.338245', NULL, NULL, '2026-05-09 14:26:00.338245', 'Cần bổ sung thông tin lịch sử bản thân giai đoạn 2015–2018.', NULL, NULL, NULL, '2026-05-12 14:26:00.351776', '2026-05-12 14:26:00.351783', NULL, 5, 57, 5, 3, 1, NULL, 57, NULL, NULL, 1, NULL, NULL, 60),
(44, 'HS-2026-004', 'Nguyễn Văn Bình', NULL, 'male', '1995-04-28', NULL, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Trung học phổ thông', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Lái xe', 'Công ty vận tải Nhà Bè', NULL, 'Lái xe', '2011-04-28', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Nguyễn Văn Bình', '2026-04-16', NULL, 72, '2026-05-12 14:26:00.338245', NULL, 'returned', '2026-04-16 14:26:00.338245', NULL, NULL, '2026-05-09 14:26:00.338245', 'Cần bổ sung thông tin lịch sử bản thân giai đoạn 2015–2018.', NULL, NULL, NULL, '2026-05-12 14:26:00.355552', '2026-05-12 14:26:00.355560', NULL, 9, 56, 9, 3, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 61),
(45, 'HS-2026-005', 'Đinh Thị Nhung', NULL, 'female', '1991-09-12', NULL, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Trung học phổ thông', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Y tá', 'Trạm y tế xã Nhà Bè', NULL, 'Y tá', '2007-09-12', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 195, 'Đinh Thị Nhung', '2026-04-25', NULL, 91, '2026-05-12 14:26:00.338245', NULL, 'returned', '2026-04-25 14:26:00.338245', NULL, NULL, '2026-05-12 18:47:14.346134', 'ddddd', NULL, NULL, NULL, '2026-05-12 14:26:00.359191', '2026-05-12 18:47:14.346388', NULL, 9, 57, 9, 4, 1, NULL, 57, NULL, NULL, 2, NULL, 1, 62),
(46, NULL, 'Hoàng Văn Đức', NULL, 'male', '1999-02-14', NULL, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 1, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Sinh viên', 'Trường Đại học Nông Lâm TP.HCM', NULL, 'Sinh viên', '2015-02-14', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Hoàng Văn Đức', NULL, NULL, NULL, NULL, NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.362748', '2026-05-12 14:26:00.362764', NULL, 9, 56, 9, 6, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 63),
(47, NULL, 'Võ Thị Lan', NULL, 'female', '1998-06-30', NULL, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Phước Kiển, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Kế toán', 'UBND Xã Phước Kiển', NULL, 'Kế toán', '2014-06-30', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Võ Thị Lan', NULL, NULL, NULL, NULL, NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.366828', '2026-05-12 14:26:00.366842', NULL, 4, 57, 4, 6, 1, NULL, 57, NULL, NULL, 1, NULL, NULL, 64),
(48, NULL, 'Bùi Quang Huy', NULL, 'male', '1996-12-08', NULL, NULL, 'Xã Long Thới, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Long Thới, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 3, Xã Long Thới, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Trung học phổ thông', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Nông dân', 'Hộ nông dân gia đình', NULL, 'Nông dân', '2012-12-08', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Bùi Quang Huy', NULL, NULL, NULL, NULL, NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.370353', '2026-05-12 14:26:00.370368', NULL, 5, 56, 5, 3, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 65),
(49, 'HS-2026-009', 'Trần Thị Hoa', NULL, 'female', '1994-08-22', NULL, NULL, 'Xã Hiệp Phước, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Hiệp Phước, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 4, Xã Hiệp Phước, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Trung học phổ thông', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Thợ mộc', 'Xưởng mộc Nhà Bè', NULL, 'Thợ mộc', '2011-08-22', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 210, 'Trần Thị Hoa', '2026-04-12', NULL, 88, '2026-05-12 14:26:00.338245', NULL, 'verifying', '2026-04-12 14:26:00.338245', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.374955', '2026-05-12 14:26:00.374964', NULL, 8, 57, 8, 3, 1, NULL, 57, NULL, NULL, 1, NULL, NULL, 66),
(50, 'HS-2026-010', 'Trương Thị Hằng', NULL, 'female', '1994-08-22', NULL, NULL, 'Xã Nhà Bè, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 2, Xã Nhà Bè, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Giáo dục', 'Trường Đại học Sư phạm', 'Sư phạm các môn', 2012, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Giáo viên THCS', 'Trường THCS Nhà Bè', NULL, 'Giáo viên', '2010-08-22', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'single', NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 235, 'Trương Thị Hằng', '2026-03-28', NULL, 98, '2026-05-12 14:26:00.338245', NULL, 'completed', '2026-03-28 14:26:00.338245', '2026-04-05 14:26:00.338245', '2026-04-12 14:26:00.338245', NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.378761', '2026-05-12 14:26:00.378768', NULL, 9, 56, 9, 6, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 67),
(51, 'HS-2026-011', 'Ngô Đình Hoàng', NULL, 'male', '1985-06-15', NULL, NULL, 'Xã Phước Kiển, Huyện Nhà Bè, TP. Hồ Chí Minh', NULL, NULL, NULL, 'Xã Phước Kiển, TP. Hồ Chí Minh', NULL, NULL, 'Ấp 2, Xã Phước Kiển, Huyện Nhà Bè, TP.HCM', NULL, NULL, NULL, NULL, 'Đại học', 'Quản lý công', 'Trường Đại học Kinh tế TP.HCM', 'Quản lý công', 2007, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Tiếng Anh (trung cấp)', NULL, NULL, NULL, 'Trưởng phòng kỹ thuật', 'Trung tâm Phát triển Quản lý Huyện', NULL, 'Trưởng phòng', '2003-06-15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'married', '2011-05-16', NULL, 0, NULL, NULL, NULL, NULL, NULL, 'Đoàn viên Thanh niên Cộng sản Hồ Chí Minh từ năm 2004. Tham gia Đảng Cộng sản Việt Nam năm 2010. Nhiệt tình trong công tác, có kỷ luật cao.', '- Khen thưởng xuất sắc hoàn thành nhiệm vụ, năm 2015\n- Bằng khen của UBND Huyện Nhà Bè, năm 2018\n- Giải thưởng lao động xuất sắc, năm 2020', NULL, 'Bản thân là người có ý thức chính trị tốt, luôn tuân thủ kỷ luật Đảng và pháp luật nhà nước. Tận tâm với công việc, có khả năng quản lý tốt, sáng tạo trong thực hiện nhiệm vụ. Được cấp trên và đồng chí đánh giá cao. Sẵn sàng rèn luyện và nâng cao trình độ lý luận chính trị. Cam kết sẽ tiếp tục nâng cao năng lực, cống hiến cho Đảng và nhân dân.', 520, 'Ngô Đình Hoàng', '2026-05-04', NULL, 96, '2026-05-12 14:26:00.338245', NULL, 'submitted', '2026-05-04 14:26:00.338245', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.382680', '2026-05-12 14:26:00.382688', NULL, 4, 56, 4, 6, 1, NULL, 56, NULL, NULL, 1, NULL, NULL, 68),
(53, NULL, 'Test Tao Nhanh 2', NULL, 'male', '1995-01-01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 17:25:09.440858', '2026-05-12 17:25:09.440880', NULL, NULL, 56, NULL, NULL, NULL, NULL, 56, NULL, NULL, NULL, NULL, 56, 70),
(56, NULL, 'NGUYEN THI LIMH', NULL, 'male', '1990-01-01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'draft', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2026-05-12 17:29:23.200192', '2026-05-12 17:29:23.200213', NULL, NULL, 1, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, 1, 73);

-- --------------------------------------------------------

--
-- Table structure for table `profile_awards`
--

CREATE TABLE `profile_awards` (
  `id` bigint(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `period_text` varchar(255) DEFAULT NULL,
  `level` varchar(100) DEFAULT NULL,
  `issued_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`issued_month` >= 0),
  `issued_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`issued_year` >= 0),
  `issuer` varchar(255) DEFAULT NULL,
  `content` longtext NOT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profile_awards`
--

INSERT INTO `profile_awards` (`id`, `type`, `period_text`, `level`, `issued_month`, `issued_year`, `issuer`, `content`, `sort_order`, `created_at`, `updated_at`, `profile_id`) VALUES
(3, 'award', NULL, 'Cấp huyện', NULL, 2022, 'UBND Huyện Nhà Bè', 'Giáo viên dạy giỏi cấp huyện năm học 2021–2022', 0, '2026-05-12 14:26:00.556539', '2026-05-12 14:26:00.556566', 41),
(4, 'award', NULL, 'Cấp huyện', NULL, 2015, 'Huyện Nhà Bè', 'Khen thưởng xuất sắc hoàn thành nhiệm vụ', 0, '2026-05-12 14:26:00.574460', '2026-05-12 14:26:00.574487', 51),
(5, 'award', NULL, 'Cấp huyện', NULL, 2018, 'UBND Huyện Nhà Bè', 'Bằng khen của UBND Huyện Nhà Bè', 1, '2026-05-12 14:26:00.575697', '2026-05-12 14:26:00.575720', 51),
(6, 'award', NULL, 'Cấp huyện', NULL, 2020, 'Huyện Nhà Bè', 'Giải thưởng lao động xuất sắc', 2, '2026-05-12 14:26:00.577053', '2026-05-12 14:26:00.577076', 51);

-- --------------------------------------------------------

--
-- Table structure for table `profile_correction_items`
--

CREATE TABLE `profile_correction_items` (
  `id` bigint(20) NOT NULL,
  `section` varchar(80) NOT NULL,
  `field_name` varchar(120) DEFAULT NULL,
  `description` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `corrected_at` datetime(6) DEFAULT NULL,
  `corrected_note` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `request_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_correction_requests`
--

CREATE TABLE `profile_correction_requests` (
  `id` bigint(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `overall_note` longtext DEFAULT NULL,
  `resolved_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) NOT NULL,
  `resolved_by` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_edit_history`
--

CREATE TABLE `profile_edit_history` (
  `id` bigint(20) NOT NULL,
  `section` varchar(80) NOT NULL,
  `field_name` varchar(120) NOT NULL,
  `old_value` longtext DEFAULT NULL,
  `new_value` longtext DEFAULT NULL,
  `edit_reason` varchar(500) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `edited_by_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_education_history`
--

CREATE TABLE `profile_education_history` (
  `id` bigint(20) NOT NULL,
  `period_text` varchar(255) DEFAULT NULL,
  `from_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_month` >= 0),
  `from_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_year` >= 0),
  `to_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_month` >= 0),
  `to_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_year` >= 0),
  `is_present` tinyint(1) NOT NULL,
  `school` varchar(500) NOT NULL,
  `major` varchar(255) DEFAULT NULL,
  `edu_level` varchar(100) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  `certificate` varchar(255) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profile_education_history`
--

INSERT INTO `profile_education_history` (`id`, `period_text`, `from_month`, `from_year`, `to_month`, `to_year`, `is_present`, `school`, `major`, `edu_level`, `location`, `certificate`, `notes`, `sort_order`, `created_at`, `updated_at`, `profile_id`) VALUES
(5, NULL, 9, 2008, 6, 2012, 0, 'Đại học Sư phạm TP.HCM', 'Giáo dục Tiểu học', NULL, NULL, 'Cử nhân', NULL, 0, '2026-05-12 14:26:00.553854', '2026-05-12 14:26:00.553875', 41),
(6, NULL, 3, 2020, 12, 2020, 0, 'Trung tâm Bồi dưỡng CT Huyện Nhà Bè', 'Lý luận chính trị Sơ cấp', NULL, NULL, 'Chứng chỉ', NULL, 1, '2026-05-12 14:26:00.555259', '2026-05-12 14:26:00.555285', 41),
(7, NULL, 9, 2003, 7, 2007, 0, 'Đại học Kinh tế TP.HCM', 'Quản lý công', NULL, NULL, 'Cử nhân', NULL, 0, '2026-05-12 14:26:00.570791', '2026-05-12 14:26:00.570812', 51),
(8, NULL, 3, 2018, 11, 2018, 0, 'Trung tâm Bồi dưỡng Chính trị Huyện', 'Lý luận Mác-Lê-Nin và Tư tưởng HCM', NULL, NULL, 'Chứng chỉ', NULL, 1, '2026-05-12 14:26:00.572082', '2026-05-12 14:26:00.572106', 51),
(9, NULL, 9, 2021, 6, 2022, 0, 'Học viện Chính trị Quốc phòng', 'Lý luận chính trị trung cấp', NULL, NULL, 'Chứng chỉ', NULL, 2, '2026-05-12 14:26:00.573300', '2026-05-12 14:26:00.573324', 51);

-- --------------------------------------------------------

--
-- Table structure for table `profile_history_entries`
--

CREATE TABLE `profile_history_entries` (
  `id` bigint(20) NOT NULL,
  `entry_type` varchar(10) NOT NULL,
  `from_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_month` >= 0),
  `from_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_year` >= 0),
  `to_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_month` >= 0),
  `to_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_year` >= 0),
  `is_present` tinyint(1) NOT NULL,
  `description` longtext NOT NULL,
  `location` varchar(500) DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `family_member_id` bigint(20) DEFAULT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profile_history_entries`
--

INSERT INTO `profile_history_entries` (`id`, `entry_type`, `from_month`, `from_year`, `to_month`, `to_year`, `is_present`, `description`, `location`, `sort_order`, `created_at`, `updated_at`, `family_member_id`, `profile_id`) VALUES
(11, 'self', NULL, 1990, NULL, 1996, 0, 'Còn nhỏ, sống với cha mẹ tại ấp 1, xã Nhà Bè, TP.HCM', 'Xã Nhà Bè, TP.HCM', 0, '2026-05-12 14:26:00.544888', '2026-05-12 14:26:00.544909', NULL, 41),
(12, 'self', 9, 1996, 8, 2005, 0, 'Học Tiểu học và THCS tại Trường THCS Nhà Bè', 'Xã Nhà Bè, TP.HCM', 1, '2026-05-12 14:26:00.546287', '2026-05-12 14:26:00.546313', NULL, 41),
(13, 'self', 9, 2005, 6, 2008, 0, 'Học THPT tại Trường THPT Nhà Bè. Kết nạp Đoàn 15/3/2007', 'Xã Nhà Bè, TP.HCM', 2, '2026-05-12 14:26:00.547719', '2026-05-12 14:26:00.547742', NULL, 41),
(14, 'self', 9, 2008, 6, 2012, 0, 'Học Đại học Sư phạm TP.HCM, Khoa Giáo dục Tiểu học', 'TP. Hồ Chí Minh', 3, '2026-05-12 14:26:00.548926', '2026-05-12 14:26:00.548954', NULL, 41),
(15, 'self', 8, 2012, NULL, NULL, 1, 'Giáo viên Trường Tiểu học Nhà Bè A, xã Nhà Bè, TP.HCM', 'Xã Nhà Bè, TP.HCM', 4, '2026-05-12 14:26:00.550329', '2026-05-12 14:26:00.550349', NULL, 41),
(16, 'self', NULL, 1985, NULL, 1991, 0, 'Tuổi thơ sống với cha mẹ tại ấp 2, xã Phước Kiển, TP.HCM', 'Xã Phước Kiển, TP.HCM', 0, '2026-05-12 14:26:00.559271', '2026-05-12 14:26:00.559291', NULL, 51),
(17, 'self', 9, 1991, 8, 1999, 0, 'Học Tiểu học và THCS tại Trường THCS Phước Kiển', 'Xã Phước Kiển, TP.HCM', 1, '2026-05-12 14:26:00.560409', '2026-05-12 14:26:00.560430', NULL, 51),
(18, 'self', 9, 1999, 6, 2003, 0, 'Học THPT tại Trường THPT Phước Kiển. Kết nạp Đoàn 1/4/2001. Đảng viên từ 3/10/2003', 'Xã Phước Kiển, TP.HCM', 2, '2026-05-12 14:26:00.561714', '2026-05-12 14:26:00.561734', NULL, 51),
(19, 'self', 9, 2003, 7, 2007, 0, 'Học Đại học Kinh tế TP.HCM, chuyên ngành Quản lý công', 'TP. Hồ Chí Minh', 3, '2026-05-12 14:26:00.562783', '2026-05-12 14:26:00.562804', NULL, 51),
(20, 'self', 9, 2007, 5, 2015, 0, 'Công tác tại Trung tâm Phát triển Huyện Nhà Bè, Phòng Kỹ thuật và Đầu tư', 'Huyện Nhà Bè', 4, '2026-05-12 14:26:00.563948', '2026-05-12 14:26:00.563969', NULL, 51),
(21, 'self', 6, 2015, NULL, NULL, 1, 'Trưởng Phòng Kỹ thuật, Trung tâm Phát triển Quản lý Huyện Nhà Bè', 'Huyện Nhà Bè', 5, '2026-05-12 14:26:00.564934', '2026-05-12 14:26:00.564954', NULL, 51);

-- --------------------------------------------------------

--
-- Table structure for table `profile_officer_assignments`
--

CREATE TABLE `profile_officer_assignments` (
  `id` bigint(20) NOT NULL,
  `note` varchar(500) DEFAULT NULL,
  `assigned_at` datetime(6) NOT NULL,
  `revoked_at` datetime(6) DEFAULT NULL,
  `assigned_by` bigint(20) DEFAULT NULL,
  `officer_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_org_participation`
--

CREATE TABLE `profile_org_participation` (
  `id` bigint(20) NOT NULL,
  `org_name` varchar(500) NOT NULL,
  `join_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`join_month` >= 0),
  `join_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`join_year` >= 0),
  `leave_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`leave_month` >= 0),
  `leave_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`leave_year` >= 0),
  `is_present` tinyint(1) NOT NULL,
  `role_in_org` varchar(255) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_overseas_relatives`
--

CREATE TABLE `profile_overseas_relatives` (
  `id` bigint(20) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `relationship` varchar(100) DEFAULT NULL,
  `country` varchar(200) NOT NULL,
  `address` varchar(500) DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_overseas_travel`
--

CREATE TABLE `profile_overseas_travel` (
  `id` bigint(20) NOT NULL,
  `period_text` varchar(255) DEFAULT NULL,
  `from_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_month` >= 0),
  `from_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_year` >= 0),
  `to_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_month` >= 0),
  `to_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_year` >= 0),
  `country` varchar(200) NOT NULL,
  `purpose` varchar(500) DEFAULT NULL,
  `sponsoring_org` varchar(500) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profile_reviews`
--

CREATE TABLE `profile_reviews` (
  `id` bigint(20) NOT NULL,
  `action` varchar(20) NOT NULL,
  `from_status` varchar(40) DEFAULT NULL,
  `to_status` varchar(40) DEFAULT NULL,
  `comment` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL,
  `reviewer_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profile_reviews`
--

INSERT INTO `profile_reviews` (`id`, `action`, `from_status`, `to_status`, `comment`, `created_at`, `profile_id`, `reviewer_id`) VALUES
(40, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-20 14:26:00.384344', 41, 56),
(41, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-19 14:26:00.384344', 42, 56),
(42, 'note', 'submitted', 'pending', 'Đã nhận hồ sơ, đang xem xét.', '2026-04-22 14:26:00.384344', 42, 56),
(43, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-17 14:26:00.384344', 43, 57),
(44, 'return', 'submitted', 'returned', 'Thiếu thông tin lịch sử công tác giai đoạn 2019–2022. Yêu cầu bổ sung.', '2026-05-09 14:26:00.384344', 43, 57),
(45, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-16 14:26:00.384344', 44, 56),
(46, 'return', 'submitted', 'returned', 'Cần bổ sung lịch sử gia đình phía cha.', '2026-05-07 14:26:00.384344', 44, 56),
(47, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-25 14:26:00.384344', 45, 57),
(48, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-03-28 14:26:00.384344', 49, 56),
(49, 'approve', 'submitted', 'approved', 'Hồ sơ đầy đủ, chuyển xác minh.', '2026-04-05 14:26:00.384344', 49, 56),
(50, 'complete', 'approved', 'completed', 'Xác minh hoàn tất, hồ sơ hoàn thiện.', '2026-04-12 14:26:00.384344', 49, 56),
(51, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ.', '2026-04-07 14:26:00.384344', 50, 57),
(52, 'approve', 'submitted', 'approved', 'Hồ sơ đạt yêu cầu.', '2026-04-17 14:26:00.384344', 50, 57),
(53, 'submit', NULL, 'submitted', 'Quần chúng tự nộp hồ sơ. Hồ sơ đầy đủ, chi tiết.', '2026-05-04 14:26:00.384344', 51, 56),
(54, 'return', 'submitted', 'returned', 'ddddd', '2026-05-12 18:47:14.349716', 45, 1);

-- --------------------------------------------------------

--
-- Table structure for table `profile_work_history`
--

CREATE TABLE `profile_work_history` (
  `id` bigint(20) NOT NULL,
  `period_text` varchar(255) DEFAULT NULL,
  `from_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_month` >= 0),
  `from_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`from_year` >= 0),
  `to_month` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_month` >= 0),
  `to_year` smallint(5) UNSIGNED DEFAULT NULL CHECK (`to_year` >= 0),
  `is_present` tinyint(1) NOT NULL,
  `employer` varchar(500) NOT NULL,
  `job_title` varchar(255) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `sort_order` smallint(5) UNSIGNED NOT NULL CHECK (`sort_order` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `profile_work_history`
--

INSERT INTO `profile_work_history` (`id`, `period_text`, `from_month`, `from_year`, `to_month`, `to_year`, `is_present`, `employer`, `job_title`, `location`, `notes`, `sort_order`, `created_at`, `updated_at`, `profile_id`) VALUES
(5, NULL, 9, 2008, 6, 2012, 0, 'Trường Đại học Sư phạm TP.HCM', 'Sinh viên', 'TP. Hồ Chí Minh', NULL, 0, '2026-05-12 14:26:00.551606', '2026-05-12 14:26:00.551627', 41),
(6, NULL, 8, 2012, NULL, NULL, 1, 'Trường Tiểu học Nhà Bè A', 'Giáo viên', 'Xã Nhà Bè, TP.HCM', NULL, 1, '2026-05-12 14:26:00.552657', '2026-05-12 14:26:00.552678', 41),
(7, NULL, 9, 2003, 7, 2007, 0, 'Đại học Kinh tế TP.HCM', 'Sinh viên', 'TP. Hồ Chí Minh', NULL, 0, '2026-05-12 14:26:00.565927', '2026-05-12 14:26:00.565948', 51),
(8, NULL, 9, 2007, 5, 2015, 0, 'Trung tâm Phát triển Huyện Nhà Bè', 'Chuyên viên', 'Huyện Nhà Bè', NULL, 1, '2026-05-12 14:26:00.567086', '2026-05-12 14:26:00.567108', 51),
(9, NULL, 6, 2015, 3, 2019, 0, 'Trung tâm Phát triển Huyện Nhà Bè', 'Phó Trưởng phòng', 'Huyện Nhà Bè', NULL, 2, '2026-05-12 14:26:00.568244', '2026-05-12 14:26:00.568266', 51),
(10, NULL, 4, 2019, NULL, NULL, 1, 'Trung tâm Phát triển Quản lý Huyện Nhà Bè', 'Trưởng Phòng Kỹ thuật', 'Huyện Nhà Bè', NULL, 3, '2026-05-12 14:26:00.569579', '2026-05-12 14:26:00.569609', 51);

-- --------------------------------------------------------

--
-- Table structure for table `ref_administrative_units`
--

CREATE TABLE `ref_administrative_units` (
  `id` bigint(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `code` varchar(20) DEFAULT NULL,
  `name` varchar(200) NOT NULL,
  `parent_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ref_administrative_units`
--

INSERT INTO `ref_administrative_units` (`id`, `type`, `code`, `name`, `parent_id`) VALUES
(1, 'province', '79', 'TP. Hồ Chí Minh', NULL),
(2, 'district', '794', 'Huyện Nhà Bè', 1),
(3, 'ward', '79401', 'Thị trấn Nhà Bè', 2),
(4, 'ward', '79402', 'Xã Phước Kiển', 2),
(5, 'ward', '79403', 'Xã Long Thới', 2),
(6, 'ward', '79404', 'Xã Nhơn Đức', 2),
(7, 'ward', '79405', 'Xã Phú Xuân', 2),
(8, 'ward', '79406', 'Xã Hiệp Phước', 2),
(9, 'ward', '79407', 'Xã Nhà Bè', 2);

-- --------------------------------------------------------

--
-- Table structure for table `ref_education_levels`
--

CREATE TABLE `ref_education_levels` (
  `id` bigint(20) NOT NULL,
  `code` varchar(40) NOT NULL,
  `name` varchar(120) NOT NULL,
  `sort` smallint(5) UNSIGNED NOT NULL CHECK (`sort` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ref_education_levels`
--

INSERT INTO `ref_education_levels` (`id`, `code`, `name`, `sort`) VALUES
(1, 'tieu_hoc', 'Tiểu học', 1),
(2, 'thcs', 'THCS (9/12)', 2),
(3, 'thpt', '12/12', 3),
(4, 'trung_cap', 'Trung cấp', 4),
(5, 'cao_dang', 'Cao đẳng', 5),
(6, 'dai_hoc', 'Đại học', 6),
(7, 'thac_si', 'Thạc sĩ', 7),
(8, 'tien_si', 'Tiến sĩ', 8);

-- --------------------------------------------------------

--
-- Table structure for table `ref_ethnic_groups`
--

CREATE TABLE `ref_ethnic_groups` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ref_ethnic_groups`
--

INSERT INTO `ref_ethnic_groups` (`id`, `name`) VALUES
(9, 'Dao'),
(10, 'Gia-rai'),
(8, 'Hmông'),
(4, 'Hoa'),
(11, 'Khác'),
(5, 'Khmer'),
(1, 'Kinh'),
(6, 'Mường'),
(7, 'Nùng'),
(2, 'Tày'),
(3, 'Thái');

-- --------------------------------------------------------

--
-- Table structure for table `ref_political_levels`
--

CREATE TABLE `ref_political_levels` (
  `id` bigint(20) NOT NULL,
  `code` varchar(40) NOT NULL,
  `name` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ref_political_levels`
--

INSERT INTO `ref_political_levels` (`id`, `code`, `name`) VALUES
(1, 'so_cap', 'Sơ cấp chính trị'),
(2, 'trung_cap', 'Trung cấp chính trị'),
(3, 'cao_cap', 'Cao cấp chính trị'),
(4, 'cu_nhan', 'Cử nhân chính trị');

-- --------------------------------------------------------

--
-- Table structure for table `ref_religions`
--

CREATE TABLE `ref_religions` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ref_religions`
--

INSERT INTO `ref_religions` (`id`, `name`) VALUES
(4, 'Cao Đài'),
(3, 'Công giáo'),
(6, 'Hồi giáo'),
(7, 'Khác'),
(1, 'Không'),
(2, 'Phật giáo'),
(5, 'Tin Lành');

-- --------------------------------------------------------

--
-- Table structure for table `report_exports`
--

CREATE TABLE `report_exports` (
  `id` bigint(20) NOT NULL,
  `report_type` varchar(20) NOT NULL,
  `format` varchar(10) NOT NULL,
  `params` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`params`)),
  `file_name` varchar(500) DEFAULT NULL,
  `file_size` int(10) UNSIGNED DEFAULT NULL CHECK (`file_size` >= 0),
  `created_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `report_exports`
--

INSERT INTO `report_exports` (`id`, `report_type`, `format`, `params`, `file_name`, `file_size`, `created_at`, `created_by_id`) VALUES
(1, 'monthly', 'excel', '{\"year\": 2026, \"month\": null}', 'BaoCao_2026.xlsx', 4955, '2026-05-12 12:53:50.416229', 1);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` bigint(20) NOT NULL,
  `code` varchar(40) NOT NULL,
  `name` varchar(120) NOT NULL,
  `description` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `code`, `name`, `description`, `created_at`) VALUES
(1, 'admin', 'Quản trị hệ thống', NULL, '2026-05-12 02:52:14.185326'),
(2, 'can_bo_bxd', 'Cán bộ Ban Xây dựng Đảng', 'Thẩm định và phê duyệt hồ sơ', '2026-05-12 04:05:46.496282'),
(3, 'quan_chung', 'Quần chúng', 'Kê khai lý lịch xin vào Đảng', '2026-05-12 04:05:46.499814');

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` varchar(128) NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(500) DEFAULT NULL,
  `payload` longtext DEFAULT NULL,
  `last_activity` int(10) UNSIGNED NOT NULL CHECK (`last_activity` >= 0),
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `stats_monthly`
--

CREATE TABLE `stats_monthly` (
  `id` bigint(20) NOT NULL,
  `year` smallint(6) NOT NULL,
  `month` smallint(6) NOT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `count_draft` int(11) NOT NULL,
  `count_submitted` int(11) NOT NULL,
  `count_under_review` int(11) NOT NULL,
  `count_approved` int(11) NOT NULL,
  `count_rejected` int(11) NOT NULL,
  `count_archived` int(11) NOT NULL,
  `count_total` int(11) NOT NULL,
  `computed_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint(20) NOT NULL,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

INSERT INTO `token_blacklist_blacklistedtoken` (`id`, `blacklisted_at`, `token_id`) VALUES
(1, '2026-05-12 04:20:58.117175', 5),
(2, '2026-05-12 07:36:59.654142', 6),
(3, '2026-05-12 09:58:23.960429', 7),
(4, '2026-05-12 11:01:25.676191', 8),
(5, '2026-05-12 12:07:07.106007', 9),
(6, '2026-05-12 14:17:25.144251', 14),
(7, '2026-05-12 15:25:26.678449', 15),
(8, '2026-05-12 16:00:48.713995', 16),
(9, '2026-05-12 16:25:27.670179', 17),
(10, '2026-05-12 17:14:46.038250', 18),
(11, '2026-05-12 17:16:41.554992', 19),
(12, '2026-05-12 17:25:40.575126', 21),
(13, '2026-05-12 18:17:50.031349', 20),
(14, '2026-05-12 18:26:56.673017', 22),
(15, '2026-05-13 00:19:29.587211', 24);

-- --------------------------------------------------------

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint(20) NOT NULL,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `jti` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

INSERT INTO `token_blacklist_outstandingtoken` (`id`, `token`, `created_at`, `expires_at`, `user_id`, `jti`) VALUES
(1, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE1OTkyNCwiaWF0IjoxNzc4NTU1MTI0LCJqdGkiOiJlMjgxNzk0Njg1YWY0MzdjYThhMDhiZjkxZDJhNWIzZiIsInVzZXJfaWQiOiIxIn0.V0qKTajJllCWMdjGEaoUkLP33xk3RrQehZYM9k_pvbA', '2026-05-12 03:05:24.387991', '2026-05-19 03:05:24.000000', 1, 'e281794685af437ca8a08bf91d2a5b3f'),
(2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE1OTk0MCwiaWF0IjoxNzc4NTU1MTQwLCJqdGkiOiJlZTljYzFkMTA2OTI0ZTVmOGRhYjUyOWIyODdmZWVjMSIsInVzZXJfaWQiOiIxIn0.n1slBAVRN0oN8ipY2ysHF34p6OcgM1vMWD_mPTk1cKA', '2026-05-12 03:05:40.285369', '2026-05-19 03:05:40.000000', 1, 'ee9cc1d106924e5f8dab529b287feec1'),
(3, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE2MDQyNCwiaWF0IjoxNzc4NTU1NjI0LCJqdGkiOiJiNWI4MmMyMzkwNGE0MDI4OTJhZDhhMDA2NmE2MjA0MyIsInVzZXJfaWQiOiIxIn0.JfKhoZwvy3JvR1Y3w27qpjWiJiUa4MNCSX2WQbEkhIU', '2026-05-12 03:13:44.472896', '2026-05-19 03:13:44.000000', 1, 'b5b82c23904a402892ad8a0066a62043'),
(4, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE2MDUxNSwiaWF0IjoxNzc4NTU1NzE1LCJqdGkiOiJlYTcwOGExMDkyMWM0ZDU2YWYwNDk0MWM4MzIzNTE2OCIsInVzZXJfaWQiOiIxIn0.phRUgUmQuofyIt0K8U9Wpsurfu7lMsEk_upXi10AH4A', '2026-05-12 03:15:15.853707', '2026-05-19 03:15:15.000000', 1, 'ea708a10921c4d56af04941c83235168'),
(5, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE2MDcwMywiaWF0IjoxNzc4NTU1OTAzLCJqdGkiOiJjNTkxNDhlMzEyZWE0MGVjOGZhMTQ2Y2Y5YmExMDk3MCIsInVzZXJfaWQiOiIxIn0.KARLt_weuSn49hxah3YTugqTAl7Xaz7Y_7DGtFoGg9Y', '2026-05-12 03:18:23.131250', '2026-05-19 03:18:23.000000', 1, 'c59148e312ea40ec8fa146cf9ba10970'),
(6, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE2NDQ1OCwiaWF0IjoxNzc4NTU5NjU4LCJqdGkiOiI5OGRkZGYzYjVjODk0ZmEwYjliZDZkNzMzMGJjMmVjYiIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.YJK9rh8sPhgjCuIBgvSJAiwg00FmCqOx3I73kOKs4KA', '2026-05-12 04:20:58.100974', '2026-05-19 04:20:58.000000', 1, '98dddf3b5c894fa0b9bd6d7330bc2ecb'),
(7, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE3NjIxOSwiaWF0IjoxNzc4NTcxNDE5LCJqdGkiOiJmYzY1NjMyNzU5ZTQ0M2Y0ODc3MzFmN2U0NTZkNGQyMCIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.6ZIRhEGGvRxWfg5h8t7YLnIkPGLrAGc5SDoxlzHCCWc', '2026-05-12 07:36:59.630267', '2026-05-19 07:36:59.000000', 1, 'fc65632759e443f487731f7e456d4d20'),
(8, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE4NDcwMywiaWF0IjoxNzc4NTc5OTAzLCJqdGkiOiIyYjI0NDRiMzA5NTc0YmVkOTllZDU5YWM3YmE0MzQyNiIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.HKRQuIuBWDW6zLrzMU8yQt2zKToE_V1BmF-9qcFaMQo', '2026-05-12 09:58:23.949194', '2026-05-19 09:58:23.000000', 1, '2b2444b309574bed99ed59ac7ba43426'),
(9, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE4ODQ4NSwiaWF0IjoxNzc4NTgzNjg1LCJqdGkiOiI0MWFjOTY3NTBmZmY0ZjM1ODgwNzJmMWU4N2UyNzMwMyIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.yG3nPQqjUMLQi4lzLNlghpBFuCCSWgDFeV9LQFA-GF0', '2026-05-12 11:01:25.623978', '2026-05-19 11:01:25.000000', 1, '41ac96750fff4f3588072f1e87e27303'),
(10, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE5MTQ2NywiaWF0IjoxNzc4NTg2NjY3LCJqdGkiOiI5ZDczNWRlZjQ0MWY0ZDAwYWU2NmRiNGE3MTE1NzUxNyIsInVzZXJfaWQiOiIxOCJ9.nM-lvRQVQ-YKC3lbzBxPmU_b6CXZELnOde8PwYFkaqY', '2026-05-12 11:51:07.829135', '2026-05-19 11:51:07.000000', NULL, '9d735def441f4d00ae66db4a71157517'),
(11, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE5MTU0MywiaWF0IjoxNzc4NTg2NzQzLCJqdGkiOiIyZDVjNTA3Yzk2N2I0YmY2ODMxYmI5MTg0Nzg1ZDZhYSIsInVzZXJfaWQiOiIxOCJ9.DP9Nyb5YoDMt81axQkaoQY9SFlvqMjIhUXRIBgoAD9g', '2026-05-12 11:52:23.331733', '2026-05-19 11:52:23.000000', NULL, '2d5c507c967b4bf6831bb9184785d6aa'),
(12, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE5MTU0OSwiaWF0IjoxNzc4NTg2NzQ5LCJqdGkiOiI2Mjg2ZmFiYTA3NzQ0NGE2YWRhZGQwZjljMjg2YjUzNiIsInVzZXJfaWQiOiIxOCJ9.N_tYYQBdA0babjYE74DmbJkEwiSyI6WG54hAkFgv9Z8', '2026-05-12 11:52:29.292541', '2026-05-19 11:52:29.000000', NULL, '6286faba077444a6adadd0f9c286b536'),
(13, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE5MTY0MywiaWF0IjoxNzc4NTg2ODQzLCJqdGkiOiI4MGY1N2EyYTAwMjc0MWNhYjYyOWI5NGVkYmYzOGViNSIsInVzZXJfaWQiOiIxOCJ9.IyMa81Yt6v6o0M7YjJhireDQJMR5fUIWC0ru9XAtJwk', '2026-05-12 11:54:03.048104', '2026-05-19 11:54:03.000000', NULL, '80f57a2a002741cab629b94edbf38eb5'),
(14, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTE5MjQyNywiaWF0IjoxNzc4NTg3NjI3LCJqdGkiOiIwYTkzMmVmMWQ4OGE0NTlkODkyNGFhMGQ1ZTAwY2FmMyIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.2FAw0JiEWtaUw1VKa51fw20Kp13S2B4h9mkYgCK7sXo', '2026-05-12 12:07:07.090196', '2026-05-19 12:07:07.000000', 1, '0a932ef1d88a459d8924aa0d5e00caf3'),
(15, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIwMDI0NSwiaWF0IjoxNzc4NTk1NDQ1LCJqdGkiOiJiZjNmODgxYTUxOTE0ZTJhOTQ5MjhmODExOTY3MTE4MSIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ._JD53uvXk_dWwdt5JAQ4NB9OQn0yQd0T8yRc80hFfNg', '2026-05-12 14:17:25.128957', '2026-05-19 14:17:25.000000', 1, 'bf3f881a51914e2a94928f8119671181'),
(16, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIwMTU0NSwiaWF0IjoxNzc4NTk2NzQ1LCJqdGkiOiIxNTEyOGQ4M2JjMzY0MWQ3YTU2YWJjMDFmNzM3ODU0MiIsInVzZXJfaWQiOiI1NiJ9.SEVFZFjS8hD0J5bOIskh7OnMEc531d8eFrb0PQyWpTI', '2026-05-12 14:39:05.272947', '2026-05-19 14:39:05.000000', 56, '15128d83bc3641d7a56abc01f7378542'),
(17, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIwNDMyNiwiaWF0IjoxNzc4NTk5NTI2LCJqdGkiOiI4MGZhZWNiMGUwMzU0MTk3ODMzMWIxMTQ3ZjY5OTUyNiIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.Fe6DwautofOnOrjefFeXbMPedWjorDWDfTOqgvDOdM8', '2026-05-12 15:25:26.663739', '2026-05-19 15:25:26.000000', 1, '80faecb0e03541978331b1147f699526'),
(18, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIwNjQ0OCwiaWF0IjoxNzc4NjAxNjQ4LCJqdGkiOiI4OWZlMTNlNjE4OTA0MGJiOTQ3ZGJjMDc0MThmYTE5YiIsInVzZXJfaWQiOiI1NiIsInJvbGUiOiJjYW5fYm9fYnhkIiwiZnVsbF9uYW1lIjoiTmd1eVx1MWVjNW4gVGhcdTFlY2IgSFx1MDFiMFx1MDFhMW5nIn0.rxh5e1MuVED_2_AT1dD50XkCdgRaz7Vy29MndoobvwM', '2026-05-12 16:00:48.700382', '2026-05-19 16:00:48.000000', 56, '89fe13e6189040bb947dbc07418fa19b'),
(19, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIwNzkyNywiaWF0IjoxNzc4NjAzMTI3LCJqdGkiOiI5ZTVjOWY1YzViZmI0NWZiOTlkZTRmZDkwODdmYmFjMyIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.EJFtoiSW2ZkWVI84ZEh-ae3kIGWxk4wjLfzJPFgFiQI', '2026-05-12 16:25:27.655105', '2026-05-19 16:25:27.000000', 1, '9e5c9f5c5bfb45fb99de4fd9087fbac3'),
(20, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIxMDg4NiwiaWF0IjoxNzc4NjA2MDg2LCJqdGkiOiIxZWRjMmQ2NTgxZDQ0OGZjOGY3MzM1MzRlZjBlOTNiNCIsInVzZXJfaWQiOiI1NiIsInJvbGUiOiJjYW5fYm9fYnhkIiwiZnVsbF9uYW1lIjoiTmd1eVx1MWVjNW4gVGhcdTFlY2IgSFx1MDFiMFx1MDFhMW5nIn0.wshdHnl-MCDEuhTuAxO7DFT88_mQGQabZiEC1ZCs8DY', '2026-05-12 17:14:46.016289', '2026-05-19 17:14:46.000000', 56, '1edc2d6581d448fc8f733534ef0e93b4'),
(21, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIxMTAyMSwiaWF0IjoxNzc4NjA2MjIxLCJqdGkiOiI1OTcwODczMWU1NmU0NjExYTU4NmQ3ZmE1ZDRiNjk5OSIsInVzZXJfaWQiOiI2OCJ9.mJyHvbU3SU9A4fE8sAGQCxXE7O1UuPyteT-0UPsFIPE', '2026-05-12 17:17:01.008743', '2026-05-19 17:17:01.000000', 68, '59708731e56e4611a586d7fa5d4b6999'),
(22, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIxMTU1NCwiaWF0IjoxNzc4NjA2NzU0LCJqdGkiOiIzNjBjMWVjYTkxNmQ0OTEzODFlYzA2ZGUxY2M4MGEyNiIsInVzZXJfaWQiOiIxIn0.bY3xJjw2gbiKdW01u44Bu-K_8cFeT8xQk59__l6pczI', '2026-05-12 17:25:54.033255', '2026-05-19 17:25:54.000000', 1, '360c1eca916d491381ec06de1cc80a26'),
(23, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIxNDY3MCwiaWF0IjoxNzc4NjA5ODcwLCJqdGkiOiJhZTEzNDBmNWEyNjM0NDAxOTI3MDM0YjkyNzQ1NzY4YiIsInVzZXJfaWQiOiI1NiIsInJvbGUiOiJjYW5fYm9fYnhkIiwiZnVsbF9uYW1lIjoiTmd1eVx1MWVjNW4gVGhcdTFlY2IgSFx1MDFiMFx1MDFhMW5nIn0.hrWdjGs2LsfsnHtZekYy3eOkbBvGT0Gqfek2qGKKaiw', '2026-05-12 18:17:50.013267', '2026-05-19 18:17:50.000000', 56, 'ae1340f5a2634401927034b92745768b'),
(24, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIxNTIxNiwiaWF0IjoxNzc4NjEwNDE2LCJqdGkiOiIxM2I2MTYzN2JlMzg0YTQ1YWMyMGNiNGZhZGMyYjQ5ZiIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.QtBm473brlJOpdUH01qT7Q0hkf8N_Pj_xw_2LUSyoY0', '2026-05-12 18:26:56.661006', '2026-05-19 18:26:56.000000', 1, '13b61637be384a45ac20cb4fadc2b49f'),
(25, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3OTIzNjM2OSwiaWF0IjoxNzc4NjMxNTY5LCJqdGkiOiJiM2JkYjM1YWExZDQ0MmFkYjMwODAzOGFlNTQ0ZTM4ZSIsInVzZXJfaWQiOiIxIiwicm9sZSI6ImFkbWluIiwiZnVsbF9uYW1lIjoiYWRtaW4ifQ.8sNaxMi3ejZ4pSjbaqjNSbtPs-e5kORk_i7oZi2hCsI', '2026-05-13 00:19:29.502597', '2026-05-20 00:19:29.000000', 1, 'b3bdb35aa1d442adb308038ae544e38e');

-- --------------------------------------------------------

--
-- Table structure for table `uploaded_files`
--

CREATE TABLE `uploaded_files` (
  `id` bigint(20) NOT NULL,
  `category` varchar(40) NOT NULL,
  `original_name` varchar(500) NOT NULL,
  `stored_path` varchar(1000) NOT NULL,
  `mime_type` varchar(127) DEFAULT NULL,
  `file_size` int(10) UNSIGNED DEFAULT NULL CHECK (`file_size` >= 0),
  `created_at` datetime(6) NOT NULL,
  `uploader_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `cccd` varchar(12) DEFAULT NULL,
  `zalo_uid` varchar(100) DEFAULT NULL,
  `otp_code` varchar(8) DEFAULT NULL,
  `otp_expires_at` datetime(6) DEFAULT NULL,
  `avatar_path` varchar(500) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `email_verified` tinyint(1) NOT NULL,
  `phone_verified` tinyint(1) NOT NULL,
  `last_login_at` datetime(6) DEFAULT NULL,
  `login_attempts` smallint(5) UNSIGNED NOT NULL CHECK (`login_attempts` >= 0),
  `locked_until` datetime(6) DEFAULT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `created_by` bigint(20) DEFAULT NULL,
  `updated_by` bigint(20) DEFAULT NULL,
  `role_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `password`, `last_login`, `is_superuser`, `full_name`, `phone`, `email`, `cccd`, `zalo_uid`, `otp_code`, `otp_expires_at`, `avatar_path`, `status`, `email_verified`, `phone_verified`, `last_login_at`, `login_attempts`, `locked_until`, `deleted_at`, `created_at`, `updated_at`, `is_staff`, `created_by`, `updated_by`, `role_id`) VALUES
(1, 'pbkdf2_sha256$1200000$1aQZ7VaYbWw9J5X4ITeXZT$WymGLy+HU1A3GvfCa9CbqYxM1DCnuXZkqafALmsAENk=', '2026-05-12 02:55:13.136340', 1, 'admin', '0382786317', NULL, NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, '2026-05-12 17:25:54.027245', 0, NULL, NULL, '2026-05-12 02:52:14.886298', '2026-05-12 02:52:14.886329', 1, NULL, NULL, 1),
(54, 'pbkdf2_sha256$1200000$W5e7LtGYvXcqnru5GBEmmj$7npVB5Bda576SjzPjHBT+I4CZNOrkRNg2OaVGDlL9Z4=', NULL, 0, 'eeeeeee', '0978765432', 'linh@gmail.comd', '05456453535', NULL, NULL, NULL, NULL, 'active', 0, 1, NULL, 0, NULL, NULL, '2026-05-12 12:46:39.938174', '2026-05-12 12:46:39.938197', 0, 1, NULL, 3),
(55, 'pbkdf2_sha256$1200000$6oTqfLLWCb4A2kFyuQF124$LHuhUUpMiVyBCzQIT7Ghjg7GBjcpc/4k/4eSGjDNqHE=', NULL, 1, 'Quản trị viên', '0900000001', 'admin@lylich.gov.vn', NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:50.276768', '2026-05-12 14:25:51.019024', 1, NULL, NULL, 1),
(56, 'pbkdf2_sha256$1200000$eXFfIC2LlYwUvlJFcUZTss$M5PFK4eLQFUDm7GYEslm4hQwSD1sULYraPJuRncVjSA=', NULL, 0, 'Nguyễn Thị Hương', '0900000002', 'huong@lylich.gov.vn', NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, '2026-05-12 14:39:05.266664', 0, NULL, NULL, '2026-05-12 14:25:51.032330', '2026-05-12 14:25:51.735778', 0, NULL, NULL, 2),
(57, 'pbkdf2_sha256$1200000$PFPhYhi3Xcmh1e8tvnfX7p$g9yNKhaaPyMOMBI5EbGtian2t2a8KVwoA2MAUl9/KWY=', NULL, 0, 'Trần Văn Khoa', '0900000003', 'khoa@lylich.gov.vn', NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:51.740585', '2026-05-12 14:25:52.440175', 0, NULL, NULL, 2),
(58, 'pbkdf2_sha256$1200000$lMm3LcnFRllYQefJ0QYV0I$YziqXdFhtcB8xsNg7u1aVGxxdJBGTek35H9anBD+TBk=', NULL, 0, 'Lê Thị Mai', '0901111001', 'lethi.mai@gmail.com', '079095001001', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:52.443970', '2026-05-12 14:25:53.157602', 0, NULL, NULL, 3),
(59, 'pbkdf2_sha256$1200000$QClEH3qebWAIwviwI4ZZfn$W3ayJgm4+VOm5QFpPD9/MKh+S40TiX0cg/llnxNhTYM=', NULL, 0, 'Trần Minh Tuấn', '0901111002', 'tran.tuan@gmail.com', '079093002002', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:53.160807', '2026-05-12 14:25:53.856326', 0, NULL, NULL, 3),
(60, 'pbkdf2_sha256$1200000$bLcvyfylyb16fOwMIslSzS$jJRrEKnicOv7miuEd+666jARIKXccq4MioD/kUp9MGM=', NULL, 0, 'Phạm Thị Dung', '0901111003', 'pham.dung@gmail.com', '079097003003', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:53.860090', '2026-05-12 14:25:54.571401', 0, NULL, NULL, 3),
(61, 'pbkdf2_sha256$1200000$qdWg3rdgTBwJnhXYfrXSrm$fn94NVVDwE/GX9jFkrX+hpaNjj6yDX0jd+Np24TfwCY=', NULL, 0, 'Nguyễn Văn Bình', '0901111004', 'nguyen.binh@gmail.com', '079095004004', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:54.575803', '2026-05-12 14:25:55.281176', 0, NULL, NULL, 3),
(62, 'pbkdf2_sha256$1200000$T64dDLo6fdz2sQgcdd6EPG$OPL6HVY3MqpR/BB7yVa3h9xSvVmC+vvAVEkQiTfnpqA=', NULL, 0, 'Đinh Thị Nhung', '0901111005', 'dinh.nhung@gmail.com', '079091005005', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:55.284970', '2026-05-12 14:25:55.994168', 0, NULL, NULL, 3),
(63, 'pbkdf2_sha256$1200000$24Jg6ZDiSRvoHruTHoCEZf$f+g/km3gOoCZKAS8Zy64z/0PUeTgy1pGIkKEY4qP2TY=', NULL, 0, 'Hoàng Văn Đức', '0901111006', 'hoang.duc@gmail.com', '079095006006', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:55.997631', '2026-05-12 14:25:56.722710', 0, NULL, NULL, 3),
(64, 'pbkdf2_sha256$1200000$IdbMwSaTapWrtBtTCRO31T$sX1QeKGSqeh//4RzoHepC02jFfDOEL6J25GdPo+8IKo=', NULL, 0, 'Võ Thị Lan', '0901111007', 'vo.lan@gmail.com', '079096007007', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:56.726871', '2026-05-12 14:25:57.450287', 0, NULL, NULL, 3),
(65, 'pbkdf2_sha256$1200000$N5y9rK2kMNSMMGlLtIHDRq$X0I5QKxrXem2jAoV5kWgUwXNAzMBln4SLF+qOsbK47c=', NULL, 0, 'Bùi Quang Huy', '0901111008', 'bui.huy@gmail.com', '079091008008', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:57.454061', '2026-05-12 14:25:58.211835', 0, NULL, NULL, 3),
(66, 'pbkdf2_sha256$1200000$ruUp17wvIYTPu20fOBwpDB$aQ3qSt4LsU9kKpnEmBzTu2exu+CnKoD+Ao6aqOIs0qo=', NULL, 0, 'Trương Thị Hằng', '0901111009', 'truong.hang@gmail.com', '079095009009', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:58.215477', '2026-05-12 14:25:58.915108', 0, NULL, NULL, 3),
(67, 'pbkdf2_sha256$1200000$NFcV5WsFwvNMUKuRkNh3VV$Sf43VPuDdwgl9OqYGMQWi8hhp1uTNKjSiveTU47trYw=', NULL, 0, 'Nguyễn Thị Bình An', '0901111010', 'nguyen.binh.an@gmail.com', '079094010010', NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 14:25:58.918558', '2026-05-12 14:25:59.614998', 0, NULL, NULL, 3),
(68, 'pbkdf2_sha256$1200000$teD9nTtOdnRfA7B2M6ZJVP$e7b8NlDldtMNPyFmCosUWlA8OvbUfFwz9+RaT9JCaaE=', NULL, 0, 'Ngô Đình Hoàng', '0901111011', 'ngo.dinh.hoang@gmail.com', '079092011011', NULL, NULL, NULL, NULL, 'active', 0, 0, '2026-05-12 17:17:01.002208', 0, NULL, NULL, '2026-05-12 14:25:59.618273', '2026-05-12 14:26:00.325439', 0, NULL, NULL, 3),
(70, '', NULL, 0, 'Test Tao Nhanh 2', '0999435644', NULL, NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 17:25:09.437964', '2026-05-12 17:25:09.437988', 0, 56, NULL, 3),
(71, '', NULL, 0, 'Hồ sơ mới 12/05/2026 17:27', '0999272221', NULL, NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 17:27:38.274403', '2026-05-12 17:27:38.274427', 0, 56, NULL, 3),
(72, '', NULL, 0, 'Hồ sơ mới 12/05/2026 17:28', '0999203977', NULL, NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 17:28:42.206325', '2026-05-12 17:28:42.206352', 0, 56, NULL, 3),
(73, '', NULL, 0, 'NGUYEN THI LIMH', '0999195072', NULL, NULL, NULL, NULL, NULL, NULL, 'active', 0, 0, NULL, 0, NULL, NULL, '2026-05-12 17:29:23.196954', '2026-05-12 17:29:23.196977', 0, 1, NULL, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users_groups`
--

CREATE TABLE `users_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_user_permissions`
--

CREATE TABLE `users_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `verification_reminder_log`
--

CREATE TABLE `verification_reminder_log` (
  `id` bigint(20) NOT NULL,
  `channel` varchar(20) NOT NULL,
  `note` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `sent_by` bigint(20) DEFAULT NULL,
  `verification_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `verification_requests`
--

CREATE TABLE `verification_requests` (
  `id` bigint(20) NOT NULL,
  `agency_name` varchar(500) NOT NULL,
  `agency_contact` varchar(500) DEFAULT NULL,
  `content` longtext NOT NULL,
  `urgency` varchar(20) NOT NULL,
  `sent_date` date DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `result_summary` longtext DEFAULT NULL,
  `reminder_count` smallint(5) UNSIGNED NOT NULL CHECK (`reminder_count` >= 0),
  `last_reminded_at` datetime(6) DEFAULT NULL,
  `received_at` datetime(6) DEFAULT NULL,
  `completed_at` datetime(6) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` bigint(20) NOT NULL,
  `profile_id` bigint(20) NOT NULL,
  `result_file_id` bigint(20) DEFAULT NULL,
  `updated_by` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `verification_requests`
--

INSERT INTO `verification_requests` (`id`, `agency_name`, `agency_contact`, `content`, `urgency`, `sent_date`, `deadline`, `status`, `result_summary`, `reminder_count`, `last_reminded_at`, `received_at`, `completed_at`, `notes`, `created_at`, `updated_at`, `created_by_id`, `profile_id`, `result_file_id`, `updated_by`) VALUES
(13, 'UBND xã Nhà Bè', NULL, 'Xác minh nơi cư trú và lịch sử công tác', 'normal', '2026-04-15', '2026-05-15', 'pending', NULL, 0, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.456081', '2026-05-12 14:26:00.456096', 56, 41, NULL, NULL),
(14, 'Công an xã Phước Kiển', NULL, 'Xác minh nhân thân, không tiền án tiền sự', 'normal', '2026-04-12', '2026-05-22', 'received', NULL, 0, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.460041', '2026-05-12 14:26:00.460056', 57, 42, NULL, NULL),
(15, 'UBND xã Long Thới', NULL, 'Xác minh hộ khẩu và khai sinh', 'urgent', '2026-04-22', '2026-05-09', 'overdue', NULL, 0, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.463949', '2026-05-12 14:26:00.463962', 56, 43, NULL, NULL),
(16, 'Bệnh viện Huyện Nhà Bè', NULL, 'Xác nhận quá trình công tác 2015–2026', 'normal', '2026-04-07', '2026-06-01', 'completed', NULL, 0, NULL, NULL, NULL, NULL, '2026-05-12 14:26:00.467545', '2026-05-12 14:26:00.467559', 57, 50, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `word_export_logs`
--

CREATE TABLE `word_export_logs` (
  `id` bigint(20) NOT NULL,
  `template_name` varchar(120) DEFAULT NULL,
  `file_name` varchar(500) DEFAULT NULL,
  `file_size` int(10) UNSIGNED DEFAULT NULL CHECK (`file_size` >= 0),
  `sections_json` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`sections_json`)),
  `created_at` datetime(6) NOT NULL,
  `exported_by_id` bigint(20) NOT NULL,
  `file_id` bigint(20) DEFAULT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `word_export_logs`
--

INSERT INTO `word_export_logs` (`id`, `template_name`, `file_name`, `file_size`, `sections_json`, `created_at`, `exported_by_id`, `file_id`, `profile_id`) VALUES
(14, 'Mẫu 2-KNĐ', 'SoYeuLyLich_Ngô_Đình_Hoàng.docx', 16956, NULL, '2026-05-12 14:27:22.282701', 1, NULL, 51),
(15, 'Mẫu 2-KNĐ', 'SoYeuLyLich_NGUYEN_THI_LIMH.docx', 15586, NULL, '2026-05-12 17:33:56.988737', 1, NULL, 56),
(16, 'Mẫu 2-KNĐ', 'SoYeuLyLich_NGUYEN_THI_LIMH.docx', 15586, NULL, '2026-05-12 17:58:10.290965', 1, NULL, 56),
(17, 'Mẫu 2-KNĐ', 'SoYeuLyLich_Lê_Thị_Mai.docx', 16490, NULL, '2026-05-12 17:58:33.811633', 1, NULL, 41),
(18, 'Mẫu 2-KNĐ', 'SoYeuLyLich_Ngô_Đình_Hoàng.docx', 16956, NULL, '2026-05-12 18:48:02.266114', 1, NULL, 51);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_requests`
--
ALTER TABLE `account_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_requests_user_id_8b03959c_fk_users_id` (`user_id`),
  ADD KEY `account_requests_officer_in_charge_af8df074_fk_users_id` (`officer_in_charge`),
  ADD KEY `account_requests_requested_by_id_acb58cab_fk_users_id` (`requested_by_id`),
  ADD KEY `account_req_status_5e8981_idx` (`status`),
  ADD KEY `account_req_cccd_171a25_idx` (`cccd`);

--
-- Indexes for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `activity_lo_user_id_b8c999_idx` (`user_id`,`created_at` DESC),
  ADD KEY `activity_lo_target__23e139_idx` (`target_model`,`target_id`),
  ADD KEY `activity_lo_action_b49f28_idx` (`action`);

--
-- Indexes for table `ai_scan_results`
--
ALTER TABLE `ai_scan_results`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ai_scan_results_resolved_by_ab2321c3_fk_users_id` (`resolved_by`),
  ADD KEY `ai_scan_results_scanned_by_id_f7e295c0_fk_users_id` (`scanned_by_id`),
  ADD KEY `ai_scan_res_profile_e104ac_idx` (`profile_id`,`status`),
  ADD KEY `ai_scan_res_severit_1d88d5_idx` (`severity`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `committee_comments`
--
ALTER TABLE `committee_comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `committee_comments_updated_by_9662944e_fk_users_id` (`updated_by`),
  ADD KEY `committee_comments_profile_id_7287d8ce_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_id` (`user_id`);

--
-- Indexes for table `django_celery_beat_clockedschedule`
--
ALTER TABLE `django_celery_beat_clockedschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_crontabschedule`
--
ALTER TABLE `django_celery_beat_crontabschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_intervalschedule`
--
ALTER TABLE `django_celery_beat_intervalschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  ADD KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  ADD KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  ADD KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`);

--
-- Indexes for table `django_celery_beat_periodictasks`
--
ALTER TABLE `django_celery_beat_periodictasks`
  ADD PRIMARY KEY (`ident`);

--
-- Indexes for table `django_celery_beat_solarschedule`
--
ALTER TABLE `django_celery_beat_solarschedule`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`);

--
-- Indexes for table `django_celery_results_chordcounter`
--
ALTER TABLE `django_celery_results_chordcounter`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`);

--
-- Indexes for table `django_celery_results_groupresult`
--
ALTER TABLE `django_celery_results_groupresult`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`),
  ADD KEY `django_cele_date_cr_bd6c1d_idx` (`date_created`),
  ADD KEY `django_cele_date_do_caae0e_idx` (`date_done`);

--
-- Indexes for table `django_celery_results_taskresult`
--
ALTER TABLE `django_celery_results_taskresult`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `task_id` (`task_id`),
  ADD KEY `django_cele_task_na_08aec9_idx` (`task_name`),
  ADD KEY `django_cele_status_9b6201_idx` (`status`),
  ADD KEY `django_cele_worker_d54dd8_idx` (`worker`),
  ADD KEY `django_cele_date_cr_f04a50_idx` (`date_created`),
  ADD KEY `django_cele_date_do_f59aad_idx` (`date_done`),
  ADD KEY `django_cele_periodi_1993cf_idx` (`periodic_task_name`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `family_members`
--
ALTER TABLE `family_members`
  ADD PRIMARY KEY (`id`),
  ADD KEY `family_members_updated_by_953ff324_fk_users_id` (`updated_by`),
  ADD KEY `family_memb_profile_b70347_idx` (`profile_id`,`relationship`),
  ADD KEY `family_memb_full_na_07132b_idx` (`full_name`);

--
-- Indexes for table `login_history`
--
ALTER TABLE `login_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `login_histo_user_id_af9937_idx` (`user_id`,`created_at`),
  ADD KEY `login_histo_status_c9661d_idx` (`status`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notifications_profile_id_e4c89532_fk_profiles_id` (`profile_id`),
  ADD KEY `notifications_sender_id_57e62d28_fk_users_id` (`sender_id`),
  ADD KEY `notifications_batch_id_944482d2_fk_notification_batches_id` (`batch_id`),
  ADD KEY `notifications_template_id_2988e288_fk_notification_templates_id` (`template_id`),
  ADD KEY `notificatio_recipie_583549_idx` (`recipient_id`,`is_read`),
  ADD KEY `notificatio_type_8a8a78_idx` (`type`),
  ADD KEY `notificatio_created_e4c995_idx` (`created_at`);

--
-- Indexes for table `notification_batches`
--
ALTER TABLE `notification_batches`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notification_batches_created_by_id_09920833_fk_users_id` (`created_by_id`),
  ADD KEY `notification_batches_template_id_8bbb148a_fk_notificat` (`template_id`);

--
-- Indexes for table `notification_templates`
--
ALTER TABLE `notification_templates`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `password_resets_user_id_b63fc445_fk_users_id` (`user_id`);

--
-- Indexes for table `profiles`
--
ALTER TABLE `profiles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `profile_number` (`profile_number`),
  ADD KEY `profiles_status_0dafe7_idx` (`status`),
  ADD KEY `profiles_full_na_caac6a_idx` (`full_name`),
  ADD KEY `profiles_dob_b7f83b_idx` (`dob`),
  ADD KEY `profiles_deleted_9c701c_idx` (`deleted_at`),
  ADD KEY `profiles_ai_scor_6f9d44_idx` (`ai_score`),
  ADD KEY `profiles_submitt_d1af8a_idx` (`submitted_at`),
  ADD KEY `profiles_approved_by_a91d4613_fk_users_id` (`approved_by`),
  ADD KEY `profiles_birth_place_ward_id_c0ca7167_fk_ref_admin` (`birth_place_ward_id`),
  ADD KEY `profiles_created_by_8bc91aa1_fk_users_id` (`created_by`),
  ADD KEY `profiles_current_ward_id_8e47c519_fk_ref_administrative_units_id` (`current_ward_id`),
  ADD KEY `profiles_edu_level_id_1546ffa1_fk_ref_education_levels_id` (`edu_level_id`),
  ADD KEY `profiles_ethnic_group_id_7ab7bd4d_fk_ref_ethnic_groups_id` (`ethnic_group_id`),
  ADD KEY `profiles_hometown_ward_id_e7093e13_fk_ref_admin` (`hometown_ward_id`),
  ADD KEY `profiles_officer_in_charge_id_32cae696_fk_users_id` (`officer_in_charge_id`),
  ADD KEY `profiles_photo_file_id_ee5543bd_fk_uploaded_files_id` (`photo_file_id`),
  ADD KEY `profiles_political_level_id_b4e8988a_fk_ref_political_levels_id` (`political_level_id`),
  ADD KEY `profiles_religion_id_8f6b6625_fk_ref_religions_id` (`religion_id`),
  ADD KEY `profiles_temporary_ward_id_87d45ae0_fk_ref_admin` (`temporary_ward_id`),
  ADD KEY `profiles_updated_by_56038105_fk_users_id` (`updated_by`);

--
-- Indexes for table `profile_awards`
--
ALTER TABLE `profile_awards`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_awards_profile_id_0041997a_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_correction_items`
--
ALTER TABLE `profile_correction_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_correction_i_request_id_71d4c56a_fk_profile_c` (`request_id`);

--
-- Indexes for table `profile_correction_requests`
--
ALTER TABLE `profile_correction_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_correction_requests_created_by_id_1933e8f6_fk_users_id` (`created_by_id`),
  ADD KEY `profile_correction_requests_resolved_by_c3eee55e_fk_users_id` (`resolved_by`),
  ADD KEY `profile_cor_profile_3f9de4_idx` (`profile_id`,`status`);

--
-- Indexes for table `profile_edit_history`
--
ALTER TABLE `profile_edit_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_edit_history_edited_by_id_47910ff6_fk_users_id` (`edited_by_id`),
  ADD KEY `profile_edi_profile_729a9d_idx` (`profile_id`,`created_at` DESC),
  ADD KEY `profile_edi_section_d37782_idx` (`section`);

--
-- Indexes for table `profile_education_history`
--
ALTER TABLE `profile_education_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_education_history_profile_id_5cba7141_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_history_entries`
--
ALTER TABLE `profile_history_entries`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_history_entr_family_member_id_037c75a2_fk_family_me` (`family_member_id`),
  ADD KEY `profile_his_profile_50278a_idx` (`profile_id`,`entry_type`),
  ADD KEY `profile_his_from_ye_de09b8_idx` (`from_year`,`to_year`);

--
-- Indexes for table `profile_officer_assignments`
--
ALTER TABLE `profile_officer_assignments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_officer_assignments_assigned_by_6938b8b0_fk_users_id` (`assigned_by`),
  ADD KEY `profile_officer_assignments_officer_id_efae7f2b_fk_users_id` (`officer_id`),
  ADD KEY `profile_officer_assignments_profile_id_c2487f51_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_org_participation`
--
ALTER TABLE `profile_org_participation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_org_participation_profile_id_47794ccb_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_overseas_relatives`
--
ALTER TABLE `profile_overseas_relatives`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_overseas_relatives_profile_id_61d942f6_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_overseas_travel`
--
ALTER TABLE `profile_overseas_travel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_overseas_travel_profile_id_c189ab02_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `profile_reviews`
--
ALTER TABLE `profile_reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_rev_profile_6d45a9_idx` (`profile_id`,`created_at` DESC),
  ADD KEY `profile_rev_action_b98b9a_idx` (`action`),
  ADD KEY `profile_reviews_reviewer_id_ab4b704c_fk_users_id` (`reviewer_id`);

--
-- Indexes for table `profile_work_history`
--
ALTER TABLE `profile_work_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `profile_work_history_profile_id_35a0fef5_fk_profiles_id` (`profile_id`);

--
-- Indexes for table `ref_administrative_units`
--
ALTER TABLE `ref_administrative_units`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ref_adminis_parent__78449b_idx` (`parent_id`),
  ADD KEY `ref_adminis_type_870086_idx` (`type`);

--
-- Indexes for table `ref_education_levels`
--
ALTER TABLE `ref_education_levels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `ref_ethnic_groups`
--
ALTER TABLE `ref_ethnic_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `ref_political_levels`
--
ALTER TABLE `ref_political_levels`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `ref_religions`
--
ALTER TABLE `ref_religions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `report_exports`
--
ALTER TABLE `report_exports`
  ADD PRIMARY KEY (`id`),
  ADD KEY `report_exports_created_by_id_c81e3607_fk_users_id` (`created_by_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sessions_user_id_05e26f4a_fk_users_id` (`user_id`);

--
-- Indexes for table `stats_monthly`
--
ALTER TABLE `stats_monthly`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `stats_monthly_year_month_unit_id_cef0dd39_uniq` (`year`,`month`,`unit_id`);

--
-- Indexes for table `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token_id` (`token_id`);

--
-- Indexes for table `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  ADD KEY `token_blacklist_outstandingtoken_user_id_83bc629a_fk_users_id` (`user_id`);

--
-- Indexes for table `uploaded_files`
--
ALTER TABLE `uploaded_files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uploaded_fi_uploade_73ad0c_idx` (`uploader_id`),
  ADD KEY `uploaded_fi_categor_bfb38e_idx` (`category`),
  ADD KEY `uploaded_fi_profile_b67583_idx` (`profile_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD UNIQUE KEY `cccd` (`cccd`),
  ADD KEY `users_role_id_7a277c_idx` (`role_id`),
  ADD KEY `users_status_9ca66f_idx` (`status`),
  ADD KEY `users_full_na_0edea9_idx` (`full_name`),
  ADD KEY `users_deleted_e48316_idx` (`deleted_at`),
  ADD KEY `users_zalo_ui_83fbf8_idx` (`zalo_uid`),
  ADD KEY `users_created_by_0c0a4e75_fk_users_id` (`created_by`),
  ADD KEY `users_updated_by_7b6b180e_fk_users_id` (`updated_by`);

--
-- Indexes for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_groups_user_id_group_id_fc7788e8_uniq` (`user_id`,`group_id`),
  ADD KEY `users_groups_group_id_2f3517aa_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_permissions_user_id_permission_id_3b86cbdf_uniq` (`user_id`,`permission_id`),
  ADD KEY `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `verification_reminder_log`
--
ALTER TABLE `verification_reminder_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `verification_reminder_log_sent_by_e7d6a2a0_fk_users_id` (`sent_by`),
  ADD KEY `verification_reminde_verification_id_9a860292_fk_verificat` (`verification_id`);

--
-- Indexes for table `verification_requests`
--
ALTER TABLE `verification_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `verificatio_profile_eece44_idx` (`profile_id`,`status`),
  ADD KEY `verificatio_deadlin_2b90a1_idx` (`deadline`),
  ADD KEY `verificatio_urgency_5efccd_idx` (`urgency`),
  ADD KEY `verification_requests_created_by_id_f2a1780a_fk_users_id` (`created_by_id`),
  ADD KEY `verification_request_result_file_id_b00e0171_fk_uploaded_` (`result_file_id`),
  ADD KEY `verification_requests_updated_by_71f8b8da_fk_users_id` (`updated_by`);

--
-- Indexes for table `word_export_logs`
--
ALTER TABLE `word_export_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `word_export_logs_exported_by_id_bb3da855_fk_users_id` (`exported_by_id`),
  ADD KEY `word_export_logs_file_id_41a50751_fk_uploaded_files_id` (`file_id`),
  ADD KEY `word_export_logs_profile_id_0ba49c8d_fk_profiles_id` (`profile_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_requests`
--
ALTER TABLE `account_requests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `activity_logs`
--
ALTER TABLE `activity_logs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT for table `ai_scan_results`
--
ALTER TABLE `ai_scan_results`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=213;

--
-- AUTO_INCREMENT for table `committee_comments`
--
ALTER TABLE `committee_comments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_clockedschedule`
--
ALTER TABLE `django_celery_beat_clockedschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_crontabschedule`
--
ALTER TABLE `django_celery_beat_crontabschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_intervalschedule`
--
ALTER TABLE `django_celery_beat_intervalschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_beat_solarschedule`
--
ALTER TABLE `django_celery_beat_solarschedule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_chordcounter`
--
ALTER TABLE `django_celery_results_chordcounter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_groupresult`
--
ALTER TABLE `django_celery_results_groupresult`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_celery_results_taskresult`
--
ALTER TABLE `django_celery_results_taskresult`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `family_members`
--
ALTER TABLE `family_members`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `login_history`
--
ALTER TABLE `login_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `notification_batches`
--
ALTER TABLE `notification_batches`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notification_templates`
--
ALTER TABLE `notification_templates`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `password_resets`
--
ALTER TABLE `password_resets`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profiles`
--
ALTER TABLE `profiles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `profile_awards`
--
ALTER TABLE `profile_awards`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `profile_correction_items`
--
ALTER TABLE `profile_correction_items`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_correction_requests`
--
ALTER TABLE `profile_correction_requests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_edit_history`
--
ALTER TABLE `profile_edit_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_education_history`
--
ALTER TABLE `profile_education_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `profile_history_entries`
--
ALTER TABLE `profile_history_entries`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `profile_officer_assignments`
--
ALTER TABLE `profile_officer_assignments`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_org_participation`
--
ALTER TABLE `profile_org_participation`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_overseas_relatives`
--
ALTER TABLE `profile_overseas_relatives`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_overseas_travel`
--
ALTER TABLE `profile_overseas_travel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profile_reviews`
--
ALTER TABLE `profile_reviews`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `profile_work_history`
--
ALTER TABLE `profile_work_history`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `ref_administrative_units`
--
ALTER TABLE `ref_administrative_units`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `ref_education_levels`
--
ALTER TABLE `ref_education_levels`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `ref_ethnic_groups`
--
ALTER TABLE `ref_ethnic_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `ref_political_levels`
--
ALTER TABLE `ref_political_levels`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ref_religions`
--
ALTER TABLE `ref_religions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `report_exports`
--
ALTER TABLE `report_exports`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `stats_monthly`
--
ALTER TABLE `stats_monthly`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `uploaded_files`
--
ALTER TABLE `uploaded_files`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `users_groups`
--
ALTER TABLE `users_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `verification_reminder_log`
--
ALTER TABLE `verification_reminder_log`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `verification_requests`
--
ALTER TABLE `verification_requests`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `word_export_logs`
--
ALTER TABLE `word_export_logs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_requests`
--
ALTER TABLE `account_requests`
  ADD CONSTRAINT `account_requests_officer_in_charge_af8df074_fk_users_id` FOREIGN KEY (`officer_in_charge`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `account_requests_requested_by_id_acb58cab_fk_users_id` FOREIGN KEY (`requested_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `account_requests_user_id_8b03959c_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `activity_logs`
--
ALTER TABLE `activity_logs`
  ADD CONSTRAINT `activity_logs_user_id_60cbbbe3_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `ai_scan_results`
--
ALTER TABLE `ai_scan_results`
  ADD CONSTRAINT `ai_scan_results_profile_id_961df879_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `ai_scan_results_resolved_by_ab2321c3_fk_users_id` FOREIGN KEY (`resolved_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `ai_scan_results_scanned_by_id_f7e295c0_fk_users_id` FOREIGN KEY (`scanned_by_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `committee_comments`
--
ALTER TABLE `committee_comments`
  ADD CONSTRAINT `committee_comments_profile_id_7287d8ce_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `committee_comments_updated_by_9662944e_fk_users_id` FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `django_celery_beat_periodictask`
--
ALTER TABLE `django_celery_beat_periodictask`
  ADD CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  ADD CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`);

--
-- Constraints for table `family_members`
--
ALTER TABLE `family_members`
  ADD CONSTRAINT `family_members_profile_id_1cc9a8e9_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `family_members_updated_by_953ff324_fk_users_id` FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `login_history`
--
ALTER TABLE `login_history`
  ADD CONSTRAINT `login_history_user_id_0eeaebb8_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `notifications`
--
ALTER TABLE `notifications`
  ADD CONSTRAINT `notifications_batch_id_944482d2_fk_notification_batches_id` FOREIGN KEY (`batch_id`) REFERENCES `notification_batches` (`id`),
  ADD CONSTRAINT `notifications_profile_id_e4c89532_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `notifications_recipient_id_e1133bac_fk_users_id` FOREIGN KEY (`recipient_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `notifications_sender_id_57e62d28_fk_users_id` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `notifications_template_id_2988e288_fk_notification_templates_id` FOREIGN KEY (`template_id`) REFERENCES `notification_templates` (`id`);

--
-- Constraints for table `notification_batches`
--
ALTER TABLE `notification_batches`
  ADD CONSTRAINT `notification_batches_created_by_id_09920833_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `notification_batches_template_id_8bbb148a_fk_notificat` FOREIGN KEY (`template_id`) REFERENCES `notification_templates` (`id`);

--
-- Constraints for table `password_resets`
--
ALTER TABLE `password_resets`
  ADD CONSTRAINT `password_resets_user_id_b63fc445_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `profiles`
--
ALTER TABLE `profiles`
  ADD CONSTRAINT `profiles_approved_by_a91d4613_fk_users_id` FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profiles_birth_place_ward_id_c0ca7167_fk_ref_admin` FOREIGN KEY (`birth_place_ward_id`) REFERENCES `ref_administrative_units` (`id`),
  ADD CONSTRAINT `profiles_created_by_8bc91aa1_fk_users_id` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profiles_current_ward_id_8e47c519_fk_ref_administrative_units_id` FOREIGN KEY (`current_ward_id`) REFERENCES `ref_administrative_units` (`id`),
  ADD CONSTRAINT `profiles_edu_level_id_1546ffa1_fk_ref_education_levels_id` FOREIGN KEY (`edu_level_id`) REFERENCES `ref_education_levels` (`id`),
  ADD CONSTRAINT `profiles_ethnic_group_id_7ab7bd4d_fk_ref_ethnic_groups_id` FOREIGN KEY (`ethnic_group_id`) REFERENCES `ref_ethnic_groups` (`id`),
  ADD CONSTRAINT `profiles_hometown_ward_id_e7093e13_fk_ref_admin` FOREIGN KEY (`hometown_ward_id`) REFERENCES `ref_administrative_units` (`id`),
  ADD CONSTRAINT `profiles_officer_in_charge_id_32cae696_fk_users_id` FOREIGN KEY (`officer_in_charge_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profiles_photo_file_id_ee5543bd_fk_uploaded_files_id` FOREIGN KEY (`photo_file_id`) REFERENCES `uploaded_files` (`id`),
  ADD CONSTRAINT `profiles_political_level_id_b4e8988a_fk_ref_political_levels_id` FOREIGN KEY (`political_level_id`) REFERENCES `ref_political_levels` (`id`),
  ADD CONSTRAINT `profiles_religion_id_8f6b6625_fk_ref_religions_id` FOREIGN KEY (`religion_id`) REFERENCES `ref_religions` (`id`),
  ADD CONSTRAINT `profiles_temporary_ward_id_87d45ae0_fk_ref_admin` FOREIGN KEY (`temporary_ward_id`) REFERENCES `ref_administrative_units` (`id`),
  ADD CONSTRAINT `profiles_updated_by_56038105_fk_users_id` FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profiles_user_id_36580373_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `profile_awards`
--
ALTER TABLE `profile_awards`
  ADD CONSTRAINT `profile_awards_profile_id_0041997a_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_correction_items`
--
ALTER TABLE `profile_correction_items`
  ADD CONSTRAINT `profile_correction_i_request_id_71d4c56a_fk_profile_c` FOREIGN KEY (`request_id`) REFERENCES `profile_correction_requests` (`id`);

--
-- Constraints for table `profile_correction_requests`
--
ALTER TABLE `profile_correction_requests`
  ADD CONSTRAINT `profile_correction_requests_created_by_id_1933e8f6_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profile_correction_requests_profile_id_1b5c9e0d_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `profile_correction_requests_resolved_by_c3eee55e_fk_users_id` FOREIGN KEY (`resolved_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `profile_edit_history`
--
ALTER TABLE `profile_edit_history`
  ADD CONSTRAINT `profile_edit_history_edited_by_id_47910ff6_fk_users_id` FOREIGN KEY (`edited_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profile_edit_history_profile_id_d8450548_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_education_history`
--
ALTER TABLE `profile_education_history`
  ADD CONSTRAINT `profile_education_history_profile_id_5cba7141_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_history_entries`
--
ALTER TABLE `profile_history_entries`
  ADD CONSTRAINT `profile_history_entr_family_member_id_037c75a2_fk_family_me` FOREIGN KEY (`family_member_id`) REFERENCES `family_members` (`id`),
  ADD CONSTRAINT `profile_history_entries_profile_id_a30f4354_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_officer_assignments`
--
ALTER TABLE `profile_officer_assignments`
  ADD CONSTRAINT `profile_officer_assignments_assigned_by_6938b8b0_fk_users_id` FOREIGN KEY (`assigned_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profile_officer_assignments_officer_id_efae7f2b_fk_users_id` FOREIGN KEY (`officer_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `profile_officer_assignments_profile_id_c2487f51_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_org_participation`
--
ALTER TABLE `profile_org_participation`
  ADD CONSTRAINT `profile_org_participation_profile_id_47794ccb_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_overseas_relatives`
--
ALTER TABLE `profile_overseas_relatives`
  ADD CONSTRAINT `profile_overseas_relatives_profile_id_61d942f6_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_overseas_travel`
--
ALTER TABLE `profile_overseas_travel`
  ADD CONSTRAINT `profile_overseas_travel_profile_id_c189ab02_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `profile_reviews`
--
ALTER TABLE `profile_reviews`
  ADD CONSTRAINT `profile_reviews_profile_id_d9ee5b89_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `profile_reviews_reviewer_id_ab4b704c_fk_users_id` FOREIGN KEY (`reviewer_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `profile_work_history`
--
ALTER TABLE `profile_work_history`
  ADD CONSTRAINT `profile_work_history_profile_id_35a0fef5_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);

--
-- Constraints for table `ref_administrative_units`
--
ALTER TABLE `ref_administrative_units`
  ADD CONSTRAINT `ref_administrative_u_parent_id_0e3454d0_fk_ref_admin` FOREIGN KEY (`parent_id`) REFERENCES `ref_administrative_units` (`id`);

--
-- Constraints for table `report_exports`
--
ALTER TABLE `report_exports`
  ADD CONSTRAINT `report_exports_created_by_id_c81e3607_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `sessions`
--
ALTER TABLE `sessions`
  ADD CONSTRAINT `sessions_user_id_05e26f4a_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `token_blacklist_blacklistedtoken`
--
ALTER TABLE `token_blacklist_blacklistedtoken`
  ADD CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`);

--
-- Constraints for table `token_blacklist_outstandingtoken`
--
ALTER TABLE `token_blacklist_outstandingtoken`
  ADD CONSTRAINT `token_blacklist_outstandingtoken_user_id_83bc629a_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `uploaded_files`
--
ALTER TABLE `uploaded_files`
  ADD CONSTRAINT `uploaded_files_profile_id_b11d644c_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `uploaded_files_uploader_id_f00a315b_fk_users_id` FOREIGN KEY (`uploader_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_created_by_0c0a4e75_fk_users_id` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_role_id_1900a745_fk_roles_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `users_updated_by_7b6b180e_fk_users_id` FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `users_groups`
--
ALTER TABLE `users_groups`
  ADD CONSTRAINT `users_groups_group_id_2f3517aa_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `users_groups_user_id_f500bee5_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `users_user_permissions`
--
ALTER TABLE `users_user_permissions`
  ADD CONSTRAINT `users_user_permissio_permission_id_6d08dcd2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_user_permissions_user_id_92473840_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `verification_reminder_log`
--
ALTER TABLE `verification_reminder_log`
  ADD CONSTRAINT `verification_reminde_verification_id_9a860292_fk_verificat` FOREIGN KEY (`verification_id`) REFERENCES `verification_requests` (`id`),
  ADD CONSTRAINT `verification_reminder_log_sent_by_e7d6a2a0_fk_users_id` FOREIGN KEY (`sent_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `verification_requests`
--
ALTER TABLE `verification_requests`
  ADD CONSTRAINT `verification_request_result_file_id_b00e0171_fk_uploaded_` FOREIGN KEY (`result_file_id`) REFERENCES `uploaded_files` (`id`),
  ADD CONSTRAINT `verification_requests_created_by_id_f2a1780a_fk_users_id` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `verification_requests_profile_id_3d6c4e86_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`),
  ADD CONSTRAINT `verification_requests_updated_by_71f8b8da_fk_users_id` FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

--
-- Constraints for table `word_export_logs`
--
ALTER TABLE `word_export_logs`
  ADD CONSTRAINT `word_export_logs_exported_by_id_bb3da855_fk_users_id` FOREIGN KEY (`exported_by_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `word_export_logs_file_id_41a50751_fk_uploaded_files_id` FOREIGN KEY (`file_id`) REFERENCES `uploaded_files` (`id`),
  ADD CONSTRAINT `word_export_logs_profile_id_0ba49c8d_fk_profiles_id` FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
