import math
from tkinter import *

# COLOURS
PINK = "#f4847c"
RED = "#fb2801"
GREEN = "#8ac11f"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 30
reps = 1
mark = ""
timer = None

# TIMER RESET
def reset_timer():
    global mark
    global reps

    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    reps = 1
    mark = ""
    checkmarks.config(text=mark)
    canvas.itemconfig(timer_text, text="00:00")
    start_button.config(state="active")


# TIMER MECHANISM
def start_timer():

    work_secs = WORK_TIME * 60
    short_break_secs = SHORT_BREAK * 60
    long_break_secs = LONG_BREAK * 60

    if reps % 2 == 1:
        countdown(work_secs)
        title_label.config(text="Work", fg=GREEN)

    elif reps % 2 == 0 and reps != 8:
        countdown(short_break_secs)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(long_break_secs)
        title_label.config(text="Break", fg=RED)

    start_button.config(state="disabled")

# COUNTDOWN MECHANISM
def countdown(count):
    global reps
    global mark
    global timer

    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        if reps % 2 == 0:
           mark += "✓"
        checkmarks.config(text=mark)
        start_timer()

# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

canvas = Canvas(width=520, height=520, bg=YELLOW, highlightthickness=0)
Tomato_image = PhotoImage(file="Tomato.png")
canvas.create_image(260, 260, image=Tomato_image)
timer_text = canvas.create_text(260, 265, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), state="active", command=start_timer)
start_button.grid(column=0, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()