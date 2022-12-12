# mountains satisfy the euation x**2 + y**2 + z**2 = 734 where x,y,z are all integers
# also x**2 + y**2 is less than 28**2
# height of the mountain = z*0.1875
import math
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from py2opt.routefinder import RouteFinder



#setup variables from question
beta = math.asin(6/10)
thetaup = 0.5*((math.pi/2)-beta)
thetadown = 0.5*((math.pi/2)+beta)


#speeds in km/s

#uu = 0.001*2*(math.tan(beta)*(1+math.cos(2*thetaup))+math.sin(2*thetaup))
#ud = 0.001*2*math.tan(-beta)+2*math.tan(-beta)*math.cos(2*thetadown)+2*math.sin(2*thetadown)
#uf = 0.001*2

uu=0.001
ud=0.004
uf=0.002

tanalpha = math.tan(beta)
            
        
def plot_island():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # plot the peaks
    for m in peaks:
        ax.scatter(m[0], m[1], m[2], c='r', marker='o')
        #plot the mountain base
        steps = 18
        
        for a in range(steps):
            base = m[2]/tanalpha
            point = circlepoint(m,base,a*(math.pi*2)/steps)
            point2 = circlepoint(m,base,(a+1)*(math.pi*2)/steps)
            
            ax.plot([point[0],point2[0]],[point[1],point2[1]],[0,0],c='b')
            if a % 4 == 0:
                ax.plot([m[0],point[0]],[m[1],point[1]],[m[2],point[2]],c='r')

    #plot the shore
    for l in lzs:
        ax.scatter(l[0],l[1],l[2], c='g',marker ='o')
    
    # plot the sea    
    for x in range(0,32):
        for y in range(0,32):
            if x**2 + y**2 >= 28**2:
                ax.scatter(x,y,0, c='b', marker = '*')

        
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

#point on a cirle given the centre, radius and angle in radians    
def circlepoint(centre,radius,angle):
    x,y,z = centre
    r = radius
    a = angle
    xpoint = x+ (r*math.sin(a))
    ypoint = y+ (r*math.cos(a))
    zpoint = z
    point = [xpoint,ypoint,0]
    return point
    


#create list of mountains
def mountains():
    peaks = []
    for x in range(28):
      for y in range(28):
         for z in range(28):
                if x**2 + y**2 < 28**2:
                    if x**2 + y**2 + z**2 == 734:
                        peaks.append([x,y,0.1875*z])            
    return peaks
def isInside(circle_x, circle_y, rad, x, y):
     
    # Compare radius of circle
    # with distance of its center
    # from given point
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True;
    else:
        return False;

#list of start/end points - !!remember to worry about the mountains on the beach!!
def landing_zones():
    lz = []
    for x in range(29):
        for y in range (29):
            flat = True
            hyp = x**2 + y**2
            for m in peaks:
                #check to see if the lading zone is flat
                if isInside(m[0],m[1],m[2]/(tanalpha),x,y):
                    flat = False   
            if (hyp < 28**2) and (hyp >= 26.6 **2) and flat == True:
                lz.append([x,y,0])
    return lz


# having looked at all the possible landing zones, the list below is those that dont cross with a mountain
flat_landingzones = [
    [0, 27, 0], [5, 27, 0],  [6, 27, 0],  [7, 27, 0], 
    [8, 26, 0], [9, 26, 0],  [10, 26, 0], [11, 25, 0], 
    [12, 25, 0],[17, 22, 0], [18, 21, 0], [21, 18, 0],  
    [22, 17, 0],[25, 11, 0], [25, 12, 0], [26, 8, 0], 
    [26, 9, 0], [26, 10, 0], [27, 0, 0],  [27, 5, 0], 
    [27, 6, 0], [27, 7, 0]
]

peaks = mountains()
#lzs = landing_zones()




mountainous_landing_zones= [
    [1, 27, 0], [2, 27, 0], [3, 27, 0], [4, 27, 0], [6, 26, 0],[7, 26, 0],[10, 25, 0],[12, 24, 0],
    [13, 24, 0],[14, 24, 0], [14, 23, 0], [15, 22, 0], [15, 23, 0],[16, 22, 0],[17, 21, 0],[18, 20, 0],[19, 19, 0],[19, 20, 0],
    
    [27, 1, 0], [27, 2, 0], [27, 3, 0], [27, 4, 0],[26, 6, 0], [26, 7, 0], [25, 10, 0],[24, 12, 0],
    [24, 13, 0],[24, 14, 0], [23, 14, 0],[22, 15, 0],[23, 15, 0],  [22, 16, 0], [21, 17, 0],[20, 18, 0], [20, 19, 0]
]










