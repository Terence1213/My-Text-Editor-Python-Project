import os.path
from tkinter import *
from tkinter import filedialog, colorchooser, font

window = Tk()

#The text editor is closed.
def quit():
    window.destroy()


#The font of all the text is set.
def changeFont(*args):
    text_area.config(font=(font_name.get(), current_size.get()))


#An image is inserted
def insertImg():

    image_path = filedialog.askopenfilename(filetypes=(("PNG", ".png"), ("JPEG", ".jpg")))
    #With tkinter, and the .image_create, the photo image HAS to be global (if not an error will occur).
    global photo
    #The png image is converted into a filetype which tkinter / pycharm understands and can use.
    photo = PhotoImage(file=image_path)
    #The position that the image is to be inserted at is set. (Where the selected part of the text is).
    position = text_area.index(INSERT)
    #The image is inserted.
    text_area.image_create(position, image=photo)


def italic():

    #The italic font's actual font and size are gotten from the selected heading.
    italic_font = font.Font(font=(font_name.get(), current_size.get()))
    #The italic quality is being configured into the italic font.
    italic_font.config(slant="italic")
    text_area.tag_configure("italic", font=italic_font)

    #Grabs all the tags in the selected text.
    current_tags = text_area.tag_names("sel.first")

    #If any of the characters in the selected text are not italic, then all the characters in the selected text
    #are set to italic. If all the characters are italic, then all the characters are returned to the normal font.
    if "italic" in current_tags:
        text_area.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_area.tag_add("italic", "sel.first", "sel.last")


def bold():

    #The bold font's actual font and size are gotten from the selected heading.
    bold_font = font.Font(font=(font_name.get(), current_size.get()))
    #The bold quality is being configured into the italic font.
    bold_font.config(weight="bold")
    text_area.tag_configure("bold", font=bold_font)

    #Grabs all the tags in the selected text.
    current_tags = text_area.tag_names("sel.first")

    #If any of the characters in the selected text are not bold, then all the characters in the selected text
    #are set to bold. If all the characters are bold, then all the characters are returned to the normal font.
    if "bold" in current_tags:
        text_area.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_area.tag_add("bold", "sel.first", "sel.last")


#The default color which all text has is set.
def mainColor():

    color = colorchooser.askcolor()[1]
    text_area.config(foreground=color)


#The color of the selected text is changed. (Only one different colour can be chosen).
def changeColor():

    #The user selects his color.
    color = colorchooser.askcolor()[1]
    color_font = font.Font(font=(font_name.get(), current_size.get()))
    text_area.tag_configure("colored", font=color_font, foreground=color)

    #Grabs all the tags in the selected text.
    current_tags = text_area.tag_names("sel.first")

    #If any of the characters in the selected text are not colored, then all the characters in the selected text
    #are set to colored. If all the characters are colored, then all the characters are returned to the normal font.
    if "colored" in current_tags:
        text_area.tag_remove("colored", "sel.first", "sel.last")
    else:
        text_area.tag_add("colored", "sel.first", "sel.last")


#The background color is set.
def backgroundColor():

    #The user selects his color.
    color = colorchooser.askcolor()[1]
    text_area.config(background=color)


#Heading one is applied to the selected text.
def headingOne():

    #This is done so that when qualities are changed (ex: bold), the font size isn't set back to the normal version.
    current_size.set(30)
    #If any other headings are applied, they are overriden by the newly selected heading.
    text_area.tag_remove("heading_two", "sel.first", "sel.last")
    text_area.tag_remove("heading_three", "sel.first", "sel.last")
    text_area.tag_remove("normal", "sel.first", "sel.last")

    #Heading one is being configured and added to the selected text.
    text_area.tag_configure("heading_one", font=(font_name.get(), 30))
    text_area.tag_add("heading_one", "sel.first", "sel.last")


#Heading two is applied to the selected text.
def headingTwo():

    #This is done so that when qualities are changed (ex: bold), the font size isn't set back to the normal version.
    current_size.set(25)

    #If any other headings are applied, they are overriden by the newly selected heading.
    text_area.tag_remove("heading_one", "sel.first", "sel.last")
    text_area.tag_remove("heading_three", "sel.first", "sel.last")
    text_area.tag_remove("normal", "sel.first", "sel.last")

    #Heading two is being configured and added to the selected text.
    text_area.tag_configure("heading_two", font=(font_name.get(), 25))
    text_area.tag_add("heading_two", "sel.first", "sel.last")


#Heading three is applied to the selected text.
def headingThree():

    #This is done so that when qualities are changed (ex: bold), the font size isn't set back to the normal version.
    current_size.set(20)

    #If any other headings are applied, they are overriden by the newly selected heading.
    text_area.tag_remove("heading_one", "sel.first", "sel.last")
    text_area.tag_remove("heading_two", "sel.first", "sel.last")
    text_area.tag_remove("normal", "sel.first", "sel.last")

    #Heading three is being configured and added to the selected text
    text_area.tag_configure("heading_three", font=(font_name.get(), 20))
    text_area.tag_add("heading_three", "sel.first", "sel.last")


