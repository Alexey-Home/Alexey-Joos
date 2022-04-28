import tkinter as tk


main_window = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
main_window.iconphoto(False, photo)
main_window.title("CNCProgram")
main_window.geometry("1024x768")



main_window.mainloop()