#bottom-up approach

V = 15
n = 3
coin = [0,7,8,9]
M = [[0 for i in range(V+1)] for i in range(n+1)]

v = 0  
while v <= V:
	M[0][v] = float('inf')
	v += 1
	
i = 1  
while i <= n:
	M[i][0] = 0
	i += 1
	
v = 1  
while v <= V:
	i = 1  
	while i <= n:
		if coin[i] > v:
			M[i][v] = M[i-1][v]
		else:
			M[i][v] = min(M[i-1][v], 1+M[i][v-coin[i]])
		i += 1
	v += 1
		 
#print   
print('min # coins to sum up',V,':',M[n][V])

print('M stored values, \nrows i from 0 to',n,'\ncolumns v from 0 to',V)
i = 0  
while i <= n:
	print(M[i])
	i += 1
