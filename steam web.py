import tkinter
import pickle
from tkinter import messagebox
def raise_frame(frame):
    frame.tkraise()
label =tkinter.Label
window = tkinter.Tk()
window.state("zoomed")
window.title("STEAM")
window.geometry("340x440")
window.iconbitmap("img/steam_logo.ico")
frame1 = tkinter.Frame(bg="#333333")
frame2 = tkinter.Frame(bg="#0dfc85")
frame3= tkinter.Frame(bg="#ad14db")
frame4= tkinter.Frame(bg="#333333")
frame5= tkinter.Frame(bg="#074db0")
frame6 = tkinter.Frame(bg="#0816d1")
frame7 = tkinter.Frame(bg="#0ce8b8")
frame8= tkinter.Frame(bg="#fa4225")
frame9= tkinter.Frame(bg="#333333")
frame10= tkinter.Frame(bg="#1dcf0c")
frame11 = tkinter.Frame(bg="#f00514")
Lb = tkinter.Listbox(frame1)
Lb.insert(1, 'Among us ')
Lb.insert(2, 'Pubg mobile ')
Lb.insert(3, ' Clash of clans')
Lb.insert(5, ' Fortinite')
Lb.insert(6, ' Brawl stars')
Lb.insert(7, ' Minecraft')
Lb.insert(8, ' Monopoly')
Lb.insert(9, ' eFootball2023')
Lb.insert(10, ' Hay Day ')
Lb.insert(11, ' Clash Royale')
Lb.insert(12, ' Mortal Kombat')
Lb.insert(13, ' Hogwarst Legacy')
Lb.place(x=10, y=570)
Lb.configure(height=25, width=60)
card_number = "55555"
game_list = ["among us ", " pubg mobile ", " clash of clans ", " fortinite ", " brawl stars ", " minecraft ", " monopoly "," eFootball2023 "," Hay Day "," Clash Royale "," Mortal Kombat "," Hogwarst Legacy "]
with open("GAME.txt","w") as file :
    file.writelines(game_list)
game_list.sort()
print(game_list)
#cart və blansımın entry və labely duzeltdirem
username11_label = tkinter.Label(frame4, text="Card Number:", bg="#333333", fg="#FFFFFF", font=("Arial, 20"))
username11_entry = tkinter.Entry(frame4, font=("Arial, 16"))
username11_label.place(x=720, y=460)
username11_entry.place(x=900, y=465)
username10_label = tkinter.Label(frame4, text="BALANCE:", bg="#333333", fg="#FFFFFF", font=("Arial, 20"))
username10_label.place(x=720, y=420)
BALANCE = 0

money_photo = tkinter.PhotoImage(file="img/money40.png")
btn2 = tkinter.Button(frame4,bg="green",
                            image=money_photo)
btn2.place(x=1820, y=0)
money = tkinter.Spinbox(frame4, to=10, width=5)
money.place(x=890, y=430)


def balance():
    get_metod = username11_entry.get()
    if get_metod == card_number:
        messagebox.showinfo("Operation successfully")
    else:
        messagebox.showerror("Not equal")
    username11_entry.delete(0, "end")

def save_info():
    username = username_entry.get()
    password = password_entry.get()
    username.strip()
    password.strip()
    print(username, password)
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")
    if username == "" or password == "":
        messagebox.showerror("Wrong")
    with open("Text.dat", "wb") as file2:
        pickle.dump(username, file2)
        pickle.dump(password, file2)

    with open("Text.dat", 'rb') as file2:
        dictionry_list = pickle.load(file2)
    with open("Text_name.dat", 'rb') as file:
        dictionry = pickle.load(file)

    if dictionry == dictionry_list:
        messagebox.showinfo("REGISTRATION SUCCESSFUL")
counter = 0
total_sum = 0

def button_clicked():
    global BALANCE, money, counter, total_sum
    efootball = int(efoot.get()) * 100
    Mortal = int(mortal5.get()) * 95
    Monopoly = int(monopoly7.get()) * 70
    Hogwarst = int(hogwarst9.get()) * 50
    Minecraft = int(minecraft4.get()) * 10
    money20 = int(money.get()) * 10
    BALANCE = money20
    total_bills = BALANCE - (efootball + Mortal + Monopoly + Hogwarst + Minecraft)
    if total_bills < 0 :
        total_bills = BALANCE
        messagebox.showerror("There is not enough amount in balance")
    bills = tkinter.Label(frame4,text=f"Your Total Balance ${total_bills}",bg="#FF3399",fg="#0af716",font="Arial, 30" )
    bills.place(x=700, y=700)
    username1_label = tkinter.Label(frame4, text= f"{total_bills}", bg="#333333", fg="#FFFFFF", font=("Arial, 16"))
    username1_label.place(x=1880, y=0)



