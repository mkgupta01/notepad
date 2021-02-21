from os import times
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file 
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END)
    
    
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()



def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def Cut():
    TextArea.event_generate(("<<Cut>>"))

def Copy():
    TextArea.event_generate(("<<Copy>>"))

def Paste():
    TextArea.event_generate(("<<Paste>>"))

def About():
    showinfo("Notepad","Developed by : Mayank kr Gupta")




if __name__ == '__main__':
    root=Tk()
    root.geometry("500x400")
    root.title("Notepad")
    

    #adding text area
    TextArea= Text(root,font=(13))
    file=None
    TextArea.pack(fill=BOTH,expand=True)

    #creating a menubar
    MenuBar = Menu(root)
    #file menu start
    File = Menu(MenuBar,tearoff=0)
    File.add_command(label="New",command=newFile)
    File.add_command(label="Open",command=openFile)
    File.add_command(label="Save",command=saveFile)
    File.add_separator()
    File.add_command(label="Exit",command=quit)
    MenuBar.add_cascade(label="File",menu=File)
    #file menu ends

    #edit menu start
    Edit=Menu(MenuBar,tearoff=0)
    Edit.add_command(label="Cut",command=Cut)
    Edit.add_command(label="Copy",command=Copy)
    Edit.add_command(label="Paste",command=Paste)
    MenuBar.add_cascade(label="Edit",menu=Edit)
    #edit menu end

    #help menu start
    Helpmenu=Menu(MenuBar,tearoff=0)
    Helpmenu.add_command(label="About us",command=About)
    MenuBar.add_cascade(label="Help", menu=Helpmenu)
    #help menu end

    #adding scollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.config(menu=MenuBar)




    root.mainloop()


