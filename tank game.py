from tkinter import *
import random
import time
import math
a=Tk()
b=Canvas(a,height=715,width=1080,background="#227700")
wall1=b.create_rectangle(500,715,600,500,fill="grey")
horizonline=b.create_line(0,215,1080,215,fill="white",width=3)
sky=b.create_rectangle(0,0,1240,370,fill="cyan")
mountain=b.create_arc(0,545,215,200,start=0,extent=180,fill="green",width=3)
mountain2=b.create_arc(215,545,545,215,start=0,extent=180,fill="green",width=3)
mountain3=b.create_arc(545,535,815,220,start=0,extent=180,fill="green",width=3)
mountain4=b.create_arc(850,545,1080,215,start=0,extent=180,fill="green",width=3)
path=b.create_rectangle(0,650,1080,715,fill="#777777")
b.pack()
d=input("Colour of first player (blue, red, etc.) = ")
c=input("Colour of second player (blue, red, etc.) = ")
playera=input("Input player one's name")
playerb=input("Input player two's name")
#playera="Player One"
#playerb="Player Two"
#d="blue"
#c="red"
global x1
x1=random.randint(100,450)
y1=600
global x
x=random.randint(675,970)
y=600
global tank1position
tank1position=x1-20
global tank2position
tank2position=x-20
        #Player one tank
#left == x1-20
#top == y1
#right == x1+80
#bottom == y1+50
tank1=b.create_rectangle(x1-20,y1+20,x1+42,y1+50,fill=d)#bottom tank
tank1a=b.create_rectangle(x1-5,y1+10,x1+26,y1+30,fill=d)#top tank
tank1b=b.create_line(x1+15,y1+20,x1+55,y1,width=10,fill="black")#barrel
tank1c=b.create_text(x1-12,y1+46,text="O",font="Arial 20 bold",fill="black")
tank1d=b.create_text(x1+4,y1+46,text="O",font="Arial 20 bold",fill="black")
tank1e=b.create_text(x1+20,y1+46,text="O",font="Arial 20 bold",fill="black")
tank1f=b.create_text(x1+36,y1+46,text="O",font="Arial 20 bold",fill="black")
    #Player Two tank
