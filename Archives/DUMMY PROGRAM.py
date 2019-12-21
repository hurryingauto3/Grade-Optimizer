import help

SSE = False

formatted_style = [('Class_Project', '15', [('Interim_Demo', '15', '', ''), ('Implementation_of_DSA_Techniques', '20', '', ''), ('Interface_Output_Results', '15', '', ''), ('Challenges_Addressed', '10', '', ''), ('Completeness', '25', '', ''), ('QnA', '15', '', '')]), ('Assignment', '15', [('Assignment_1', '100', '100', '89.2'), ('Assignment_2', '100', '', ''), ('Assignment_3', '100', '', '')]), ('Class_Participation', '5', '', ''), ('Lab', '8', [('Lab_1', '100', '100', '100'), ('Lab_2', '100', '100', '100'), ('Lab_3', '100', '100', '89'), ('Lab_4', '100', '100', '100'), ('Lab_5', '100', '100', '63'), ('Lab_6', '100', '', ''), ('Lab_7', '100', '', ''), ('Lab_8', '100', '', ''), ('Lab_9', '100', '', ''), ('Lab_10', '100', '', ''), ('Lab_11', '100', '', ''), ('Lab_12', '100', '', '')]), ('Quizzes', '7', [('Quiz_1', '100', '100', '60'), ('Quiz_2', '100', '100', '100'), ('Quiz_3', '100', '100', '100'), ('Quiz_4', '100', '100', '100'), ('Quiz_5', '100', '', ''), ('Quiz_6', '100', '', ''), ('Quiz_7', '100', '', '')]), ('Midterm_Exam', '15', '100', '57'), ('Final_Exam', '30', [('Final_Exam_Theory', '10', '', ''), ('Final_Exam_Lab', '20', '', '')])]
categories_updated = [('Class_Project', '15', '', ''), ('Assignment', '15', '', ''), ('Class_Participation', '5', '', ''), ('Lab', '8', '', ''), ('Quizzes', '7', '', ''), ('Midterm_Exam', '15', '100', '57'), ('Final_Exam', '30', '', '')]

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
    print('Your current course percentage is : ' + str(percentage) + '% (' + str(grade) + ')')

print('\n\n')
help.displayGraph(weightage_and_marks)
print('\n\n')
##
##
##PHASE 3
##
##

real_time_graph_copy = Real_time_graph.copy()
weights = weightage_and_marks.copy()
priority = {'Class_Participation' : 0, 'Homework' : 1, 'Assignment' : 1, 'Lab' : 2, 'Quizzes' : 3, 'Class_Project' : 4, 'Test' : 5, 'Midterm_Exam' : 6, 'Final_Exam' : 7}
priority_queue = []
temp_lst = []
print('\n\n')
#print('Please input desired grade : ', end='')
desired_grade = 'A-'
minimum_percent = help.grade_to_minimum_percentage(desired_grade, SSE)

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
else:
    print('Error : Desired grade is unachievable at current moment')
