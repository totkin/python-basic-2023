/*

Enter custom T-SQL here that would run after SQL Server has started up.

*/

CREATE DATABASE AODATA
GO
Create login [nomaduser] with password='pa$$w0rd'
Create user [nomaduser] for login [nomaduser]
Grant Execute to [nomaduser]
GRANT CONNECT TO [nomaduser]
ALTER LOGIN nomad ENABLE
GO

CREATE SCHEMA [nomad]
GO