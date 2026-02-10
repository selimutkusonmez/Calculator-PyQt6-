import sqlite3
import pandas as pd
import os
from config import DB_PATH

login_sqlite = sqlite3.connect(DB_PATH)
login_sqlite_cursor = login_sqlite.cursor()
user_data = pd.read_sql("SELECT username,password FROM user_data",login_sqlite)
    
usernames = list(user_data["username"].values)
passwords = list(user_data["password"].values)

def login(username_input,password_input):
    if username_input == "" and password_input == "":

        return (0,"Please Enter A Valid Username And Password")
    
    if username_input in usernames:

        username_index = usernames.index(username_input)

        if password_input == passwords[username_index]:

            return (1,"Login Succesful")

        elif password_input == "":

            return (2,"Please enter a valid password")
        
        elif password_input != passwords[username_index]:

            return (3,"Username or Password wrong!")
        
        elif password_input not in passwords:

            return (4,"Username or Password wrong!")

    elif username_input not in usernames:
        
        return (5,"User Not Found")