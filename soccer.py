from Tkinter import *
from PIL import Image, ImageTk
import random
import time

root = Tk()
e = Entry(root)

w = Canvas(root, width=1300, height=768)
w.configure(background = "#479000")
w.pack()

scoreA=0
scoreB=0
step=1
t=random.randint(1,2)


def layout():
    w.create_oval(550,284,750,484, outline="yellow")
    w.create_oval(647,381,653,387, outline="yellow", fill="yellow")
    w.create_line(650,0,650,768, fill="yellow")

    w.create_rectangle(138,100,288,668, outline="yellow")
    w.create_rectangle(138,284,188,484, outline="yellow")
    w.create_arc(238,284,338,484,start=270,extent=180,outline="yellow", style=ARC)

    w.create_rectangle(1012,100,1165,668, outline="yellow")
    w.create_rectangle(1112,284,1165,484, outline="yellow")
    w.create_arc(1062,284,962,484,start=90,extent=180,outline="yellow", style=ARC)

    w.create_rectangle(118,284,138,485, outline="white", width=2)
    w.create_rectangle(110,284,118,485, outline="white", width=2, fill="white")
    w.create_line(110,284,138,275, fill="white", width=5)
    w.create_line(110,484,138,494, fill="white", width=5)

    w.create_rectangle(1165,284,1185,485, outline="white", width=2)
    w.create_rectangle(1185,284,1193,485, outline="white", width=2, fill="white")
    w.create_line(1193,284,1165,275, fill="white", width=5)
    w.create_line(1193,484,1165,494, fill="white", width=5)

    w.create_rectangle(500,10,800,40, fill="white", outline="orange")
    w.create_polygon(550,41,560,50,740,50,750,41, fill="orange", outline="orange")

    w.create_text(570, 25, text=sys.argv[1], fill="red")
    w.create_text(720, 25, text=sys.argv[2], fill="blue")

    w.create_text(650, 25, text="-", font=("Arial",30))
    teamAscore = w.create_text(630, 25, text=str(scoreA), fill="red", font=("Arial",30), tags=('scoreA'))
    teamBscore = w.create_text(670, 25, text=str(scoreB), fill="blue", font=("Arial",30), tags=('scoreB'))

    
    w.create_rectangle(138,0,1165,768, outline="brown", width=10)

    movePlayers()

teamAscore = w.create_text(630, 25, text=str(scoreA), fill="red", font=("Arial",30), tags=('scoreA'))
teamBscore = w.create_text(670, 25, text=str(scoreB), fill="blue", font=("Arial",30), tags=('scoreB'))

image = Image.open("images/crowdL.jpg")
im2 = image.resize((60,1600), Image.ANTIALIAS)
audienceLimage = ImageTk.PhotoImage(im2)
w.create_image(0,0,image=audienceLimage)
    
image = Image.open("images/adsL.jpg")
im2 = image.resize((15,1600), Image.ANTIALIAS)
adsLimage = ImageTk.PhotoImage(im2)
w.create_image(50,0,image=adsLimage)
    
image = Image.open("images/crowdR.jpg")
im2 = image.resize((60,1600), Image.ANTIALIAS)
audienceRimage = ImageTk.PhotoImage(im2)
w.create_image(1290,0,image=audienceRimage)
    
image = Image.open("images/adsR.jpg")
im2 = image.resize((15,1600), Image.ANTIALIAS)
adsRimage = ImageTk.PhotoImage(im2)
w.create_image(1240,0,image=adsRimage)

image = Image.open("images/ball.jpg")
im2 = image.resize((15,15), Image.ANTIALIAS)
ballImage = ImageTk.PhotoImage(im2)
ball = w.create_image(650,384,image=ballImage, tags=('players'))


image = Image.open("images/blueP.jpg")
im2 = image.resize((20,60), Image.ANTIALIAS)
bluePimage = ImageTk.PhotoImage(im2)

blueParray=[]
for i in range(0,4):
    blueParray.append(w.create_image(800+((i%2)*100),250+(i*100),image=bluePimage, tags=('players')))


image = Image.open("images/redP.jpg")
im2 = image.resize((20,60), Image.ANTIALIAS)
redPimage = ImageTk.PhotoImage(im2)

redParray=[]
for i in range(0,4):
    redParray.append(w.create_image(500-((i%2)*100),250+(i*100),image=redPimage, tags=('players')))


