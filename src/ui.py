import tkinter as tk
from tkinter import messagebox
from password_prompt import verify_password


class PasswordUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lockdown")
        self.root.wm_minsize(300, 200)
        # Create labels
        self.label = tk.Label(root, text="Enter Password:")
        self.label.pack()

        # Create password entry widget
        # Mask the password with "*"
        self.password = tk.Entry(root, show="*", width=30)
        self.password.pack()

        # Create submit button
        self.submitButton = tk.Button(
            root, text="Submit", command=self.verify_password)
        self.submitButton.pack()

        # Initialize a variable to store the result
        self.result = None

    def verify_password(self):
        entered_password = self.password.get()
        is_password_correct = verify_password(entered_password)
        self.result = is_password_correct  # Store the result

        if is_password_correct:
            self.root.destroy()  # Close the UI window
        else:
            messagebox.showerror("Error", "Incorrect password. Access denied.")


def show_password_prompt() -> bool:
    window = tk.Tk()
    passwordUI = PasswordUI(window)
    window.mainloop()
    return passwordUI
