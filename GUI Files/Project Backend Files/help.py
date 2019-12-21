#Helper Functions

def pop(stack):
    return stack.pop(-1)

def push(stack, item):
    stack.append(item)

def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
    
def addnodes(G,N):
    for i in N:
        G[i] = []
    return G

def addnodes1(G,N):
    for i in N:
        G[i+('','')] = []
    return G

def addedges(dic, dir):
    for i in dir:
        for f in range (len(i)-1):
                for j in range(len(i)-1):
                     if i[j+1] not in dic[i[j]]:
                        dic[i[j]].append(i[j+1])
    return dic

def graphmaker(text):
    f = open(text, 'r')
    f_new = f.read().split('\n')

    paths = []
    for path in f_new:
        path = tuple(path.split('\\'))
        paths.append(path)

    G_Course = {}
    Nodes = []

    for i in paths:
        for f in range(len(i)):
            Nodes.append(i[f])


    addnodes(G_Course, Nodes)
    addedges(G_Course, paths)

    Categories = []
    SubCategories = []
    for i in G_Course[text1]:
        Categories.append(tuple(i.split(' ')))
        if G_Course[i] == []:
            SubCategories.append(tuple(i.split(' ')))

    for i in Categories:
        for f in range(len(G_Course[' '.join(i)])):
            SubCategories.append(tuple(G_Course[' '.join(i)][f].split(' ')))
    return G_Course, SubCategories, Categories
            
    
def displayGraph(G):
    for i in G:
        print(i, ':' , G[i])

def DFS_Leaf(G, Node, Cats):
    stack = []
    visited = []
    push(stack,Node)
    while isEmpty(stack) == False:
        x = pop(stack)
        push(visited, x)
        if len(G[x]) == 1:
            val = tuple(str(x).split(' '))
            Cats.append(val)
        for i in range(len(G[x])):
            if G[x][i] in visited:
                pass
            else:
                push(stack, G[x][i])


def CategoryMaker(G_Course, Categories, text1):
    for i in G_Course[text1]:
        Categories.append(tuple(i.split(' ')))
        if G_Course[i] == []:
            SubCategories.append(tuple(i.split(' ')))
            
def SubCatMaker(Categories, SubCategories):
    for i in Categories:
        for f in range(len(G_Course[' '.join(i)])):
            SubCategories.append(tuple(G_Course[' '.join(i)][f].split(' ')))
            
def addNodes_IdealGraph(lst, G):
    for category in lst:
        if len(category) != 4:
            node = (category[0],category[1], '', '') 
            G[node] = []
            for sub_category in category[2]:
                node = (sub_category[0], sub_category[1], sub_category[2], sub_category [3])
                G[node] = []
        else:
            node = (category[0], category[1], category[2], category [3])
            G[node] = []
    return G

def addNodes_and_edges_MainGraph(lstt, lst, G):
    for category in lstt:
        temp_lst = []
        if len(category) == 4:
            if category[2] != '' and category[3] != '':
                node = (category[0], category[1], category[2], category [3])
                G[node] = []
        else:
            node1 = (category[0],category[1], '', '')
            for sub_category in category[2]:
                if sub_category[2] != '' and sub_category[3] != '':
                    node2 = (sub_category[0], sub_category[1], sub_category[2], sub_category [3])
                    temp_lst.append(node2)
                    lst.append(node2)
                    G[node2] = node1
            if len(temp_lst)!=0:
                G[node1] = temp_lst
    return lstt, G

def addEdges_IdealGraph(lstt, lst, G):
    for category in lstt:
        node1 = (category[0],category[1], '', '')
        if len(category) != 4:
            for sub_category in category[2]:
                node2 = (sub_category[0], sub_category[1], sub_category[2], sub_category [3])
                lst.append(node2)
                G[node1].append(node2)
                G[node2].append(node1)
    return G, lst
                
def addNodes_weights(graph, G):
    for nodes in graph:
        node = nodes[0]
        G[node]= []
    return G

def addWeights(graph, lst, G):
    for category in graph:
        node = category[0]
        if category[2]!='' and category not in lst:
            weightage = float(category[1])
            total_marks = float(category[2])
            marks_obtained = float(category[3])
            marks = (marks_obtained/total_marks)*weightage
            G[node] = weightage, marks
        elif category not in lst:
            sum_of_subcategories = 0
            sum_of_weightage = 0
            for sub_category in graph[category]:
                sub_node = sub_category[0]
                weightage = float(sub_category[1])
                total_marks = float(sub_category[2])
                marks_obtained = float(sub_category[3])
                marks = (marks_obtained/total_marks)*weightage
                G[sub_node] = (node, str(weightage), str(marks))
                sum_of_subcategories += marks
                sum_of_weightage += weightage
            weightage = float(category[1])
            marks = (sum_of_subcategories/sum_of_weightage)*weightage
            G[node] = weightage, marks
    return G

def calculate_current_percentage(G):
    marks = 0
    weightage = 0
    for category in G:
        if type(G[category][0])==float:
            marks += G[category][1]
            weightage += G[category][0]
    percentage = (marks/weightage)*100
    return round(percentage, 3), marks, weightage


