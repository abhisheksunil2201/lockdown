import tkinter as tk


def main():
    window = tk.Tk()
    window.wm_minsize(300, 200)
    window.title("Lockdown")
    greeting = tk.Label(text="Please enter your password")
    greeting.pack()
    entry = tk.Entry()
    entry.pack()
    button = tk.Button(text="Submit", command=lambda: print(entry.get()))
    button.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