#The selected text is returned to normal.
def normal():

    #This is done so that when qualities are changed (ex: bold), the font size isn't set back to the normal version.
    current_size.set(15)

    #All headings, are removed, and the selected text is returned to normal.
    text_area.tag_remove("heading_one", "sel.first", "sel.last")
    text_area.tag_remove("heading_two", "sel.first", "sel.last")
    text_area.tag_remove("heading_three", "sel.first", "sel.last")


#All the text in the editor is deleted.
def newFile():
    text_area.delete(1.0, END)


#The user is prompted to enter a file to open from the file manager.
def openFile():

    #The filepath of the file that the user selects is set in the variable file.
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("All types", ".*"), ("Text Files", ".txt")))

    try:
        #The title of the window is set to the name of the file selected.
        window.title(os.path.basename(file))

        #The current text in the file is deleted, and the text stored in the opened file is inserted into the editor.
        text_area.delete(1.0, END)
        with open(file) as data:
            text_area.insert(1.0, data.read())

    except:
        print("Couldn't open file!")


#The user is prompted to save the file wherever he wants, from the file manager.
def saveFile():

    #The user is asked to save a file somewhere, and it's location path is saved into the variable file.
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        filetypes=(("Text Files", ".txt"), ("All Files", ".*")))

    #If the user cancels, or doesn't save anything, the method is stopped.
    if file is None:
        return

    #The program writes the text which it contains onto the saved file.
    try:
        window.title(os.path.basename(file))
        with open(file, "w") as data:
            data.write(str(text_area.get(1.0, END)))

    except Exception:
        print("Couldn't save file!")


#This method is to allow the user to cut text by means of a button.
def cut():
    text_area.event_generate("<<Cut>>")


#This method is to allow the user to copy text by means of a button.
def copy():
    text_area.event_generate("<<Copy>>")


#This method is to allow the user to paste text by means of a button.
def paste():
    text_area.event_generate("<<Paste>>")


#The default title is set to "Text Editor Program".
window.title("Text Editor Program")

#Default window width and height are 500 and 535.
window_width = 500
window_height = 535
window.geometry(f"{window_width}x{window_height}")

#The font name which is used every time a quality is modified.
font_name = StringVar()
#The default font is Arial.
font_name.set("Arial")

#The size which is used every time a quality is modified.
current_size = StringVar()
#The default size is 15.
current_size.set("15")

#The text area is created.
text_area = Text(window, font=(font_name.get(), 15), undo=True)

#The scroll bar is created.
scroll_bar = Scrollbar(text_area, command=text_area.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

#The scroll bar is added to the text area.
text_area.config(yscrollcommand=scroll_bar.set)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N + E + S + W)

#This is the frame which contains all the quality buttons.
frame = Frame(window)
frame.grid()

#The user changes the color of the selected text with this button.
color_button = Button(frame, text="Change Color", command=changeColor)
color_button.grid(row=0, column=0)

#The user changes the font of all the text in the program with this button. If not done in the beginning, the font is
#a bit glitched out.
font_box = OptionMenu(frame, font_name, *font.families(), command=changeFont)
font_box.grid(row=0, column=1)

#The user makes the selected text italic with this button.
italic_box = Button(frame, text="Italic", command=italic)
italic_box.grid(row=0, column=2)

#The user makes the selected text bold with this button.
bold_box = Button(frame, text="Bold", command=bold)
bold_box.grid(row=0, column=3)

#The user changes the background color with this button
background_box = Button(frame, text="Background color", command=backgroundColor)
background_box.grid(row=0, column=4)

#The user changes the default colour of all the text with this button.
main_color_box = Button(frame, text="Main Text Color", command=mainColor)
main_color_box.grid(row=1, columnspan=5)

#The menu bar contains all the menus.
menu_bar = Menu(window)

#The menu of the window is set to the menu "menu_bar".
window.config(menu=menu_bar)

#All the separate menus are instantiated.
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
heading_menu = Menu(menu_bar, tearoff=0)
insert_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)

#The "File" menu is added to the menubar.
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

#The "Edit" menu is added to the menubar.
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_cascade(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo (Ctrl + Z)")
edit_menu.add_command(label="Redo (Ctrl + Y)")

#The "Headings" menu is added to the menubar.
menu_bar.add_cascade(label="Headings", menu=heading_menu)
heading_menu.add_command(label="Heading 1", command=headingOne)
heading_menu.add_command(label="Heading 2", command=headingTwo)
heading_menu.add_command(label="Heading 3", command=headingThree)
heading_menu.add_command(label="Normal", command=normal)

#The "Insert" menu is added to the menubar.
menu_bar.add_cascade(label="Insert", menu=insert_menu)
insert_menu.add_command(label="Image", command=insertImg)

#The "Help" menu is added to the menubar.
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="When saving a file, only the text is saved")
help_menu.add_command(label="Undo and Redo buttons don't work, only the shortcuts do")

window.mainloop()