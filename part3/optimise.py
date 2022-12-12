from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

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
            if (hyp <= 28**2) and (hyp > 27**2):
                lz.append([x,y,0])
    return lz

# how far apart are 2 mountains
def separation(PointA,PointB):
    distance = math.sqrt((PointB[0]-PointA[0])**2 + ((PointB[1]-PointA[1])**2))
    return distance

#does an allowed path exist between two mountains
def path_exists(pointA,pointB,allowed_gradient):
    rise = pointB[2]-pointA[2]
    tread = separation([pointA[0],pointA[1]],[pointB[0],pointB[1]])
    if tread == 0:
        return False
    path_gradient = rise / tread
    if abs(path_gradient) > allowed_gradient:
        return False
    else:
        return True

def find_times(points):
    times = []
    for p1 in points: 
        times_row = []
        for p2 in points:
            times_row.append('X')
        times.append(times_row)

    for m in range(len(points)):
        for n in range(len(points)):
            if  m != n:
                if path_exists(points[m],points[n],tanalpha):
                    times[m][n] = path_time(points[m],points[n])
                else:
                    times[m][n] = 100_000_000_000
            else:
                times[m][n] = 0
    return times

def plot_route(route):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  
    x,y,z = zip(*route)
    ax.plot(x,y,z,c='b')
    for i in range(len(x)):
        ax.text(x[i],y[i],z[i],'%s:(%s,%s)' % (str(i),str(x[i]),str(y[i])))
    
    ax.view_init(elev=10., azim=45)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

def plot_points(points):
    
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for p in points:
        ax.scatter(p[0], p[1], p[2], c='r', marker='o')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


def path_time(m1,m2):
    dt = separation(m1,m2)
    z1 = m1[2]
    z2 = m2[2]
    
    # is there a path?
    if not path_exists(m1,m2,tanalpha):
        return 1_000_000_000
    # as there is a path
    #path time is distance down * ud + distance along * uf + distance up * uu
    #find intecept point of up/down and sealevel
    # yd = -Ax+y1
    # yu = Ax+y2-Ax2
    # yf = 0
    #
    #intercept yd with yu
    intercept_ud = ((tanalpha*dt)-z2+z1)/(2*tanalpha)
    intercept_uf = ((tanalpha*dt)-z2)/(tanalpha)
    intercept_df = (z1/tanalpha)
    
    d_down_to_flat = intercept_df
    d_along_flat = intercept_uf - intercept_df
    d_up_after_flat = dt - intercept_uf
    d_down_to_up = intercept_ud
    d_up_to_top = dt - intercept_ud
    
    # if the slope gets to sea level
    if intercept_df < intercept_ud:        
        total_time = (d_down_to_flat /ud) + (d_along_flat / uf) + (d_up_after_flat / uu)
    else:
        total_time = (d_down_to_up / ud) + (d_up_to_top / uu)
    return total_time   

def route_time(route):
    elapsed_time = 0
    for r in range(len(route)-1):
        start_index = allpoints.index(route[r])
        end_index = allpoints.index(route[r+1])
        elapsed_time = elapsed_time + alltimes[start_index][end_index]
    return elapsed_time
        


#setup

uu=0.001
ud=0.004
uf=0.002

beta = math.asin(6/10)
thetaup = 0.5*((math.pi/2)-beta)
thetadown = 0.5*((math.pi/2)+beta)

tanalpha = math.tan(beta)

allpoints = mountains() + landing_zones()
alltimes = find_times(allpoints)



answer = [94366.74, [[26, 8, 0], [26, 7, 0.5625], [25, 10, 0.5625], [23, 14, 0.5625], [23, 13, 1.125], [22, 13, 1.6875], [22, 15, 0.9375], [21, 17, 0.375], [19, 18, 1.3125], [18, 17, 2.0625], [17, 18, 2.0625], [18, 19, 1.3125], [17, 21, 0.375], [15, 22, 0.9375], [14, 23, 0.5625], [13, 23, 1.125], [13, 22, 1.6875], [10, 25, 0.5625], [7, 26, 0.5625], [2, 27, 0.1875], [1, 27, 0.375], [3, 26, 1.3125], [3, 25, 1.875], [3, 23, 2.625], [2, 21, 3.1875], [5, 22, 2.8125], [6, 23, 2.4375], [9, 22, 2.4375], [7, 19, 3.375], [7, 18, 3.5625], [11, 18, 3.1875], [11, 17, 3.375], [9, 13, 4.125], [6, 13, 4.3125], [5, 15, 4.125], [2, 17, 3.9375], [3, 14, 4.3125], [3, 10, 4.6875], [3, 7, 4.875], [1, 2, 5.0625], [2, 1, 5.0625], [7, 3, 4.875], [10, 3, 4.6875], [14, 3, 4.3125], [17, 2, 3.9375], [15, 5, 4.125], [13, 6, 4.3125], [13, 9, 4.125], [17, 11, 3.375], [18, 11, 3.1875], [18, 7, 3.5625], [19, 7, 3.375], [22, 9, 2.4375], [23, 6, 2.4375], [22, 5, 2.8125], [21, 2, 3.1875], [23, 3, 2.625], [25, 3, 1.875], [26, 3, 1.3125], [27, 1, 0.375], [27, 2, 0.1875], [27, 1, 0]]]
route = answer[1]

time_taken = route_time(route)


answer = [time_taken,route]
#print out results
print(round(time_taken,2))
for r in route:
    print(r[0],',',r[1])

plot_route(route)