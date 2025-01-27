import sqlite3




def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    img_name TEXT
    )    
    ''')
    connection.commit()
    connection.close()

def set_product(title,description,price,img_name):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (title,description,price, img_name) VALUES (?,?,?,?)',
                   (f'{title}',f'{description}',f'{price}',f'{img_name}'))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    total = cursor.fetchall()
    connection.close()
    return total


# initiate_db()
# set_product("Product_A",'Самый лучший комплекс_A',100, "1.jpg")
# set_product("Product_B",'Самый лучший комплекс_B',200, "2.jpg")
# set_product("Product_C",'Самый лучший комплекс_C',300, "3.jpg")
# set_product("Product_D",'Самый лучший комплекс_D',400, "4.jpg")