btn60 = tkinter.Button(frame4,text='Download',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 30", command=balance)
btn60.place(x=890, y=620)
#burda framelerimi şekillerimi duzenlemişem 122 - 475
for frame in (frame1,frame2,frame3,frame4, frame5, frame6,frame7,frame8,frame9, frame10, frame11):
    frame.grid(row=0, column=0, sticky="news")
frame1_title= tkinter.Label(frame2, text="This frame 2", bg="red")
frame1_title.grid()
btn1 = tkinter.Button(frame1,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 30", command=lambda:raise_frame(frame2))
btn1.place(x=20, y=350)
btn_image = tkinter.PhotoImage(file="img/brawl.png")


btn2 = tkinter.Button(frame2,bg="green",
                            image=btn_image)
btn2.grid(row=0, column=1, sticky="news")
frame2_btn = tkinter.Button(frame2,text='Main Menu', fg="black", bg="yellow",command= lambda:raise_frame(frame1))
frame2_btn.grid(row=0, column=0, sticky="news")
frame2_label = tkinter.Label(frame2, text="BRAWL STARS", fg="white", bg="#333333",font="Arial, 20")
frame2_label.grid(row=1, column=1)
label_among = tkinter.Label(frame2, text="AMONG US", fg="white", bg="#333333",font="Arial, 20")
label_among.grid(row=1, column=2)
button_img = tkinter.PhotoImage(file="img/among_us.png")
button2 = tkinter.Button(frame2, fg="black", bg="yellow",
                            image=button_img)
button2.grid(row=0, column=2, sticky="news")

pubg_btn = tkinter.PhotoImage(file="img/pubg.png")
button3 = tkinter.Button(frame2, fg="black", bg="#333333",
                            image=pubg_btn)
button3.grid(row=0, column=3, sticky="news")
pubg_label = tkinter.Label(frame2, text="PUBG MOBILE", fg="white", bg="#333333",font="Arial, 20")
pubg_label.grid(row=1, column=3)

clash_img = tkinter.PhotoImage(file="img/clas_of_clans.png")
button4 = tkinter.Button(frame2, fg="green", bg="blue",
                            image=clash_img)
button4.grid(row=0, column= 4, sticky="news")
clash_label = tkinter.Label(frame2, text="CLASH OF CLANS", fg="white", bg="#333333",font="Arial, 20")
clash_label.grid(row=1, column=4)

fortinete_img = tkinter.PhotoImage(file="img/fotinete.png")
button5 = tkinter.Button(frame2, fg="green", bg="purple",
                            image=fortinete_img)
button5.grid(row=2, column=1, sticky="news")
fortinete_label = tkinter.Label(frame2, text="FORTNITE", fg="white", bg="#333333",font="Arial, 20")
fortinete_label.grid(row=3, column=1)

minecraft_img = tkinter.PhotoImage(file="img/minecraft10.png")
button6 = tkinter.Button(frame2, fg="green", bg="green",
                            image=minecraft_img)
button6.grid(row=2, column=2, sticky="news")
minecraft_label = tkinter.Label(frame2, text="MINECRAFT\n10$", fg="white", bg="#333333",font="Arial, 20")
minecraft_label.grid(row=3, column=2)

monopoly_img = tkinter.PhotoImage(file="img/monopoly.png")
button7 = tkinter.Button(frame2, bg="RED",
                            image=monopoly_img)
button7.grid(row=2, column=3, sticky="news")
monopoly_label = tkinter.Label(frame2, text="MONOPOLY\n70$", fg="white", bg="#333333",font="Arial, 20")
monopoly_label.grid(row=3, column=3)

efootbol_img = tkinter.PhotoImage(file="img/efootball.png")
button7 = tkinter.Button(frame2, bg="#1d126b",
                            image=efootbol_img)
button7.grid(row=2, column=4, sticky="news")
EFOOTBALL_label = tkinter.Label(frame2, text="eFootball™ 2023\n100$ ", fg="white", bg="#333333",font="Arial, 20")
EFOOTBALL_label.grid(row=3, column=4)


hayday_img = tkinter.PhotoImage(file="img/Hay day.png")
button9= tkinter.Button(frame2, bg="#e7eb1c",
                            image=hayday_img)
button9.grid(row=4, column=1, sticky="news")
hayday_label = tkinter.Label(frame2, text="Hay Day", fg="white", bg="#333333",font="Arial, 20")
hayday_label.grid(row=5, column=1)


clash_royale_img = tkinter.PhotoImage(file="img/Clash royale.png")
button11 = tkinter.Button(frame2, bg="#04c922",
                            image=clash_royale_img)
button11.grid(row=4, column=2, sticky="news")
clashroyale_label = tkinter.Label(frame2, text="CLASH ROYALE", fg="white", bg="#333333",font="Arial, 20")
clashroyale_label.grid(row=5, column=2)



mortal_img = tkinter.PhotoImage(file="img/mortal kombat.png")
button10 = tkinter.Button(frame2, bg="#15e1e8",
                            image=mortal_img)
button10.grid(row=4, column=3, sticky="news")
mortal1 = tkinter.Label(frame2, text="MORTAL KOMBAT\n95$", fg="white", bg="#333333",font="Arial, 20")
mortal1.grid(row=5, column=3)


HOGWARST_img = tkinter.PhotoImage(file="img/HOGWARST LEGARY.png")
button12 = tkinter.Button(frame2, bg="#1d211d",
                            image=HOGWARST_img)
button12.grid(row=4, column=4, sticky="news")
hogwarst_label = tkinter.Label(frame2, text="Hogwarts Legacy\n$50", fg="white", bg="#333333",font="Arial, 20")
hogwarst_label.grid(row=5, column=4)

profil_img = tkinter.PhotoImage(file="img/profil1.png")
buton14 = tkinter.Button(frame2, bg="#1d211d", image=profil_img,command= lambda:raise_frame(frame3))
buton14.grid(row=0, column=5, sticky="news")
profil_label = tkinter.Label(frame2, text="Profile", fg="white", bg="#333333",font="Arial, 20")
profil_label.grid(row=1, column=5)

profil5_img = tkinter.PhotoImage(file="img/profil_bilgileri.png")
buton15 = tkinter.Button(frame3, bg="#1d211d", image=profil5_img)
buton15.grid(row=1, column=7, sticky="news")
button16 = tkinter.Button(frame3,text="Games", bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame2))
button16.grid(row=1, column=0)
button17 = tkinter.Button(frame3,text="Main Menu", bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame1))
button17.grid(row=2, column=0)

