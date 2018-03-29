m = int(input('Input Number Of Rows For 1st Matrix: '))
n = int(input('Input Number Of Columns For 1st Matrix: '))

matrix= [[0 for j in range(n)] for i in range(m)]

for i in range(0,m):
	for j in range(0,n):
		print('input for row', i+1, 'input for column', j+1)
		matrix[i][j] = int(input())

print('1st Matrix')
print matrix

o = int(input('Input Number Of Rows For 2nd Matrix: '))
p = int(input('Input Number Of Columns For 2nd Matrix: '))

matrix2 = [[0 for j in range(p)] for i in range(o)]

for i in range(0,o):
	for j in range(0,p):
		print('input for row', i+1, 'input for column', j+1)
		matrix2[i][j] = int(input())

print('2nd Matrix')
print matrix2

if o != n:
	print ('cannot multiply matrices')

if o == n:
	result = [[0 for j in range(p)] for i in range(m)]

	for i in range(len(matrix)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix2)):
				result[i][j] += matrix[i][k] * matrix2[k][j]
				
print result

