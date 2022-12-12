# u = 2( tan(beta)(1+cos2*theta)+sin(2*theta))
# u = 2tan(B)+2tan(B)cos(2T)+2sin(2T)
# du/dtheta = 4cos(2theta)-4tan(beta)sin(2theta)
# max when du/dtheta = 0
# cos(2theta) = tan(beta)sin(2theta)
# tan(2theta) = 1/tan(beta)
# tan(2T)*tan(B) = 1
# 2T + B = pi/2
# sin(2T) = cos(B)
# cos(2T) = Sin(B)
# u = 2 tan(B)+2tab(B)sin(B)+2cos(B)
#
# u = 2[sinB/cosB + sin2(B)/cosB + cos2B/cosB]
# assuming cosB != 0
# u= (2*[sinB+1])/cosB
#
# uu = 4ud
# Bu = - Bd
# cos Bu = Cos Bd
# Sin Bu = - Sin Bd
#  
# uu = (2*[sinBu +1])/cosBu
# ud = 2/cosBd*[sinBd +1] = 2/cosBu*[1-SinBu]
#
# 2/cosBu*[sinBu+1] = 8/cosBu*[1-sinBu]
#with CosBu != 0
# SinBu = 3/5
# Bu = alpha = arcsin(3/5)

# alpha =  0.6435 = arcsin(6/10)
# ud = 4 and uu= 1 
 
import math

alpha = math.asin(6/10)
thetaup = 0.5*((math.pi/2)-beta)
thetadown = 0.5*((math.pi/2)+beta)

# when Beta = 0
# uflat === uf = 2sin(2T)
# so max uf is when 2T = pi/2
# Tf = pi/4
# uf = 2

print (thetaup,thetadown)


uup=2*(math.tan(beta)*(1+math.cos(2*thetaup))+math.sin(2*thetaup))
udown=2*math.tan(-beta)+2*math.tan(-beta)*math.cos(2*thetadown)+2*math.sin(2*thetadown)
uflat = 2

print(uup)
print(udown)
print(uflat)
