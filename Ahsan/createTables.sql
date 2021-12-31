-- create tables inside database LMS
-- drop database  if exists Logi_database;
drop database if exists logi_database;
create database if not exists logi_database;
USE logi_database;

-- DROP TABLE IF EXISTS SellerProduct;
-- CREATE TABLE SellerProduct (sellerID char(10),
--                             productID char(10),
--                             weightPrice decimal(10,2),
--                             deliveryPrice decimal(10,2),
--                             sellerPrice decimal(10,2),
--                             CONSTRAINT identifier PRIMARY KEY (sellerID, productID));
-- DESCRIBE SellerProduct;

-- DROP TABLE IF EXISTS ClientProduct;
-- CREATE TABLE ClientProduct (clientPhoneNumber char(11),
--                             productID char(10),
--                             deliveryAddress char(70),
--                             CONSTRAINT identifier PRIMARY KEY (clientPhoneNumber, productID));
-- DESCRIBE ClientProduct;

DROP TABLE IF EXISTS LoginInfo;
CREATE TABLE LoginInfo (ID char(10),
                        userName char(15),
                        userPassword char(64),     
                        CONSTRAINT uniqueness UNIQUE (userName),
                        CONSTRAINT primary_login PRIMARY KEY (userName));
                        -- CONSTRAINT primary_login PRIMARY KEY (ID));
-- DESCRIBE LoginInfo;

-- CONSTRAINT identifier PRIMARY KEY (ID)

DROP TABLE IF EXISTS Client;
CREATE TABLE Client(phoneNumber char(15),
                    clientAddress char(70),
                    city char(15),
                    CONSTRAINT identifier PRIMARY KEY (phoneNumber));
-- DESCRIBE Client;

DROP TABLE IF EXISTS Seller;
CREATE TABLE Seller(sellerID char(15),
                    sellerName char(30),
                    phoneNumber char(15),
                    city char(15),
                    CONSTRAINT identifier PRIMARY KEY (sellerID));
-- DESCRIBE Seller;

DROP TABLE IF EXISTS Warehouse;
CREATE TABLE Warehouse (warehouseID char(15),
                        city char(15),
                        CONSTRAINT identifier PRIMARY KEY (warehouseID));
-- DESCRIBE Warehouse;

DROP TABLE IF EXISTS Product;
CREATE TABLE Product   (trackingID char(15),
                        sellerID char(15),
                        warehouseID char(15),
                        currentLocation char(30),
                        productRoute char(30),
                        paymentStatus int,
                        price decimal(10,2),
                        clientPhoneNumber char(15),

                        CONSTRAINT identifier PRIMARY KEY (trackingID));
-- DESCRIBE Product;

DROP TABLE IF EXISTS Rider;
CREATE TABLE Rider (riderID char(15),
                    riderName char(30),
                    phoneNumber char(15),
                    warehouseID char(15),
                    productID char(15),
                    CONSTRAINT identifier PRIMARY KEY (riderID));
-- DESCRIBE Rider;
