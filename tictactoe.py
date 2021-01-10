# x = True O = false
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Satyam programme")
root.geometry("400x400")
root.resizable(0,0)
root.wm_iconbitmap('4.ico')

p1_score = StringVar()
p2_score = StringVar()
ptr1 = 0
ptr2 = 0
flag = True
ctr=0

def click(event):
	global flag,ctr
	if event['text']==" " and flag==True:
		flag = False
		event['text'] = "X"
		ctr+=1
		check()
	elif event['text']==" " and flag==False:
		flag = True
		event['text'] = "O"
		ctr+=1
		check()
		flag = True
	else:
		messagebox.showinfo("tictactoe","Wrong input")
def clearButton():
	btn1["text"]=" "	
	btn2["text"]=" "
	btn3["text"]=" "
	btn4["text"]=" "
	btn5["text"]=" "
	btn6["text"]=" "
	btn7["text"]=" "
	btn8["text"]=" "
	btn9["text"]=" "	

def check():
	global ptr1,ptr2,p1_score,p2_score,ctr
	if (btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X" or 
		btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X" or 
		btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X" or 
		btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X" or 
		btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X" or 
		btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X" or 
		btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X" or 
		btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X" or 
		btn7["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X"):
		clearButton()
		messagebox.showinfo("tictactoe","PLayer 1 win")
		ptr1+=1
		ctr=0
		p1_score.set(ptr1)	
	elif(btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
		btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O" or
		btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O" or
		btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O" or
		btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O" or
		btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O" or
		btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O" or
		btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O" or
		btn7["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O"):
		clearButton()
		messagebox.showinfo("tictactoe","PLayer 2 win")
		ptr2+=1
		ctr=0
		p2_score.set(ptr2)	

	elif (ctr == 9):
		messagebox.showinfo("tictactoe","It is a tie")
		clearButton()
		ctr=0
					

f = Frame(root,bg="gray")

btn1 = Button(f,fg="black",command=lambda:click(btn1),text=" ",borderwidth=2,relief=SUNKEN,width=3,bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn1.pack(side="left")


btn2 = Button(f,fg="black",command=lambda:click(btn2),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn2.pack(side="left")

btn3 = Button(f,fg="black",command=lambda:click(btn3),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn3.pack(side="left")



f.pack()

f1 = Frame(root,bg="gray")

btn4 = Button(f1,fg="black",command=lambda:click(btn4),text=" ",borderwidth=2,relief=SUNKEN,width=3,bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn4.pack(side="left")


btn5 = Button(f1,fg="black",command=lambda:click(btn5),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn5.pack(side="left")

btn6 = Button(f1,fg="black",command=lambda:click(btn6),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn6.pack(side="left")



f1.pack()
f2 = Frame(root,bg="gray")

btn7 = Button(f2,fg="black",command=lambda:click(btn7),text=" ",borderwidth=2,relief=SUNKEN,width=3,bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn7.pack(side="left")


btn8 = Button(f2,fg="black",command=lambda:click(btn8),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn8.pack(side="left")

btn9 = Button(f2,fg="black",command=lambda:click(btn9),text=" ",borderwidth=2,relief=SUNKEN,width=3, bg="yellow",font=("sans-serif",34,'bold'),pady=10)
btn9.pack(side="left")



f2.pack()


# player values
f3 = Frame(root,bg="grey")
player1 = Label(root,text="Player 1:", bg = "green", fg = "white",font=("lucida", 15, "bold") )
player1.pack(side=LEFT)

player1_entry = Entry(root,width=8,textvariable=p1_score)
player1_entry.pack(side=LEFT,padx=12)

f3.pack()

f4 = Frame(root,bg="grey")

player2 = Label(root,text="Player 2:", bg = "green", fg = "white",font=("lucida", 15, "bold") )
player2.pack(side=RIGHT)

player2_entry = Entry(root,width=8,textvariable=p2_score)
player2_entry.pack(side=RIGHT,padx=12)


f4.pack()
root.mainloop()



















