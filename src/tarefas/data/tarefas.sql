DROP DATABASE IF EXISTS `tarefas`;

CREATE DATABASE IF NOT EXISTS `tarefas`;

USE `tarefas`;

DROP TABLE IF EXISTS `tarefas`;

CREATE TABLEIF NOT EXISTS `tarefa` (
    `id_tarefa` BIGINT NOT NULL PRIMARY KEY,
    `titulo_tarefa` VARCHAR(100) NOT NULL,
    `data_tarefa` DATETIME NULL
);