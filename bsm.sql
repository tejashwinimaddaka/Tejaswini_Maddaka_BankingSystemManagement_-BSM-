create database BankingSystem;
use BankingSystem;

create table Customers(
customer_id int primary key identity(001,1),
first_name varchar(30) ,
last_name varchar(30) , 
DOB date , 
email varchar(100) , 
phone_number varchar(100) ,
address varchar(50) 
);

create table Accounts(
account_id varchar(20) primary key,
customer_id int, 
account_type varchar(20),
balance decimal(20,2),
foreign key(customer_id) references Customers(customer_id) 
);

create table Transactions(
transaction_id varchar(100) primary key,
account_id varchar(20),
transaction_type varchar(20),
amount decimal(8,2), transaction_date date,
foreign key (account_id) references Accounts(account_id)
);

insert into Customers (first_name,last_name,DOB,email,phone_number,address)
values
('Anne','John','2001-10-12', 'annejohn@gmail.com','9852654753','14/480,Church street,Miami'),
('Emma','Thomas','1998-01-08', 'emma@gmail.com','8695756984','1C-10, Lakeview,Portland'),
('Noah','Olivia','2000-09-04', 'olivia12@gmail.com','789654357','12-B,Grifender street,New York'),
('David','Son','1999-02-05', 'david8@gmail.com','7895651423','63/1,Johnson street,San Jose'),
('Martin','Rich','2002-04-06', 'martinz@gmail.com','9563285412','56/9,Wainut,Tucson'),
('Blue','Harris','1997-10-03', 'blue97@gmail.com','6859352946','35-D,Main street,Fort Worth'),
('Kevin','Jose','2003-07-12', 'kevinjose@gmail.com','8534976581','89/7,Cedar,Honolulu'),
('Pat','Carol','2001-04-09', 'patcarol@gmail.com','7689572612','475,Maple,Omaha'),
('Amy','Mathew','2004-10-12', 'amymathew7@gmail.com','7654892642','165/1B,Kingston,Las Vegas'),
('Laura','James','1998-03-05', 'laurajames9@gmail.com','9556411791','164,Second street,Phoenix');

insert into Accounts (account_id,customer_id,account_type,balance)
values
(4568794568,1,'savings',0.00),
(2563597841,2,'current',1900.00),
(8659145286,3,'current',7856.00),
(7568246648,4,'savings',-1500.00),
(2487965441,5,'zero_balance',5600.00),
(3774662889,6,'savings',47080.90),
(4757678441,7,'zero_balance',148300.00),
(5896423598,8,'savings',165000.00),
(5221440003,9,'zero_balance',2000.00),
(2336640078,10,'current',38250.00);

insert into Transactions (transaction_id, account_id,transaction_type,amount,transaction_date)
values
('T7609182336333033272666',4568794568,'withdrawal',10000.00,'2023-12-30'),
('T1235682336333033272456',2563597841,'deposit',250000.90,'2022-06-12'),
('T9409145897333033272898',8659145286,'transfer',11060.00,'2021-11-03'),
('T2709182336999993272753',4568794568,'deposit',120050.50,'2024-06-22'),
('T2129182336333035654159',2487965441,'transfer',1600.00,'2020-03-13'),
('T9809182336347326272369',4568794568,'withdrawal',75000.00,'2023-02-07'),
('T2409182336333033272666',4757678441,'deposit',29500.00,'2024-07-11'),
('T5409182336396458272147',4568794568,'deposit',50000.00,'2024-06-22'),
('T3209182336362351272852',5221440003,'withdrawal',90800.00,'2020-10-28'),
('T4809182336316598272862',2487965441,'deposit',346120.00,'2024-12-01');

select * from Customers;
select * from Accounts;
select * from Transactions;