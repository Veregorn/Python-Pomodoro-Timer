from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- VARIABLES ------------------------------- # 
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global state
    global check_marks
    global canvas
    global reps

    window.after_cancel(timer)
    state.config(text="Work", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global state

    # work_sec = WORK_MIN * 60
    work_sec = 25
    # short_break_sec = SHORT_BREAK_MIN * 60
    short_break_sec = 5
    # long_break_sec = LONG_BREAK_MIN * 60
    long_break_sec = 15

    # If it's the 8th rep:
    if reps % 8 == 0:
        state.config(text="Break", fg=RED) # Long
        count_down(long_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    elif reps % 2 != 0:
        state.config(text="Work", fg=GREEN)
        count_down(work_sec)
    # If it's 2nd/4th/6th rep:
    else:
        state.config(text="Break", fg=PINK) # Short
        count_down(short_break_sec)

    # We need to update reps
    if reps < 8:
        reps += 1
    else:
        reps = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global check_marks
    global timer
    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Format seconds and minutes so it always have 2 digits
    if count_sec < 10:
        count_sec = f"0{count_sec}" # We can do this thanks to dynamic typing of Python!!!
    if count_min < 10:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1) # Recursive call
    else:
        if reps % 2 == 0:
            # Increase check marks
            current_text = check_marks.cget("text")
            if current_text == "✔✔✔":
                check_marks.config(text=current_text+"✔ ")
            else:
                check_marks.config(text=current_text+"✔")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=130, pady=105, bg=YELLOW)

# We are going to create a canvas to put an image an a counter text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # Half of the width and the height

# Counter text
timer_text = canvas.create_text(100, 130, text="00:25", font=(FONT_NAME, 35, "bold"), fill=WHITE)
canvas.grid(column=1, row=1)

# Create a Label for the current state of the App
state = Label(text="Work", font=(FONT_NAME, 50, 'normal'), fg=GREEN, bg=YELLOW)
state.grid(column=1, row=0)

# Create a button to start the counter
start_button = Button(text="Start", command=start_timer, highlightthickness=0, borderwidth=0, relief=FLAT)
start_button.grid(column="0", row="2")

# Create a button to reset the counter
def reset_counter():
    print("Counter reset")

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, borderwidth=0, relief=FLAT)
reset_button.grid(column="2", row="2")

# Create the check mark
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
check_marks.grid(column=1, row=3)





window.mainloop()