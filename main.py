
from tkinter import *
import sqlite3
import csv

def main():
    
    def submit():
        connect = sqlite3.connect("tumblr_blogs.db")
        c = connect.cursor()
        
        # Insert Into Table
        c.execute("INSERT INTO art_blogs VALUES (:art_blog_name, :art_blog_url)",
                  {
                      'art_blog_name': art_blog_name.get(),
                      'art_blog_url': art_blog_url.get()
                  }
                  
                  )
        
        #Commit Data
        connect.commit()
    
        connect.close()
        
        art_blog_name.delete(0, END)
        art_blog_url.delete(0, END)
        
    def query():
        connect = sqlite3.connect("tumblr_blogs.db")
        c = connect.cursor()
        
        #Query the database
        c.execute("SELECT *, oid FROM art_blogs")
        records = c.fetchall()
        #print(records)
        
        #Loop through results
        print_records = ""
        for record in records:
            print_records +=  str(record[2]) + "\t" + str(record[0]) + "\t"  + str(record[1]) +  "\n"
            
        query_label = Label(root, text = print_records)
        query_label.grid(row = 1, column = 2, columnspan = 2)
        
        #Commit Data
        connect.commit()
    
        connect.close()
        
    def delete():
        connect = sqlite3.connect("tumblr_blogs.db")
        c = connect.cursor()

        # Delete a Record
        c.execute("DELETE from art_blogs WHERE oid = " + select_box.get())
        
        #Commit Data
        connect.commit()
    
        connect.close()
        
    def save():
        connect = sqlite3.connect("tumblr_blogs.db")
        c = connect.cursor()
        
        record_id = select_box.get()
        
        c.execute("""
                  UPDATE art_blogs SET 
                  art_blog_name = :name, 
                  art_blog_url = :url,
                  
                  WHERE oid = :oid""", 
                {
                    'name': art_blog_name_update.get(),
                    'url': art_blog_url_update.get(),
                    
                    'oid': record_id
                }) 
        
        connect.commit()
        connect.close()
        
        editor.destroy()
        
    def update():
        global editor
        # Open New Window
        editor = Tk()
        editor.title("Update a Tumblr Blog")
        editor.geometry("400x400")
        
        # Connect to database
        connect = sqlite3.connect("tumblr_blogs.db")
        c = connect.cursor()
        
        record_id =  select_box.get()
        c.execute("SELECT * FROM art_blogs WHERE oid = " + record_id)
        records = c.fetchall()
        
        # Global so other functions can use these
        global art_blog_name_update
        global art_blog_url_update
        
        #Textboxes and Labels
        art_blog_name_update = Entry(editor, width = 30)
        art_blog_name_update.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
        
        art_blog_url_update = Entry(editor, width = 30)
        art_blog_url_update.grid(row = 1, column = 1, padx = 20)
        
        art_blog_name_label = Label(editor, text = "Blog Name")
        art_blog_name_label.grid(row = 0, column = 0, pady = (10, 0))
    
        art_blog_url_label = Label(editor, text = "Blog URL")
        art_blog_url_label.grid(row = 1, column = 0)
        
        update_btn = Button(editor, text = "Save Blog", command = save)
        update_btn.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 145)
    
        for record in records:
            art_blog_name_update.insert(0, record[0])
            art_blog_url_update.insert(0, record[1])
        
       
        
        
        
        #Commit Data
        connect.commit()
    
        connect.close()
        
        
        
    
    # Tkinter Window
    root = Tk()
    root.title("Tumblr Blog Database")
    root.geometry("800x400")
    
    # Database
    connect = sqlite3.connect('tumblr_blogs.db')
    c = connect.cursor()
    
    # Create Table
    c.execute("""
              CREATE TABLE IF NOT EXISTS art_blogs (
                art_blog_name text, 
                art_blog_url text 
              )
              
              """)
    
    # Text Boxes
    art_blog_name = Entry(root, width = 30)
    art_blog_name.grid(row = 0, column = 1, padx = 20, pady = (10, 0))
    
    art_blog_url = Entry(root, width = 30)
    art_blog_url.grid(row = 1, column = 1, padx = 20)
    
    select_box = Entry(root, width = 30)
    select_box.grid(row = 9, column = 1)
    
    #Text Box Labels
    art_blog_name_label = Label(root, text = "Blog Name")
    art_blog_name_label.grid(row = 0, column = 0, pady = (10, 0))
    
    art_blog_url_label = Label(root, text = "Blog URL")
    art_blog_url_label.grid(row = 1, column = 0)
    
    delete_box_label = Label(root, text = "Select Blog (Number ID)")
    delete_box_label.grid(row = 9, column = 0)
    
    # Submit Button
    submit_btn = Button(root, text = "Add Record to Database", command = submit)
    submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)
    
    # Query Button
    query_btn = Button(root, text = "Show Records", command = query)
    query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 137)
    
    # Delete Button
    delete_btn = Button(root, text = "Delete Record", command = delete)
    delete_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 136)
    
    # Update Button
    update_btn = Button(root, text = "Edit Record", command = update)
    update_btn.grid(row = 12, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 145)
    
    
    #Commit Data
    connect.commit()
    
    connect.close()
    
    root.mainloop()


if __name__ == '__main__':
    main()
    
    