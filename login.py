from tkinter import *   #importing tkinter module
def Login_check():      #function to check if login details are correct
    try:                #if file with the provided username exists

        file = open(username_in.get()+".txt","r") #To open the file
        username_check = file.readline()          #To read the username from the file
        password_check = file.readline()          #To read the password from the file
        
        us = username_in.get() + "\n"             #newline character added to simplify the comparision

        #input username and passwords are compared below with the registered data
        if us == username_check and password_check == password_in.get():
            Label(screen2, text = "Welcome", fg = "green").pack()
        else:
            Label(screen2, text = "Incorrect Password", fg = "red").pack()
        file.close()


    except IOError:       #if the file does not exist
        Label(screen2, text = "Invaid Username", fg = "red").pack()
    
def regsiter_user():                    #Function to register new username
    username_info = username.get()      #Getting username from textvariable of Label
    password_info = password.get()      #Getting Password from textvariable of Label

    file = open(username_info+".txt","w")   #creating a new file with the given username
    file.write(username_info+"\n")          #Writing the username data
    file.write(password_info)               #Writing the password data
    file.close()                            #closing the file

    username_entry.delete(0,END)            #Clearing the data field
    password_entry.delete(0,END)            #Clearing the data field

    Label(screen1, text = "Registrartion Successfull!!", fg = "green").pack()

def register():                 #function for register button

    global screen1
    screen1 = Toplevel(screen)  #Definig new screen1 on the top of screen
    screen1.title("Register")   #Title
    screen1.geometry("300x250") #Size
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please Enter Details *").pack() #Label is used to show text on screen
    Label(screen1, text = "").pack()                       
    Label(screen1, text = "Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    Label(screen1, text = "Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()

    Button(screen1, text = "Register", command = regsiter_user).pack()  #Button is used to execute certain commands
    

def login():                       #Function for login command is same as above register
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")


    Label(screen2, text = "Please enter your credentils").pack()
    Label(screen2, text = "").pack()
    global username_in
    global password_in
    username_in = StringVar()
    password_in = StringVar()
    
    Label(screen2, text = "Username").pack()
    Entry(screen2, textvariable = username_in).pack()

    Label(screen2, text = "Password").pack()
    Entry(screen2, textvariable = password_in).pack()

    Button(screen2, text = "Login", command = Login_check).pack()

def main_screen():    #The main function
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300" , height = "2" , font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30" , height = "2", command = login  ).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30" , height = "2", command = register ).pack()

    screen.mainloop()
main_screen()
    

