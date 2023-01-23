
# FORD FULKERSON AND NETWORK FLOW GRAPH FOR STUDENT REGISTRATION PROBLEM

# constraints:
    #1. an optimal set of registrations may cause an individual student to be enrolled in too few or too many classes 
    #the algorithm must ensure that this dosnt happen ( also this may not be possible given constraints)
    # number N = exact number of courses that students must be enrolled in (no more no less)--> less
    # each course has a course cap which is the max number of students that can enroll in the course

# the number of courses that a student should be enrolled in is provided only once, and applies to all students.
# the course cap is course specific, and thus is provided once for every course 

def create_network(students, courses, min_enroll):
   #
    index = {}

    for x, stud in enumerate(students, start=1):
        index[stud] = x
    for y, course in enumerate(courses, start=x+1):
        index[course] = y
    
    #length of both students and courses plus sink and start
    size_of_graph = len(students)+ len(courses)+2 

    network = [[0 for x in range(size_of_graph)] for y in range(size_of_graph)]

    for stud in students:
        #setting min enrollment for students = 2
        network[0][index[stud]] = int(min_enroll)

        #edges inside the graph, students can only enroll in one class once
        for request in students[stud]:
            network[index[stud]][index[request]] = 1
        
    for course in courses:
        network[index[course]][size_of_graph-1]= courses[course]
    
    return [network, size_of_graph]


def depth_first(start, end, path):
    # basic depth first implementation to complete FF algorithm 
    #using stack instead of recursion

    visited = []
    stack = []
    stack = [0]
    visited.append(start)

    while stack:
        node = stack.pop(0)
        for index, nod in enumerate (network[node]):
            if nod > 0 and index not in visited:
                stack.append(index)
                visited.append(index)
                path[index]= node
                if index == end:
                    return True
    return False 



def ford_fulkerson(network, size):
    first_size = len(network)
    source = 0 
    sink = first_size-1
    max_flow = 0
    aug_path = [-1 for x in range(size)]

    #while there is an augmenting path (found by dfs)
    while depth_first(source, sink, aug_path):
        temp1 = sink
        min_flow = float('inf')
        while temp1 != source:
            min_flow = min(min_flow, network[aug_path[temp1]][temp1])
            temp1 = aug_path[temp1]

        max_flow+=min_flow
        temp2 = sink
        while temp2 != source:
            y = aug_path[temp2]
            network[y][temp2]-= min_flow
            network[temp2][y] += min_flow
            temp2 = aug_path[temp2]
        
    return max_flow


# reading in the input 

total_students = []
total_courses = []
courses_needed =[]
# testfile = open("schedule.txt")
#first_line = testfile.readline().split()
while True:
    # print(first_line)
    #if first_line == [0,0,0]:
    first_line = input().split()

    r = int(first_line[0])
    c = int(first_line[1])
    n = int(first_line[2])

    #creating a map to hold the students and their couses 

    if r == 0 and c== 0 and n== 0:
        break

    students = {}
    courses = {}
    courses_needed.append(n)


    for x in range(r):
        line = input().split()
        stud = line[0]
        course = line[1]

        if stud in students:
            students[stud].append(course)
        else:
            students[stud] = [course]
        
    for y in range(c):
        line = input().split()
        course = line[0]
        cap = line[1]
        course=course

        courses[course]= int(cap)

    total_students.append(students)
    total_courses.append(courses)
    end = input()

#ford_length = len(total_students)+len(total_courses)+2

total_length = len(total_students)
for x in range(total_length):
    if total_students[x] == {}:
        # if the input is 0
        print('Yes')
    else:
        #
        make = create_network(total_students[x], total_courses[x], courses_needed[x])
        network = make[0]
        size = make[1]
        # for row in g.G:
        #     print(row)
        max_flow = ford_fulkerson(network, size)

        if max_flow < (courses_needed[x] * len(total_students[x])):
            print('No')
        else:
            print('Yes')
