#Emt8kdn Liza Trundle trading
import math

#nput is the points sorted by y, the median, and the width of the strip
#returns a list of all the points that are located within the
# strip that we need to check for 

# the strip points are the points sorted by y
#checking with points in the whole galaxy are within delta of eachother 
def get_strip(points, median, width):
    point_list= []
    for point in points:
        if median - width <= point[0] <= median + width:
            point_list.append(point)
    return point_list
    
def get_distance(p1, p2):
    return (math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))

def brute_force_closest_pair(points):
    #makes the current closest pair infinity
    closest_pair = float('inf')
    for x in range(len(points)):
        for y in range(x+1, len(points)):
            if get_distance(points[x], points[y]) < closest_pair:
                closest_pair = get_distance(points[x], points[y])
    #make sure to sort it though 
    sorted_by_y_value = sorted(points, key = lambda x: x[1])
    # closest_pair = round(closest_pair, 4)
    return closest_pair, sorted_by_y_value

def merge(left, right):
        output = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            
            if left[i] < right[j]:
                output.append(left[i])
                # 10. Move pointer to the right
                i += 1
            else:
                output.append(right[j])
                j += 1
        output.extend(left[i:])
        output.extend(right[j:])

        return output
  

def closest_pair(points):
    size = len(points)
    #base case: if there are less than 4 points, use brute force to find the closest pair
    if size < 2:
        return brute_force_closest_pair(points)
    
    #divide: split list into two halves, save the median, split down the x axis
    divide_point = len(points) // 2
    left = points[:divide_point]
    right = points[divide_point:]

    distance_left, sorted_left_by_y = closest_pair(left)
    distance_right, sorted_right_by_y = closest_pair(right)

    #with is equal to delta 
    width = min(distance_left, distance_right)



    #combine: find the closest pair in the left and right halves
    #find the closest pair in the strip
    #return the min of the three
    #MERGE the two sorted by y list to get the total points 
    merged = merge(sorted_left_by_y, sorted_right_by_y)
    #use ths merged to get the strip 
    strip = get_strip(merged, points[divide_point][0], width)
    strip_size = len(strip)
    # now we have the strip, so we need to check the distance between all of the points in the strip
    for x in range(strip_size):
         for point in range(x+1, strip_size, x+8): #look at the next 7 points
            dist = get_distance(strip[x], strip[point])
            if dist < width:
                width = dist
    # width = str(width)

    return width, merged
    #this will return the closest pair distance and also the sorted 
    # lists by y value, to be able to use in the recursive calls  


#this a function to return the min distnace, formatted as a string, regardless of breadth approach or closest pair
def sort_closest_pair(points):
    points = sorted(points)
    min_distance = closest_pair(points)[0]
    if min_distance > 10000:
        return "infinity"
    # min_distance = str(min_distance)
    return "{:.4f}".format(min_distance)

num_stars = int(input())
while (num_stars!=0):
    star_locations = []
    for x in range(num_stars):
        x, y = input().split()
        # x, y = test_file.readline().split()
        star_locations.append((float(x), float(y)))
    print(sort_closest_pair(star_locations))
    num_stars = int(input())
  