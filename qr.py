import tkinter as tk
import qrcode
sp=[]
def next():
    file=str(n.get()+'.png')
    sp.append(file)
    dat=str(d.get())
    sp.append(dat)
    img=qrcode.make(sp[-1])
    img.save(sp[0])



win=tk.Tk()
win.geometry('600x150')
win.title('QR 2.0')
win['bg']='#EF00FF'
win.resizable(width=False,height=False)

n=tk.Entry(win,font=('Arial',20))
n.grid(row=0, column=1, columnspan=5, padx=5, pady=5,stick='we')
d=tk.Entry(win,font=('Arial',20))
d.grid(row=1, column=1, columnspan=5, padx=5, pady=5,stick='we')

tk.Label(win,text='Name:',font=('Arial',20), bg='#EF00FF').grid(row=0, column=0, padx=5,pady=5,stick='we')
tk.Label(win,text='Data:',font=('Arial',20),bg='#EF00FF').grid(row=1, column=0, padx=5, pady=5,stick='we')

btn=tk.Button(win,text='Next', bg='#FFB300', command=lambda:next())
btn.grid(row=2, column=2, columnspan=2, padx=5, pady=5,stick='wens')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=100)
win.grid_columnconfigure(4, minsize=100)
win.grid_columnconfigure(5, minsize=100)

win.grid_rowconfigure(2,minsize=50)

win.mainloop()
