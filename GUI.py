import tkinter as tk


# create the tkinter window
window = tk.Tk()
greetings = tk.Label(window, text='Hello, World!')
greetings.pack()



# main function
def main():
    window.mainloop()

if __name__ == '__main__':
    main()