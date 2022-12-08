# area from altitudes

import math
alt1 = 9     
alt2 = 10
alt3 = 11

inva1 = 1/alt1
inva2 = 1/alt2
inva3 = 1/alt3

area = 1/math.sqrt((inva1+inva2+inva3)*(inva2+inva3-inva1)*(inva1+inva3-inva2)*(inva1+inva2-inva3))

print(area)

#answer = 58.2