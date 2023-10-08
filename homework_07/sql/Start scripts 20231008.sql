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


CREATE SCHEMA [nomad] AUTHORIZATION [nomaduser]


alter USER [nomaduser] WITH DEFAULT_SCHEMA =[nomad]


GRANT CONNECT TO [nomaduser]


GRANT INSERT ON SCHEMA :: nomad TO nomaduser


select CURRENT_USER 


ALTER LOGIN nomad ENABLE


SELECT pr.principal_id
    ,pr.name
    ,pr.type_desc
    ,pr.authentication_type_desc
    ,pe.state_desc
    ,pe.permission_name  
FROM sys.database_principals AS pr  
INNER JOIN sys.database_permissions AS pe ON pe.grantee_principal_id = pr.principal_id;




Create login nomaduser with password='pa$$w0rd';
Create user nomaduser for login nomaduser;
Grant Execute to nomaduser