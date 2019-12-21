import help

f = open('DSA.txt', 'r')
f_new = f.read().split('\n')
paths = []
for path in f_new:
    path = tuple(path.split('\\'))
    paths.append(path)

G = {}
G_Course = {}
Nodes = []

for i in paths:
    for f in range(len(i)):
        Nodes.append(i[f])

Cats = []
SubCats = []


#print('Node List',Nodes)
#print('\n\n')

help.addnodes(G_Course, Nodes)
print('\n\n')
help.addedges(G_Course, paths)
#print('DSA\n\n', G_Course)
#print('\n\n\n Adjacency List \n\n\n')
#for i in G_Course:
#    print('\t', i, ':', G_Course[i], '\n')
#print('\n\n\n')
#help.DFS_Leaf(G_Course, 'DSA',Cats,)
#print('C', Cats)
#
#
#
#for i in Cats:
#    i = i + ('','')
#    print('')
#    print(i)
#
#G_Course1 = {}
#
#help.addnodes1(G_Course1, Cats)
#
#print(G_Course1)

Categories = []
for i in G_Course['DSA']:
    Categories.append(tuple(i.split(' ')))
SubCats = []
for i in Categories:
    for f in range(len(G_Course[' '.join(i)])):
        SubCats.append(tuple(G_Course[' '.join(i)][f].split(' ')))

print(Categories)
print('\n\n')
print(SubCats)

    


