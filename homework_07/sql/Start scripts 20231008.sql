use AODATA

create schema REPORT;

create table REPORT.test20231008(
id int,
name nvarchar(255))

INSERT INTO AODATA.REPORT.test20231008
(id, name)
VALUES(5, 'test name');

INSERT INTO AODATA.REPORT.test20231008
(id, name)
VALUES(6, 'another name');

select * from AODATA.REPORT.test20231008


CREATE SCHEMA [nomad] AUTHORIZATION [nomaduser@s-sql5]


alter USER [nomaduser] WITH DEFAULT_SCHEMA =[nomad]