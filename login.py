from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed by Lalitha")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        # =========== Images ===========
        self.phone_image = ImageTk.PhotoImage(file="img/images/phone.png")  
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0)  
        self.lbl_Phone_image.place(x=200, y=50)

        # ======= Login Frame ========
        self.employee_id = StringVar()
        self.password = StringVar()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=650, y=90, width=350, height=460)

        title = Label(login_frame, text="Login System", font=("Elephant", 20, "bold"), bg="white")
        title.place(x=50, y=30)

        lbl_user = Label(login_frame, text="Employee ID", font=('Andalus', 15), bg="white", fg="#767171")
        lbl_user.place(x=30, y=100)

        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15), bg="#ECF0F1")
        txt_employee_id.place(x=30, y=130, width=280)

        lbl_pass = Label(login_frame, text="Password", font=("Andalus", 15), bg="white", fg='#767171')
        lbl_pass.place(x=30, y=180)

        txt_pass = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), bg="white", fg="#767171")
        txt_pass.place(x=30, y=210, width=280)

        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Arial Rounded MT Bold", 15), bg="#00759E", fg="white")
        btn_login.place(x=100, y=260, width=150)

        hr = Label(login_frame, bg="lightgray")
        hr.place(x=50, y=310, width=250, height=2)

        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15, "bold"))
        or_.place(x=150, y=300)

        # ======= Forget Password Button (Fixed) =======
        btn_forget = Button(login_frame, text="Forget Password?",command=self.forget_window, font=("times new roman", 13), bg="white", fg="#00759E",bd=0, activebackground="white", activeforeground="#00759E")
        btn_forget.place(x=100, y=330)

        # ========= Frame 2 ============
        register_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        register_frame.place(x=650, y=570, width=350, height=60)

        lbl_reg = Label(register_frame, text="SUBSCRIBE | LIKE | SHARE", font=("times new roman", 13), bg='white')
        lbl_reg.place(x=0, y=20, relwidth=1)

        # ============ Animation Images ========
        self.images = [
            ImageTk.PhotoImage(file="img/images/im1.png"),
            ImageTk.PhotoImage(file="img/images/im2.png"),
            ImageTk.PhotoImage(file="img/images/im3.png")
        ]
        
        self.image_index = 0  # Keep track of current image

        self.lbl_change_image = Label(self.root, bg="white")
        self.lbl_change_image.place(x=367, y=153, width=240, height=428)

        self.animate()  # Start the animation

    def animate(self):
        """Handle image animation"""
        self.image_index = (self.image_index + 1) % len(self.images)
        self.lbl_change_image.config(image=self.images[self.image_index])
        self.lbl_change_image.after(2000, self.animate)

    def login(self):
        """Handle login logic"""
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                if user is None:
                    messagebox.showerror("Error", "Invalid USERNAME/PASSWORD", parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def forget_window(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute("SELECT email FROM employee WHERE eid=?", (self.employee_id.get(),))
                email = cur.fetchone()
                if email is None:
                    messagebox.showerror("Error", "Invalid Employee ID,try again", parent=self.root)
                else:
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("RESET PASSWORD")
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()

                    title=Label(self.forget_win,text="RESET PASSWORD",font=('goudy old style',15,'bold'),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP sent on registerd email",font=("times new roamn",15)).place(x=20,y=50)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roamn",15),bg='lightyellow').place(x=20,y=90,width=250,height=30)
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",font=("times new roamn",15),bg='lightblue')
                    self.btn_reset.place(x=280,y=90,width=100,height=30)

                    lbl_new_pass = Label(self.forget_win, text="New Password", font=("times new roman", 15))
                    lbl_new_pass.place(x=20, y=140)

                    txt_new_pass = Entry(self.forget_win, textvariable=self.var_new_pass, font=("times new roman", 15), bg="lightyellow")
                    txt_new_pass.place(x=20, y=170, width=250, height=30)
                    
                    lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roamn",15)).place(x=20,y=220)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roamn",15),bg='lightyellow').place(x=20,y=250,width=250,height=30)

                    
                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED,font=("times new roamn",15),bg='lightblue')
                    self.btn_update.place(x=150,y=300,width=100,height=30)

                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
