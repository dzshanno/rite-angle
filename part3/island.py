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
            point2 = circlepoint(m,base,(math.pi*2)/(a+1))
            ax.plot([m[0],point[0]],[m[1],point[1]],[m[2],point[2]],c='b')

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


#list of start/end points - !!remember to worry about the mountains on the beach!!
def landing_zones():
    lz = []
    for x in range(29):
        for y in range (29):
            hyp = x**2 + y**2
            if (hyp < 28**2) and (hyp >= 26.6 **2):
                lz.append([x,y,0])
    return lz
                

                
    
    
# how far apart are 2 mountains
def separation(mountainA,mountainB):
    distance = math.sqrt((mountainB[0]-mountainA[0])**2 + ((mountainB[1]-mountainA[1])**2))
    return distance

#does an allowed path exist between two mountains
def path_exists(mountainA,mountainB):
    rise = mountainB[2]-mountainA[2]
    tread = separation([mountainA[0],mountainA[1]],[mountainB[0],mountainB[1]])
    if tread == 0:
        return False
    path_gradient = rise / tread
    if abs(path_gradient) > tanalpha:
        return False
    else:
        return True
    


peaks = mountains()
lzs = landing_zones()
print(lzs)
plot_island()









