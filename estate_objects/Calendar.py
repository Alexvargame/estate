import calendar
from datetime import *
from tkinter import *


calendar_choice = Tk()
calendar_choice.geometry('180x220+150+50')
fr = Frame()
fr.pack()
fr_1 = Frame()
fr_1.pack()
fr_2 = Frame()
fr_2.pack()
#text=Text(width=25, height=15)
#text.pack()

month_={1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
today=datetime.today()
i=0
j=0
m_y = [today.month,today.year]
list_day=[]
c = calendar.Calendar()
for k in c.itermonthdays (today.year, today.month):
    list_day.append(k)
lbl_m_y = Label(fr, text="  ")
lbl_m_y['text'] = str(month_[today.month])+"  "+str(today.year)
def month_prev():
    if m_y[0]!=1:
        m_y[0]=m_y[0]-1
        m_y[1]=m_y[1]
        lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
        day_number()
        ent_date_begin.delete(0, END)
        ent_date_end.delete(0, END)
    else:
        m_y[0]=12
        m_y[1]=m_y[1]-1
        lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
        day_number()
        ent_date_begin.delete(0, END)
        ent_date_end.delete(0, END)
    return m_y
def month_post():
    if m_y[0]!=12:
        m_y[0]=m_y[0]+1
        m_y[1]=m_y[1]
        lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
        day_number()
        ent_date_begin.delete(0, END)
        ent_date_end.delete(0, END)
    else:
        m_y[0]=1
        m_y[1]=m_y[1]+1
        lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
        day_number()
        ent_date_begin.delete(0, END)
        ent_date_end.delete(0, END)
    return m_y
def day_number():
    list_day.clear()
    for widget in fr_1.winfo_children():
            widget.destroy()

    c = calendar.Calendar()
    for k in c.itermonthdays (m_y[1], m_y[0]):
        list_day.append(k)
    for i in range(int(len(list_day)/7)):
     for j in range(7):
     
        btn_day=Button(fr_1,width=1, height=1)
        btn_day.bind("<Button-1>", choice_date)
        btn_day['text']=''
        if list_day[j+7*i]!=0:
           btn_day['text']=list_day[j+7*i]
        btn_day.grid(row=i, column=j)
        j=j+1
     i=i+1
    return list_day
def choice_date(event):
    grid_info = event.widget.grid_info()
    if ent_date_begin.get()=="":
        date_begin=datetime(m_y[1], m_y[0], list_day[grid_info["row"]*7+grid_info["column"]])
        ent_date_begin.insert(0, date_begin)
    else:
        date_end=datetime(m_y[1], m_y[0], list_day[grid_info["row"]*7+grid_info["column"]])
        ent_date_end.insert(0, date_end)
def end_stat():
       calendar_choice.destroy()

lbl_week = Label(fr, text="Mo  Tu  We  Th  Fr  Sa  Su")
btn_prev = Button(fr, text="<<", width=2, command=month_prev)
btn_post = Button(fr, text=">>", width=2, command=month_post)
btn_prev.grid(row=0, column=0)
btn_post.grid(row=0, column=6)
lbl_m_y.grid(row=0, column=1, columnspan=5)
lbl_week.grid(row=1, column=0, columnspan=7)
ent_date_begin = Entry(fr_2, width=10)
ent_date_end = Entry(fr_2, width=10)
ent_date_begin.grid(row=0, column=0)
ent_date_end.grid(row=0, column=6)
btn_end = Button(fr_2, text="Завершить", command=end_stat)
btn_end.grid(row=2, column=0, sticky='w')

for i in range(int(len(list_day)/7)):
     for j in range(7):     
        btn_day=Button(fr_1,width=1, height=1)
        btn_day.bind("<Button-1>", choice_date)
        if list_day[j+7*i]!=0:
            btn_day['text']=list_day[j+7*i]
        else: btn_day['text']=''
        btn_day.grid(row=i, column=j)
        j=j+1
     i=i+1

#calendar_choice.mainloop()

def main():
   calendar_choice.mainloop()



if __name__ == "__main__":
    main()



