from tkinter import *
from tkinter import messagebox

from db import Database
from myapi import Api


class NlpApp:
    def __init__(self):
        # creating Database class object
        self.dbo = Database()
        # creating api class object
        self.apio = Api()

        # creating gui
        self.root = Tk()
        self.root.title('NLP App - Created by Sambhav Gupta')
        self.root.geometry('400x600')
        self.root.configure(bg='#142249')
        self.root.iconbitmap('resources\\nlpapp.ico')
        self.login_gui()
        self.root.mainloop()

    def clear_screen(self):
        # clears the screen widgets
        for i in self.root.pack_slaves():
            i.destroy()

    def login_gui(self):
        self.clear_screen()
        # making heading of the gui
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(15, 30))

        # username
        lusername = Label(text='Username', font=(40), bg='#142249', fg='white')
        lusername.pack()
        self.input_username = Entry(width=50)
        self.input_username.pack(pady=(15, 30))

        # password
        lpassword = Label(text='Password', font=(40), bg='#142249', fg='white', )
        lpassword.pack()
        self.input_password = Entry(width=50, show='*')
        self.input_password.pack(pady=(15, 30))

        # Login button
        login = Button(text='Login', height=1, width=15, font=(20), command=self.onclick_login)
        login.pack(pady=(10, 70))

        # register button
        label1 = Label(text='if not Registered,click to register', font=('verdana', 7, 'bold'), fg='white',
                       bg='#142249')
        label1.pack()
        register = Button(text='Register', height=1, width=15, font=(20), command=self.registration_gui)
        register.pack(pady=(10, 5))

    def registration_gui(self):
        self.clear_screen()

        # making heading of the gui
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(15, 30))

        # name input
        lname = Label(text='Enter You Name', font=(40), bg='#142249', fg='white')
        lname.pack()
        self.input_name = Entry(width=50)
        self.input_name.pack(pady=(15, 30))

        # input email
        lemail = Label(text='Enter You email', font=(40), bg='#142249', fg='white', )
        lemail.pack()
        self.input_email = Entry(width=50)
        self.input_email.pack(pady=(15, 30))

        # password
        lpassword = Label(text='Password', font=(40), bg='#142249', fg='white', )
        lpassword.pack()
        self.input_password = Entry(width=50, show='*')
        self.input_password.pack(pady=(15, 30))

        # register button
        register = Button(text='Register', height=1, width=15, font=(20), command=self.onclick_register)
        register.pack(pady=(10, 10))

        # login if not registered

        label2 = Label(text='if not Registered,click to register', font=('verdana', 7, 'bold'), fg='white',
                       bg='#142249')
        label2.pack()
        # Login button
        login = Button(text='Login', height=1, width=15, font=(20), command=self.login_gui)
        login.pack()

    def onclick_register(self):
        name = self.input_name.get()
        email = self.input_email.get()
        password = self.input_password.get()

        if len(email) == 0:
            messagebox.showerror('Error', 'Enter the data')

        else:
            response = self.dbo.add_data(name, email, password)
            if response:
                messagebox.showinfo('Success', 'successfully registered')
            else:
                messagebox.showinfo('Error', 'Email Exists')

    def onclick_login(self):
        username = self.input_username.get()
        password = self.input_password.get()

        response = self.dbo.search(username, password)
        if response:
            messagebox.showinfo('success', 'login successfully')
            self.user_dashboard()

        else:
            messagebox.showerror('error', 'incorrect email')

    def user_dashboard(self):
        self.clear_screen()

        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(15, 30))

        # sentiment analysis
        sentiment_btn = Button(text='Sentiment Analysis', height=1, width=15, font=(20),
                               command=self.onclick_sentiment_btn)
        sentiment_btn.pack(pady=(10, 30))

        # emotion analysis
        emotion_btn = Button(text='Emotion Analysis', height=1, width=15, font=(20), command=self.onclick_emotion_btn)
        emotion_btn.pack(pady=(10, 30))

        # abusive analysis
        abusive_btn = Button(text='Abusive Analysis', height=1, width=15, font=(20), command=self.onclick_abusive_btn)
        abusive_btn.pack(pady=(10, 30))

        # name entity recognition
        name_entity_finder_btn = Button(text='Name entity Recognition', height=1, width=30, font=(15),
                                        command=self.onclick_name_entity_finder_btn)
        name_entity_finder_btn.pack(pady=(10, 30))

    def onclick_sentiment_btn(self):
        self.clear_screen()
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(10, 20))

        lsentiment = Label(text='Input Text For Sentiment Analysis', font=('verdana', 10, 'bold'))
        lsentiment.pack(pady=(10, 20))

        self.input_sentiment_txt = Entry(width=50)
        self.input_sentiment_txt.pack()

        self.analyze_btn = Button(text='Analyse now', height=2, width=10, command=self.onclick_sentiment_analyse_btn)
        self.analyze_btn.pack(pady=(30, 10))

        self.output_sentiment = Label(text='', font=('verdana', 10, 'bold'), fg='white', bg='#142249')
        self.output_sentiment.pack(pady=(10, 20))

        self.back_btn = Button(text='Back', command=self.user_dashboard)
        self.back_btn.pack(pady=(30, 10))

    def onclick_emotion_btn(self):
        self.clear_screen()
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(10, 20))

        lemotion = Label(text='Input Text For Emotion Analysis', font=('verdana', 10, 'bold'))
        lemotion.pack(pady=(10, 20))

        self.input_emotion_txt = Entry(width=50)
        self.input_emotion_txt.pack()

        self.analyze_btn = Button(text='Analyse now', command=self.onclick_emotion_analyse_btn, height=2, width=10)
        self.analyze_btn.pack(pady=(10, 30))

        self.output_emotion = Label(text='', font=('verdana', 10, 'bold'), fg='white', bg='#142249')
        self.output_emotion.pack(pady=(10, 20))

        self.back_btn = Button(text='Back', command=self.user_dashboard)
        self.back_btn.pack(pady=(30, 10))

    def onclick_abusive_btn(self):
        self.clear_screen()
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(10, 20))

        labusive = Label(text='Input Text for Abusive Analysis', font=('verdana', 10, 'bold'))
        labusive.pack(pady=(10, 30))

        self.input_abusive_txt = Entry(width=50)
        self.input_abusive_txt.place(width=150, height=50)
        self.input_abusive_txt.pack()

        self.analyze_btn = Button(text='Analyse now', command=self.onclick_abuse_analyse_btn, height=2, width=10)
        self.analyze_btn.pack(pady=(30, 10))

        self.output_abusive = Label(text='', font=('verdana', 10, 'bold'), fg='white', bg='#142249')
        self.output_abusive.pack(pady=(10, 20))

        self.back_btn = Button(text='Back', command=self.user_dashboard)
        self.back_btn.pack(pady=(30, 10))

    def onclick_name_entity_finder_btn(self):
        self.clear_screen()
        heading = Label(text='NLP App', font=('verdana', 60, 'bold'))
        heading.pack(pady=(10, 20))

        lnameentity = Label(text='Input Text for Name entity Recogniton', font=('verdana', 10, 'bold'))
        lnameentity.pack(pady=(10, 30))

        self.input_name_entity_finder_txt = Entry(width=50)
        self.input_name_entity_finder_txt.pack()

        self.analyze_btn = Button(text='Analyse now', command=self.onclick_name_entity_finder_analyse_btn, height=2,
                                  width=10)
        self.analyze_btn.pack(pady=(30, 10))

        self.output_name_entity_finder = Label(text='', font=('verdana', 10, 'bold'), fg='white', bg='#142249')
        self.output_name_entity_finder.pack(pady=(10, 20))

        self.back_btn = Button(text='Back', command=self.user_dashboard)
        self.back_btn.pack(pady=(30, 10))

    def onclick_sentiment_analyse_btn(self):
        txt = self.input_sentiment_txt.get()
        response = self.apio.sentiment_analysis(txt)

        newtxt = ''
        for i in response['sentiment']:
            newtxt = newtxt + i + ' --> ' + str(round(response['sentiment'][i] * 100)) + '%' + '\n'

        self.output_sentiment['text'] = newtxt

    def onclick_emotion_analyse_btn(self):
        txt = self.input_emotion_txt.get()
        response = self.apio.emotion_analysis(txt)

        newtxt = ''
        for i in response['emotion']:
            newtxt = newtxt + i + ' --> ' + str(round((response['emotion'][i] * 100))) + '%' + '\n'

        self.output_emotion['text'] = newtxt

    def onclick_abuse_analyse_btn(self):
        txt = self.input_abusive_txt.get()
        response = self.apio.abuse_analysis(txt)

        newtxt = ''
        for i in response:
            newtxt = newtxt + i + ' --> ' + str(round((response[i] * 100))) + '%' + '\n'

        self.output_abusive['text'] = newtxt

    def onclick_name_entity_finder_analyse_btn(self):
        txt = self.input_name_entity_finder_txt.get()

        response = self.apio.name_entity_finder(txt)
        print(response)

        self.output_name_entity_finder['text'] = response


myapp = NlpApp()
myapp()
