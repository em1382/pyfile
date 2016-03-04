######### ##    ## ######### ##  ##       ########
##     ## ##    ## ##        ##  ##       ##
##     ## ##    ## ##        ##  ##       ##
######### ######## ########  ##  ##       #######
##           ##    ##        ##  ##       ##
##           ##    ##        ##  ##       ##
##           ##    ##        ##  ##       ##
##           ##    ##        ##  ######## ######## 
    
# Pyfile, release 1.0
# Author: Ellis Madagan

# Pyfile is done! A final project for CIS 181: Programming I,
# Pyfile is a useful automated file organizer.
# Point it to a messy directory, and it sorts files by type
# into respective subdirectories!

import os       # For traversing directories
import shutil   # For move files
import sqlite3  # For storage of the file names
from tkinter import * # For GUI

class PyFileOrganizer(Frame):

    # Set it up

    def __init__(self, master=None):
        
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    # Create all Tkinter widgets

    def createWidgets(self):
        
        self.QUIT = Button(self, text="Quit", fg="red", bg="#ffffff",
                           command=root.destroy).grid(row=0, column=3, sticky=E,
                                                      padx=5, pady=5)
        
        self.dir_entry_label = Label(self, text="Path:").grid(row=0, column=0, sticky=E,
                                                              padx=5, pady=5)
        self.pathStr = StringVar()
        self.dir_entry = Entry(self, textvariable=self.pathStr).grid(row=0, column=1, sticky=E,
                                                                     padx=5, pady=5)

        self.sort_files = Button(self, fg="#336699", bg="#ffffff",
                                 text="Sort", command=self.sort).grid(row=0, column=2, sticky=E,
                                                                      padx=5, pady=5)

        self.output = Listbox(self, width=40)
        self.output.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

    def sort(self):
        
        #sortFiles("C:\\Users\\Ellis\\Desktop\\Mock", self.output)
        sortFiles(self.pathStr.get(), self.output) #DANGER! BE CAREFUL WITH THIS FUNCTION!

########################################################################
####   This section was for an un-implemented databasing system     ####
####   which would add the file name and exts. to a database,       ####
####   allowing for a lookup of the proper file names. It's dead.   ####
########################################################################

##def updateDatabase(ext):
    
    
##def createDatabase():
##    conn = sqlite.connect("fileorg.db")
##    c = conn.cursor()
##
##    c.execute('''CREATE TABLE extensions(id int PRIMARY KEY, extension text, filetype text)''')
##    c.commit()
##    conn.close()

########################################################################
########################################################################
       
# This function iterates through all files in a given directory,
# then sorts those files into folders based on type. (Output is a Listbox)
def sortFiles(rootDir, output):

    output.delete(0, END)

    for directory, subdir, files in os.walk(rootDir):
        
        for file in files:
            
            ext = file.split(".")[1]
            newPath = os.path.join(directory, ext)
            if os.path.exists(newPath):
                shutil.move(os.path.join(directory, file), newPath)
            elif os.path.basename(directory) != ext and not os.path.exists(newPath):
                output.insert(END, "Creating new directory: {}".format(newPath))
                os.mkdir(newPath)
                shutil.move(os.path.join(directory, file), newPath)

    output.insert(END, "Done!")

# Run Tkinter Interface
root = Tk()
root.resizable(width=FALSE, height=FALSE)
fileOrg = PyFileOrganizer(master=root)
fileOrg.master.title("PyFile")
fileOrg.mainloop()
