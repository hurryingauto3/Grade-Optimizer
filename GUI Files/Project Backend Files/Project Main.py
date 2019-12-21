import help
import pickle
import os

#Misc Variables
CurDir = os.getcwd()

#Course and School Database
DSSE = ['DSA.txt', 'Calculus_2.txt','Discrete_Math.txt','IntroToSustainaibility.txt'] 
AHSS = ['Modernity.txt','WiredforWriting.txt']
Schools = {'DSSE':DSSE, 'AHSS':AHSS}
SchoolsList = ['DSSE', 'AHSS']

Username = input('Please input your username: ') # Getting Username

First_time_User = False #Created flag for First time users
NewCourse = False #Created flag for a new course addition, as an old user may add a new course as well

#Opening the Namelist file to check database for currently registered users
File = open(CurDir + '\\Users\\'+'Userlist.txt', 'a+')
FileR = open(CurDir + '\\Users\\'+'Userlist.txt', 'r')
Name = FileR.read().split('\n')
Namelist = []
for i in Name:
    Namelist.append(i)
    
if Username in Namelist: #Checks if user is new
    UPath = os.path.join(CurDir+'\\Users\\'+Username, Username+'CourseData.txt')
    NameFile = open(UPath, 'a+')
    NameFileR = open(UPath, 'r') #Opens the user's file
else:
    First_time_User = True #Declares user as new user
    os.mkdir(CurDir + '\\Users\\' + Username)
    UPath = os.path.join(CurDir+'\\Users\\'+Username, Username+'CourseData.txt')
    NameFile = open(UPath, 'a+') #Opens new file for new user
    NameFileR = open(UPath, 'r')
    File.write(Username + '\n')
    File.close()
    FileR.close()

#declares course as new if user is new
if First_time_User == True:
    NewCourse = True

