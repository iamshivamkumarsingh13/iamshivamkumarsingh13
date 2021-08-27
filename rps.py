from tkinter import *
from PIL import Image,ImageTk
from random import randint

# main window
root = Tk()
root.title("ROCK PAPER Scissors")
root.configure(background="#9b59b6")

# attach photos
rock_img =ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img =ImageTk.PhotoImage(Image.open("paper_user.png"))
scissors_img =ImageTk.PhotoImage(Image.open("scissors_user.png"))
rock_img_comp =ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp =ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp =ImageTk.PhotoImage(Image.open("scissors.png"))

# # insert picture 

user_label= Label(root,image=rock_img,bg="#9b59b6")
comp_label= Label(root,image=rock_img_comp,bg="#9b59b6")

comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores

playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")

computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators

user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white").grid(row=0,column=3)
computer_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white").grid(row=0, column=1)

#messages

msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)


count=Label(root,font=10,bg="black",text=0,fg="white")
count.grid(row=1,column=2)
round=Label(root,font=10,bg="black",text="round",fg="white")
round.grid(row=0,column=2)
#update message

def updateMessage(x):

    msg['text'] = x

# Update Count

def updateCount():

    cnt=int(count["text"])
    cnt +=1
    count["text"]=str(cnt)

#update User Score
 
def updateUserScore():
    score=int(playerscore["text"])
    score +=1
    playerscore["text"]=str(score)

#update Computer Score 

def updateCompScore():
    score=int(computerscore["text"])
    score += 1
    computerscore["text"]=str(score)

#check winner
def checKWin(player,computer):
    
    if(player==computer):
        updateMessage("Its a Tie !")
        updateCount()
    elif(player=="rock"):
        if computer=="paper":
            updateMessage("you Loose")
            updateCompScore()
            updateCount()
        else:
            updateMessage("You Win !!")
            updateUserScore()
            updateCount()
    elif player=="paper":
        if computer=="scissors":
            updateMessage("YOu Loose")
            updateCompScore()
            updateCount()
        else:
            updateMessage("You Win")
            updateUserScore()
            updateCount()
    elif player=="scissors":
        if computer=="rock":
            updateMessage("YOu Loose")
            updateCompScore()
            updateCount()
        else:
            updateMessage("You Win")
            updateUserScore()
            updateCount()
    else:
        pass





#update choices

choices=["rock","paper","scissors"]

def updateChoice(x):

    #for Computer
    compChoice = choices[randint(0,2)]

    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)

    #for user

    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checKWin(x,compChoice) # called the function 


#Buttons

rock= Button(root,width=20,height=2,text="ROCK",
bg="brown",fg="white",command = lambda:updateChoice("rock")).grid(row=2,column=1)

paper= Button(root,width=20,height=2,text="PAPER",
bg="green",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)

scissors= Button(root,width=20,height=2,text="SCISSORS",
bg="blue",fg="white",command = lambda:updateChoice("scissors")).grid(row=2,column=3)

root.mainloop()