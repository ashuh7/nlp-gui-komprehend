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

        heading = Label(self.root, text='NLP-App', bg='#85442D' , fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))
        

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=3)




nlp = NLPApp()