def gradescale(percentage, SSE):
    percentage = int(percentage)
    if SSE == False:
        if percentage >= 97:
            return 'A+'
        elif percentage >= 93 and percentage <= 96:
            return 'A'
        elif percentage >= 90 and percentage <= 92:
            return 'A-'
        elif percentage >= 80 and percentage <= 89:
            return 'B+'
        elif percentage >= 75 and percentage <= 79:
            return 'B'
        elif percentage >= 70 and percentage <= 74:
            return 'B-'
        elif percentage >= 67 and percentage <= 69:
            return 'C+'
        elif percentage >= 63 and percentage <= 66:
            return 'C'
        elif percentage >= 60 and percentage <= 62:
            return 'C-'
        else:
            return 'F'
    else:
        if percentage >= 95:
            return 'A+'
        elif percentage >= 90 and percentage <= 94:
            return 'A'
        elif percentage >= 85 and percentage <= 89:
            return 'A-'
        elif percentage >= 80 and percentage <= 84:
            return 'B+'
        elif percentage >= 75 and percentage <= 79:
            return 'B'
        elif percentage >= 70 and percentage <= 74:
            return 'B-'
        elif percentage >= 67 and percentage <= 69:
            return 'C+'
        elif percentage >= 63 and percentage <= 66:
            return 'C'
        elif percentage >= 60 and percentage <= 62:
            return 'C-'
        else:
            return 'F'
    
def Enqueue(queue, item, priority):
    length=len(queue)
    tup=(item, priority)
    c=0
    for original in queue:
        alphabet, priority2 = original
        if priority<priority2:
            queue.insert(c, tup)
            return queue
        c+=1
    queue.insert(length, tup)
    return queue
    
def grade_to_minimum_percentage(grade, SSE):
    if SSE == False:
        if grade == 'A+':
            return 97
        elif grade == 'A':
            return 93
        elif grade == 'A-':
            return 90
        elif grade == 'B+':
            return 80
        elif grade == 'B':
            return 75
        elif grade == 'B-':
            return 70
        elif grade == 'C+':
            return 67
        elif grade == 'C':
            return 63
        elif grade == 'C-':
            return 60
        else:
            return 59
    else:
        if grade == 'A+':
            return 95
        elif grade == 'A':
            return 90
        elif grade == 'A-':
            return 85
        elif grade == 'B+':
            return 80
        elif grade == 'B':
            return 75
        elif grade == 'B-':
            return 70
        elif grade == 'C+':
            return 67
        elif grade == 'C':
            return 63
        elif grade == 'C-':
            return 60
        else:
            return 59
    
def calculator(cur_marks, cur_weightage, min_percent, weightage_cat):
    x = ((min_percent*(cur_weightage + weightage_cat))/100) - cur_marks
    if x > weightage_cat:
        cur_marks = cur_marks + weightage_cat
        cur_weightage = cur_weightage + weightage_cat
        return cur_marks, cur_weightage
    else:
        percent = (x/weightage_cat)*100
        return percent
    
def weighted_graph_calculation(category1, weighted_graph):
    category1 = category1[0]
    subcategories_weightage = 0
    subcategories_marks = 0
    for node in weighted_graph:
        if weighted_graph[node][0] == category1:
            subcategories_weightage += float(weighted_graph[node][1])
            subcategories_marks += float(weighted_graph[node][2])
        if node == category1:
            category_weightage = weighted_graph[category1][0]
            category_marks = weighted_graph[category1][1]
    return subcategories_weightage, subcategories_marks, category_weightage, category_marks 

def calculator_sub_nodes(subcats_weightage, subcats_marks, cat_weightage, cat_marks, cur_marks, cur_weightage, min_percent, subcat_weightage):
    x = ((((min_percent*cur_weightage)/100)-(cur_marks-cat_marks))*((subcats_weightage+subcat_weightage)/cat_weightage))- subcats_marks
    if x > subcat_weightage:
        cur_marks = (cur_marks-cat_marks)+((subcats_marks+subcat_weightage)/(subcats_weightage+subcat_weightage))* cat_weightage
        return cur_marks, cur_weightage
    else:
        percent = (x/subcat_weightage)*100
        return percent


def FrstInputTaker(G_Course, formatted_style, SubCategories, categories_updated, text1):
    for actual_node in G_Course[text1]:
        actual_node1 = tuple(actual_node.split(' '))
        temp_list = []
        if actual_node1 not in SubCategories:
            for final_node in G_Course[actual_node]:
                final_node1 = tuple(final_node.split(' '))
                print('Please input marks obtained of ' + str(final_node1[0]) +' : ', end = '')
                marks_obtained = input()
                print('Please input total marks of ' + str(final_node1[0]) +' : ', end = '')
                total_marks = input()
                print()
                temp_list.append(final_node1 + (total_marks, marks_obtained))
        else:
            print('Please input marks obtained of ' + str(actual_node1[0]) +' : ', end = '')
            marks_obtained = input()
            print('Please input total marks of ' + str(actual_node1[0]) +' : ', end = '')
            total_marks = input()
            print()
            formatted_style.append(actual_node1 + (total_marks, marks_obtained))
            categories_updated.append(actual_node1 + (total_marks, marks_obtained))
        if len(temp_list)!=0:
            formatted_style.append(actual_node1 + (temp_list,))
            categories_updated.append(actual_node1 + ('', ''))
            

