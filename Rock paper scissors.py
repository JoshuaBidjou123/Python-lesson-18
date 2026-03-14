from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTK

# Setting up Main Window
root = TK()
root.title('Denomination Counter')
root.configure(bg = 'light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
# Resize the Image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1.place( relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox to see if OK is clicked
def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
             if MsgBox == 'OK'
                topwin()


# Adding Buttons to the Main Window
button1 = Button(root, text='Let's get started!', command=msg, bg='brown', fg='white')
                 button1.place(x=260, y=360)

def topwin():
    # Top Window
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x450')

    # Centering Widgets in the Top WIndow
    label.place('x=230, y=50')
    entry.place('x=200, y=80')
    btn.place('x=240, y=120')
    lbl.place('x=140, y=170')

    l1.place('x=180, y=200')
    l2.place('x=180, y=230')
    l3.place('x=180, y=260')

    t1.place('x=270, y=200')
    t2.place('x=270, y=230')               
    t3.place('x=270, y=260')

    top.mainloop()

root.mainloop()             
        
                 
             
        
             
              
