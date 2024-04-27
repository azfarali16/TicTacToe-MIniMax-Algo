import tkinter as tk
from frontend.interface import Frontend

def main():
    root = tk.Tk()  # Create the main Tkinter window
    frontend = Frontend(root)  # Pass the root argument
    root.mainloop()

if __name__ == "__main__":
    main()
