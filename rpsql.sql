create database if not exists RetailPlatform;

use retailplatform;

create table user_details (uid varchar(10) not null unique primary key, uname varchar(30) not null, umail varchar(30) not null, uph bigint not null unique, upwd varchar(20) not null);

select * from user_details;

create table merchant_details (merid varchar(10) not null unique primary key, mname varchar(30) not null unique, mermail varchar(30), merpwd varchar(20) not null);

create table inventory (prodid varchar(10) not null unique primary key, prodname varchar(30) not null, prodqty int, prodseller varchar(10) not null, prodprice float not null);

create table upayments (uid int not null unique primary key, uname varchar(30), ubalance float);

alter table user_details add column (uaddress varchar(40) not null);

alter table user_details add column uid varchar(10) not null unique primary key first;


alter table user_details modify column uph bigint not null unique;

drop table user_details;