from tkinter import *

class NLPApp:


    def __init__(self):
        
        self.root = Tk()
        self.root.title('NLPApp') # Changing title to 'NLPApp'
        self.root.iconbitmap("C:/Ashu/Core Java/Scaler-Py/OOPS-Project/nlp-gui-komprehend/resources/favicon.ico")
        self.root.geometry('350x600') # height and width of ui
        self.root.configure(bg='#85442D')
        

        self.login_gui()

        self.root.mainloop()


    def login_gui(self):

        self.clear()

        heading = Label(self.root, text='NLP-App', bg='#85442D' , fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2 = Label(self.root,text='Enter Passsword')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=35,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)   

        # to add Login Button ->  we use Button() class
        login_btn = Button(self.root, text='Login',width=30,height=2)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Register now',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

        
    def register_gui(self):
        # To clear gui
        self.clear()

        heading = Label(self.root, text='NLP-App', bg='#85442D' , fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=35)
        self.name_input.pack(pady=(5,10),ipady=3)
        

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=3)

        label2 = Label(self.root,text='Enter Passsword')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=35,show='*')
        self.password_input.pack(pady=(5,10),ipady=3)   

        # to add Login Button ->  we use Button() class
        register_btn = Button(self.root, text='Register me',width=30,height=2)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Already a member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Login now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def clear(self):
        # Logic To clear gui while registering
        for i in self.root.pack_slaves():
            i.destroy()







nlp = NLPApp()