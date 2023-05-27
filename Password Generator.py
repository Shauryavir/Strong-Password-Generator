from tkinter import*
import random

root=Tk()
root.title("Strong Password Generator")
root.geometry("400x400")

label= Label(root)

array_3d =[[['1','2','3','4','5','6','7'],["!","@","#","$","%","&","*"],["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]]


def new_password():
    random_no_1 = random.randint(0,7)
    random_no_2 = random.randint(0,7)
    random_no_3 = random.randint(0,26)
    random_no_4 = random.randint(0,26)
    random_no_5 = random.randint(0,7)
    random_no_6 = random.randint(0,26)
    random_no_7 = random.randint(0,7)
    random_no_8 = random.randint(0,26)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    letter4 = (array_3d[0][3][random_no_4])
    letter5 = str(array_3d[0][0][random_no_5])
    letter6 = (array_3d[0][1][random_no_7])
    letter7 = (array_3d[0][2][random_no_8])
    letter8 = (array_3d[0][3][random_no_6])
    label["text"] = letter1 + "" + letter2 + "" + letter3 + "" + letter4 + "" + letter5 + "" + letter6 + "" + letter7 + "" + letter8
    
    
btn = Button(root, text="Your New & Strong Password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()