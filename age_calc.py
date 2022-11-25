from tkinter import *

# create an App Root
root = Tk()

# window title
root.title('Age Calculator')

# window geometry (w x h)
root.geometry('500x300')

# window background
root['bg'] = '#11DFBB'

'''steps
1.Write name of widget class
2.pass root as parameter to class
3.save it in a variable
pack, place , grid
'''

# Clear all button
def clearAll():
    # deleting the content from the entry box
    day_entrytext.delete(0, END)
    month_entrytext.delete(0, END)
    year_entrytext.delete(0, END)
    givenday_entrytext.delete(0, END)
    givenmonth_entrytext.delete(0, END)
    givenyear_entrytext.delete(0, END)
    res_days_entrytext.delete(0, END)
    res_month_entrytext.delete(0, END)
    res_year_entrytext.delete(0, END)


def checkError():
    # if any of the entry field is empty
    # then show an error message and clear
    # all the entries
    if (day_entrytext.get() == "" or month_entrytext.get() == ""
            or year_entrytext.get() == "" or givenday_entrytext.get() == ""
            or givenmonth_entrytext.get() == "" or givenyear_entrytext.get() == ""):
        # show the error message
        messagebox.showerror("Input Error")

        # clearAll function calling
        clearAll()

        return -1


def calculate_age():
    # check for error
    value = checkError()

    # if error is occur then return
    if value == -1:
        return

    else:
        birth_day = int(day_entrytext.get())         #30
        birth_month = int(month_entrytext.get())      #10
        birth_year = int(year_entrytext.get())       #2004

        given_day = int(givenday_entrytext.get())     #27
        given_month = int(givenmonth_entrytext.get())  #8
        given_year = int(givenyear_entrytext.get())       #2021

        months = [31, 28, 31, 30.31, 30, 31, 31, 30, 31, 30, 31]


        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + months[birth_month - 1]

        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12



        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;

        res_days_entrytext.insert(10, str(calculated_day))
        res_month_entrytext.insert(10, str(calculated_month))
        res_year_entrytext.insert(10, str(calculated_year))


'''Entry for dob'''

# DOB Label
dob_label = Label(root, text='Date of Birth', bg='red')
dob_label.grid(row=0, column=1)

# day
day_label = Label(root, text='Day', bg='#11DFBB')
day_label.grid(row=1, column=0)

day_entrytext = Entry(root)
day_entrytext.grid(row=1, column=1)

# month
month_label = Label(root, text='Month', bg='#11DFBB')
month_label.grid(row=2, column=0)

month_entrytext = Entry(root)
month_entrytext.grid(row=2, column=1)

# year
year_label = Label(root, text='Year', bg='#11DFBB')
year_label.grid(row=3, column=0)

year_entrytext = Entry(root)
year_entrytext.grid(row=3, column=1)

'''Entry Given Date'''

# Given date label
given_date = Label(root, text='Given Date', bg='red')
given_date.grid(row=0, column=4)

# Given day
givenday_label = Label(root, text='Given Day', bg='#11DFBB')
givenday_label.grid(row=1, column=3)

givenday_entrytext = Entry(root)
givenday_entrytext.grid(row=1, column=4)

# Given month
givenmonth_label = Label(root, text='Given Month', bg='#11DFBB')
givenmonth_label.grid(row=2, column=3)

givenmonth_entrytext = Entry(root)
givenmonth_entrytext.grid(row=2, column=4)

# year
givenyear_label = Label(root, text='Given Year', bg='#11DFBB')
givenyear_label.grid(row=3, column=3)

givenyear_entrytext = Entry(root)
givenyear_entrytext.grid(row=3, column=4)

'''Result Age'''
result_age = Button(root, command = calculate_age, text='Resultant Age', fg='white', bg='black')
result_age.grid(row=4, column=2)

# result year
res_year_label = Label(root, text='Years', bg='#11DFBB')
res_year_label.grid(row=5, column=2)

res_year_entrytext = Entry(root)
res_year_entrytext.grid(row=6, column=2)

# result month
res_month_label = Label(root, text='Months', bg='#11DFBB')
res_month_label.grid(row=7, column=2)

res_month_entrytext = Entry(root)
res_month_entrytext.grid(row=8, column=2)

# result days
res_days_label = Label(root, text='Days', bg='#11DFBB')
res_days_label.grid(row=9, column=2)

res_days_entrytext = Entry(root)
res_days_entrytext.grid(row=10, column=2)

clear_all = Button(root, command=clearAll, text='Clear All', fg='white', bg='black')
clear_all.grid(row=11, column=2)

# start / run window
root.mainloop()
