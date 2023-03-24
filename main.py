import customtkinter as ctk
import random
import time
from playsound import playsound


sound_loc = "button.wav"
wrong_loc = "wrong.wav"
sound = False
music = False
c_button = None
started = False
score = 0
start_time = None
elapsed_time = None
ctk.set_appearance_mode("Dark")



def main():

    window = ctk.CTk()
    window.geometry("500x250")
    window.title("Happy Button")

    frame = ctk.CTkFrame(window,width=450,height=200)
    frame.place(x=25,y=25)
    
    def sound_toggle():
        global sound
        sound = switch.get()
        
    switch = ctk.CTkSwitch(master=frame, command=sound_toggle, onvalue=True, offvalue=False,text="")
    
    switch.place(x=400,y=175)


    def red_button():
        global recent_button
        global score
        global start_time
        recent_button = "red"
        if started == False:
            return
        if recent_button == c_button:
            start_time += 0.2
            score += 1
            if sound == True:
                playsound(sound_loc,False)
            score_label.configure(text=f"{score}")
            random_button()
        else:
            start_time -= 1
            if sound == True:
                playsound(wrong_loc,False)
            return
        
    def yellow_button():
        global score
        global recent_button
        global start_time
        if started == False:
            return
        recent_button = "yellow"
        if recent_button == c_button:
            start_time += 0.2
            if sound == True:
                playsound(sound_loc,False)
            score += 1
            score_label.configure(text=f"{score}")
            random_button()
        else:
            if sound == True:
                playsound(wrong_loc,False)
            start_time -= 1
            return
    def blue_button():
        global score
        global recent_button
        global start_time
        recent_button = "blue"
        if started == False:
            return
        if recent_button == c_button:
            
            start_time += 0.2
            if sound == True:
                playsound(sound_loc,False)
            score += 1
            score_label.configure(text=f"{score}")
            random_button()
        else:
            playsound(wrong_loc,False)
            if sound == True:
                start_time -= 1
            return
    def green_button():
        global score
        global recent_button
        global start_time
        if started == False:
            return
        recent_button = "green"
        if recent_button == c_button:
            if sound == True:
                playsound(sound_loc,False)
            start_time += 0.2
            score += 1
            score_label.configure(text=f"{score}")
            random_button()
        else:
            if sound == True:
                playsound(wrong_loc,False)
            start_time -= 1
            return
    def restore():
        button1.configure(fg_color="#FF0000",hover_color="#8B0000")
        time.sleep(0.01)
        button2.configure(fg_color="#FFFF00",hover_color="#999900")
        time.sleep(0.01)
        button3.configure(fg_color="#0000FF",hover_color="#00008B")
        time.sleep(0.01)
        button4.configure(fg_color="#008000",hover_color="#006400")
        time.sleep(0.01)
        
    def random_button():
        global c_button
        buttonnum = random.choice(["red","yellow","blue","green"])
        if buttonnum == c_button:
            random_button()
            return
        restore()
        if buttonnum == "red":
            button1.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "yellow":
            button2.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "blue":
            button3.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        elif buttonnum == "green":
            button4.configure(fg_color="#FFFFFF",hover_color="#FFFFFF")
        else:
            print(buttonnum)
        c_button = buttonnum
            
            
    #1 = Red, 2 = Yellow, 3 = Blue, 4 = Green

    button1 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=100,fg_color="#FF0000",hover_color="#8B0000",command=red_button)
    button1.place(x=18,y=50)

    button2 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=100,fg_color="#FFFF00",hover_color="#999900",command=yellow_button)
    button2.place(x=123,y=50)

    button3 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=100,fg_color="#0000FF",hover_color="#00008B",command=blue_button)
    button3.place(x=228,y=50)

    button4 = ctk.CTkButton(frame,width=100,height=100,text="",corner_radius=100,fg_color="#008000",hover_color="#006400",command=green_button)
    button4.place(x=333,y=50)

    time_ = ctk.CTkLabel(frame,text="Time",font=("Helvetica",12))
    time_.place(x=5,y=175)

    sound_label = ctk.CTkLabel(frame,text="SFX",font=("Helvetica",12))
    sound_label.place(x=370,y=173)
    
    score_label = ctk.CTkLabel(frame,text=f"{score}",font=("Helvetica",24))
    score_label.place(x=10,y=10)
    window.bind("1",lambda event: red_button())
    window.bind("2",lambda event: yellow_button())
    window.bind("3",lambda event: blue_button())
    window.bind("4",lambda event: green_button())
    def start_():
        global start_time
        global started
        global score
        score = 0
        started = True
        start.place(x=100000,y=10)
        random_button()
        start_time = time.time()
        clock()
        
    start = ctk.CTkButton(frame,width=100,height=25,text="Start",command=start_)
    start.place(x=175,y=10)
            
    def clock():
        global start_time
        global elapsed_time
        global score
        global started
        limit = 15
        
        elapsed_time = time.time() - start_time - limit
        if elapsed_time >= 0:
            started = False
            start_time = None
            
            start.place(x=175,y=10)
            button1.configure(fg_color="#FF0000",hover_color="#8B0000")
            button2.configure(fg_color="#FFFF00",hover_color="#999900")
            button3.configure(fg_color="#0000FF",hover_color="#00008B")
            button4.configure(fg_color="#008000",hover_color="#006400")
            score_label.configure(text=f"{score}")
            return
        _time = int(elapsed_time*-1)
        time_.configure(text=(_time))
        
        window.after(25,clock)
        
    window.mainloop()
    
    
main()
