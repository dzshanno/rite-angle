import math

def set_sig_fig(answer,sigfig):
    result = round(answer, sigfig - int(math.floor(math.log10(abs(answer)))) - 1)
    return result

OA = 1
AB = 1/math.cos(math.radians(18))
BC = 1/math.cos(math.radians(18))
CD = 1/math.cos(math.radians(36))
DE = 1/math.cos(math.radians(36))
EF = 1/math.cos(math.radians(54))
FG = 1/math.cos(math.radians(54))
GH = 1/math.cos(math.radians(72))
print(OA,AB)


Result = OA + AB + BC + CD + DE + EF + FG +GH

print(Result)
Result_3sf = set_sig_fig(Result,3)
print(Result_3sf)
Answer = int(Result_3sf*0.74)

print(Answer)
# answer = 9
