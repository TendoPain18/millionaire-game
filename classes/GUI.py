from classes.Questions import Questions
from classes.Audio import Audio
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import random


class GUI:
    def __init__(self):
        self.audio = Audio()
        self.my_questions = Questions()
        self.my_questions.readfile()
        self.start()

    def start(self):
        start_window = Tk()
        start_window.geometry('800x400+270+140')
        start_window.resizable(False, False)
        start_window.iconbitmap('images/icon.ico')
        start_window.title('Who Wants To Be A Millionaire')
        start_window.config(bg='black')

        start_BG = Image.open('images/start_BG.png')
        start_BG1 = start_BG.resize((800, 400))
        start_BG2 = ImageTk.PhotoImage(start_BG1)
        start_BG_label = Label(start_window, image=start_BG2)
        start_BG_label.pack()

        start_button_image = Image.open('images/start_button.png')
        start_button_image1 = start_button_image.resize((200, 90))
        start_button_image2 = ImageTk.PhotoImage(start_button_image1)
        start_button = Button(start_window, image=start_button_image2, width=180, height=75, bd=0, bg='#000042',
                              command=lambda: (start_window.destroy(), self.GameWindow()), activebackground='#000042')
        start_button.place(x=623, y=3)

        exit_button_image = Image.open('images/exit_button.png')
        exit_button_image1 = exit_button_image.resize((92, 92))
        exit_button_image2 = ImageTk.PhotoImage(exit_button_image1)
        exit_button = Button(start_window, image=exit_button_image2, command=lambda: start_window.destroy(), width=58,
                             height=57, bd=0, bg='white', activebackground='white')
        exit_button.place(x=10, y=10)

        start_window.mainloop()

    def GameWindow(self):
        def which_choice(event):
            # region Helps clear after each question
            bar_A.place_forget()
            bar_A_label.place_forget()
            bar_B.place_forget()
            bar_B_label.place_forget()
            bar_C.place_forget()
            bar_C_label.place_forget()
            bar_D.place_forget()
            bar_D_label.place_forget()
            oncall_button.place_forget()
            choose_A_button.config(cursor='hand2')
            choose_A_button.place(x=112, y=457)
            choose_B_button.config(cursor='hand2')
            choose_B_button.place(x=494, y=457)
            choose_C_button.config(cursor='hand2')
            choose_C_button.place(x=112, y=527)
            choose_D_button.config(cursor='hand2')
            choose_D_button.place(x=494, y=527)
            # endregion
            answer = event.widget['text']
            W_Q = self.my_questions.All_Q.index(question.cget('text'))
            if answer == self.my_questions.All_R[W_Q]:
                if question.cget('text') == self.my_questions.All_Q[14]:
                    n0_label.config(image=n[15])

                    def play_again():
                        self.my_questions.readfile()

                        self.audio.PlayTheme()
                        H1_button.config(state=NORMAL, image=H1, cursor='hand2')
                        H2_button.config(state=NORMAL, image=H2, cursor='hand2')
                        H3_button.config(state=NORMAL, image=H3, cursor='hand2')
                        question.config(text=self.my_questions.All_Q[0])
                        choose_A_button.config(text=self.my_questions.All_A[0], cursor='hand2')
                        choose_B_button.config(text=self.my_questions.All_B[0], cursor='hand2')
                        choose_D_button.config(text=self.my_questions.All_C[0], cursor='hand2')
                        choose_C_button.config(text=self.my_questions.All_D[0], cursor='hand2')
                        n0_label.config(image=n0)
                        win_frame.destroy()

                    def close_():
                        win_frame.destroy()
                        game_window.destroy()

                    # region win window
                    self.audio.PlayThemeWin()
                    win_frame = Frame(game_window, bg='black', width=500, height=400, bd=2, highlightbackground='white',
                                      highlightthickness=4)
                    win_frame.place(x=170, y=95)
                    win_frame.grab_set()

                    bg_label_ = Label(win_frame, image=BG, bd=0, bg='black')
                    bg_label_.place(x=142, y=67)

                    how_much_label_ = Label(win_frame, bd=0, bg='black', text='Millionaire__Millionaire',
                                            font=('arial', 22, 'bold'), fg='white')
                    how_much_label_.place(x=85, y=270)

                    you_win = Label(win_frame, text='You  Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                    you_win.place(x=125, y=0)

                    play_again_button = Button(win_frame, text='Play Again', font=('arial', 18, 'bold'), bg='black',
                                               fg='white', bd=0, activebackground='black', cursor='hand2',
                                               activeforeground='white', command=play_again)
                    play_again_button.place(x=170, y=310)

                    close_button = Button(win_frame, text='Close', font=('arial', 16, 'bold'), bg='black', fg='white',
                                          bd=0, activebackground='black', cursor='hand2', activeforeground='white',
                                          command=close_)
                    close_button.place(x=203, y=351)

                    H1_button.config(cursor='')
                    H2_button.config(cursor='')
                    H3_button.config(cursor='')
                    choose_A_button.config(cursor='')
                    choose_B_button.config(cursor='')
                    choose_C_button.config(cursor='')
                    choose_D_button.config(cursor='')

                    # endregion
                else:
                    # region move to next question
                    question.config(text=self.my_questions.All_Q[W_Q + 1])
                    choose_A_button.config(text=self.my_questions.All_A[W_Q + 1])
                    choose_B_button.config(text=self.my_questions.All_B[W_Q + 1])
                    choose_C_button.config(text=self.my_questions.All_C[W_Q + 1])
                    choose_D_button.config(text=self.my_questions.All_D[W_Q + 1])
                    n0_label.config(image=n[W_Q + 1])
                    # endregion

            elif answer != self.my_questions.All_R[W_Q]:
                def try_again():
                    self.my_questions.readfile()

                    self.audio.PlayTheme()
                    H1_button.config(state=NORMAL, image=H1, cursor='hand2')
                    H2_button.config(state=NORMAL, image=H2, cursor='hand2')
                    H3_button.config(state=NORMAL, image=H3, cursor='hand2')
                    question.config(text=self.my_questions.All_Q[0])
                    choose_A_button.config(text=self.my_questions.All_A[0], cursor='hand2')
                    choose_B_button.config(text=self.my_questions.All_B[0], cursor='hand2')
                    choose_C_button.config(text=self.my_questions.All_C[0], cursor='hand2')
                    choose_D_button.config(text=self.my_questions.All_D[0], cursor='hand2')
                    n0_label.config(image=n0)
                    lose_frame.destroy()

                def close():
                    lose_frame.destroy()
                    game_window.destroy()

                # region lose window
                lose_frame = Frame(game_window, bg='black', width=500, height=400, bd=0, highlightbackground='white',
                                   highlightthickness=4)
                lose_frame.place(x=170, y=95)
                lose_frame.grab_set()

                bg_label = Label(lose_frame, image=BG, bd=0, bg='black')
                bg_label.place(x=151, y=67)

                cost = question.cget('text')
                index_cost = self.my_questions.All_Q.index(cost)

                how_much_label = Label(lose_frame, bd=0, bg='black', text=f'you won {how_much[index_cost]} Euros',
                                       font=('arial', 22, 'bold'), fg='white')
                how_much_label.place(x=118, y=270)

                you_lose = Label(lose_frame, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
                you_lose.place(x=130, y=0)

                tryagain_button = Button(lose_frame, text='Try Again', font=('arial', 18, 'bold'), bg='black',
                                         fg='white', bd=0, activebackground='black', cursor='hand2',
                                         activeforeground='white', command=try_again)
                tryagain_button.place(x=185, y=310)

                close_button = Button(lose_frame, text='Close', font=('arial', 16, 'bold'), bg='black', fg='white',
                                      bd=0, activebackground='black', cursor='hand2', activeforeground='white',
                                      command=close)
                close_button.place(x=213, y=353)

                H1_button.config(cursor='')
                H2_button.config(cursor='')
                H3_button.config(cursor='')
                choose_A_button.config(cursor='')
                choose_B_button.config(cursor='')
                choose_C_button.config(cursor='')
                choose_D_button.config(cursor='')
                # endregion

        def H1_function():
            H1_button.config(image=H1A, state=DISABLED, cursor='')
            W_Q = self.my_questions.All_Q.index(question.cget('text'))
            k = [choose_A_button.cget('text'), choose_B_button.cget('text'), choose_C_button.cget('text'),
                 choose_D_button.cget('text')]
            x = random.choice(k)
            y = random.choice(k)
            while x == self.my_questions.All_R[W_Q] or y == self.my_questions.All_R[W_Q] or x == y:
                x = random.choice(k)
                y = random.choice(k)
            if x == self.my_questions.All_A[W_Q] or y == self.my_questions.All_A[W_Q]:
                choose_A_button.place_forget()
            if x == self.my_questions.All_B[W_Q] or y == self.my_questions.All_B[W_Q]:
                choose_B_button.place_forget()
            if x == self.my_questions.All_C[W_Q] or y == self.my_questions.All_C[W_Q]:
                choose_C_button.place_forget()
            if x == self.my_questions.All_D[W_Q] or y == self.my_questions.All_D[W_Q]:
                choose_D_button.place_forget()

        def H2_function():
            H2_button.config(image=H2A, state=DISABLED, cursor='')
            bar_A.place(x=640, y=145)
            bar_A_label.place(x=638, y=275)
            bar_B.place(x=680, y=145)
            bar_B_label.place(x=678, y=275)
            bar_C.place(x=720, y=145)
            bar_C_label.place(x=718, y=275)
            bar_D.place(x=760, y=145)
            bar_D_label.place(x=758, y=275)
            W_Q = self.my_questions.All_Q.index(question.cget('text'))
            k_ = [40, 45, 50, 55, 60, 65, 70]
            k_2 = [65, 70, 75, 80, 85, 90, 95]
            x = random.choice(k_2)
            y_1 = random.choice(k_)
            y_2 = random.choice(k_)
            y_3 = random.choice(k_)
            while y_1 == y_2 or y_1 == y_3 or y_2 == y_3 or y_1 == x or y_2 == x or y_3 == x or (y_1 and y_2 > x) or (
                    y_1 and y_3 > x) or (y_2 and y_3 > x):
                y_1 = random.choice(k_)
                y_2 = random.choice(k_)
                y_3 = random.choice(k_)
            if choose_A_button.cget('text') == self.my_questions.All_R[W_Q]:
                bar_A.config(value=x)
                bar_B.config(value=y_1)
                bar_C.config(value=y_2)
                bar_D.config(value=y_3)
            if choose_B_button.cget('text') == self.my_questions.All_R[W_Q]:
                bar_B.config(value=x)
                bar_A.config(value=y_1)
                bar_C.config(value=y_2)
                bar_D.config(value=y_3)
            if choose_C_button.cget('text') == self.my_questions.All_R[W_Q]:
                bar_C.config(value=x)
                bar_A.config(value=y_1)
                bar_B.config(value=y_2)
                bar_D.config(value=y_3)
            if choose_D_button.cget('text') == self.my_questions.All_R[W_Q]:
                bar_D.config(value=x)
                bar_A.config(value=y_1)
                bar_B.config(value=y_2)
                bar_C.config(value=y_3)

        def H3_function_part1():
            H3_button.config(image=H3A, state=DISABLED, cursor='')
            oncall_button.place(x=50, y=230)
            self.audio.PlayPhoneSound()

        def H3_function_part2():
            W_Q = self.my_questions.All_Q.index(question.cget('text'))
            self.audio.PlayTheme()
            self.audio.Pause()
            self.audio.Say(f'after thinking i think the answer is {self.my_questions.All_R[W_Q]}')
            self.audio.Continue()

        # region game_window_configs
        self.audio.PlayTheme()

        game_window = Tk()
        game_window.geometry('1275x600')
        game_window.resizable(False, False)
        game_window.iconbitmap('images/icon.ico')
        game_window.title('Who Wants To Be A Millionaire')
        game_window.config(bg='black')
        # endregion

        # region Help buttons
        H1 = PhotoImage(file='images/H1.png')
        H1_button = Button(game_window, image=H1, bg='black', bd=0, activebackground='black', width=106, height=64,
                           cursor='hand2', command=H1_function)
        H1_button.place(x=167, y=10.5)
        H1A = PhotoImage(file='images/H1A.png')

        H2 = PhotoImage(file='images/H2.png')
        H2_button = Button(game_window, image=H2, bg='black', bd=0, activebackground='black', width=106, height=64,
                           cursor='hand2', command=H2_function)
        H2_button.place(x=373, y=10.5)
        H2A = PhotoImage(file='images/H2A.png')

        H3 = PhotoImage(file='images/H3.png')
        H3_button = Button(game_window, image=H3, bg='black', bd=0, activebackground='black', width=106, height=64,
                           cursor='hand2', command=H3_function_part1)
        H3_button.place(x=579, y=10.5)
        H3A = PhotoImage(file='images/H3A.png')
        oncall = PhotoImage(file='images/oncall.png')
        oncall_button = Button(game_window, bg='black', bd=0, activebackground='black', image=oncall,
                               cursor='hand2', command=H3_function_part2)
        # endregion

        # region H2_bar
        bar_A = Progressbar(game_window, orient=VERTICAL, mode='determinate', length=130)
        bar_A_label = Label(game_window, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

        bar_B = Progressbar(game_window, orient=VERTICAL, mode='determinate', length=130)
        bar_B_label = Label(game_window, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

        bar_C = Progressbar(game_window, orient=VERTICAL, mode='determinate', length=130)
        bar_C_label = Label(game_window, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

        bar_D = Progressbar(game_window, orient=VERTICAL, mode='determinate', length=130)
        bar_D_label = Label(game_window, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')
        # endregion

        # region Back_ground_in_middle_frame
        BG = PhotoImage(file='images/BG.png')
        BG_label = Label(game_window, image=BG, bg='black', width=200, height=250)
        BG_label.place(x=323, y=80)
        # endregion

        # region questions_body
        questions_body = PhotoImage(file='images/questions.png')
        n0_label = Label(game_window, image=questions_body, width=852, height=320, bg='black', bd=0)
        n0_label.place(x=0, y=305)
        question = Label(game_window, font=("arial", 20, "bold",),
                         text=self.my_questions.All_Q[0],
                         bg='#000076',
                         fg='white', bd=0, width=37, height=2, wraplength=630)
        question.place(x=110, y=354)

        # endregion

        # region choose_A
        choose_A = Label(game_window, font=("arial", 16, "bold",), text='A:', bg='#000076', fg='white')
        choose_A.place(x=88, y=460)
        choose_A_button = Button(game_window, text=self.my_questions.All_A[0], font=('arial', 16, 'bold'), bg='#000076',
                                 fg='white', cursor='hand2', bd=0, activebackground='#000076', activeforeground='white',
                                 width=20)
        choose_A_button.place(x=112, y=457)
        choose_A_button.bind('<Button-1>', which_choice)
        # endregion

        # region choose_B
        choose_B = Label(game_window, font=("arial", 16, "bold",), text='B:', bg='#000076', fg='white')
        choose_B.place(x=470, y=461)
        choose_B_button = Button(game_window, text=self.my_questions.All_B[0], font=('arial', 16, 'bold'), bg='#000076',
                                 fg='white', cursor='hand2', bd=0, activebackground='#000076', activeforeground='white',
                                 width=20)
        choose_B_button.place(x=494, y=457)
        choose_B_button.bind('<Button-1>', which_choice)
        # endregion

        # region choose_C
        choose_C = Label(game_window, font=("arial", 16, "bold",), text='C:', bg='#000076', fg='white')
        choose_C.place(x=88, y=530)
        choose_C_button = Button(game_window, text=self.my_questions.All_C[0], font=('arial', 16, 'bold'), bg='#000076',
                                 fg='white', cursor='hand2', bd=0, activebackground='#000076', activeforeground='white',
                                 width=20)
        choose_C_button.place(x=112, y=527)
        choose_C_button.bind('<Button-1>', which_choice)
        # endregion

        # region choose_D
        choose_D = Label(game_window, font=("arial", 16, "bold",), text='D:', bg='#000076', fg='white')
        choose_D.place(x=470, y=531)
        choose_D_button = Button(game_window, text=self.my_questions.All_D[0], font=('arial', 16, 'bold'), bg='#000076',
                                 fg='white', cursor='hand2', bd=0, activebackground='#000076', activeforeground='white',
                                 width=20)
        choose_D_button.place(x=494, y=527)
        choose_D_button.bind('<Button-1>', which_choice)
        # endregion

        # region questions_progress
        n0 = PhotoImage(file='images/n0.png')
        n1 = PhotoImage(file='images/n1.png')
        n2 = PhotoImage(file='images/n2.png')
        n3 = PhotoImage(file='images/n3.png')
        n4 = PhotoImage(file='images/n4.png')
        n5 = PhotoImage(file='images/n5.png')
        n6 = PhotoImage(file='images/n6.png')
        n7 = PhotoImage(file='images/n7.png')
        n8 = PhotoImage(file='images/n8.png')
        n9 = PhotoImage(file='images/n9.png')
        n10 = PhotoImage(file='images/n10.png')
        n11 = PhotoImage(file='images/n11.png')
        n12 = PhotoImage(file='images/n12.png')
        n13 = PhotoImage(file='images/n13.png')
        n14 = PhotoImage(file='images/n14.png')
        n15 = PhotoImage(file='images/n15.png')
        n = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]
        how_much = ['0', '100', '200', '300', '500', '1,000', '2,000', '4,000', '8,000', '16,000', '32,000', '64,000',
                    '125,000', '500,000', '1,000,000']
        n0_label = Label(game_window, image=n0, bg='black', bd=0, height=610)
        n0_label.place(x=852, y=0)
        # endregion

        game_window.mainloop()
