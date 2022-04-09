import tkinter as tk

main_window = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
main_window.title("ProgramCNC")
main_window.geometry("1024x768")
main_window.resizable(False, False)

main_window.mainloop()
