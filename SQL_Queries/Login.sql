-- Seller Logins
DELETE FROM LoginInfo WHERE ID = "S01";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("S01", "Faaiq", "MM2001");

DELETE FROM LoginInfo WHERE ID = "S02";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("S02", "Haashim", "Phupo");

DELETE FROM LoginInfo WHERE ID = "S03";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("S03", "Sarah", "HTML");

-- Warehouse Logins
DELETE FROM LoginInfo WHERE ID = "W01";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("W01", "Lahore", "123");

DELETE FROM LoginInfo WHERE ID = "W02";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("W02", "Islamabad", "456");

DELETE FROM LoginInfo WHERE ID = "W03";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("W03", "Multan", "789");

DELETE FROM LoginInfo WHERE ID = "W04";
INSERT INTO LoginInfo(ID, userName, userPassword)
VALUES ("W04", "Karachi", "abc");