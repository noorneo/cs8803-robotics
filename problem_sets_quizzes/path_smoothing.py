# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth)
# and returns a smooth path.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the previous video:
#
# If your function isn't submitting it is possible that the
# runtime is too long. Try sacrificing accuracy for speed.
# -----------


from math import *

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

# ------------------------------------------------
# smooth coordinates
#

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]


    #### ENTER CODE BELOW THIS LINE ###
    error = 1
    while error > tolerance:
        error = 0
        for idx,i in enumerate(newpath):
            #skips the first and last node
            if idx == 0 or idx == len(newpath)-1:
                continue
            
            x = i[0]
            y = i[1]
            
            change_y1 = weight_data * (path[idx][1] - y)            
            change_y2 = weight_smooth * (newpath[idx-1][1] + newpath[idx+1][1] - 2 * y)
            y+= change_y1
            y+= change_y2
            
            change_x1 = weight_data * (path[idx][0] - x)            
            change_x2 = weight_smooth * (newpath[idx-1][0] + newpath[idx+1][0] - 2 * x) 
            x += change_x1
            x += change_x2
              
            error += abs(change_y1+change_y2) + abs(change_x1+change_x2)
            print 'error is %s' %error
            newpath[idx] = [x, y]
    
    return newpath # Leave this line for the grader!

# feel free to leave this and the following lines if you want to print.
newpath = smooth(path)

# thank you - EnTerr - for posting this on our discussion forum
for i in range(len(path)):
    print '['+ ', '.join('%.3f'%x for x in path[i]) +'] -> ['+ ', '.join('%.3f'%x for x in newpath[i]) +']'






