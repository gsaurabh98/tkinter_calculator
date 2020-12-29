# author saurabh, created at 29th Dec, 2020
import tkinter as tk

# export DISPLAY=:0.0


# make a new window
window = tk.Tk()

# show popup
window.title("Calculator")
# set the background colour of GUI window
# window.configure(background="light green")
window.geometry("417x517")


def get_text():
    text = textbox.get("1.0", "end")
    return text


def clear_text():
    textbox.delete(1.0, "end")


def show_text(index, text):
    textbox.insert(index, text)


def execute_expression():
    try:
        expression = str(get_text())
        val = eval(expression)
        clear_text()
        show_text("1.0", str(val))
        print("expression", expression)
        print("output", val)
    except Exception as e:
        print("error", e)
        clear_text()
        show_text("1.0", "bad expression")


textbox = tk.Text(window, width=300, height=10, font=("Segoe UI", 10, "bold"))
btn1 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="1",
    command=lambda: show_text(2.0, "1"),
)
btn2 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="2",
    command=lambda: show_text(2.0, "2"),
)
btn3 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="3",
    command=lambda: show_text(2.0, "3"),
)
btn4 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="4",
    command=lambda: show_text(2.0, "4"),
)
btn5 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="5",
    command=lambda: show_text(2.0, "5"),
)
btn6 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="6",
    command=lambda: show_text(2.0, "6"),
)
btn7 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="7",
    command=lambda: show_text(2.0, "7"),
)
btn8 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="8",
    command=lambda: show_text(2.0, "8"),
)
btn9 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="9",
    command=lambda: show_text(2.0, "9"),
)
btn0 = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="0",
    command=lambda: show_text(2.0, "0"),
)
btn_clear = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="clear",
    command=lambda: clear_text(),
)

dot_btn = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text=".",
    command=lambda: show_text(2.0, "."),
)
add_btn = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text=" ",
    fg="crimson",
    command=lambda: show_text(2.0, " "),
)
sub_btn = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="-",
    fg="crimson",
    command=lambda: show_text(2.0, "-"),
)
mul_btn = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="x",
    fg="crimson",
    command=lambda: show_text(2.0, "*"),
)
div_btn = tk.Button(
    window,
    width=8,
    height=7,
    font=("Calibri", 10, "bold"),
    bg="white",
    activebackground="crimson",
    text="/",
    fg="crimson",
    command=lambda: show_text(2.0, "/"),
)
equal_btn = tk.Button(
    window,
    width=8,
    height=31,
    font=("Calibri", 10, "bold"),
    text="=",
    bg="crimson",
    activebackground="white",
    command=execute_expression,
)


textbox.pack()

btn1.place(x=1, y=100)
btn2.place(x=84, y=100)
btn3.place(x=167, y=100)
div_btn.place(x=250, y=100)

btn4.place(x=1, y=204)
btn5.place(x=84, y=204)
btn6.place(x=167, y=204)
mul_btn.place(x=250, y=204)


btn7.place(x=1, y=308)
btn8.place(x=84, y=308)
btn9.place(x=167, y=308)
sub_btn.place(x=250, y=308)

btn_clear.place(x=1, y=412)
btn0.place(x=84, y=412)
dot_btn.place(x=167, y=412)
add_btn.place(x=250, y=412)
equal_btn.place(x=333, y=100)


window.resizable(0, 0)
window.mainloop()
