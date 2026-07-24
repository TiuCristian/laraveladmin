-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 24, 2026 at 02:19 PM
-- Server version: 8.4.3
-- PHP Version: 8.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laravel_admin`
--

-- --------------------------------------------------------

--
-- Table structure for table `cache`
--

CREATE TABLE `cache` (
  `key` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cache_locks`
--

CREATE TABLE `cache_locks` (
  `key` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `owner` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `expiration` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `parent_id` bigint UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `slug`, `description`, `parent_id`, `created_at`, `updated_at`) VALUES
(1, 'Test Category', 'test-category', 'test category description', NULL, '2026-06-15 10:28:28', '2026-06-15 10:28:28'),
(2, 'Test Cat 2', 'test-cat-2', NULL, NULL, '2026-06-19 06:03:09', '2026-06-19 06:03:09');

-- --------------------------------------------------------

--
-- Table structure for table `category_post`
--

CREATE TABLE `category_post` (
  `id` bigint UNSIGNED NOT NULL,
  `category_id` bigint UNSIGNED NOT NULL,
  `post_id` bigint UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `category_post`
--

INSERT INTO `category_post` (`id`, `category_id`, `post_id`, `created_at`, `updated_at`) VALUES
(1, 1, 1, NULL, NULL),
(2, 1, 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` bigint UNSIGNED NOT NULL,
  `post_id` bigint UNSIGNED DEFAULT NULL,
  `page_id` bigint UNSIGNED DEFAULT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `website` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `content` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'pending',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `post_id`, `page_id`, `name`, `email`, `website`, `content`, `status`, `created_at`, `updated_at`) VALUES
(1, 1, NULL, 'name', 'email@gmail.com', 'https://dailylifepulse.com/', 'oasjdaoijdaoijdaoijdo asodjadoiajdadasdasd', 'approved', '2026-06-16 06:43:07', '2026-06-16 08:02:36');

-- --------------------------------------------------------

--
-- Table structure for table `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint UNSIGNED NOT NULL,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `forms`
--

CREATE TABLE `forms` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fields` json DEFAULT NULL,
  `submit_text` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'Submit',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `forms`
--

INSERT INTO `forms` (`id`, `name`, `fields`, `submit_text`, `created_at`, `updated_at`) VALUES
(1, 'Contact Us Form', '[{\"type\": \"text\", \"label\": \"Name\", \"options\": \"\", \"required\": true}, {\"type\": \"email\", \"label\": \"Email \", \"options\": \"\", \"required\": true}, {\"type\": \"text\", \"label\": \"Phone\", \"options\": \"\", \"required\": true}, {\"type\": \"textarea\", \"label\": \"Message \", \"options\": \"\", \"required\": true}, {\"type\": \"checkbox\", \"label\": \"You agree with terms\", \"options\": \"\", \"required\": false}]', 'Submit', '2026-06-16 10:22:34', '2026-06-17 09:38:14'),
(2, 'Pop-up Form (Newsletter)', '[{\"type\": \"email\", \"label\": \"Subscribe\", \"options\": \"\", \"required\": false}, {\"type\": \"checkbox\", \"label\": \"Agree to terms\", \"options\": \"\", \"required\": false}]', 'Subscribe', '2026-06-16 11:14:47', '2026-06-17 05:32:46');

-- --------------------------------------------------------

--
-- Table structure for table `form_submissions`
--

CREATE TABLE `form_submissions` (
  `id` bigint UNSIGNED NOT NULL,
  `form_id` bigint UNSIGNED NOT NULL,
  `data` json NOT NULL,
  `ip_address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `form_submissions`
--

INSERT INTO `form_submissions` (`id`, `form_id`, `data`, `ip_address`, `user_agent`, `created_at`, `updated_at`) VALUES
(1, 1, '{\"fields\": {\"Name\": \"Tiu Cristian\", \"Phone\": \"0788999555\", \"Email \": \"tiucrs@gmail.com\", \"Message \": \"hello there this is a new message from the contact form\"}}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:151.0) Gecko/20100101 Firefox/151.0', '2026-06-16 10:39:12', '2026-06-16 10:39:12'),
(2, 2, '{\"Subscribe\": \"tiucrs@gmail.com\", \"Agree to terms\": [\"Yes\"]}', '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:151.0) Gecko/20100101 Firefox/151.0', '2026-06-17 05:37:07', '2026-06-17 05:37:07');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `id` bigint UNSIGNED NOT NULL,
  `queue` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `attempts` tinyint UNSIGNED NOT NULL,
  `reserved_at` int UNSIGNED DEFAULT NULL,
  `available_at` int UNSIGNED NOT NULL,
  `created_at` int UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `job_batches`
--

CREATE TABLE `job_batches` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_jobs` int NOT NULL,
  `pending_jobs` int NOT NULL,
  `failed_jobs` int NOT NULL,
  `failed_job_ids` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `options` mediumtext COLLATE utf8mb4_unicode_ci,
  `cancelled_at` int DEFAULT NULL,
  `created_at` int NOT NULL,
  `finished_at` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `media`
--

CREATE TABLE `media` (
  `id` bigint UNSIGNED NOT NULL,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `filename` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `filepath` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mime_type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `size` bigint UNSIGNED NOT NULL DEFAULT '0',
  `alt_text` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `caption` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `dimensions` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `media`
--

INSERT INTO `media` (`id`, `user_id`, `filename`, `filepath`, `url`, `mime_type`, `size`, `alt_text`, `title`, `caption`, `description`, `dimensions`, `created_at`, `updated_at`) VALUES
(5, 2, 'E6C3kUWXRV5uIDzexNGvIRypb0VfxaKXqEPXpfAz.jpg', 'uploads/editor/E6C3kUWXRV5uIDzexNGvIRypb0VfxaKXqEPXpfAz.jpg', '/storage/uploads/editor/E6C3kUWXRV5uIDzexNGvIRypb0VfxaKXqEPXpfAz.jpg', 'image/jpeg', 27993, 'Test Post II Amazing', 'Test Post II Amazing', 'Test Post II Amazing', 'Test Post II Amazing', '738 by 288 pixels', '2026-07-24 08:00:16', '2026-07-24 11:08:42');

-- --------------------------------------------------------

--
-- Table structure for table `menus`
--

CREATE TABLE `menus` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `items` json DEFAULT NULL,
  `auto_add_pages` tinyint(1) NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `menus`
--

INSERT INTO `menus` (`id`, `name`, `items`, `auto_add_pages`, `created_at`, `updated_at`) VALUES
(1, 'Header Menu', '[{\"url\": \"/home\", \"type\": \"page\", \"title\": \"Home\"}, {\"url\": \"/test-page\", \"type\": \"page\", \"title\": \"Test Page\"}, {\"url\": \"/category/test-category\", \"type\": \"category\", \"title\": \"Test Category\"}, {\"url\": \"/about-us\", \"type\": \"page\", \"title\": \"About Us\"}, {\"url\": \"/category/test-cat-2\", \"type\": \"category\", \"title\": \"Test Cat 2\"}, {\"url\": \"/blog\", \"type\": \"page\", \"title\": \"Blog\"}, {\"url\": \"/contact-us\", \"type\": \"page\", \"title\": \"Contact Us\"}]', 0, '2026-06-16 09:57:17', '2026-06-19 10:01:11'),
(2, 'Footer Menu', '[{\"url\": \"/home\", \"type\": \"page\", \"title\": \"Home\"}, {\"url\": \"/blog\", \"type\": \"page\", \"title\": \"Blog\"}, {\"url\": \"/contact-us\", \"type\": \"page\", \"title\": \"Contact Us\"}]', 0, '2026-06-18 09:36:01', '2026-06-18 09:36:23');

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '0001_01_01_000000_create_users_table', 1),
(2, '0001_01_01_000001_create_cache_table', 1),
(3, '0001_01_01_000002_create_jobs_table', 1),
(4, '2026_06_15_111039_add_avatar_to_users_table', 1),
(5, '2026_06_15_115921_create_posts_table', 2),
(6, '2026_06_15_115922_create_pages_table', 2),
(7, '2026_06_15_115923_create_categories_table', 2),
(8, '2026_06_15_115925_create_tags_table', 2),
(9, '2026_06_15_115941_create_category_post_table', 2),
(10, '2026_06_15_115942_create_post_tag_table', 2),
(11, '2026_06_15_121856_add_publish_fields_to_pages_table', 3),
(12, '2026_06_15_122125_add_is_pillar_to_pages_table', 4),
(13, '2026_06_15_122651_add_deleted_at_to_pages_table', 5),
(14, '2026_06_15_125841_add_deleted_at_to_posts_table', 6),
(15, '2026_06_16_090922_create_settings_table', 7),
(16, '2026_06_16_093013_create_comments_table', 8),
(17, '2026_06_16_093020_add_allow_comments_to_posts_and_pages', 8),
(18, '2026_06_16_104444_create_media_table', 9),
(19, '2026_06_16_105017_add_caption_to_media_table', 10),
(20, '2026_06_16_124841_create_menus_table', 11),
(21, '2026_06_16_131229_create_forms_table', 12),
(22, '2026_06_16_133718_create_form_submissions_table', 13),
(23, '2026_06_17_081647_add_template_to_pages_table', 14),
(24, '2026_07_24_000001_add_seo_fields_to_posts_table', 15);

-- --------------------------------------------------------

--
-- Table structure for table `pages`
--

CREATE TABLE `pages` (
  `id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `excerpt` text COLLATE utf8mb4_unicode_ci,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'draft',
  `allow_comments` tinyint(1) NOT NULL DEFAULT '1',
  `author_id` bigint UNSIGNED NOT NULL,
  `featured_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `published_at` timestamp NULL DEFAULT NULL,
  `parent_id` bigint UNSIGNED DEFAULT NULL,
  `is_pillar` tinyint(1) NOT NULL DEFAULT '0',
  `template` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `pages`
--

INSERT INTO `pages` (`id`, `title`, `slug`, `content`, `excerpt`, `status`, `allow_comments`, `author_id`, `featured_image`, `created_at`, `updated_at`, `published_at`, `parent_id`, `is_pillar`, `template`, `deleted_at`) VALUES
(1, 'Test Page', 'test-page', '{\"time\":1781783999127,\"blocks\":[{\"id\":\"5M5ogTTpRW\",\"type\":\"image\",\"data\":{\"file\":{\"url\":\"/storage/uploads/editor/4BV4kfnjoJnCgGvgDWoADOUckfu4UZl0YN3wzcRS.jpg\"},\"caption\":\"\",\"withBorder\":false,\"stretched\":false,\"withBackground\":false}}],\"version\":\"2.31.6\"}', NULL, 'published', 0, 1, NULL, '2026-06-15 09:20:02', '2026-06-18 09:00:05', NULL, NULL, 1, NULL, NULL),
(2, 'Contact Us', 'contact-us', '{\"time\":1781701709706,\"blocks\":[{\"id\":\"NhbWs5vkMx\",\"type\":\"paragraph\",\"data\":{\"text\":\"Lorem ipsum dolor sit:<br><br><br>\"}},{\"id\":\"oQ5E41kcBa\",\"type\":\"shortcode\",\"data\":{\"code\":\"[form id=\\\"1\\\"]\"}},{\"id\":\"N5oBuLQo4u\",\"type\":\"shortcode\",\"data\":{\"code\":\" [form id=\\\"2\\\"] \"}}],\"version\":\"2.31.6\"}', NULL, 'published', 0, 1, NULL, '2026-06-16 10:05:27', '2026-06-17 10:08:33', NULL, NULL, 0, NULL, NULL),
(3, 'About Us', 'about-us', '{\"time\":1782131364638,\"blocks\":[{\"id\":\"gKaU3rrvrZ\",\"type\":\"paragraph\",\"data\":{\"text\":\"Lorem ipsum dolor sit&nbsp;\"}}],\"version\":\"2.31.6\"}', NULL, 'published', 0, 1, NULL, '2026-06-16 10:05:44', '2026-06-22 09:29:32', NULL, NULL, 0, NULL, NULL),
(4, 'Blog', 'blog', '{\"time\":1781684472818,\"blocks\":[],\"version\":\"2.31.6\"}', NULL, 'published', 1, 1, NULL, '2026-06-17 05:21:28', '2026-06-17 07:52:14', NULL, NULL, 0, 'frontend.page-posts', NULL),
(5, 'Test Template Page', 'test-template-page', '{\"time\":1781699492980,\"blocks\":[],\"version\":\"2.31.6\"}', NULL, 'published', 0, 1, NULL, '2026-06-17 07:23:48', '2026-06-17 09:31:59', NULL, NULL, 0, 'frontend.page-about', NULL),
(6, 'Home', 'home', '{\"time\":1784902513278,\"blocks\":[{\"id\":\"6HRu-CnmOm\",\"type\":\"header\",\"data\":{\"text\":\"This is the homepage test\",\"level\":2}},{\"id\":\"pjTc2f4vVw\",\"type\":\"paragraph\",\"data\":{\"text\":\"lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit \"}},{\"id\":\"GE6iHClBP6\",\"type\":\"paragraph\",\"data\":{\"text\":\"lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit \"}},{\"id\":\"Wtb4kyqs_9\",\"type\":\"paragraph\",\"data\":{\"text\":\"lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit \"}},{\"id\":\"RwxXduvfys\",\"type\":\"paragraph\",\"data\":{\"text\":\"lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit \"}}],\"version\":\"2.31.6\"}', NULL, 'published', 0, 1, NULL, '2026-06-18 09:01:56', '2026-07-24 11:15:15', NULL, NULL, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` bigint UNSIGNED NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_unicode_ci,
  `excerpt` text COLLATE utf8mb4_unicode_ci,
  `status` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'draft',
  `allow_comments` tinyint(1) NOT NULL DEFAULT '1',
  `author_id` bigint UNSIGNED NOT NULL,
  `featured_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `seo_title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `seo_description` text COLLATE utf8mb4_unicode_ci,
  `focus_keyword` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_pillar` tinyint(1) NOT NULL DEFAULT '0',
  `seo_score` tinyint UNSIGNED NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `title`, `slug`, `content`, `excerpt`, `status`, `allow_comments`, `author_id`, `featured_image`, `seo_title`, `seo_description`, `focus_keyword`, `is_pillar`, `seo_score`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Test Post', 'test', '{\"time\":1781597512147,\"blocks\":[{\"id\":\"ix4EmDVnDX\",\"type\":\"paragraph\",\"data\":{\"text\":\"Lorem ipsum dolor sit lorem ipsum dolor sit&nbsp;&nbsp;lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit<br><br>Lorem ipsum dolor sit lorem ipsum dolor sit  lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit<br><br>Lorem ipsum dolor sit lorem ipsum dolor sit  lorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sitlorem ipsum dolor sit \"}},{\"id\":\"p5HFLvjNQw\",\"type\":\"header\",\"data\":{\"text\":\"Test Heading Test\",\"level\":2}},{\"id\":\"kJKYK7xycO\",\"type\":\"image\",\"data\":{\"file\":{\"url\":\"/storage/uploads/editor/CyQJdZhOJzy3N22fOMwYhmxN1dUunXlw03HygNDS.jpg\"},\"caption\":\"\",\"withBorder\":false,\"stretched\":false,\"withBackground\":false}}],\"version\":\"2.31.6\"}', NULL, 'published', 1, 1, 'posts/3KCPyRJG0VBaEmCtjATk8KfChbmQUPgURvYuykro.jpg', NULL, NULL, NULL, 0, 0, '2026-06-15 09:56:52', '2026-06-16 05:11:54', NULL),
(2, 'Test Post II Amazing', 'test-post-ii', '{\"time\":1784902752759,\"blocks\":[{\"id\":\"nhORlddNQ4\",\"type\":\"header\",\"data\":{\"text\":\"Test Post II Amazing\",\"level\":2}},{\"id\":\"40VQETBZkn\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post II Amazing\"}},{\"id\":\"RDTXnu-4nI\",\"type\":\"image\",\"data\":{\"file\":{\"url\":\"/storage/uploads/editor/E6C3kUWXRV5uIDzexNGvIRypb0VfxaKXqEPXpfAz.jpg\"},\"caption\":\"\",\"withBorder\":false,\"stretched\":false,\"withBackground\":false}},{\"id\":\"IpT04hkqHN\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post II\"}},{\"id\":\"j9vj12P_94\",\"type\":\"paragraph\",\"data\":{\"text\":\"test&nbsp;Test Post II Amazing\"}},{\"id\":\"GPHgxml7zk\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II<a href=\\\"https://www.youtube.com/watch?v=J3ziPQLQzDY\\\">Test Post II</a>Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II<a href=\\\"http://127.0.0.1:8000/test-category/test\\\">Test Post II</a>Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"DZM5J4COyz\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"SAo-ps2eYc\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"zIhgxkeiSf\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"17Ms1pX783\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"aToDShpazF\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"nz1SH-EFam\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"QYL1ADl8Mg\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}},{\"id\":\"XX2QVVa14w\",\"type\":\"paragraph\",\"data\":{\"text\":\"Test Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post IITest Post II\"}}],\"version\":\"2.31.6\"}', 'Test Post II', 'published', 0, 1, 'uploads/editor/E6C3kUWXRV5uIDzexNGvIRypb0VfxaKXqEPXpfAz.jpg', 'Test Post II', 'Test Post II', 'Test Post II', 0, 72, '2026-06-16 05:40:03', '2026-07-24 11:19:13', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `post_tag`
--

CREATE TABLE `post_tag` (
  `id` bigint UNSIGNED NOT NULL,
  `post_id` bigint UNSIGNED NOT NULL,
  `tag_id` bigint UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `post_tag`
--

INSERT INTO `post_tag` (`id`, `post_id`, `tag_id`, `created_at`, `updated_at`) VALUES
(1, 1, 1, NULL, NULL),
(2, 2, 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` bigint UNSIGNED DEFAULT NULL,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_activity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`id`, `user_id`, `ip_address`, `user_agent`, `payload`, `last_activity`) VALUES
('wfHuaNqMjg0a9wIfImn6LOvD3vJ1rkMw2IjW7ekh', 2, '127.0.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:153.0) Gecko/20100101 Firefox/153.0', 'YTo0OntzOjY6Il90b2tlbiI7czo0MDoiRVRZV2N3dFc1VjFWSnZuOGRoVlVhM0kwSTFmU2hyM1NXbmd5ZzVjcCI7czo5OiJfcHJldmlvdXMiO2E6Mjp7czozOiJ1cmwiO3M6MzM6Imh0dHA6Ly8xMjcuMC4wLjE6ODAwMC9hZG1pbi9wb3N0cyI7czo1OiJyb3V0ZSI7czoxMToicG9zdHMuaW5kZXgiO31zOjY6Il9mbGFzaCI7YToyOntzOjM6Im9sZCI7YTowOnt9czozOiJuZXciO2E6MDp7fX1zOjUwOiJsb2dpbl93ZWJfNTliYTM2YWRkYzJiMmY5NDAxNTgwZjAxNGM3ZjU4ZWE0ZTMwOTg5ZCI7aToyO30=', 1784902760);

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` bigint UNSIGNED NOT NULL,
  `key` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `value` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `key`, `value`, `created_at`, `updated_at`) VALUES
(1, 'site_title', 'Test Website Title', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(2, 'tagline', 'Just another CMS site test', '2026-06-16 06:14:23', '2026-06-16 06:16:34'),
(3, 'site_url', 'http://127.0.0.1:8000', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(4, 'home_url', 'http://127.0.0.1:8000', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(5, 'admin_email', 'admin@example.com', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(6, 'membership', '0', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(7, 'default_role', 'Subscriber', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(8, 'timezone', 'UTC', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(9, 'date_format', 'd/m/Y', '2026-06-16 06:14:23', '2026-06-16 06:16:34'),
(10, 'time_format', 'g:i a', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(11, 'start_of_week', 'Monday', '2026-06-16 06:14:23', '2026-06-16 06:14:23'),
(12, 'homepage_display', 'static', '2026-06-16 06:23:08', '2026-06-16 06:23:08'),
(13, 'page_on_front', '6', '2026-06-16 06:23:08', '2026-06-18 09:02:10'),
(14, 'page_for_posts', '4', '2026-06-16 06:23:08', '2026-06-17 05:21:37'),
(15, 'posts_per_page', '10', '2026-06-16 06:23:08', '2026-06-16 06:23:08'),
(16, 'posts_per_rss', '10', '2026-06-16 06:23:08', '2026-06-16 06:23:08'),
(17, 'rss_use_excerpt', '0', '2026-06-16 06:23:08', '2026-06-16 06:23:08'),
(18, 'discourage_search_engines', '0', '2026-06-16 06:23:08', '2026-06-16 06:23:08'),
(19, 'menu_locations', '{\"primary\":1,\"footer\":2,\"mobile\":null}', '2026-06-16 09:57:36', '2026-06-19 06:02:17'),
(20, 'permalink_structure', '/%postname%/', '2026-06-18 09:08:25', '2026-06-18 09:08:25'),
(21, 'custom_permalink_structure', '/%postname%/', '2026-06-18 09:08:25', '2026-06-18 09:08:25'),
(22, 'category_base', NULL, '2026-06-18 09:08:25', '2026-06-18 09:08:25'),
(23, 'tag_base', NULL, '2026-06-18 09:08:25', '2026-06-18 09:08:25'),
(24, 'remove_category_base', '1', '2026-06-18 09:08:25', '2026-06-19 06:33:28'),
(25, 'remove_tag_base', '1', '2026-06-18 09:08:25', '2026-06-18 09:08:25'),
(26, 'sidebar_widgets', '[{\"type\":\"recent_posts\",\"title\":\"Recent Posts\",\"limit\":\"5\",\"show_thumbnail\":true},{\"type\":\"categories\",\"title\":\"Categories\"}]', '2026-06-18 09:22:41', '2026-06-22 04:47:09');

-- --------------------------------------------------------

--
-- Table structure for table `tags`
--

CREATE TABLE `tags` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tags`
--

INSERT INTO `tags` (`id`, `name`, `slug`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Test Tag', 'test-tag', 'this is a test tag description', '2026-06-15 10:35:27', '2026-06-15 10:35:27'),
(2, 'test post II', 'test-post-ii', NULL, '2026-07-24 06:43:55', '2026-07-24 06:43:55');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'subscriber',
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `avatar` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `role`, `email_verified_at`, `password`, `remember_token`, `created_at`, `updated_at`, `avatar`) VALUES
(1, 'Admin User', 'admin@example.com', 'administrator', '2026-06-15 08:20:54', '$2y$12$Y2ARsxNf9Cq8Db35AFTLX.JW9EMtRN1LuN1XWZPtAjNTKkDDT4bOS', 'SMjMmc9hhl', '2026-06-15 08:20:54', '2026-06-15 08:20:54', NULL),
(2, 'Cristi', 'tiucrs@gmail.com', 'administrator', NULL, '$2y$12$xpjUkFtzicqM1/hm3L4zYekzH46kJHMMNoJkXYKF79zaFKD6VudlW', NULL, '2026-06-15 08:22:56', '2026-06-16 04:35:35', NULL),
(3, 'Test User', 'test@example.com', 'subscriber', NULL, '$2y$12$4hxDpEKSPi3Mxaf7o8T0..2fjGJF0ulx0SlHAJ1rva7pfl7nOxVhm', NULL, '2026-06-15 09:50:36', '2026-06-15 09:50:36', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cache`
--
ALTER TABLE `cache`
  ADD PRIMARY KEY (`key`),
  ADD KEY `cache_expiration_index` (`expiration`);

--
-- Indexes for table `cache_locks`
--
ALTER TABLE `cache_locks`
  ADD PRIMARY KEY (`key`),
  ADD KEY `cache_locks_expiration_index` (`expiration`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `categories_slug_unique` (`slug`),
  ADD KEY `categories_parent_id_foreign` (`parent_id`);

--
-- Indexes for table `category_post`
--
ALTER TABLE `category_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_post_category_id_foreign` (`category_id`),
  ADD KEY `category_post_post_id_foreign` (`post_id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `comments_post_id_foreign` (`post_id`),
  ADD KEY `comments_page_id_foreign` (`page_id`);

--
-- Indexes for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`);

--
-- Indexes for table `forms`
--
ALTER TABLE `forms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `form_submissions`
--
ALTER TABLE `form_submissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `form_submissions_form_id_foreign` (`form_id`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jobs_queue_index` (`queue`);

--
-- Indexes for table `job_batches`
--
ALTER TABLE `job_batches`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `media`
--
ALTER TABLE `media`
  ADD PRIMARY KEY (`id`),
  ADD KEY `media_user_id_foreign` (`user_id`);

--
-- Indexes for table `menus`
--
ALTER TABLE `menus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pages`
--
ALTER TABLE `pages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pages_slug_unique` (`slug`),
  ADD KEY `pages_author_id_foreign` (`author_id`),
  ADD KEY `pages_parent_id_foreign` (`parent_id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `posts_slug_unique` (`slug`),
  ADD KEY `posts_author_id_foreign` (`author_id`);

--
-- Indexes for table `post_tag`
--
ALTER TABLE `post_tag`
  ADD PRIMARY KEY (`id`),
  ADD KEY `post_tag_post_id_foreign` (`post_id`),
  ADD KEY `post_tag_tag_id_foreign` (`tag_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sessions_user_id_index` (`user_id`),
  ADD KEY `sessions_last_activity_index` (`last_activity`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `settings_key_unique` (`key`);

--
-- Indexes for table `tags`
--
ALTER TABLE `tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tags_slug_unique` (`slug`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `category_post`
--
ALTER TABLE `category_post`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `forms`
--
ALTER TABLE `forms`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `form_submissions`
--
ALTER TABLE `form_submissions`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `media`
--
ALTER TABLE `media`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `menus`
--
ALTER TABLE `menus`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `pages`
--
ALTER TABLE `pages`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `post_tag`
--
ALTER TABLE `post_tag`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `tags`
--
ALTER TABLE `tags`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `categories`
--
ALTER TABLE `categories`
  ADD CONSTRAINT `categories_parent_id_foreign` FOREIGN KEY (`parent_id`) REFERENCES `categories` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `category_post`
--
ALTER TABLE `category_post`
  ADD CONSTRAINT `category_post_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `category_post_post_id_foreign` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `comments_page_id_foreign` FOREIGN KEY (`page_id`) REFERENCES `pages` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `comments_post_id_foreign` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `form_submissions`
--
ALTER TABLE `form_submissions`
  ADD CONSTRAINT `form_submissions_form_id_foreign` FOREIGN KEY (`form_id`) REFERENCES `forms` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `media`
--
ALTER TABLE `media`
  ADD CONSTRAINT `media_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `pages`
--
ALTER TABLE `pages`
  ADD CONSTRAINT `pages_author_id_foreign` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `pages_parent_id_foreign` FOREIGN KEY (`parent_id`) REFERENCES `pages` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_author_id_foreign` FOREIGN KEY (`author_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `post_tag`
--
ALTER TABLE `post_tag`
  ADD CONSTRAINT `post_tag_post_id_foreign` FOREIGN KEY (`post_id`) REFERENCES `posts` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `post_tag_tag_id_foreign` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
