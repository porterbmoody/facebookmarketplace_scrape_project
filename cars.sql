USE cars; 
-- create temp table
CREATE TEMPORARY TABLE unique_cars (`id` INT NOT NULL AUTO_INCREMENT,  `title` VARCHAR(100) NULL,  `year` FLOAT(20) NULL,  `miles` FLOAT NULL,  `price` FLOAT(20) NULL,  `link` VARCHAR(100) NULL,  `location` VARCHAR(60) NULL,  PRIMARY KEY (`id`),  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
-- insert unique data into temp table
INSERT INTO unique_cars SELECT 	MIN(id),title,year, miles,price,link,location FROM cars GROUP BY title,year, miles,	price,link,location;
-- insert newly nonduplicate rows into old table
TRUNCATE cars;
INSERT INTO cars SELECT id,title,year, miles,price,link,location FROM unique_cars;
DROP TABLE unique_cars;
SELECT * FROM cars;