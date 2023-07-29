-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2023 at 06:22 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stocks_algo`
--

-- --------------------------------------------------------

--
-- Table structure for table `candle_stick_log`
--

CREATE TABLE `candle_stick_log` (
  `date` timestamp NULL DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `close` double DEFAULT NULL,
  `volume` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `candle_stick_log`
--

INSERT INTO `candle_stick_log` (`date`, `open`, `high`, `low`, `close`, `volume`) VALUES
('2023-07-26 01:15:00', 45845, 45845, 45845, 45845, 0),
('2023-07-26 01:45:00', 45845, 45845, 45845, 45845, 0),
('2023-07-26 02:15:00', 45845, 45845, 45845, 45845, 0),
('2023-07-26 02:45:00', 45845, 45845, 45845, 45845, 0),
('2023-07-26 03:15:00', 45845, 45935.15, 45845, 45935.15, 0),
('2023-07-26 03:45:00', 45935.15, 45937.3, 45809.6, 45849.85, 0),
('2023-07-26 04:15:00', 45850.2, 45961.5, 45813.95, 45959.8, 0),
('2023-07-26 04:45:00', 45960.65, 45995.85, 45917.25, 45928.9, 0),
('2023-07-26 05:15:00', 45925.85, 45944.75, 45867.9, 45872.95, 0),
('2023-07-26 05:45:00', 45871.2, 45937.85, 45843.7, 45926.95, 0),
('2023-07-26 06:15:00', 45929.65, 45966.95, 45890.6, 45960.2, 0),
('2023-07-26 06:45:00', 45958.55, 45996.9, 45931.65, 45953.25, 0),
('2023-07-26 07:15:00', 45953.9, 45998.75, 45903.25, 45933, 0),
('2023-07-26 07:45:00', 45932.45, 46034, 45932.45, 45999.05, 0),
('2023-07-26 08:15:00', 45998.35, 46040.3, 45931.35, 45985.65, 0),
('2023-07-26 08:45:00', 45983.45, 46095.9, 45977.15, 46016.05, 0),
('2023-07-26 09:15:00', 46014.15, 46077.4, 45941.6, 46071.25, 0),
('2023-07-26 09:45:00', 46069.7, 46083.35, 46025.5, 46043.4, 0),
('2023-07-28 01:15:00', 45679.3, 45679.3, 45679.3, 45679.3, 0),
('2023-07-28 01:45:00', 45679.3, 45679.3, 45679.3, 45679.3, 0),
('2023-07-28 02:15:00', 45679.3, 45679.3, 45679.3, 45679.3, 0),
('2023-07-28 02:45:00', 45679.3, 45679.3, 45679.3, 45679.3, 0),
('2023-07-28 03:15:00', 45679.3, 45679.3, 45560.9, 45560.9, 0),
('2023-07-28 03:45:00', 45560.9, 45703.5, 45370.75, 45472.45, 0),
('2023-07-28 04:15:00', 45473.15, 45526.3, 45394.3, 45423.8, 0),
('2023-07-28 04:45:00', 45424.95, 45487.8, 45376.2, 45470.05, 0),
('2023-07-28 05:15:00', 45468.65, 45521.05, 45441.6, 45446.5, 0),
('2023-07-28 05:45:00', 45446.75, 45491.45, 45372.2, 45378.25, 0),
('2023-07-28 06:15:00', 45381.15, 45429.1, 45366.75, 45380.35, 0);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `pwd` varchar(100) NOT NULL,
  `angel_user` varchar(100) NOT NULL,
  `angel_pwd` int(100) NOT NULL,
  `pan` int(20) DEFAULT NULL,
  `aadhar` int(20) DEFAULT NULL,
  `mobileno` int(11) DEFAULT NULL,
  `fin_q` int(100) NOT NULL,
  `totpkey` varchar(50) NOT NULL,
  `initialdeposit` double DEFAULT NULL,
  `lotsize` int(11) DEFAULT NULL,
  `signupdate` datetime DEFAULT NULL,
  `createdate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `pwd`, `angel_user`, `angel_pwd`, `pan`, `aadhar`, `mobileno`, `fin_q`, `totpkey`, `initialdeposit`, `lotsize`, `signupdate`, `createdate`) VALUES
