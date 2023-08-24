--create table authtors
--(id serial primary key,
--username varchar unique not null,
--email varchar unique)
--
--select * from authtors
--
--insert into authtors (username,email)
--values ('jhon','jhon@fgfg.ru')
--
select * from users


drop table users
commit
--
--

create table posts
(id serial primary key,
title varchar(200) not null,
body text not null default '',
raw_meta jsonb,
author_id int not null constraint for_key_3939
references authtors(id)
)

commit