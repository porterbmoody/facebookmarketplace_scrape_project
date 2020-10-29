# %%
import mysql.connector
import pandas as pd


config = {"user":'root', 
            "password":'Yoho1mes',
            "host":'127.0.0.1',
            "database":"cars"}
dat1 = pd.read_csv("data/cars.csv")
# dat1.fillna(None, inplace = True)
dat1 = dat1.where(pd.notnull(dat1), None)
columns_titles = ['title', 'year', 'miles', 'price', 'link', 'location']
dat1 = dat1.reindex(columns=columns_titles)
dat = dat1

# %%
def main():
    mydb = mysql.connector.connect(**config, auth_plugin='mysql_native_password')
    mycursor2 = mydb.cursor()
    mycursor1 = mydb.cursor()
    mycursor = mydb.cursor()


    cols = "`,`".join([str(i) for i in dat.columns.tolist()])
    print(cols)

    ### query epic data 
    query = "SELECT * FROM cars WHERE year >= 2008 AND miles <= 150000 AND price <= 4500;"
    mycursor1.execute(query)
    data = []
    for row in mycursor:
        data.append(row)
    dat_epic_before = pd.DataFrame(data, columns = ['id','title','year','miles','price','link','location'])

    ##### insert new data
    for i, row in dat.iterrows():
        insert_statement = "INSERT INTO `cars` (`id`,`" + cols + "`) VALUES (DEFAULT," + "%s," * (len(row)-1) + "%s)"
        # statement_insert = "INSERT INTO `cars` (`" + cols + "`) VALUES (" + "%s," * (len(row)-1) + "%s)"
        # print(insert_statement, tuple(row))
        mycursor.execute(insert_statement, tuple(row))
        mydb.commit()

    ################################ deleting duplicate rows sql
    # title, year, miles, price, link, location
    mysql_commands =    ["USE cars;",
                        "CREATE TEMPORARY TABLE unique_cars (`id` INT NOT NULL AUTO_INCREMENT,  `title` VARCHAR(100) NULL,  `year` FLOAT(20) NULL,  `miles` FLOAT NULL,  `price` FLOAT(20) NULL,  `link` VARCHAR(100) NULL,  `location` VARCHAR(60) NULL,  PRIMARY KEY (`id`),  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);",
                        "INSERT INTO unique_cars SELECT MIN(id),title,year, miles,price,link,location FROM cars GROUP BY title,year, miles,	price,link,location;",
                        "TRUNCATE cars;",
                        "INSERT INTO cars SELECT id,title,year, miles,price,link,location FROM unique_cars;",
                        "DROP TABLE unique_cars;"]
    for command in mysql_commands:
        print(command)
        mycursor.execute(command)
        mydb.commit()
    
    ### query epic data 
    query = "SELECT * FROM cars WHERE year >= 2008 AND miles <= 150000 AND price <= 4500;"
    mycursor2.execute(query)
    data = []
    for row in mycursor:
        data.append(row)
    dat_epic_after = pd.DataFrame(data, columns = ['id','title','year','miles','price','link','location'])
    print("Length before: ", len(dat_epic_before), "Length after: ", len(dat_epic_after))
    print(dat_epic_before)
    print()
    print(dat_epic_after)
    


    mydb.close()
    ### testing
    # statement_insert = '''"INSERT INTO `cars` (`title`,`price`,`link`,`location`,`miles`) VALUES ('2002 Ford F-150 Short Bed 4D',2500,'https://www.facebook.com/marketplace/item/1291798527839337/','Pueblo, CO',200000.0)" % (,2500,,,,2002.0)'''


#%%

if __name__ == "__main__":
    main()
# %%