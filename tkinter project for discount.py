from tkinter import*
from tkinter import messagebox as b
a=Tk()
a.title('quantity')
a.geometry('500x400')
def process():
    en=int(Entry.get(en_1))
    en1=en*100
    if en1>1000:
        c=('cost is...Rs.'+str((en*100)-(0.1*en*100)))
        t=Text(a,width=30,height=2)
        t.insert(INSERT,c)
        t.place(x=100,y=300)
    else:
        b.showinfo('cost',en*100)
Label(a,text='quantity',font=('times new roman',16)).pack()
Label(a,text='no of product quantity',font=('times new roman',16)).place(x=20,y=50)
en_1=Entry(a,font=('times new roman',16),width=15)
en_1.place(x=300,y=52)
btn=Button(a,text='submit',font=('times new roman',16),command=process)
btn.place(x=300,y=100)
a.mainloop()