a,b=1,2
m=(a+b)/2
while abs((m**3-2))>0.001:
    if m**3>2:
        b=m
        m=(a+b)/2
    else:
        a=m
        m=(a+b)/2
print(m,m**3-2)
