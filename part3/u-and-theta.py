# u = 2( tan(beta)(1+cos2*theta)+sin(2*theta))
# u = 2tan(B)+2tan(B)cos(2T)+2sin(2T)
# du/dtheta = 4cos(2theta)-4tan(beta)sin(2theta)
# max when du/dtheta = 0
# cos(2theta) = tan(beta)sin(2theta)
# caution loses some values for theta!!
# tan(2theta) = 1/tan(beta)
# tan(2T)*tan(B) = 1
# 2T + B = pi/2
# u = 2 tan(B)+2tab(B)sin(B)+2cos(B)
#
# u = 2[sinB/cosB + sin2(B)/cosB + cos2B/cosB]
# u= 2/cosB*[sinB+1]
#
# uu = 4ud
# Bu = - Bd
# cos Bu = Cos Bd
# Sin Bu = - Sin Bd
#  
# uu = 2/cosBu*[sinBu +1]
# ud = 2/cosBd*[sinBd +1] = 2/cosBu*[1-SinBu]
#
# 2/cosBu*[sinBu+1] = 8/cosBu*[1-sinBu]
#with CosBu != 0
# SinBu = 3/5
# Bu = alpha = arcsin(3/5)

# beta = - 0.6435 arcsin(-6/10)
# u = 4 and u= 1 
# theta = -0.4636 and 
import math

beta = math.asin(6/10)

print (beta)
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
