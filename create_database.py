import sqlite3

def create_database():
    
        #connect/create database
    connection = sqlite3.connect("tumblr_blogs.db")
    c = connection.cursor()
    
    #Create an art blog table
    c.execute("""CREATE TABLE  IF NOT EXISTS
        art_blogs (
        blog_name text, 
        url_link text
        )
              """)
    
    
    # Commit database
    connection.commit()
    
    connection.close()
    
if __name__ == "__create_database__":
    create_database()