def animate():
    global step
    global t
    global scoreA
    global scoreB
    global blueParray
    global ball
    global root
    
    ballX, ballY = w.coords(ball)
    


    if (scoreB==7) | (scoreA==7):
        root.quit()
        root.destroy()
        
        if scoreA==7:
            print "team A won!"
        if scoreB==7:
            print "team B won!"
            
    else:
        if t==1:
            if step==1:
                w.move(ball,-100,70)
            if step==2:
                w.move(ball,-130,-100)
            if step==3:
                w.move(ball,-300,-50)
                scoreB=scoreB+1
            if step==4:
                time.sleep(1)
            step=step+1
            
            e.after(9,movePlayers)
            
            if step==5:
                w.delete('players','scoreB')
                ball = w.create_image(650,384,image=ballImage, tags=('players'))
                for i in range(0,4):
                    blueParray[i]=w.create_image(800+((i%2)*100),250+(i*100),image=bluePimage, tags=('players'))
                    redParray[i]=w.create_image(500-((i%2)*100),250+(i*100),image=redPimage, tags=('players'))
                teamBscore = w.create_text(670, 25, text=str(scoreB), fill="blue", font=("Arial",30), tags=('scoreB'))

                step=1
                t=random.randint(1,2)
                return
    
        else:
            if step==1:
                w.move(ball,200,70)
            if step==2:
                w.move(ball,130,-100)
            if step==3:
                w.move(ball,190,-30)
                scoreA=scoreA+1
            if step==4:
                time.sleep(1)
            step=step+1
            e.after(9,movePlayers)

            if step==5:
                w.delete('players','scoreA')
                ball = w.create_image(650,384,image=ballImage, tags=('players'))
                for i in range(0,4):
                    blueParray[i]=w.create_image(800+((i%2)*100),250+(i*100),image=bluePimage, tags=('players'))
                    redParray[i]=w.create_image(500-((i%2)*100),250+(i*100),image=redPimage, tags=('players'))
                teamAscore = w.create_text(630, 25, text=str(scoreA), fill="red", font=("Arial",30),tags=('scoreA'))

                step=1
                t=random.randint(1,2)
                return





def movePlayers():
    ballX, ballY = w.coords(ball)
    global step
    global t
    
    if t==1:
        if (w.coords(blueParray[0]) <= w.coords(ball)) | (w.coords(blueParray[1]) <= w.coords(ball)) | (w.coords(blueParray[2]) <= w.coords(ball)) | (w.coords(blueParray[3]) <= w.coords(ball)):
            animate()
            return
        else:
            if (step==1):
                w.move(blueParray[0],-3.5,2.5)
                w.move(blueParray[1],-2,1)
                w.move(blueParray[2],-1,-2)
                w.move(blueParray[3],-2,-2)
            
                w.move(redParray[0],0.25,0.5)
                w.move(redParray[1],0.25,1)
                w.move(redParray[2],0.25,-2)
                w.move(redParray[3],0.25,-2)

                e.after(33,movePlayers)

            if (step==2):
                w.move(blueParray[0],-2.5,2.5)
                w.move(blueParray[1],-2,1)
                w.move(blueParray[2],-1,-2)
                w.move(blueParray[3],-2,-2)
            
                w.move(redParray[0],1,0.5)
                w.move(redParray[1],0.25,1)
                w.move(redParray[2],0.25,-2)
                w.move(redParray[3],0.25,-2)

                e.after(33,movePlayers)

            if (step==3):
                w.move(blueParray[0],-2,-2)
                w.move(blueParray[1],-2,-1)
                w.move(blueParray[2],-1,2)
                w.move(blueParray[3],-2,2)
            
                w.move(redParray[0],-1,-0.5)
                w.move(redParray[1],-0.25,-1)
                w.move(redParray[2],-1,2)
                w.move(redParray[3],-0.25,2)

                e.after(33,movePlayers)

            if (step==4):
                w.move(blueParray[0],-2,-2)
                w.move(blueParray[1],-2,-1)
                w.move(blueParray[2],-1,2)
                w.move(blueParray[3],-2,2)
            
                w.move(redParray[0],-0.5,0.5)
                w.move(redParray[1],-0.5,1)
                w.move(redParray[2],-0.5,-2)
                w.move(redParray[3],-0.5,-2)
                animate()

    else:
        if(w.coords(redParray[0]) >= w.coords(ball)) | (w.coords(redParray[1]) >= w.coords(ball)) | (w.coords(redParray[2]) >= w.coords(ball)) | (w.coords(redParray[3]) >= w.coords(ball)):
            animate()
        
        else:
            if (step==1):
                w.move(redParray[0],3.5,2.5)
                w.move(redParray[1],2,1)
                w.move(redParray[2],1,-2)
                w.move(redParray[3],2,-2)
                
                w.move(blueParray[0],-0.25,0.5)
                w.move(blueParray[1],-0.25,1)
                w.move(blueParray[2],-0.25,-2)
                w.move(blueParray[3],-0.25,-2)
                
                e.after(33,movePlayers)
        
            if (step==2):
                w.move(redParray[0],3,1.5)
                w.move(redParray[1],2,1)
                w.move(redParray[2],1,-2)
                w.move(redParray[3],2,-2)
                
                w.move(blueParray[0],-1,0.5)
                w.move(blueParray[1],-0.25,1)
                w.move(blueParray[2],-0.25,-2)
                w.move(blueParray[3],-0.25,-2)
                
                e.after(33,movePlayers)
            
            if (step==3):
                w.move(redParray[0],2,-2)
                w.move(redParray[1],2,-1)
                w.move(redParray[2],1,2)
                w.move(redParray[3],2,2)
                
                w.move(blueParray[0],1,-0.5)
                w.move(blueParray[1],2,-1)
                w.move(blueParray[2],1,2)
                w.move(blueParray[3],2,2)
                
                e.after(33,movePlayers)
            
            if (step==4):
                w.move(redParray[0],0.25,-3)
                w.move(redParray[1],2,-1)
                w.move(redParray[2],1,2)
                w.move(redParray[3],2,2)
                
                w.move(blueParray[0],0.5,0.5)
                w.move(blueParray[1],0.5,1)
                w.move(blueParray[2],0.5,-2)
                w.move(blueParray[3],0.5,-2)
                animate()
         
            return


layout()
root.title("Soccer server")
root.geometry("1300x768")
root.configure(background = "#479000")
root.mainloop()
