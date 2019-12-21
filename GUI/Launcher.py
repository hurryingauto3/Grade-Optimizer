from tkinter import *
import tkinter.messagebox #popup messages

#Notes
#Tkinter = Module which allows programming of Graphic User Interface (GUI)
#Tk = Basic function to create a window
#grid = Treat the GUI window like a table and 'grid' each button/text/field etc. in rows and columns.
#Label = All the text to be displayed
#messagebox.showinfo = Create pop-up dialog box to display additional information at button/menu clicks
#messagebox.askquestion = Create pop-up dialog box to prompt the user with a yes/no question.

########################################################################################################################
#Calculator Code

#Default (Main) Window {Calculator}
window = Tk() #Create basic window
window.geometry("650x345") #Dimensions of Application Window
window.resizable(width=False, height=False) #Lock Size of window and disable maximize button
window.title('GPA Calculator') #Header/Title of Window
def Optimizer_Launcher():
    import Optimzer

def credits():
    tkinter.messagebox.showinfo('Wow, people actually read this?','Software developed by: \n \n Ali Hamza \n Maaz Saeed \n Maham Shoaib \n \n (and Moazzam Moriani"s Typhoid)\n \n All Rights Reserved ® \n Thank You, for using GPA Otimizer 1.0')

def virus():
    tkinter.messagebox.showinfo('Sad', 'Your malicious intentions are the real virus.')

def time():
    tkinter.messagebox.showinfo('I Warned You', 'You wasted your time.')

def optimizer_propaganda():
    answer = tkinter.messagebox.askquestion('Extremely well hidden function', 'Want to Optimize your GPA?')
    if answer == 'yes':
        tkinter.messagebox.showinfo('Yes, please help me, Supreme Overlords', 'Then click the green button, genius.')
    else:
        tkinter.messagebox.showinfo('No, I am dumb', 'I hope your parents have a lot of money...')