(1, 'chetan londhe', 'chetan@3333', 'chetan123', 0, 1234567890, 2147483647, 123456788, 0, 'ierereererwirwi', 1000, 13, NULL, '2023-07-24 19:30:45'),
(2, 'Ashok', 'KnsAng@12#', 'A51886317', 1971, 1235, 0, 2147483647, 15, 'YMHPXY2ONJ7C4DGBXX4RZTYNFM', 0, 0, NULL, '2023-07-28 15:04:08'),
(3, '', '', '', 0, 0, 0, 0, 0, '', 0, 45768, NULL, '2023-07-24 19:38:55');

-- --------------------------------------------------------

--
-- Table structure for table `defaults_log`
--

CREATE TABLE `defaults_log` (
  `id` int(200) NOT NULL,
  `name` varchar(30) NOT NULL,
  `value` int(200) NOT NULL,
  `createdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `entryconditions`
--

CREATE TABLE `entryconditions` (
  `id` int(200) NOT NULL,
  `tradingstreategy` bigint(20) DEFAULT NULL,
  `Start Date` text DEFAULT NULL,
  `End Date` text DEFAULT NULL,
  `High` double DEFAULT NULL,
  `Low` double DEFAULT NULL,
  `Entry Above High` double DEFAULT NULL,
  `Entry Below Low` double DEFAULT NULL,
  `Stop Loss Above Entry` double DEFAULT NULL,
  `Stop Loss Below Entry` double DEFAULT NULL,
  `Target Profit Above Entry` double DEFAULT NULL,
  `Target Profit Below Entry` double DEFAULT NULL,
  `Entry Date` text DEFAULT NULL,
  `Position` text DEFAULT NULL,
  `Entry_value` double DEFAULT NULL,
  `Exit Date` text DEFAULT NULL,
  `Result` text DEFAULT NULL,
  `Profit/Loss` double DEFAULT NULL,
  `stop loss value` double DEFAULT NULL,
  `Target Profit value` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `entryconditions`
--

INSERT INTO `entryconditions` (`id`, `tradingstreategy`, `Start Date`, `End Date`, `High`, `Low`, `Entry Above High`, `Entry Below Low`, `Stop Loss Above Entry`, `Stop Loss Below Entry`, `Target Profit Above Entry`, `Target Profit Below Entry`, `Entry Date`, `Position`, `Entry_value`, `Exit Date`, `Result`, `Profit/Loss`, `stop loss value`, `Target Profit value`) VALUES
(1, 1, '2023-07-21 13:15:00', '2023-07-21 13:45:00', 46263.15, 46076.7, 46263.15, 46076.7, 46076.7, 46263.15, 46542.82500000001, 45797.024999999994, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 1, '2023-07-21 14:15:00', '2023-07-21 14:45:00', 46206.55, 45948.9, 46206.55, 45948.9, 45948.9, 46206.55, 46593.02500000001, 45562.425, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(81, 1, '2023-07-26 13:15:00', '2023-07-26 13:45:00', 46040.3, 45931.35, 46040.3, 45931.35, 45931.35, 46040.3, 46203.725000000006, 45767.92499999999, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(82, 1, '2023-07-26 13:45:00', '2023-07-26 14:15:00', 46095.9, 45931.35, 46095.9, 45931.35, 45931.35, 46095.9, 46342.725000000006, 45684.524999999994, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(87, 1, '2023-07-28 09:45:00', '2023-07-28 10:15:00', 45526.3, 45376.2, 45526.3, 45376.2, 45376.2, 45526.3, 45751.45000000001, 45151.04999999999, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(88, 1, '2023-07-28 10:15:00', '2023-07-28 10:45:00', 45521.05, 45376.2, 45521.05, 45376.2, 45376.2, 45521.05, 45738.32500000001, 45158.92499999999, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `login_history`
--

CREATE TABLE `login_history` (
  `id` int(100) NOT NULL,
  `user-id` int(100) NOT NULL,
  `status` varchar(200) NOT NULL,
  `createdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order_log`
--

CREATE TABLE `order_log` (
  `customerusername` text DEFAULT NULL,
  `status` text DEFAULT NULL,
  `object` text DEFAULT NULL,
  `createdate` datetime DEFAULT NULL,
  `symboltoken` text DEFAULT NULL,
  `symbolname` text DEFAULT NULL,
  `instrumenttype` text DEFAULT NULL,
  `priceden` text DEFAULT NULL,
  `pricenum` text DEFAULT NULL,
  `genden` text DEFAULT NULL,
  `gennum` text DEFAULT NULL,
  `precision` text DEFAULT NULL,
  `multiplier` text DEFAULT NULL,
  `boardlotsize` text DEFAULT NULL,
  `exchange` text DEFAULT NULL,
  `producttype` text DEFAULT NULL,
  `tradingsymbol` text DEFAULT NULL,
  `symbolgroup` text DEFAULT NULL,
  `strikeprice` text DEFAULT NULL,
  `optiontype` text DEFAULT NULL,
  `expirydate` text DEFAULT NULL,
  `lotsize` text DEFAULT NULL,
  `cfbuyqty` text DEFAULT NULL,
  `cfsellqty` text DEFAULT NULL,
  `cfbuyamount` text DEFAULT NULL,
  `cfsellamount` text DEFAULT NULL,
  `buyavgprice` text DEFAULT NULL,
  `sellavgprice` text DEFAULT NULL,
  `avgnetprice` text DEFAULT NULL,
  `netvalue` text DEFAULT NULL,
  `netqty` text DEFAULT NULL,
  `totalbuyvalue` text DEFAULT NULL,
  `totalsellvalue` text DEFAULT NULL,
  `cfbuyavgprice` text DEFAULT NULL,
  `cfsellavgprice` text DEFAULT NULL,
  `totalbuyavgprice` text DEFAULT NULL,
  `totalsellavgprice` text DEFAULT NULL,
  `netprice` text DEFAULT NULL,
  `buyqty` text DEFAULT NULL,
  `sellqty` text DEFAULT NULL,
  `buyamount` text DEFAULT NULL,
  `sellamount` text DEFAULT NULL,
  `pnl` text DEFAULT NULL,
  `realised` text DEFAULT NULL,
  `unrealised` text DEFAULT NULL,
  `ltp` text DEFAULT NULL,
  `close` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_log`
--

INSERT INTO `order_log` (`customerusername`, `status`, `object`, `createdate`, `symboltoken`, `symbolname`, `instrumenttype`, `priceden`, `pricenum`, `genden`, `gennum`, `precision`, `multiplier`, `boardlotsize`, `exchange`, `producttype`, `tradingsymbol`, `symbolgroup`, `strikeprice`, `optiontype`, `expirydate`, `lotsize`, `cfbuyqty`, `cfsellqty`, `cfbuyamount`, `cfsellamount`, `buyavgprice`, `sellavgprice`, `avgnetprice`, `netvalue`, `netqty`, `totalbuyvalue`, `totalsellvalue`, `cfbuyavgprice`, `cfsellavgprice`, `totalbuyavgprice`, `totalsellavgprice`, `netprice`, `buyqty`, `sellqty`, `buyamount`, `sellamount`, `pnl`, `realised`, `unrealised`, `ltp`, `close`) VALUES
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000233DDECF220>', '2023-07-19 21:44:12', '37192', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345800PE', 'XX', '45800.0', 'PE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '361.10', '263.45', '0.00', '-2441.25', '0', '9027.50', '6586.25', '0.00', '0.00', '361.10', '263.45', '0.00', '25', '25', '9027.50', '6586.25', '-2441.25', '-2441.25', '0.00', '205.05', '445.85'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001CF81C9F220>', '2023-07-19 21:45:28', '37192', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345800PE', 'XX', '45800.0', 'PE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '361.10', '263.45', '0.00', '-2441.25', '0', '9027.50', '6586.25', '0.00', '0.00', '361.10', '263.45', '0.00', '25', '25', '9027.50', '6586.25', '-2441.25', '-2441.25', '0.00', '205.05', '445.85'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-19 21:55:07', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000021B2452F220>', '2023-07-19 21:55:07', '37192', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345800PE', 'XX', '45800.0', 'PE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '361.10', '263.45', '0.00', '-2441.25', '0', '9027.50', '6586.25', '0.00', '0.00', '361.10', '263.45', '0.00', '25', '25', '9027.50', '6586.25', '-2441.25', '-2441.25', '0.00', '205.05', '445.85'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-20 20:28:00', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Failed', 'k31094_noobj', '2023-07-20 20:28:15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-20 20:30:09', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Failed', 'k31094_noobj', '2023-07-20 20:30:10', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-20 20:32:49', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000141790DF220>', '2023-07-20 20:32:50', '37185', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345500CE', 'XX', '45500.0', 'CE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '277.60', '385.90', '0.00', '2707.50', '0', '6940.00', '9647.50', '0.00', '0.00', '277.60', '385.90', '0.00', '25', '25', '6940.00', '9647.50', '2707.50', '2707.50', '-0.00', '689.9', '187.75'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000141790DF220>', '2023-07-20 20:32:50', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '961.25', '0.00', '961.25', '-28837.50', '30', '28837.50', '0.00', '0.00', '0.00', '961.25', '0.00', '961.25', '30', '0', '28837.50', '0.00', '3060.00', '-0.00', '3060.00', '1063.25', '700.8'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-20 20:37:12', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000023882F2F250>', '2023-07-20 20:37:12', '37185', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345500CE', 'XX', '45500.0', 'CE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '277.60', '385.90', '0.00', '2707.50', '0', '6940.00', '9647.50', '0.00', '0.00', '277.60', '385.90', '0.00', '25', '25', '6940.00', '9647.50', '2707.50', '2707.50', '-0.00', '689.9', '187.75'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000023882F2F250>', '2023-07-20 20:37:12', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '961.25', '0.00', '961.25', '-28837.50', '30', '28837.50', '0.00', '0.00', '0.00', '961.25', '0.00', '961.25', '30', '0', '28837.50', '0.00', '3060.00', '-0.00', '3060.00', '1063.25', '700.8'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-20 21:59:20', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000016270E4F250>', '2023-07-20 21:59:21', '37185', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY20JUL2345500CE', 'XX', '45500.0', 'CE', '20JUL2023', '25', '0', '0', '0.00', '0.00', '277.60', '385.90', '0.00', '2707.50', '0', '6940.00', '9647.50', '0.00', '0.00', '277.60', '385.90', '0.00', '25', '25', '6940.00', '9647.50', '2707.50', '2707.50', '-0.00', '689.9', '187.75'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000016270E4F250>', '2023-07-20 21:59:21', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '961.25', '0.00', '961.25', '-28837.50', '30', '28837.50', '0.00', '0.00', '0.00', '961.25', '0.00', '961.25', '30', '0', '28837.50', '0.00', '3060.00', '-0.00', '3060.00', '1063.25', '700.8'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 11:01:07', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000024F84A5F1C0>', '2023-07-21 11:01:08', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2309.40', '-0.00', '2309.40', '1040.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 13:01:53', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001F003E4B940>', '2023-07-21 13:01:54', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2613.90', '-0.00', '2613.90', '1050.15', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 19:03:23', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000015FACB66170>', '2023-07-21 19:03:23', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 19:05:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002A979E66170>', '2023-07-21 19:05:57', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 19:46:35', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EAAC526110>', '2023-07-21 19:46:36', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:00:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000132BC606140>', '2023-07-21 20:00:57', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:13:53', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002BEACB36170>', '2023-07-21 20:13:54', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:22:19', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002B22B6B6110>', '2023-07-21 20:22:19', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:26:50', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000028E0F4D60E0>', '2023-07-21 20:26:50', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:29:11', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001B618E160E0>', '2023-07-21 20:29:11', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 20:31:15', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000191864660E0>', '2023-07-21 20:31:15', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 21:43:24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000021126C360E0>', '2023-07-21 21:43:24', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 21:47:01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020CF58360E0>', '2023-07-21 21:47:01', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 21:54:14', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000022FC9C860E0>', '2023-07-21 21:54:14', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 21:56:34', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000028D7C2760E0>', '2023-07-21 21:56:34', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-21 22:03:53', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001AF9BC36110>', '2023-07-21 22:03:53', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '2969.40', '-0.00', '2969.40', '1062.0', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-22 12:28:17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001D72A1B6110>', '2023-07-22 12:28:17', '60511', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800CE', 'XX', '45800.0', 'CE', '31AUG2023', '15', '30', '0', '28890.74', '0.00', '0.00', '0.00', '0.00', '-28890.74', '30', '28890.74', '0.00', '963.02', '0.00', '963.02', '0.00', '963.02', '0', '0', '0.00', '0.00', '1836.90', '-0.00', '1836.90', '1024.25', '1543.3'),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 19:53:39', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000014F077A42B0>', '2023-07-26 19:53:39', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000014F077A42B0>', '2023-07-26 19:53:39', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 19:53:40', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 19:57:34', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EE22340190>', '2023-07-26 19:57:34', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EE22340190>', '2023-07-26 19:57:34', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 19:57:35', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:00:12', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002588B530190>', '2023-07-26 20:00:12', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002588B530190>', '2023-07-26 20:00:12', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:00:13', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:02:36', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002110F140190>', '2023-07-26 20:02:36', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002110F140190>', '2023-07-26 20:02:36', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:02:37', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:09:08', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001B542EA0160>', '2023-07-26 20:09:08', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001B542EA0160>', '2023-07-26 20:09:08', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:09:10', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:15:16', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000015826730190>', '2023-07-26 20:15:16', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000015826730190>', '2023-07-26 20:15:16', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:15:18', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:25:36', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001FA97CC42B0>', '2023-07-26 20:25:37', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001FA97CC42B0>', '2023-07-26 20:25:37', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:25:38', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:27:47', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002E5F97E42B0>', '2023-07-26 20:27:47', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002E5F97E42B0>', '2023-07-26 20:27:47', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:27:49', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 20:30:44', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001DC442A42B0>', '2023-07-26 20:30:44', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001DC442A42B0>', '2023-07-26 20:30:44', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 20:30:45', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:12:25', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000252B5AE42B0>', '2023-07-26 21:12:25', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000252B5AE42B0>', '2023-07-26 21:12:25', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:12:34', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:18:01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000011DBC2242B0>', '2023-07-26 21:18:01', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000011DBC2242B0>', '2023-07-26 21:18:01', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:18:09', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:22:24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001F7183442B0>', '2023-07-26 21:22:24', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001F7183442B0>', '2023-07-26 21:22:24', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:22:32', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:47:39', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001C23E5361D0>', '2023-07-26 21:47:39', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001C23E5361D0>', '2023-07-26 21:47:39', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:47:40', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:51:45', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000022B256C8220>', '2023-07-26 21:51:45', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000022B256C8220>', '2023-07-26 21:51:45', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:51:45', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 21:58:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001C6F2FB61D0>', '2023-07-26 21:58:54', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001C6F2FB61D0>', '2023-07-26 21:58:54', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 21:59:02', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:02:24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002C02AD36350>', '2023-07-26 22:02:25', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002C02AD36350>', '2023-07-26 22:02:25', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:02:26', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:03:56', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000028540556350>', '2023-07-26 22:03:56', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000028540556350>', '2023-07-26 22:03:56', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:03:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `order_log` (`customerusername`, `status`, `object`, `createdate`, `symboltoken`, `symbolname`, `instrumenttype`, `priceden`, `pricenum`, `genden`, `gennum`, `precision`, `multiplier`, `boardlotsize`, `exchange`, `producttype`, `tradingsymbol`, `symbolgroup`, `strikeprice`, `optiontype`, `expirydate`, `lotsize`, `cfbuyqty`, `cfsellqty`, `cfbuyamount`, `cfsellamount`, `buyavgprice`, `sellavgprice`, `avgnetprice`, `netvalue`, `netqty`, `totalbuyvalue`, `totalsellvalue`, `cfbuyavgprice`, `cfsellavgprice`, `totalbuyavgprice`, `totalsellavgprice`, `netprice`, `buyqty`, `sellqty`, `buyamount`, `sellamount`, `pnl`, `realised`, `unrealised`, `ltp`, `close`) VALUES
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:06:51', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EC850D6350>', '2023-07-26 22:06:51', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EC850D6350>', '2023-07-26 22:06:51', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:06:52', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:09:14', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020980266380>', '2023-07-26 22:09:14', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020980266380>', '2023-07-26 22:09:14', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:09:21', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:10:47', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002194B936380>', '2023-07-26 22:10:47', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000002194B936380>', '2023-07-26 22:10:47', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:10:48', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:15:34', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020853556380>', '2023-07-26 22:15:34', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020853556380>', '2023-07-26 22:15:34', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:15:34', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-26 22:17:29', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020DBC136320>', '2023-07-26 22:17:29', '52974', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2345700CE', 'XX', '45700.0', 'CE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '338.85', '390.98', '0.00', '1563.75', '0', '10165.50', '11729.25', '0.00', '0.00', '338.85', '390.98', '0.00', '30', '30', '10165.50', '11729.25', '1563.90', '1563.90', '-0.00', '396.0', '320.9'),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000020DBC136320>', '2023-07-26 22:17:29', '52987', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'INTRADAY', 'BANKNIFTY27JUL2346300PE', 'XX', '46300.0', 'PE', '27JUL2023', '15', '0', '0', '0.00', '0.00', '410.45', '409.60', '0.00', '-25.50', '0', '12313.50', '12288.00', '0.00', '0.00', '410.45', '409.60', '0.00', '30', '30', '12313.50', '12288.00', '-25.50', '-25.50', '0.00', '313.0', '446.95'),
('', 'Failed', '_noobj', '2023-07-26 22:17:30', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 12:35:36', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000024D03BB60B0>', '2023-07-28 12:35:37', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '160.20', '-425.40', '585.60', '757.85', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 12:35:40', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 12:49:03', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000247498160E0>', '2023-07-28 12:49:04', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '538.20', '-425.40', '963.60', '770.45', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 12:49:05', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 12:56:02', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000021B805A6110>', '2023-07-28 12:56:02', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '824.70', '-425.40', '1250.10', '780.0', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 12:56:03', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 12:57:35', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000201D3B06050>', '2023-07-28 12:57:35', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '404.70', '-425.40', '830.10', '766.0', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 12:57:36', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 12:59:09', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000019E5DC26050>', '2023-07-28 12:59:09', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '314.70', '-425.40', '740.10', '763.0', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 12:59:10', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 13:12:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000239C072FFD0>', '2023-07-28 13:12:56', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '379.20', '-425.40', '804.60', '765.15', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 13:13:01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 13:16:24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000025969D660B0>', '2023-07-28 13:16:25', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '211.20', '-425.40', '636.60', '759.55', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 13:16:27', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 13:20:28', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x0000027F3EB36080>', '2023-07-28 13:20:30', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '224.70', '-425.40', '650.10', '760.0', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 13:20:31', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 14:30:28', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001B1675D8520>', '2023-07-28 14:30:29', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '311.70', '-425.40', '737.10', '762.9', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 14:30:30', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 14:39:07', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x00000112C5BF8F70>', '2023-07-28 14:39:08', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '1037.70', '-425.40', '1463.10', '787.1', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 14:39:10', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 14:53:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('sridharan', 'Success', '<SmartApi.smartConnect.SmartConnect object at 0x000001EBC4F49060>', '2023-07-28 14:54:01', '60599', 'BANKNIFTY', 'OPTIDX', '1.00', '1.00', '1.00', '1.00', '2', '-1', '1', 'NFO', 'CARRYFORWARD', 'BANKNIFTY31AUG2345800PE', 'XX', '45800.0', 'PE', '31AUG2023', '15', '0', '0', '0.00', '0.00', '738.33', '724.15', '752.50', '-22575.00', '30', '44299.50', '21724.50', '0.00', '0.00', '738.33', '724.15', '752.50', '60', '30', '44299.50', '21724.50', '-286.80', '-425.40', '138.60', '742.95', '583.45'),
('', 'Failed', '_noobj', '2023-07-28 14:54:04', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:12:46', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:12:48', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:16:32', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:16:33', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:32:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:32:55', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:40:53', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:40:54', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:43:16', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:43:17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:44:39', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:44:40', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:46:56', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:46:57', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:50:36', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:50:37', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('chetan londhe', 'Failed', 'chetan123_noobj', '2023-07-28 15:52:01', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
('', 'Failed', '_noobj', '2023-07-28 15:52:02', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `program_status`
--

CREATE TABLE `program_status` (
  `id` int(11) NOT NULL,
  `status` datetime NOT NULL,
  `indexname` varchar(100) DEFAULT NULL,
  `optionexpiry` datetime DEFAULT NULL,
  `calloptionsymbol` varchar(100) DEFAULT NULL,
  `putoptionsymbol` varchar(100) DEFAULT NULL,
  `createdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tls_error_log`
--

CREATE TABLE `tls_error_log` (
  `id` int(200) NOT NULL,
  `createdate` datetime NOT NULL,
  `error` varchar(500) NOT NULL,
  `validation` varchar(200) DEFAULT NULL,
  `sql_query` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tls_error_log`
--

INSERT INTO `tls_error_log` (`id`, `createdate`, `error`, `validation`, `sql_query`) VALUES
(1, '2023-07-27 08:57:30', 'invalid access token', 'token is not available for today', NULL),
(2, '2023-07-27 08:58:21', 'invalid access token', 'token is not available for today', NULL),
(3, '2023-07-28 12:01:56', 'invalid access token', 'token is not available for today', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `trading_strategy`
--

CREATE TABLE `trading_strategy` (
  `id` int(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `createdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(100) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `createdate` datetime NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `fullname`, `username`, `password`, `createdate`, `email`) VALUES
(1, 'Chetan Arvind Londhe', 'chetan@SL', '$2b$12$btYAcPht5Tprmc5WAdYpUeA5OJMD8HUIi.5g.fY97IxPuIKHPUYqi', '2023-07-11 17:28:34', 'chetanlondhe1112@gmail.com'),
(2, 'umesh londhe', 'umesh@SL', '$2b$12$VE8hyNkgWUR41hKn5DbM5Oq7SUuMQCUl6RS5c6nNjwolA94y7cOgy', '2023-07-12 16:51:10', 'umeshlondhe1112@gmail.com'),
(3, 'ggffgcghcfhfhgcfgfh', 'hubb@SS', '$2b$12$4wcUugl/VADyELqjV3BT2.wr61wrsk/3NQoUi8dvAsV0zm4vMIccW', '2023-07-26 12:55:51', 'hgfhgchfg@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `zerodha_creds`
--

CREATE TABLE `zerodha_creds` (
  `id` bigint(20) DEFAULT NULL,
  `api_key` text DEFAULT NULL,
  `api_secret` text DEFAULT NULL,
  `access_token` text DEFAULT NULL,
  `createdate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `zerodha_creds`
--

INSERT INTO `zerodha_creds` (`id`, `api_key`, `api_secret`, `access_token`, `createdate`) VALUES
(1, 'm8lqe0lp92mndpzw', 'lhg6sx4g3etshuleybete974h3voo8gz', 'x5JPPV2hBTj40mYEEr3Nzmh26arGfpIB', '2023-07-28 12:03:06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- Indexes for table `defaults_log`
--
ALTER TABLE `defaults_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `entryconditions`
--
ALTER TABLE `entryconditions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_history`
--
ALTER TABLE `login_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `program_status`
--
ALTER TABLE `program_status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tls_error_log`
--
ALTER TABLE `tls_error_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trading_strategy`
--
ALTER TABLE `trading_strategy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `defaults_log`
--
ALTER TABLE `defaults_log`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `entryconditions`
--
ALTER TABLE `entryconditions`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `login_history`
--
ALTER TABLE `login_history`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tls_error_log`
--
ALTER TABLE `tls_error_log`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `trading_strategy`
--
ALTER TABLE `trading_strategy`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
