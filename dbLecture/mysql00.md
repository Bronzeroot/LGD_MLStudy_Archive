# Create Table

> mysql> CREATE TABLE topic(
>    ->   id INT(11) NOT NULL AUTO_INCREMENT,
>    ->   title VARCHAR(100) NOT NULL,
>    ->   description TEXT NULL,
>    ->   creeated DATETIME NOT NULL,
>    ->   author VARCHAR(30) NULL,
>    ->   profile VARCHAR(100) NULL,
>    ->   PRIMARY KEY(id));

** ALTER TABLE topic CHANGE creeated created datetime;

# Insert table

> INSERT INTO topic(title,description,creeated,author,profile) VALUES('MySQL','MySQL is ...', NOW(),'egoing','developer');

> SELECT * FROM topic;