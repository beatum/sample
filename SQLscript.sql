-- SQL Script
-- Created by Ivan Semernyakov <direct@beatum-group.ru> оn July 2016
-- Создать 4 таблицы, 3 из которых наполнить имеющимися данными создать
-- запрос на обход 3 таблиц и записать полученный результат в 4-ю таблицу


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- База данных: `sample_query`
--

CREATE DATABASE IF NOT EXISTS `sample_query` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `sample_query`;

-- --------------------------------------------------------

--
-- Структура таблицы `table_one`
--

DROP TABLE IF EXISTS `table_1`;
CREATE TABLE IF NOT EXISTS `table_1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `salary_year` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;


--
-- Дамп данных таблицы `table_1`
--

INSERT INTO `table_1` (`id`, `name`, `surname`, `salary_year`) VALUES
(1, 'John', 'Terrible', 11000),
(2, 'Maggie', 'Woodstock', 15000),
(3, 'Joel', 'Muegos', 22000),
(4, 'Jeroen', 'van Kapf', 44000);

-- --------------------------------------------------------

--
-- Структура таблицы table_2
--

DROP TABLE IF EXISTS `table_2`;
CREATE TABLE `table_2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `month` date NOT NULL,
  `taxes` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы table_2
--

INSERT INTO `table_2` (`id`, `month`, `taxes`, `employee_id`) VALUES
(1, '01.01.15', 250, 1),
(2, '01.02.15', 267, 1),
(3, '01.01.15', 300, 2),
(4, '01.02.15', 350, 2),
(5, '01.01.15', 245, 3),
(6, '01.02.15', 356, 3),
(7, '01.01.15', 246, 4),
(8, '01.02.15', 356, 4),
(9, '01.03.15', 412, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `table_3`
--

DROP TABLE IF EXISTS `table_3`;
CREATE TABLE IF NOT EXISTS `table_3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `internal_number` int(11) NOT NULL,
  `position` varchar(30) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Дамп данных таблицы `table_3`
--

INSERT INTO `table_3` (`id`, `internal_number`, `position`, `employee_id`) VALUES
(1, 32894, 'Manager', 1),
(2, 23409, 'Top Manager', 2),
(3, 23908, 'CEO', 3),
(4, 128, 'Board Chairman', 4);

-- --------------------------------------------------------

--
-- Структура таблицы `table_4`
--

DROP TABLE IF EXISTS `table_4`;
CREATE TABLE IF NOT EXISTS `table_4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `internal_number` int(11) NOT NULL,
  `position` varchar(80) NOT NULL,
  `name_surname` varchar(80) NOT NULL,
  `salary_month` varchar(80) NOT NULL,
  `tax` int(11) NOT NULL,
  `month` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Выборка и запись данных из предыдущих таблиц в `table_4`
--

-- Выводим все уникальные записи из таблиц `table_1`, `table_2`, `table_3`,
-- и записываем их в `table_4`, что вполне удовлетворяет требованиям TЗ

INSERT INTO `table_4` (`internal_number`, `position`, `name_surname`,
`salary_month` , `tax`, `month`) SELECT DISTINCT `table_3`.`internal_number` ,
`table_3`.`position` , CONCAT (`table_1`.`name`, ' ' , `table_1`.`surname`)
AS `name_surname` , CONCAT (`table_1`.`salary_year`, ' ' , `table_2`.`month`)
AS `salary_month` ,  `table_2`.`taxes`, `table_2`.`month` FROM
`table_1` , `table_2` , `table_3` LIMIT 0 , 30

-- --------------------------------------------------------