def grades():
    
    def error_grade(course):
        tkinter.messagebox.showinfo('Error', course)

    def error_credits():
        tkinter.messagebox.showinfo("GPA Calculator", 'Your estimated GPA is: ' + gpa)

    def printGPA():
        tkinter.messagebox.showinfo("GPA Calculator", 'Your estimated GPA is: ' +gpa +"\n \n We're better than HU intranet, just by the way")

    course_one = grade1.get()
    course_two = grade2.get()
    course_three = grade3.get()
    course_four = grade4.get()
    course_five = grade5.get()
    course_six = grade6.get()

    ali= quiz1.get()

    credit_one = cr1.get()
    credit_two = cr2.get()
    credit_three = cr3.get()
    credit_four = cr4.get()
    credit_five = cr5.get()
    credit_six = cr6.get()

    x.get()

    if course_one=='A+' or course_one=='A':
        course_one='4.0'
        course_one=float(course_one)
    elif course_one=='A-':
        course_one='3.67'
        course_one=float(course_one)
    elif course_one=='B+':
        course_one='3.33'
        course_one=float(course_one)
    elif course_one=='B':
        course_one='3.0'
        course_one=float(course_one)
    elif course_one=='B-':
        course_one='2.67'
        course_one=float(course_one)
    elif course_one=='C+':
        course_one='2.33'
        course_one=float(course_one)
    elif course_one=='C':
        course_one='2.0'
        course_one=float(course_one)
    elif course_one=='C-':
        course_one='1.67'
        course_one=float(course_one)
    elif course_one=='F':
        course_one='0.0'
        course_one=float(course_one)
    else:
        course_one=('Please enter a valid grade for course 1 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Second Course
    if course_two=='A+' or course_two=='A':
        course_two='4.0'
        course_two=float(course_two)
    elif course_two=='A-':
        course_two='3.67'
        course_two=float(course_two)
    elif course_two=='B+':
        course_two='3.33'
        course_two=float(course_two)
    elif course_two=='B':
        course_two='3.0'
        course_two=float(course_two)
    elif course_two=='B-':
        course_two='2.67'
        course_two=float(course_two)
    elif course_two=='C+':
        course_two='2.33'
        course_two=float(course_two)
    elif course_two=='C':
        course_two='2.0'
        course_two=float(course_two)
    elif course_two=='C-':
        course_two='1.67'
        course_two=float(course_two)
    elif course_two=='F':
        course_two='0.0'
        course_two=float(course_two)
    else:
        course_two=('Please enter a valid grade for course 2 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Third Course
    if course_three=='A+' or course_three=='A':
        course_three='4.0'
        course_three=float(course_three)
    elif course_three=='A-':
        course_three='3.67'
        course_three=float(course_three)
    elif course_three=='B+':
        course_three='3.33'
        course_three=float(course_three)
    elif course_three=='B':
        course_three='3.0'
        course_three=float(course_three)
    elif course_three=='B-':
        course_three='2.67'
        course_three=float(course_three)
    elif course_three=='C+':
        course_three='2.33'
        course_three=float(course_three)
    elif course_three=='C':
        course_three='2.0'
        course_three=float(course_three)
    elif course_three=='C-':
        course_three='1.67'
        course_three=float(course_three)
    elif course_three=='F':
        course_three='0.0'
        course_three=float(course_three)
    else:
        course_three=('Please enter a valid grade for course 3 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Fourth Course
    if course_four=='A+' or course_four=='A':
        course_four='4.0'
        course_four=float(course_four)
    elif course_four=='A-':
        course_four='3.67'
        course_four=float(course_four)
    elif course_four=='B+':
        course_four='3.33'
        course_four=float(course_four)
    elif course_four=='B':
        course_four='3.0'
        course_four=float(course_four)
    elif course_four=='B-':
        course_four='2.67'
        course_four=float(course_four)
    elif course_four=='C+':
        course_four='2.33'
        course_four=float(course_four)
    elif course_four=='C':
        course_four='2.0'
        course_four=float(course_four)
    elif course_four=='C-':
        course_four='1.67'
        course_four=float(course_four)
    elif course_four=='F':
        course_four='0.0'
        course_four=float(course_four)
    else:
        course_four=('Please enter a valid grade for course 4 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Fifth Course
    if course_five=='A+' or course_five=='A':
        course_five='4.0'
        course_five=float(course_five)
    elif course_five=='A-':
        course_five='3.67'
        course_five=float(course_five)
    elif course_five=='B+':
        course_five='3.33'
        course_five=float(course_five)
    elif course_five=='B':
        course_five='3.0'
        course_five=float(course_five)
    elif course_five=='B-':
        course_five='2.67'
        course_five=float(course_five)
    elif course_five=='C+':
        course_five='2.33'
        course_five=float(course_five)
    elif course_five=='C':
        course_five='2.0'
        course_five=float(course_five)
    elif course_five=='C-':
        course_five='1.67'
        course_five=float(course_five)
    elif course_five=='F':
        course_five='0.0'
        course_five=float(course_five)
    else:
        course_five=('Please enter a valid grade for course 5 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Sixth Course
    if course_six=='A+' or course_six=='A':
        course_six='4.0'
        course_six=float(course_six)
    elif course_six=='A-':
        course_six='3.67'
        course_six=float(course_six)
    elif course_six=='B+':
        course_six='3.33'
        course_six=float(course_six)
    elif course_six=='B':
        course_six='3.0'
        course_six=float(course_six)
    elif course_six=='B-':
        course_six='2.67'
        course_six=float(course_six)
    elif course_six=='C+':
        course_six='2.33'
        course_six=float(course_six)
    elif course_six=='C':
        course_six='2.0'
        course_six=float(course_six)
    elif course_six=='C-':
        course_six='1.67'
        course_six=float(course_six)
    elif course_six=='F':
        course_six='0.0'
        course_six=float(course_six)
    else:
        course_six=('Please enter a valid grade for course 6 \n \n Valid grades include: A+, A, A- ... C-, F \n \n Remember to use uppercase alphabets.')

    #Case: Single Course
    if x.get()==1:
        if type(course_one)==float:
            if cr1.get()>0 and cr1.get()<5:
                gpa=str(course_one)
                printGPA()
            else:
                gpa='not defined, please choose CR between 1 and 4 for course 1'
                error_credits()
        elif type(course_one)!=float:
            error_grade(course_one)

    #Case: Two Courses
    if x.get()==2:
        if type(course_one)==float and type(course_two)==float:
            if cr1.get()>0 and cr1.get()<5:
                if cr2.get() > 0 and cr2.get() < 5:
                    gpa=round(((course_one*cr1.get())+(course_two*cr2.get()))/(cr1.get()+cr2.get()),2)
                    gpa=str(gpa)
                    printGPA()
                else:
                    gpa = 'not defined, please choose CR between 1 and 4 for course 2'
                    error_credits()
            else:
                gpa='not defined, please choose CR between 1 and 4 for course 2'
                error_credits()
        elif type(course_one)!=float:
            error_grade(course_one)
        elif type(course_two)!=float:
            error_grade(course_two)

    #Case: Three Courses
    if x.get()==3:
        if type(course_one)==float and type(course_two)==float and type(course_three)==float:
            if cr1.get()>0 and cr1.get()<5:
                if cr2.get() > 0 and cr2.get() < 5:
                    if cr3.get() > 0 and cr3.get() < 5:
                        gpa=round(((course_one*cr1.get())+(course_two*cr2.get())+(course_three*cr3.get()))/(cr1.get()+cr2.get()+cr3.get()),2)
                        gpa=str(gpa)
                        printGPA()
                    else:
                        gpa = 'not defined, please choose CR between 1 and 4 for course 3'
                        error_credits()
                else:
                    gpa = 'not defined, please choose CR between 1 and 4 for course 3'
                    error_credits()
            else:
                gpa='not defined, please choose CR between 1 and 4 for course 3'
                error_credits()
        elif type(course_one)!=float:
            error_grade(course_one)
        elif type(course_two)!=float:
            error_grade(course_two)
        elif type(course_three)!=float:
            error_grade(course_two)

    #Case: Four Courses
    if x.get() == 4:
        if type(course_one) == float and type(course_two) == float and type(course_three) == float and type(course_four) == float:
            if cr1.get() > 0 and cr1.get() < 5:
                if cr2.get() > 0 and cr2.get() < 5:
                    if cr3.get() > 0 and cr3.get() < 5:
                        if cr4.get() > 0 and cr4.get() <5:
                            gpa=round(((course_one*cr1.get())+(course_two*cr2.get())+(course_three*cr3.get())+(course_four*cr4.get()))/(cr1.get()+cr2.get()+cr3.get()+cr4.get()),2)
                            gpa = str(gpa)
                            printGPA()
                        else:
                            gpa = 'not defined, please choose CR between 1 and 4 for course 4'
                            error_credits()
                    else:
                        gpa = 'not defined, please choose CR between 1 and 4 for course 4'
                        error_credits()
                else:
                    gpa = 'not defined, please choose CR between 1 and 4 for course 4'
                    error_credits()
            else:
                gpa = 'not defined, please choose CR between 1 and 4 for course 4'
                error_credits()
        elif type(course_one) != float:
            error_grade(course_one)
        elif type(course_two) != float:
            error_grade(course_two)
        elif type(course_three) != float:
            error_grade(course_three)
        elif type(course_four) != float:
            error_grade(course_four)

    #Case: Five Courses
    if x.get() == 5:
        if type(course_one) == float and type(course_two) == float and type(course_three) == float and type(course_four) == float and type(course_five) == float:
            if cr1.get() > 0 and cr1.get() < 5:
                if cr2.get() > 0 and cr2.get() < 5:
                    if cr3.get() > 0 and cr3.get() < 5:
                        if cr4.get() > 0 and cr4.get() < 5:
                            if cr5.get() > 0 and cr5.get() < 5:
                                gpa=round(((course_one*cr1.get())+(course_two*cr2.get())+(course_three*cr3.get())+(course_four*cr4.get())+(course_five*cr5.get()))/(cr1.get()+cr2.get()+cr3.get()+cr4.get()+cr5.get()),2)
                                gpa = str(gpa)
                                printGPA()
                            else:
                                gpa = 'not defined, please choose CR between 1 and 4 for course 5'
                                error_credits()
                        else:
                            gpa = 'not defined, please choose CR between 1 and 4 for course 5'
                            error_credits()
                    else:
                        gpa = 'not defined, please choose CR between 1 and 4 for course 5'
                        error_credits()
                else:
                    gpa = 'not defined, please choose CR between 1 and 4 for course 5'
                    error_credits()
            else:
                gpa = 'not defined, please choose CR between 1 and 4 for course 5'
                error_credits()
        elif type(course_one) != float:
            error_grade(course_one)
        elif type(course_two) != float:
            error_grade(course_two)
        elif type(course_three) != float:
            error_grade(course_three)
        elif type(course_four) != float:
            error_grade(course_four)
        elif type(course_five) != float:
            error_grade(course_five)

    #Case: Six Courses
    if x.get() == 6:
        if type(course_one) == float and type(course_two) == float and type(course_three) == float and type(course_four) == float and type(course_five) == float and type(course_six) == float:
            if cr1.get() > 0 and cr1.get() < 5:
                if cr2.get() > 0 and cr2.get() < 5:
                    if cr3.get() > 0 and cr3.get() < 5:
                        if cr4.get() > 0 and cr4.get() < 5:
                            if cr5.get() > 0 and cr5.get() < 5:
                                if cr6.get() > 0 and cr6.get() < 5:
                                    gpa=round(((course_one*cr1.get())+(course_two*cr2.get())+(course_three*cr3.get())+(course_four*cr4.get())+(course_five*cr5.get())+(course_six*cr6.get()))/(cr1.get()+cr2.get()+cr3.get()+cr4.get()+cr5.get()+cr6.get()),2)
                                    gpa = str(gpa)
                                    printGPA()
                                else:
                                    gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                                    error_credits()
                            else:
                                gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                                error_credits()
                        else:
                            gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                            error_credits()
                    else:
                        gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                        error_credits()
                else:
                    gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                    error_credits()
            else:
                gpa = 'not defined, please choose CR between 1 and 4 for course 6'
                error_credits()
        elif type(course_one) != float:
            error_grade(course_one)
        elif type(course_two) != float:
            error_grade(course_two)
        elif type(course_three) != float:
            error_grade(course_three)
        elif type(course_four) != float:
            error_grade(course_four)
        elif type(course_five) != float:
            error_grade(course_five)
        elif type(course_six) != float:
            error_grade(course_six)
    return

grade1=StringVar()
grade2=StringVar()
grade3=StringVar()
grade4=StringVar()
grade5=StringVar()
grade6=StringVar()

cr1=IntVar()
cr2=IntVar()
cr3=IntVar()
cr4=IntVar()
cr5=IntVar()
cr6=IntVar()

x=IntVar()

#Frames
top_frame = Frame(window) #Create Frame
#top_frame.pack(side=TOP) #Place frame
bottom_frame = Frame(window)
#bottom_frame.pack(side=BOTTOM)


#Text Labels
Welcome = Label(window, text="Please enter your estimated alphabet grades and credit hours below \n  ") #Create Text
Welcome.grid(row=0, columnspan=2) #Grid Text onto window

Field_one = Label(window, text='Grade 1') #Create entry text
Field_two = Label(window, text='Grade 2')
Field_three = Label(window, text='Grade 3')
Field_four = Label(window, text='Grade 4')
Field_five = Label(window, text='Grade 5')
Field_six = Label(window, text='Grade 6')

Field_Cone = Label(window, text='CH') #Create entry text
Field_Ctwo = Label(window, text='CH')
Field_Cthree = Label(window, text='CH')
Field_Cfour = Label(window, text='CH')
Field_Cfive = Label(window, text='CH')
Field_Csix = Label(window, text='CH')

empty=Label(window, text='') #Line skipper

entry_one = Entry(window, textvariable=grade1) #Store entry input to variable
entry_two = Entry(window, textvariable=grade2)
entry_three = Entry(window, textvariable=grade3)
entry_four = Entry(window, textvariable=grade4)
entry_five = Entry(window, textvariable=grade5)
entry_six = Entry(window, textvariable=grade6)

entry_Cone = Entry(window, textvariable=cr1) #Store entry input to variable
entry_Ctwo = Entry(window, textvariable=cr2)
entry_Cthree = Entry(window, textvariable=cr3)
entry_Cfour = Entry(window, textvariable=cr4)
entry_Cfive = Entry(window, textvariable=cr5)
entry_Csix = Entry(window, textvariable=cr6)

Field_one.grid(row=1, column=0) #Grid entry text onto window
Field_two.grid(row=2, column=0)
Field_three.grid(row=3, column=0)
Field_four.grid(row=4, column=0)
Field_five.grid(row=5, column=0)
Field_six.grid(row=6, column=0)

Field_Cone.grid(row=1, column=2) #Grid entry text onto window
Field_Ctwo.grid(row=2, column=2)
Field_Cthree.grid(row=3, column=2)
Field_Cfour.grid(row=4, column=2)
Field_Cfive.grid(row=5, column=2)
Field_Csix.grid(row=6, column=2)

empty.grid(row=7)

entry_one.grid(row=1, column=1) #Grid entry fields onto window
entry_two.grid(row=2, column=1)
entry_three.grid(row=3, column=1)
entry_four.grid(row=4, column=1)
entry_five.grid(row=5, column=1)
entry_six.grid(row=6, column=1)

entry_Cone.grid(row=1, column=3) #Grid entry fields onto window
entry_Ctwo.grid(row=2, column=3)
entry_Cthree.grid(row=3, column=3)
entry_Cfour.grid(row=4, column=3)
entry_Cfive.grid(row=5, column=3)
entry_Csix.grid(row=6, column=3)

#Buttons
button_one = Button(window, text="Calculate GPA", bg="purple", fg='white', command=grades) #click button to call function
empty=Label(window, text='')
button_two = Button(window, text="GPA Optimzer", bg="green", fg='white', command=Optimizer_Launcher) #click button to call function


radio1=Radiobutton(window, text='1 Courses', value=1, variable=x)
radio2=Radiobutton(window, text='2 Courses', value=2, variable=x)
radio3=Radiobutton(window, text='3 Courses', value=3, variable=x)
radio4=Radiobutton(window, text='4 Courses', value=4, variable=x)
radio5=Radiobutton(window, text='5 Courses', value=5, variable=x)
radio6=Radiobutton(window, text='6 Courses', value=6, variable=x)

radio1.grid(row=8, column=1)
radio2.grid(row=9, column=1)
radio3.grid(row=10, column=1)
radio4.grid(row=8, column=2)
radio5.grid(row=9, column=2)
radio6.grid(row=10, column=2)

empty.grid(row=11)
button_one.grid(row=12, column=1) #Grid button onto window
button_two.grid(row=12, column=2) #Grid button onto window

#TnC=Checkbutton(window, text='Use my info for research purposes')
#TnC.grid(columnspan=2)

#Menu
menu = Menu(window) #Create Menu in window
window.config(menu=menu)

oneMenu=Menu(menu) #Create menu 1
menu.add_cascade(label="Click Me", menu=oneMenu) #Main Dropdown
oneMenu.add_command(label="View Credits...", command=credits) #Option within menu
oneMenu.add_command(label="Install Virus", command=virus) #Option within menu

twoMenu=Menu(menu) #Create menu 2
menu.add_cascade(label="Don't Click here", menu=twoMenu) #Main Dropdown
twoMenu.add_command(label="Seriously, stop", command=time) #Option within menu

threeMenu=Menu(menu) #Create menu 3
menu.add_cascade(label="Secret Button", menu=threeMenu)
threeMenu.add_command(label="Very BIG secret", command=optimizer_propaganda) #Option within menu

#Status Bar
status = Label(window, text='I hope you offered Namaz...', bd=1, relief=FLAT) #Create Status Bar
empty.grid() #Leave line
empty2=Label(window, text='')
empty2.grid() #Leave line
status.grid(sticky=SW) #Grid status bar on to window


#Window loop
window.mainloop() #Inifinitely call the window function to ensure the application stays on-screen instead of executing once and exiting.
########################################################################################################################

#Code khatam hogaya bhai aur kya chaiyay?
#Ghar Jao
#Ajeeb.