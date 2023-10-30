import tkinter as ctk
import customtkinter as tk
tk.set_appearance_mode("Dark")
l=["",""]
def main():
    m=tk.CTk()
    m.title('Fake News Detection')
    m.geometry("800x500")
        
    def fp():
        for w in m.winfo_children():
            w.destroy()
        
        f = tk.CTkLabel(m,
                  text = "Fake " , font=("Helvetica", 60)).place(x = 40,
                                           y = 60)
        f1 = tk.CTkLabel(m,
                  text = "News Detection" , font=("Helvetica", 60)).place(x = 40,
                                           y = 150)
        btn = tk.CTkButton(m, text='Next', width=180,height=35 , command =sp)
        btn.place(x=600, y=450)
        m.mainloop()
        

    def sp():
        tp(0)
        
    
    def tp(f):
        
        #print(l[0],l[1])
        if f==0:
            import pickle
            for w in m.winfo_children():
                w.destroy()
            model = pickle.load(open('C:\\Users\\B NAGA RAKSHITHA\\Desktop\\fake news detection\\fake news detection\\model', 'rb'))
            def predict_cls():
                inp = T.get("1.0", "end-1c")
        #inp = inp.lower()
        #inp = punctuation_removal(inp)


                if inp is not None:
                    txt = [inp]
                p=model.predict(txt)
                if p==1:
                    s="the news is predicted as FAKE!!"
                else:
                    s="the news is predicted as REAL!!"
                f2=tk.CTkLabel(m,
                  text = s , font=("Helvetica", 20)).place(x = 250,
                                           y =400 )
                m.mainloop()

            
            
            f = tk.CTkLabel(m,
                  text = "Enter the News here to Test " , font=("Helvetica", 20)).place(x = 40,
                                           y = 30)
            T = tk.CTkTextbox(m, height = 300, width = 760)
            T.place(x=20,y=70)
            btn = tk.CTkButton(m, text='Test', width=180,height=35 ,command= predict_cls)
            btn.place(x=600, y=450)
            btn1 = tk.CTkButton(m, text='Back', width=180,height=35 , command =sp)
            btn1.place(x=25, y=450)
        
            m.mainloop()
            
            
            

        def predict_cls():
            inp = T.get("1.0", "end-1c")
            #inp = inp.lower()
            #inp = punctuation_removal(inp)


            if inp is not None:
                txt = [inp]
                p=model.predict(txt)
            if p==1:
                s="the news is predicted as FAKE!!"
            else:
                s="the news is predicted as REAL!!"
            f2=tk.CTkLabel(m,
                  text = s , font=("Helvetica", 20)).place(x = 250,
                                           y =400 )
            m.mainloop()

        f = tk.CTkLabel(m,
                  text = "Enter the News here to Test " , font=("Helvetica", 20)).place(x = 40,
                                           y = 30)
        T = tk.CTkTextbox(m, height = 300, width = 760)
        T.place(x=20,y=70)
        btn = tk.CTkButton(m, text='Test', width=180,height=35 ,command= predict_cls)
        btn.place(x=600, y=450)
        btn1 = tk.CTkButton(m, text='Back', width=180,height=35 , command =sp)
        btn1.place(x=25, y=450)
        
        m.mainloop()
        
        
    fp()
main()
    