def InputTaker(formatted_style, categories_updated):
    formatted_style_copy = []
    categories_updated_copy = []
    for category in formatted_style:
        temp_list = []
        if len(category) == 4:
            if category[2] == '' and category[3] == '':
                print('Please input marks obtained of ' + str(category[0]) +' : ', end = '')
                marks_obtained = input()
                print('Please input total marks of ' + str(category[0]) +' : ', end = '')
                total_marks = input()
                print()
                formatted_style_copy.append((category[0], category[1], total_marks, marks_obtained))
                categories_updated_copy.append((category[0], category[1], total_marks, marks_obtained))
            else:
                formatted_style_copy.append((category[0], category[1], category[2], category[3]))
                categories_updated_copy.append((category[0], category[1], category[2], category[3]))
        else:
            for sub_category in category[2]:
                if sub_category[2] == '' and sub_category[3] == '':
                    print('Please input marks obtained of ' + str(sub_category[0]) +' : ', end = '')
                    marks_obtained = input()
                    print('Please input total marks of ' + str(sub_category[0]) +' : ', end = '')
                    total_marks = input()
                    print()
                    temp_list.append((sub_category[0], sub_category[1], total_marks, marks_obtained))
                else:
                    temp_list.append((sub_category[0], sub_category[1], sub_category[2], sub_category[3]))
        if len(temp_list)!=0:
            formatted_style_copy.append((category[0], category[1], temp_list))
            categories_updated_copy.append((category[0], category[1], '', ''))
    return formatted_style_copy, categories_updated_copy

                
def gradeboi():
    while flag == False and higher == False or flag == True and higher == True:
        print('\n\n')
        print('Please input desired grade : ', end='')
        desired_grade = str(input())
        minimum_percent = help.grade_to_minimum_percentage(desired_grade, SSE)
        for category in priority_queue:
            category = category[0]
            if category not in Real_time_graph:
                unknown = help.calculator(current_marks, current_weightage, minimum_percent, int(category[1]))
                if type(unknown)==tuple:
                    printing_lst.append(str(category[0]) + ' : ' + str(100) + '%')
                    current_marks, current_weightage = unknown
                    flag = False
                else:
                    printing_lst.append(str(category[0]) + ' : ' + str(unknown) + '%')
                    flag = True
                    for i in printing_lst:
                        print(i)
                    if desired_grade != 'A+':
                        print()
                        print('Do you want to test for a higher desired grade? (please enter "True" or "False") : ', end = '')
                        flag2 = False
                        while flag2 == False:
                            higher_input = input()
                            if higher_input == 'True' or higher_input == 'true':
                                higher = True
                                flag2 = True
                                printing_lst = []
                                printing_lst.append('For you to achieve your desired grade, you need to achieve the following percentages in the following categories : ')
                                break
                            elif higher_input == 'False' or higher_input == 'false':
                                higher = False
                                flag2 = True
                                break
                            else:
                                print()
                                print('Error : Please enter "True" or "False"')
                                print('Do you want to test for a higher desired grade? (please enter "True" or "False") : ', end = '')
                    break
            else:
                category2 = Ideal_graph[category][len(Real_time_graph[category])]
                subcategories_weightage, subcategories_marks, category_weightage, category_marks = help.weighted_graph_calculation(category, weightage_and_marks)
                unknown = help.calculator_sub_nodes(subcategories_weightage, subcategories_marks, category_weightage, category_marks, current_marks, current_weightage, minimum_percent, int(category2[1]))
                if type(unknown)==tuple:
                    printing_lst.append(str(category2[0]) + ' : ' + str(100) + '%')
                    current_marks, current_weightage = unknown
                    flag = False
                else:
                    printing_lst.append(str(category2[0]) + ' : ' + str(unknown) + '%')
                    flag = True
                    for i in printing_lst:
                        print(i)
                    if desired_grade != 'A+':
                        print()
                        print('Do you want to test for a higher desired grade? (please enter "True" or "False") : ', end = '')
                        flag2 = False
                        while flag2 == False:
                            higher_input = input()
                            if higher_input == 'True' or higher_input == 'true':
                                higher = True
                                flag2 = True
                                printing_lst = []
                                printing_lst.append('For you to achieve your desired grade, you need to achieve the following percentages in the following categories : ')
                                break
                            elif higher_input == 'False' or higher_input == 'false':
                                higher = False
                                flag2 = True
                                break
                            else:
                                print()
                                print('Error : Please enter "True" or "False"')
                                print('Do you want to test for a higher desired grade? (please enter "True" or "False") : ', end = '')
                                break

                                if flag == False:
                                    if flag == False and higher == True:
                                        print('Error: This grade is no longer achievable')
                                        break
                                    else:
                                        print('Error: This grade is no longer achievable')
                                        print()