#################################################################################################################################
##################################################################################################################################
Exit = False
while Exit==False:
    #Shows user the Available schools and asks for choice
    print('This is the list of available Schools: \n\n',SchoolsList) 
    Key = input('\n\nType the name of your School of Choice: ')
    Key = Key.upper().strip(' ')

    #Shows user available courses in selected school and takes input
    print('\n\nThis is the list of Available courses in your chosen school: \n\n', Schools[Key])
    number1 = int(input('\n\nSelect your Course of Choice using a number of 1 or more: ')) - 1
    text = Schools[Key][number1]
    text1 = text.strip('.txt')

    print('\n\nYou have selected:', text1, '\n\n') #Reiterates user's choice

    SSE = False #Creating a flag for SSE Courses
    if text in DSSE: #Checking flag for later Grade Thresholds
        SSE = True
        
    ########################################################################################################################################

    if First_time_User == False: #Added a check for new user
        course_list = [] 
        Course1 = NameFileR.read().split('\n')
        for i in Course1:
            course_list.append(i) #adds courses to the course list
        if text1 not in course_list: #check if course is new for old user by checking in the course list
            NewCourse = True

    #adds course to name file if course is new
    if NewCourse == True:
        NameFile.write(text1+'\n')#Registering the new course
        NameFile.close()
        
    NameFileR.close()

    #######################################################################################################################################

    #Getting the file of the selected course from the Course Directory
    fpath = os.path.join(CurDir+'\\Courses', text)
    f = open(fpath)
    f_new = f.read().split('\n')

    #Turning each directory in the file into a tuple format, preparing for creating dictionary
    paths = []
    for path in f_new:
        path = tuple(path.split('\\'))
        paths.append(path)
    Nodes = []
    for i in paths: #Creating nodes list
        for f in range(len(i)):
            Nodes.append(i[f])

    G_Course = {} #Dictionary of Course defined
    help.addnodes(G_Course, Nodes) #Adding nodes to Course Dictionary
    help.addedges(G_Course, paths) #Adding edges to Course Dictionary

    Categories = [] 
    SubCategories = []

    for i in G_Course[text1]:
        Categories.append(tuple(i.split(' ')))
        if G_Course[i] == []:
            SubCategories.append(tuple(i.split(' ')))

    for i in G_Course[text1]:
        Categories.append(tuple(i.split(' ')))
        if G_Course[i] == []:
            SubCategories.append(tuple(i.split(' ')))
            


        
    categories_updated = []
    formatted_style = []
        
    print('If marks not obtained, leave space blank')

    if NewCourse == False:
        #if the course has already been registered before, the data is read.
        with open (CurDir + '\\Users\\' + Username+ '\\' + Username+text1+'Form.txt', 'rb') as fp:
            formatted_style = pickle.load(fp)
        with open (CurDir + '\\Users\\' + Username+ '\\' + Username+text1+'Cat.txt', 'rb') as fp:
            categories_updated = pickle.load(fp)
            
            formatted_style, categories_updated = help.InputTaker(formatted_style, categories_updated)
    else:
        #if the course is new irrespective of the user, new data is taken as input
        help.FrstInputTaker(G_Course, formatted_style, SubCategories, categories_updated, text1)
        
    print(categories_updated)
    print('\n\n')
    print(formatted_style)


    #The Input data is saved onto a text file as a pickled list
    with open(CurDir + '\\Users\\' + Username+ '\\' + Username+text1+'Form.txt', 'wb') as fp:
        pickle.dump(formatted_style, fp) 
    with open(CurDir + '\\Users\\' + Username+ '\\' + Username+text1+'Cat.txt', 'wb') as fp:
        pickle.dump(categories_updated, fp)


    Ideal_graph = {}
    Real_time_graph = {}
    weightage_and_marks = {}
    main_lst = []
    real_time_lst = []

    help.addNodes_IdealGraph(formatted_style, Ideal_graph)
    help.addEdges_IdealGraph(formatted_style, main_lst, Ideal_graph)
    help.addNodes_and_edges_MainGraph(formatted_style, real_time_lst, Real_time_graph)


    if Real_time_graph != {}:
        help.addNodes_weights(Real_time_graph, weightage_and_marks)
        help.addWeights(Real_time_graph, real_time_lst, weightage_and_marks)
        percentage, current_marks, current_weightage = help.calculate_current_percentage(weightage_and_marks)    
        grade = help.gradescale(percentage, SSE)
        print('\n\nYour current course percentage is : ' + str(percentage) + ' (' + str(grade) + ')')
    print('\n\n')
    
    full_graph = False
    for i in categories_updated:
        if i[2]!="" and i[3]!="":
            full_graph = True
            break
    if full_graph ==True:
        print('Error : Grade is at maximum')
        break

    ###
    ###
    ###PHASE 3
    ###
    ###
    ###
    input_grade_again = True

    while input_grade_again == True:
        new_desired_grade = False
        while new_desired_grade == False:
            print('\n\n')
            print('Please input desired grade : ', end='')
            desired_grade = str(input())
            priority = {'Class_Participation' : 0, 'Homework' : 1, 'Assignment' : 1, 'Lab' : 2, 'Quizzes' : 3, 'Class_Project' : 4, 'Test' : 5, 'Midterm_Exam' : 6, 'Final_Exam' : 7}
            priority_queue = []
            temp_lst = []
            minimum_percent = help.grade_to_minimum_percentage(desired_grade, True)
            if minimum_percent <= percentage:
                print()
                print('Error : Inputted desired grade or higher has already been achieved')
            else:
                new_desired_grade = True

        for category in categories_updated:
            if category in Real_time_graph:
                if len(Ideal_graph[category]) != len(Real_time_graph[category]):
                    position = priority[category[0]]
                    help.Enqueue(priority_queue, category, position)
                else:
                    pass
            else:
                position = priority[category[0]]
                help.Enqueue(priority_queue, category, position)


        printing_lst = []
        printing_lst.append('For you to achieve your desired grade, you need to achieve the following percentages in the following categories : ')

        flag = False

        for category in priority_queue:
            category = category[0]
            if category not in Real_time_graph:
                unknown = help.calculator(current_marks, current_weightage, minimum_percent, int(category[1]))
                if type(unknown)==tuple:
                    printing_lst.append(str(category[0]) + ' : ' + str(100) + '%')
                    current_marks, current_weightage = unknown
                else:
                    printing_lst.append(str(category[0]) + ' : ' + str(unknown) + '%')
                    flag = True
                    break
            else:
                category2 = Ideal_graph[category][len(Real_time_graph[category])]
                subcategories_weightage, subcategories_marks, category_weightage, category_marks = help.weighted_graph_calculation(category, weightage_and_marks)
                unknown = help.calculator_sub_nodes(subcategories_weightage, subcategories_marks, category_weightage, category_marks, current_marks, current_weightage, minimum_percent, int(category2[1]))
                if type(unknown)==tuple:
                    printing_lst.append(str(category2[0]) + ' : ' + str(100) + '%')
                    current_marks, current_weightage = unknown
                else:
                    printing_lst.append(str(category2[0]) + ' : ' + str(unknown) + '%')
                    flag = True
                    break

        if flag == True:
            for i in printing_lst:
                print(i)
            print()
            print('Do you want to input another desired grade? (Please input "yes" or "no") : ', end = '')
            kill = input()
            if kill == 'no' or kill == 'No':
                input_grade_again = False
        else:
            print('Error : Desired grade is unachievable at current moment')
            print()
            print('Do you want to input another desired grade? (Please input "yes" or "no") : ', end = '')
            kill = input()
            if kill == 'no' or kill == 'No':
                input_grade_again = False
    print()
    print('Do you want to test for another course? (Please input "yes" or "no") : ', end='')
    kill_program = input()
    if kill_program == 'No' or kill_program == 'no':
        Exit = True