profil20_img = tkinter.PhotoImage(file="img/sepet.png")
buton18 = tkinter.Button(frame1,image=profil20_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton18.grid(row=4, column=0)

efootbol3_img = tkinter.PhotoImage(file="img/efootball3.png")
button0 = tkinter.Button(frame4, bg="#1d126b",
                            image=efootbol3_img)
button0.grid(row=0, column=1, sticky="news")
efootball3_label = tkinter.Label(frame4, text="eFootball™ 2023\n100$ ", fg="white", bg="#333333",font="Arial, 20")
efootball3_label.grid(row=1, column=1)
efoot = tkinter.Spinbox(frame4,from_=0, to=10, width=5)
efoot.grid(row=2, column=1)


mortal_img1 = tkinter.PhotoImage(file="img/mortal4.png")
button10 = tkinter.Button(frame4, bg="#15e1e8",
                            image=mortal_img1)
button10.grid(row=0, column=2, sticky="news")
mortal2 = tkinter.Label(frame4, text="MORTAL KOMBAT\n95$", fg="white", bg="#333333",font="Arial, 20")
mortal2.grid(row=1, column=2)
mortal5 = tkinter.Spinbox(frame4,from_=0, to=10, width=5)
mortal5.grid(row=2, column=2)

monopoly2_img = tkinter.PhotoImage(file="img/monopoly2.png")
button90 = tkinter.Button(frame4, bg="RED",
                            image=monopoly2_img)
button90.grid(row=0, column=3, sticky="news")
monopoly2_label = tkinter.Label(frame4, text="MONOPOLY\n70$", fg="white", bg="#333333",font="Arial, 20")
monopoly2_label.grid(row=1, column=3)
monopoly7 = tkinter.Spinbox(frame4,from_=0, to=10, width=5)
monopoly7.grid(row=2, column=3)

HOGWARST1_img = tkinter.PhotoImage(file="img/HOGWARST LEGARY1.png")
button30 = tkinter.Button(frame4, bg="#1d211d",
                            image=HOGWARST1_img)
button30.grid(row=0, column= 4, sticky="news")
hogwarst_label = tkinter.Label(frame4, text="Hogwarts Legacy\n$50", fg="white", bg="#333333",font="Arial, 20")
hogwarst_label.grid(row=1, column=4)
hogwarst9 = tkinter.Spinbox(frame4,from_=0, to=10, width=5)
hogwarst9.grid(row=2, column=4)


minecraft1_img = tkinter.PhotoImage(file="img/minecraft1.png")
button21 = tkinter.Button(frame4,bg="#0dfc11",
                            image=minecraft1_img)
button21.grid(row=3, column=1, sticky="news")
minecraft_label = tkinter.Label(frame4, text="MINECRAFT\n10$", fg="white", bg="#333333",font="Arial, 20")
minecraft_label.grid(row=4, column=1)
minecraft4 = tkinter.Spinbox(frame4,from_=0, to=10, width=5)
minecraft4.grid(row=5, column=1)
finish = tkinter.Button(frame4,text="Purchase", font="Arial, 30" ,fg="#FF3399",bg="#333333",command=button_clicked)
finish.grid(row=3,  column=6)



friends_img = tkinter.PhotoImage(file="img/dost.png")
button40 = tkinter.Button(frame5, fg="green", bg="green",
                            image=friends_img)
button40.grid(row=3, column=1, sticky="news")
friend_label = tkinter.Label(frame5, text=" Friends", fg="white", bg="#333333",font="Arial, 20")
friend_label.grid(row=4, column=1)
firiends = tkinter.Button(frame4,text="Friends", font="Arial, 30" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame5))
firiends.place(x=1720, y=450)

