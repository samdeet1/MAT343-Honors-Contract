from scipy.linalg import eig
from scipy.linalg import solve

M = [
[0,	0,	1,	6,	6,	4,	0,	4,	5,	6,	0,	0,	4,	6,	6,	4,	3,	6,	4,	0],
[6,	0,	1,	1,	4,	3,	4,	6,	3,	3,	3,	0,	0,	4,	3,	3,	3,	4,	0,	4],
[4,	4,	0,	2,	0,	6,	4,	4,	0,	1,	3,	0,	0,	0,	3,	0,	0,	2,	0,	6],
[0,	4,	2,	0,	1,	1,	1,	2,	6,	0,	4,	3,	0,	6,	1,	3,	3,	1,	2,	1],
[0,	1,	6,	4,	0,	6,	3,	6,	4,	3,	3,	3,	2,	6,	6,	2,	4,	1,	6,	1],
[1,	3,	0,	4,	0,	0,	1,	4,	3,	1,	0,	0,	4,	3,	6,	3,	1,	6,	1,	0],
[6,	1,	1,	4,	3,	4,	0,	3,	3,	4,	4,	0,	1,	0,	3,	3,	4,	6,	3,	6],
[1,	0,	2,	1,	0,	1,	3,	0,	0,	3,	4,	0,	1,	1,	4,	1,	1,	4,	1,	0],
[1,	3,	6,	0,	1,	3,	3,	6,	0,	3,	1,	4,	1,	6,	6,	6,	3,	6,	0,	0],
[3,	3,	4,	6,	3,	4,	1,	3,	3,	0,	3,	3,	4,	3,	6,	4,	3,	6,	0,	4],
[6,	3,	3,	1,	3,	6,	1,	1,	4,	3,	0,	1,	4,	2,	6,	3,	6,	4,	6,	6],
[6,	6,	6,	3,	3,	6,	6,	6,	1,	3,	4,	0,	1,	6,	6,	6,	3,	4,	4,	6],
[1,	6,	6,	6,	2,	1,	4,	4,	4,	1,	1,	4,	0,	6,	3,	6,	3,	4,	6,	6],
[0,	1,	6,	0,	0,	3,	6,	4,	0,	3,	2,	0,	0,	0,	3,	3,	2,	4,	6,	2],
[0,	3,	3,	4,	0,	0,	3,	1,	0,	0,	0,	0,	3,	3,	0,	0,	0,	3,	0,	0],
[1,	3,	6,	3,	2,	3,	3,	4,	0,	1,	3,	0,	0,	3,	6,	0,	0,	3,	1,	1],
[3,	3,	6,	3,	1,	4,	1,	4,	3,	3,	0,	3,	3,	2,	6,	6,	0,	6,  1,	4],
[0,	1,	2,	4,	4,	0,	0,	1,	0,	0,	1,	1,	1,	1,	3,	3,	0,	0,	0,	4],
[1,	6,	6,	2,	0,	4,	3,	4,	6,	6,	0,	1,	0,	0,	6,	4,	4,	6,	0,	6],
[6,	1,	0,	4,	4,	3,	0,	3,	6,	1,	0,	0,	0,	2,	3,	4,	1,	1,	0,	0]
]

x = eig(M)
print(x)

C = [
[40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40,	-20],
[-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	-20,	 40]
]

b = [4.666666667, 2.666666667, -2, 0.3333333333, 7.666666667, -0.6666666667, 4.333333333, -4.333333333, 3.333333333, 6, 8,7.333333333, 10.33333333, 5.333333333, -9.666666667, -1.333333333, 5.333333333, -5.666666667, 6.333333333, 0]

y = solve(C,b)
print(y)




       
    
    


