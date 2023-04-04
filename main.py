from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
# database
import mysql.connector as mysql

conn = mysql.connect(user="root", password="root", host='localhost', database='survey')
c = conn.cursor()
#print(conn)

questions = [
    "1.	What is your position within the company?",
    "2.	Does your company have a security team?",
    "3.	Do you know who to contact in case you are hacked or if your computer is infected? ",
    "4.	Have you ever found  a virus or Trojan on your computer at work?",
    "5.	Do you know how to tell if your computer is hacked or infected? ",
]

answers_choice = [
    ["a. Full/Part time employee ", "b. Contractor/Vendor ", "c. Other "],
    ["a. Yes, we have a company security team. ", "b. No, we do not have a company security team. ",
     "c. I do not know."],
    ["a. Yes, I know who to contact. ", "b. No, I do not know who to contact. ", "c. I am not sure "],
    ["a. Yes, my computers has been infected before", "b. No, my computer has never been infected. ",
     "c. I do not know what a virus or Trojan is. "],
    ["a. Yes, I know what to look for to see if my computer is hacked or infected. ",
     "b. No, I do not know what to look for to see if my computer is hacked or infected. ", "c. I am not sure"]
]

answers = [1, 0, 0, 1, 0]

user_answers = []

indexes = []

gee = []


def validate(name, age, gender, email):
    name_text = name.get()
    age = age.get()
    gender_text = gender.get()
    email_text = email.get()

    if name_text == "":
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR NAME")
    elif age == "":
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR AGE")
    elif gender_text == "":
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR GENDER")
    elif email_text == "":
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR EMAIL")
    elif '@' not in email_text:
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR EMAIL")
    elif 'gmail.com' not in email_text:
        messagebox.showerror(title="No Value ", message="PLEASE ENTER YOUR EMAIL")
    else:
        survey_page()


def survey_page():
    for i in win.winfo_children():
        i.destroy()

    survey_label = Label(win, text="The survey is composed of General,\n Lifestyle Questions,etc \n"
                                   "Rules:\n"
                                   "Purpose of Surveying in the field of Civil Engineering\n"
                                   "-To determine the relative positions of the existing futures of the ground.\n"
                                   "-To layout our marked positions of proposed structures on the ground.\n"
                                   "-To determine areas, volumes and other related quantities.\n"
                                   "-To prepare a map of a country of detailed out location of cities, towns,\n"
                                   " villages and major roads.\n"
                                   "-To prepare the engineering detailed plans and sections of various\n sections such"
                                   " as roads, railways, bridges, dams and other structure.\n"
                                   "-To prepare a topographical map showing details of hills, valleys \nand rivers.\n",
                         font="Verdana 15", background="#ffc14b")
    survey_label.pack()
    Button(win, text="OK", command=next_question).pack()


def next_question():
    for i in win.winfo_children():
        i.destroy()

    question_show()
    Button(text="Next", command=button_select).pack()


def gen():
    global indexes
    for i in range(5):
        indexes.append(i)


l1, r1, r2, r3 = None, None, None, None


def question_show():
    global user_answers
    global l1, r1, r2, r3
    l1 = Label(
        win,
        text=(questions[0]),
        font=("Comic sans MS", 15, "bold"),
        background="#ffffff",
        width=500,
        justify="center",
        wraplength=1000,
    )
    l1.pack()


    r1 = Radiobutton(
        win,
        text=answers_choice[0][0],
        value=0,
        variable=var1

    )
    r1.pack()

    r2 = Radiobutton(
        win,
        text=answers_choice[0][1],
        value=1,
        variable=var1
    )
    r2.pack()

    r3 = Radiobutton(
        win,
        text=answers_choice[0][2],
        value=2,
        variable=var1

    )
    r3.pack()


def button_select():
    global radiovar, user_answers
    user_answers.append(var1.get())
    d = 1

    if len(gee) == 0:
        gee.append(d)
        l1.config(text=questions[gee[0]])
        r1['text'] = answers_choice[gee[0]][0]
        r2['text'] = answers_choice[gee[0]][1]
        r3['text'] = answers_choice[gee[0]][2]
    else:
        if gee[0] == 5:
            #print(indexes)
            print(gee)
            print(user_answers)
            thankyou_page()


        else:
            y = gee[0] + 1
            gee[0] = y
            l1.config(text=questions[gee[0]])
            r1['text'] = answers_choice[gee[0]][0]
            r2['text'] = answers_choice[gee[0]][1]
            r3['text'] = answers_choice[gee[0]][2]


win = Tk()
win.title("Survey form")
win.geometry("750x600")
win.maxsize(750, 600)
win.minsize(750, 600)
win.config(background="#ffc14b")
var1 = IntVar()

def user_page():
    name = StringVar()
    email = StringVar()
    gender = StringVar()

    Label(win, text="SURVEY FORM ", font="Helvetica  30", background="#ffc14b").place(x=450 / 2, y=40 / 2)

    Label(win, text="Name:", background="#ffc14b", font="Helvetica  15").place(x=220, y=120)
    Entry(win, textvariable=name, font="15").place(x=300, y=120)
    Label(win, text="Age:", background="#ffc14b", font="Helvetica  15").place(x=220, y=160)
    e1 = Entry(win, font="15")
    e1.place(x=300, y=160)
    Label(win, text="Gender:", background="#ffc14b", font="Helvetica  15").place(x=220, y=200)
    Entry(win, textvariable=gender, font="15").place(x=300, y=200)
    Label(win, text="Email:", background="#ffc14b", font="Helvetica  15").place(x=220, y=240)
    Entry(win, textvariable=email, font="15").place(x=300, y=240)
    Button(win, text="Submit", command=lambda: validate(name, e1, gender, email), width=12).place(x=250, y=300)
    Button(win, text='Close', command=lambda: win.destroy(), width=13).place(x=400, y=300)
    win.mainloop()

def thankyou_page():
    #create page and delete all widgets then add a label saying thankyou
    for i in win.winfo_children():
        i.destroy()

    c.execute(f"insert  into user_info_answers values('{name_text}','{age}','{gender_text}','{email_text}','{user_answers[0]} {user_answers[1]} {user_answers[2]} {user_answers[3]} {user_answers[4]}')")
    conn.commit()
    
    Label(win, text="THANK YOU FOR YOUR RESPONSE", font="Helvetica  20", background="#ffc14b").place(x=450 / 2, y=40 / 2)
    Button(win, text='Close', command=lambda: win.destroy(), width=13).place(x=400, y=300)



user_page()
