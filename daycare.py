
# cs 3100 assignment : daycare --> greedy algorithm solution
def daycare(room_map):
    # k = 0
    result = 0
    same = []
    positive = []
    negative = []
    for x in room_map:
        if x[2]==0:
            same.append(x)
        elif x[2]<0:
            negative.append(x)
        elif x[2]>0:
            positive.append(x)
    
    positive = sorted(positive, key=lambda x: x[0])
    negative = sorted(negative, key=lambda x: x[1], reverse=True)

    kids =0
    trailer = 0
    space = 0 #room in daycare
    for x in positive:
        #kids+=x[0]
        kids = x[0]
        if space !=0:
            leftover = kids-space
            if leftover > 0 :
                # trailer += leftover
                trailer = max(trailer,leftover)
        else: #space is zero, all kids in trailer 
            trailer += kids
        space += x[2]
        #

    for x in same:
        kids = x[0]
        # if space !=0:
        leftover = kids-space
        if leftover > 0 :
            trailer = max(trailer,leftover)
            
        space += x[2]
    
    for x in negative:
        kids = x[0]
        # if space !=0:
        leftover = kids-space
        if leftover > 0 :
            trailer = max(trailer,leftover)
       
        space += x[2]
    return trailer


answer_ = []
count = 0
while count<2:
    rooms = input()
    rooms = int(rooms)
    k = 0
    t = 0
    room_map = []

    for x in range(rooms):
        sizes = input()
        sizes = sizes.split()
        k = int(sizes[1])-int(sizes[0])
        room_map.append([int(sizes[0]), int(sizes[1]), k])

    answer = daycare(room_map)
    answer_.append(answer)
    count +=1
    # print(answer)
    
for x in answer_:
    print(x)