bank_img = tkinter.PhotoImage(file="img/BANK3.png")
button50 = tkinter.Button(frame4, fg="green", bg="green",
                            image= bank_img)
button50.grid(row=3, column=4, sticky="news")


efoot0_img = tkinter.PhotoImage(file="img/football.png")
button0 = tkinter.Button(frame4, fg="green", bg="green",
                            command=lambda :raise_frame(frame6),image= efoot0_img)
button0.grid(row=0, column=1, sticky="news")

efootbol3_img = tkinter.PhotoImage(file="img/efoot (2).png")
button25 = tkinter.Button(frame6, fg="green", bg="green",
                            image= efootbol3_img)
button25.grid(row=3, column=4, sticky="news")
efoot9_btn = tkinter.Button(frame6,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
efoot9_btn.place(x=1720, y=40)


profil00_img = tkinter.PhotoImage(file="img/sepet100.png")
buton13= tkinter.Button(frame5,image=profil00_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton13.place(x=1850, y=0)

btn1 = tkinter.Button(frame6,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn1.place(x=1720, y=100)

mortal_img16 = tkinter.PhotoImage(file="img/mortal10.png")
button109 = tkinter.Button(frame4, bg="#15e1e8",
                            command=lambda :raise_frame(frame7),image=mortal_img16)
button109.grid(row=0, column=2, sticky="news")
mortal200 = tkinter.Label(frame4, text="MORTAL KOMBAT\n95$", fg="white", bg="#333333",font="Arial, 20")
mortal200.grid(row=1, column=2)

mortal44_img = tkinter.PhotoImage(file="img/mortral7.png")
button54 = tkinter.Button(frame7,  bg="yellow",
                            image= mortal44_img)
button54.grid(row=3, column=4, sticky="news")
mortol_btn = tkinter.Button(frame7,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
mortol_btn.place(x=1720, y=40)

profil48_img = tkinter.PhotoImage(file="img/sepet32.png")
buton10 = tkinter.Button(frame7,image=profil48_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton10.place(x=1720, y=0)

btn1 = tkinter.Button(frame7,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn1.place(x=1720, y=100)

monopoly26_img = tkinter.PhotoImage(file="img/monopoly3.png")
button99 = tkinter.Button(frame4, bg="RED",
                          command=lambda: raise_frame(frame8), image=monopoly26_img)
button99.grid(row=0, column=3, sticky="news")
monopoly2_label = tkinter.Label(frame4, text="MONOPOLY\n70$", fg="white", bg="#333333",font="Arial, 20")
monopoly2_label.grid(row=1, column=3)

mortal4_img = tkinter.PhotoImage(file="img/monopoly9.png")
button2 = tkinter.Button(frame8,  bg="yellow",
                            image= mortal4_img)
button2.grid(row=3, column=4, sticky="news")
monpoly7_btn = tkinter.Button(frame8,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
monpoly7_btn.place(x=1720, y=40)

profil100_img = tkinter.PhotoImage(file="img/sepet5.png")
buton100 = tkinter.Button(frame8,image=profil100_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton100.place(x=1720, y=0)

btn7 = tkinter.Button(frame8,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn7.place(x=1720, y=100)

HOGWARST5_img = tkinter.PhotoImage(file="img/HOGWARST LEGARY1.png")
button300 = tkinter.Button(frame4, bg="#1d211d",
                           command=lambda: raise_frame(frame9),
                           image=HOGWARST5_img)
button300.grid(row=0, column=4, sticky="news")

hogwart_img = tkinter.PhotoImage(file="img/hogwarst6.png")
button65 = tkinter.Button(frame9,  bg="yellow",
                            image= hogwart_img)
button65.grid(row=3, column=4, sticky="news")

hogwast_btn = tkinter.Button(frame9,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
hogwast_btn.place(x=1720, y=40)

profil90_img = tkinter.PhotoImage(file="img/sepet5.png")
buton110 = tkinter.Button(frame9,image=profil90_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton110.place(x=1720, y=0)

btn7 = tkinter.Button(frame9,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn7.place(x=1720, y=100)


minecraft10_img = tkinter.PhotoImage(file="img/minecraft3.png")
button290 = tkinter.Button(frame4,bg="#0dfc11",
                           command=lambda: raise_frame(frame10),image=minecraft10_img)
button290.grid(row=3, column=1, sticky="news")

minecraft140_img = tkinter.PhotoImage(file="img/minecraft.png ")
button321 = tkinter.Button(frame10, bg="#1d211d",
                           image=minecraft140_img)
button321.grid(row=0, column=4, sticky="news")
efoot9_btn = tkinter.Button(frame10,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
efoot9_btn.place(x=1720, y=40)

profil9_img = tkinter.PhotoImage(file="img/sepet7.png")
buton11 = tkinter.Button(frame10,image=profil9_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton11.place(x=1720, y=0)

btn7 = tkinter.Button(frame10,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn7.place(x=1720, y=100)

profil45_img = tkinter.PhotoImage(file="img/sepet10.png")
buton111= tkinter.Button(frame2,image=profil45_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton111.place(x=1830, y=0)


firiends1 = tkinter.Button(frame2,text="Friends", font="Arial, 30" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame5))
firiends1.grid(row=2, column=5)

firiends1 = tkinter.Button(frame3,text="Friends", font="Arial, 20" ,fg="black",bg="#07e02f",command=lambda :raise_frame(frame5))
firiends1.grid(row=0, column=0)

profil40_img = tkinter.PhotoImage(file="img/sepet20.png")
buton114= tkinter.Button(frame3,image=profil40_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton114.place(x=1850, y=0)




firiends80 = tkinter.Button(frame1,text="Friends",fg="#FF3399",font="Arial, 30" ,bg="#333333",activebackground="green",command=lambda :raise_frame(frame5))
firiends80.place(x=20, y=450)



frame2_btn = tkinter.Button(frame5,text='Main Menu',font="Arial, 15",fg="#FF3399",bg="#333333",command= lambda:raise_frame(frame1))
frame2_btn.place(x=1810, y=40)

btn7 = tkinter.Button(frame5,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 15", command=lambda:raise_frame(frame2))
btn7.place(x=1800, y=85)

profil455_img = tkinter.PhotoImage(file="img/sebetw.png")
buton465 = tkinter.Button(frame2,image=profil455_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton465.place(x=1830, y=0)


profil235_img = tkinter.PhotoImage(file="img/sebetw.png")
buton465 = tkinter.Button(frame6,image=profil235_img,bg="#07e02f",font="Arial, 20",command= lambda:raise_frame(frame4))
buton465.place(x=1720, y=0)

menu_btn = tkinter.Button(frame4,text='Main Menu', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame1))
menu_btn.place(x=1720, y=380)


btn1000 = tkinter.Button(frame4,text='Game Menu',fg="#FF3399",bg="#333333",activebackground="green",font="Arial, 25", command=lambda:raise_frame(frame2))
btn1000.place(x=1720, y=630)

frame_11 =  tkinter.Button(frame1,text='Information about the game', font="Arial, 25" ,fg="#FF3399",bg="#333333",command=lambda :raise_frame(frame11))
frame_11.place(x=1400, y=380)

about_the_game= tkinter.PhotoImage(file="img/oyun_haqqında.png")
game_btn= tkinter.Button(frame11,image= about_the_game,bg="#07e02f",font="Arial, 20")
game_btn.place(x=0, y=0)

geri_btn = tkinter.PhotoImage(file="img/GERI.png")
back_btn= tkinter.Button(frame11,image= geri_btn,bg="#07e02f",font="Arial, 20", command=lambda :raise_frame(frame1))
back_btn.place(x=1760, y=0)

cart_img = tkinter.PhotoImage(file="img/cart.png")
cart_btn= tkinter.Button(frame4,image= cart_img,bg="#07e02f",font="Arial, 20")
cart_btn.place(x=600, y=580)

cart1_img = tkinter.PhotoImage(file="img/cart2.png")
cart1_btn= tkinter.Button(frame4,image= cart1_img,bg="#07e02f",font="Arial, 20")
cart1_btn.place(x=770, y=580)

dollar_img = tkinter.PhotoImage(file="img/deyer2.png")
dollar_btn= tkinter.Button(frame4,image= dollar_img,bg="#07e02f",font="Arial, 20")
dollar_btn.place(x=950, y=410)

registartion_label = tkinter.Label(frame1, text="Registration", fg="#FF3399", bg="#333333",font="Arial, 30")
registartion_label.place(x=0, y=10)
raise_frame(frame1)


mail = tkinter.Label(text="Mail:", fg="#FF3399",bg="#333333", font="Arial, 15")
mail.place(x=10, y=190)
şifre = tkinter.Label(text="Password:", fg="#FF3399", bg="#333333", font="Arial, 15")
şifre.place(x=10, y=140)
ad = tkinter.Label(text="Name:", fg="#FF3399", bg="#333333", font="Arial, 15")
ad.place(x=10, y=90)
mail_entr1 = tkinter.Entry()
mail_entr1.place(x=70, y=200)
password1=tkinter.Entry(show="*")
password1.place(x=120,y=145)
name =tkinter.Entry()
name.place(x=80,y=95)
#burda qeydiyyatı yoxlamışam get alıb dəyişənə yazmışam və boşluqların olmamasını yoxlamışam və fayla yazmışam
def registration():
    name2 = name.get()
    password5 = password1.get()
    if name2 == "" or password5 == "":
        messagebox.showerror("Wrong")
    else:
        messagebox.showinfo("Excellent")
    name2.strip()
    password5.strip()
    name.delete(0, "end")
    password1.delete(0, "end")
    mail_entr1.delete(0, "end")
    print(name2, password5)
    with open("Text_name.dat","wb") as file5:
        pickle.dump(name2, file5)
        pickle.dump(password5, file5)


kec_btn = tkinter.Button(window,text='Rekord', fg="black",activebackground="green",font="Arial, 15" ,command=registration)
kec_btn.place(x=200, y=200)

login_label = tkinter.Label(frame1,text="Login",bg= "#333333", fg="#FF3399", font ="Arial, 30")
username_label = tkinter.Label(frame1,text="Usarname:", bg= "#333333", fg="#FFFFFF", font =("Arial, 16"))
username_entry = tkinter.Entry(frame1,font =("Arial, 16"))
password_entry = tkinter.Entry(frame1,show="*", font =("Arial, 16"))
password_label = tkinter.Label(frame1,text="Password:", bg= "#333333", fg="#FFFFFF",  font =("Arial, 16"))
login_buton = tkinter.Button(frame1,text="Login", bg="#FF3399", fg="#FFFFFF",font="Arial, 15", command=save_info)


login_label.grid(row=0, column=0,columnspan=2, sticky="news",padx=1000, pady=40)
username_label.grid(row=1, column=0, padx=1000, pady=10)
username_entry.place(x= 1120, y= 140)
password_label.grid(row=2, column=0)
password_entry.place(x= 1120, y= 180)
login_buton.grid(row=3, column=0,columnspan=2, pady=30)

def quit():
    window.quit()

iptal = tkinter.Button(window,text="EXIT",activebackground="red",font="Arial, 15",command=quit)
iptal.place(x=1100,y=240)

tkinter. mainloop()