#left == x-20
#top == y
#right == x+80
#bottom == y+50
tank2=b.create_rectangle(x-20,y+20,x+42,y+50,fill=c)#bottom tank
tank2a=b.create_rectangle(x-5,y+10,x+26,y+30,fill=c)#top tank
tank2b=b.create_line(x+7,y+20,x-35,y,width=10,fill="black")#barrel
tank2c=b.create_text(x-12,y+46,text="O",font="Arial 20 bold",fill="black")
tank2d=b.create_text(x+4,y+46,text="O",font="Arial 20 bold",fill="black")
tank2e=b.create_text(x+20,y+46,text="O",font="Arial 20 bold",fill="black")
tank2f=b.create_text(x+36,y+46,text="O",font="Arial 20 bold",fill="black")
#direction0 === left
#direction1 === right
#180 degrees / 3.142 === 57.2883513686
#7.854 === 180 degree angle
#4.712 === 0 degree angle
#Player one by default. 0 is player #1. 1 is player #2.
#Left by default. 0 is left. 1 is right.
#GLOBAL VARIABLES
global turnover
global protimeset
global win
global turn
global turn1
global movelimit2
global movelimit1
global turntext
global stop
global moveturn
global go
go=0
moveturn=5
stop=0
movelimit1=0
movelimit2=0
gravity=10
protimeset=20.0
turn=0
win=0
turn1=0
turnover=1
turntext=b.create_text(590,150,text="It is Player One's turn",font=30)
#Wall of DOOM
#wall2=b.create_rectangle(850,218,875,150,fill="grey")
#ceiling=b.create_polygon(500,500,600,500,875,150,850,150,fill="gray",outline="black")
#sidewall=b.create_polygon(600,715,600,500,875,150,875,218,fill="grey",outline="black")
#PLAYER 1 VARIABLES
global xexplosiona
global yexplosiona
global xexplosiontempa
global yexplosiontempa
global velocitya
global anglea
global directiona
global repeata
global inpvelocitya
global vela
global anga
global inpanglea
global tankxa
global leftwalla
global topwalla
global rightwalla
global bottomwalla
global healtha
healtha=0
inpanglea=150
anga=0
repeata=0
tanka=(x1+55,y1)
directiona=1
parabolaa=0
inpvelocitya=100
redbara=b.create_rectangle(x1-40,y1-40,x1+60,y1-20,fill="red")
greenbar1a=b.create_rectangle(x1-40,y1-40,x1+60,y1-20,fill="green")
greenbar2a=b.create_rectangle(x1-40,y1-40,x1+40,y1-20,fill="green")
greenbar3a=b.create_rectangle(x1-40,y1-40,x1+20,y1-20,fill="green")
greenbar4a=b.create_rectangle(x1-40,y1-40,x1+0,y1-20,fill="green")
greenbar5a=b.create_rectangle(x1-40,y1-40,x1-20,y1-20,fill="green")
b.create_text(100,75,text="Velocity",font=20)
vela=b.create_text(150,75,text=inpvelocitya,font=20)
b.create_text(100,40,text=playera,font=20)
anga=b.create_text(150,110,text=inpanglea,font=20)
b.create_text(100,110,text="Angle",font=20)
tankxa=x1+70
leftwalla=x1-20
topwalla=y1+10
rightwalla=x1+42
bottomwalla=y1+50
#PLAYER 2 VARIABLES
global xexplosionb
global yexplosionb
global xexplosiontempb
global yexplosiontempb
global velocityb
global angleb
global directionb
global repeatb
global inpvelocityb
global velb
global angb
global inpangleb
global tankxb
global leftwallb
global topwallb
global rightwallb
global bottomwallb
global healthb
healthb=0
inpangleb=150
angb=0
repeatb=0
tankb=(x-35,y)
directionb=0
parabolab=0
inpvelocityb=100
redbarb=b.create_rectangle(x-40,y-40,x+60,y-20,fill="red")
greenbar1b=b.create_rectangle(x-40,y-40,x+60,y-20,fill="green")
greenbar2b=b.create_rectangle(x-40,y-40,x+40,y-20,fill="green")
greenbar3b=b.create_rectangle(x-40,y-40,x+20,y-20,fill="green")
greenbar4b=b.create_rectangle(x-40,y-40,x,y-20,fill="green")
greenbar5b=b.create_rectangle(x-40,y-40,x-20,y-20,fill="green")
b.create_text(980,75,text="Velocity",font=20)
velb=b.create_text(1030,75,text=inpvelocityb,font=20)
b.create_text(980,40,text=playerb,font=20)
angb=b.create_text(1030,110,text=inpangleb,font=20)
b.create_text(980,110,text="Angle",font=20)
tankxb=x-25
leftwallb=x-20
topwallb=y+10
rightwallb=x+42
bottomwallb=y+50
#left == x-20
#top == y
#right == x+80
#bottom == y+50
tankshot1=b.create_oval(tanka[0]-5,tanka[1]-5,tanka[0]+5,tanka[1]+5)
tankname1=b.create_text(tanka[0]-40,tanka[1]-60,text=playera,font=20)
tankshot2=b.create_oval(tankb[0]-5,tankb[1]-5,tankb[0]+5,tankb[1]+5)
tankname2=b.create_text(tankb[0]+50,tankb[1]-60,text=playerb,font=20)
def callback(event):
    if event.keysym=="space":
        global turn
        global win
        global anglea
        global xexplosiona
        global yexplosiona
        global xexplosiontempa
        global yexplosiontempa
        global velocitya
        global protimea
        global parabolaa
        global repeata
        global angleb
        global xexplosionb
        global yexplosionb
        global xexplosiontempb
        global yexplosiontempb
        global velocityb
        global protimeb
        global parabolab
        global repeatb
        global tank1position
        global tank2position
        global movelimit1
        global movelimit2
        global turn1
        global turn2
        global x
        global x1
        global turnover
        global inpvelocitya
        global inpvelocityb
        global inpanglea
        global inpangleb
        global vela
        global velb
        global tankxa
        global tankxb
        global turntext
        global leftwalla
        global topwalla
        global rightwalla
        global bottomwalla
        global leftwallb
        global topwallb
        global rightwallb
        global bottomwallb
        global healtha
        global healthb
        global stop
        global moveturn
        global go
        if directiona==1 and turn==0 and win==0 and go==0:
            if stop==1:
                stop=0
            velocitya=inpvelocitya
            tempanglea=inpanglea/57.2883513686
            anglea=tempanglea+4.712
            go=1
            for repeata in range(700):
                if stop==1:
                    repeata=900
                projectiona=protimeset/700
                protimea=projectiona*repeata
                xexplosiontempa=velocitya*protimea*math.cos(anglea)
                yexplosiontempa=velocitya*protimea*math.sin(anglea)-(gravity/2)*protimea**2
                xexplosiona=tankxa+xexplosiontempa
                yexplosiona=tanka[1]+yexplosiontempa*-1
                parabolaa=b.create_oval(xexplosiona-5,yexplosiona-5,xexplosiona+5,yexplosiona+5,fill="black")
                b.update()
                time.sleep(0.001)
                b.delete(parabolaa)
                if xexplosiona<600 and xexplosiona>500 and yexplosiona<715 and yexplosiona>500:
                    stop=1
                    turn=1
                    turn1=1
                    movelimit1=0
                    go=0
                if xexplosiona<rightwallb and xexplosiona>leftwallb and yexplosiona<bottomwallb and yexplosiona>topwallb:
                    stop=1
                    healthb=healthb+1
                    turn1=1
                    movelimit1=0
                    go=0
                    if healthb==1:
                        b.delete(greenbar1b)
                    elif healthb==2:
                        b.delete(greenbar2b)
                    elif healthb==3:
                        b.delete(greenbar3b)
                    elif healthb==4:
                        b.delete(greenbar4b)
                    elif healthb==5:
                        b.delete(greenbar5b)
                        b.create_text(590,200,text="Player Two has been defeated",font=30)
                        win=1
                elif xexplosiona>1080:
                    go=0
                    repeata=800
                    turn=1
                    turn1=1
                    movelimit1=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player Two's turn",font=30)
                    b.update()
                elif yexplosiona>715:
                    go=0
                    repeata=800
                    turn=1
                    turn1=1
                    movelimit1=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player Two's turn",font=30)
                    b.update()
                elif repeata==699:
                    go=0
                    turn=1
                    turn1=1
                    movelimit1=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player Two's turn",font=30)
                    b.update()
        elif directionb==0 and turn==1 and win==0 and go==0:
            if stop==1:
                stop=0
            velocityb=inpvelocityb
            tempangleb=inpangleb/57.2883513686
            angleb=tempangleb+4.712
            go=1
            for repeatb in range(700):
                if stop==1:
                    repeatb=900
                projectionb=protimeset/700
                protimeb=projectionb*repeatb
                xexplosiontempb=(velocityb*-1)*protimeb*math.cos(angleb*-1)
                yexplosiontempb=(velocityb*-1)*protimeb*math.sin(angleb*-1)-(gravity/2)*protimeb**2
                xexplosionb=tankxb+xexplosiontempb
                yexplosionb=tankb[1]+yexplosiontempb*-1
                parabolab=b.create_oval(xexplosionb-5,yexplosionb-5,xexplosionb+5,yexplosionb+5,fill="black")
                b.update()
                time.sleep(0.001)
                b.delete(parabolab)
                if xexplosionb<600 and xexplosionb>500 and yexplosionb<715 and yexplosionb>500:
                    stop=1
                    turn=1
                    turn1=0
                    movelimit1=0
                    go=0
                if xexplosionb<rightwalla and xexplosionb>leftwalla and yexplosionb<bottomwalla and yexplosionb>topwalla:        
                    stop=1
                    healtha=healtha+1
                    turn1=0
                    movelimit2=0
                    go=0
                    if healtha==1:
                        b.delete(greenbar1a)
                    elif healtha==2:
                        b.delete(greenbar2a)
                    elif healtha==3:
                        b.delete(greenbar3a)
                    elif healtha==4:
                        b.delete(greenbar4a)
                    elif healtha==5:
                        b.delete(greenbar5a)
                        b.create_text(590,200,text="Player One has been defeated",font=30)
                        win=1
                elif xexplosionb>1080:
                    go=0
                    repeatb=800
                    turn=0
                    turn1=0
                    movelimit2=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player One's turn",font=30)
                    b.update()
                elif yexplosionb>715:
                    go=0
                    repeatb=800
                    turn=0
                    turn1=0
                    movelimit2=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player One's turn",font=30)
                    b.update()
                elif repeatb==699:
                    go=0
                    turn=0
                    turn1=0
                    movelimit2=0
                    b.delete(turntext)
                    turntext=b.create_text(590,150,text="It is Player One's turn",font=30)
                    b.update()
        
    elif event.keysym=="w" and turn==0 and inpvelocitya<200:
        b.delete(vela)
        inpvelocitya=inpvelocitya+1
        vela=b.create_text(150,75,text=inpvelocitya,font=20)
        b.update()
    elif event.keysym=="s" and inpvelocitya>0 and turn==0 and inpvelocitya>0:
        b.delete(vela)
        inpvelocitya=inpvelocitya-1
        vela=b.create_text(150,75,text=inpvelocitya,font=20)
        b.update()  
    elif event.keysym=="a" and tank1position>10 and turn1==0 and turn==0:
        b.move(tank1,-moveturn,0)
        b.move(tank1a,-moveturn,0)
        b.move(tank1b,-moveturn,0)
        b.move(tank1c,-moveturn,0)
        b.move(tank1d,-moveturn,0)
        b.move(tank1e,-moveturn,0)
        b.move(tank1f,-moveturn,0)
        b.move(tankshot1,-moveturn,0)
        b.move(tankname1,-moveturn,0)
        b.move(redbara,-moveturn,0)
        b.move(greenbar1a,-moveturn,0)
        b.move(greenbar2a,-moveturn,0)
        b.move(greenbar3a,-moveturn,0)
        b.move(greenbar4a,-moveturn,0)
        b.move(greenbar5a,-moveturn,0)
        leftwalla=leftwalla-moveturn
        rightwalla=rightwalla-moveturn
        tankxa=tankxa-moveturn
        tank1position=tank1position-moveturn
        movelimit1=movelimit1+1
        b.update()
        if movelimit1==10:
            turn1=1
            movelimit1=0
            b.update()
    elif event.keysym=="d" and tank1position<1080  and tank1position<420 and turn1==0 and turn==0:
        b.move(tank1,moveturn,0)
        b.move(tank1a,moveturn,0)
        b.move(tank1b,moveturn,0)
        b.move(tank1c,moveturn,0)
        b.move(tank1d,moveturn,0)
        b.move(tank1e,moveturn,0)
        b.move(tank1f,moveturn,0)
        b.move(tankshot1,moveturn,0)
        b.move(tankname1,moveturn,0)
        b.move(redbara,moveturn,0)
        b.move(greenbar1a,moveturn,0)
        b.move(greenbar2a,moveturn,0)
        b.move(greenbar3a,moveturn,0)
        b.move(greenbar4a,moveturn,0)
        b.move(greenbar5a,moveturn,0)
        leftwalla=leftwalla+moveturn
        rightwalla=rightwalla+moveturn
        tankxa=tankxa+moveturn
        tank1position=tank1position+moveturn
        movelimit1=movelimit1+1
        b.update()
        if movelimit1==10:
            turn1=1
            movelimit1=0
            b.update()
            
            #Player 2
            
    elif event.keysym=="Up" and turn==1 and inpvelocityb<200:
        b.delete(velb)
        inpvelocityb=inpvelocityb+1
        velb=b.create_text(1030,75,text=inpvelocityb,font=20)
        b.update()
    elif event.keysym=="Down" and inpvelocityb>0 and turn==1 and inpvelocityb>0:
        b.delete(velb)
        inpvelocityb=inpvelocityb-1
        velb=b.create_text(1030,75,text=inpvelocityb,font=20)
        b.update()  
    elif event.keysym=="Left" and tank2position>0  and tank2position>620 and turn1==1 and turn==1:
        b.move(tank2,-moveturn,0)
        b.move(tank2a,-moveturn,0)
        b.move(tank2b,-moveturn,0)
        b.move(tank2c,-moveturn,0)
        b.move(tank2d,-moveturn,0)
        b.move(tank2e,-moveturn,0)
        b.move(tank2f,-moveturn,0)
        b.move(tankshot2,-moveturn,0)
        b.move(tankname2,-moveturn,0)
        b.move(redbarb,-moveturn,0)
        b.move(greenbar1b,-moveturn,0)
        b.move(greenbar2b,-moveturn,0)
        b.move(greenbar3b,-moveturn,0)
        b.move(greenbar4b,-moveturn,0)
        b.move(greenbar5b,-moveturn,0)
        leftwallb=leftwallb-moveturn
        rightwallb=rightwallb-moveturn
        tankxb=tankxb-moveturn
        tank2position=tank2position-moveturn
        movelimit2=movelimit2+1
        b.update()
        if movelimit2==10:
            turn1=0
            movelimit2=0
            b.update()
    elif event.keysym=="Right" and tank2position<1020 and turn1==1 and turn==1:
        b.move(tank2,moveturn,0)
        b.move(tank2a,moveturn,0)
        b.move(tank2b,moveturn,0)
        b.move(tank2c,moveturn,0)
        b.move(tank2d,moveturn,0)
        b.move(tank2e,moveturn,0)
        b.move(tank2f,moveturn,0)
        b.move(tankshot2,moveturn,0)
        b.move(tankname2,moveturn,0)
        b.move(redbarb,moveturn,0)
        b.move(greenbar1b,moveturn,0)
        b.move(greenbar2b,moveturn,0)
        b.move(greenbar3b,moveturn,0)
        b.move(greenbar4b,moveturn,0)
        b.move(greenbar5b,moveturn,0)
        leftwallb=leftwallb+moveturn
        rightwallb=rightwallb+moveturn
        tankxb=tankxb+moveturn
        tank2position=tank2position+moveturn
        movelimit2=movelimit2+1
        b.update()
        if movelimit2==10:
            turn1=0
            movelimit2=0
            b.update()
def mousewheel(event):
    global anga
    global angb
    global inpanglea
    global inpangleb
    global turn
    global tanka
    global tankb
    if turn==0:
        if event.delta==-120 and inpanglea>0:
            b.delete(anga)
            inpanglea=inpanglea-1
            anga=b.create_text(150,110,text=inpanglea,font=20)
            b.update()
        elif event.delta==120 and inpanglea<180:
            b.delete(anga)
            inpanglea=inpanglea+1
            anga=b.create_text(150,110,text=inpanglea,font=20)
            b.update()
    elif turn==1:
        if event.delta==-120 and inpangleb>0:
            b.delete(angb)
            inpangleb=inpangleb-1
            angb=b.create_text(1030,110,text=inpangleb,font=20)
            b.update()
        elif event.delta==120 and inpangleb<180:
            b.delete(angb)
            inpangleb=inpangleb+1
            angb=b.create_text(1030,110,text=inpangleb,font=20)
            b.update()
a.bind("<MouseWheel>", mousewheel)
b.bind_all("<Key>",callback)
a.mainloop()
#change into a lower Python version
#Print: remove brackets
# Capitalize t on tkinter
