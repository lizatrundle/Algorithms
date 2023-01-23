#greedy algorithm solution 
# Liza Trundle CS 3100 


def moving_boxes(num_boxes, take_home, whole, half):
    cost = 0
    # diff = num_boxes-take_home
    while num_boxes > 0 :
        if num_boxes // 2 >= take_home:
            num_boxes = num_boxes //2
            cost += half
        elif num_boxes//2 <= take_home:
            num_boxes = num_boxes - take_home
            cost += (whole*num_boxes)
            break

    return cost 

# my_file = open("move.txt")
# test_cases = my_file.readline()
test_cases = input()
test_cases = int(test_cases)

for case in range(test_cases):
    test_case_dict = {}
    # info = my_file.readline().split()
    info = input().split()
    num_boxes = int(info[0])
    take_home = int(info[1])
    companies = int(info[2])
    # available = int(num_boxes)-int(take_home)
    for comp in range(companies):
        # info = my_file.readline().split()
        info = input().split()
        name = info[0]
        whole = int(info[1])
        half = int(info[2])
        min = moving_boxes(num_boxes, take_home, whole,half)
        test_case_dict[name]=min
        
    
    sort_data = sorted(test_case_dict.items(), key=lambda x: x[1], reverse=False)
    print("Case", case+1)
    for x in sort_data:
        print(x[0], x[1])



