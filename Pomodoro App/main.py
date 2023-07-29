"""Pomodoro App"""
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
    # If it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=PINK)
    # If it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
"""Event Driven"""
def count_down(count):
    # total_sec / 60 = min
    # total_sec % 60 = sec left out of the total_sec
    global reps, timer
    count_min = math.floor(count / 60)
    # math.floor() going to return The largest integer(whole number) <= x
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    """after() Execute a command after a time delay"""
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# count_down(5)
'''Here commented out because the canvas is define later in the code '''

# def say_something(a, b, c):
#     print(a, b, c)

# window.after(1000, say_something, 4, 2, 5)
"""4,2,5 is passed as argument after the function is called"""

# To put Img on screen
label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 30, "bold"), fg=GREEN)
label.grid(row=0, column=1)

"""Canvas"""
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
IMG = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=IMG)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# count_down(5)

check = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check.grid(row=3, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

stop = Button(text="Reset", highlightthickness=0, command=reset_timer)
stop.grid(row=2, column=2)

window.mainloop()
