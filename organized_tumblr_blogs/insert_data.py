import sqlite3

def insert_data():
    
    # Connect to database
    connection = sqlite3.connect("tumblr_blogs.db")
    
    #Create a Cursor
    c = connection.cursor()
    
    connection.commit()
    connection.close()
    
if __name__ == "__insert_data":
    insert_data()