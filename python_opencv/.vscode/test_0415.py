import tkinter

key = 0

def KeyClick(e):
    global key
    key = e.keysym
    print(key)

tk = tkinter.Tk()

tk.title("키 입력")
tk.bind("<key>",KeyClick)
tk.mainloop()