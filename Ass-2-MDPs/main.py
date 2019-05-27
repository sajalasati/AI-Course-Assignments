n,m = raw_input().split()
n,m = int(n), int(m)
utility=[[0 for i in range(m)] for j in range(n)]
utility_t=[[0 for i in range(m)] for j in range(n)] #acts as U' here
rewards=[[0 for i in range(m)] for j in range(n)]
for i in range(n):
	rewards[i] = raw_input().split()
for i in range(n):
	for j in range(m):
		rewards[i][j] = float(rewards[i][j])
		utility_t[i][j] = rewards[i][j];
e,w = raw_input().split();
e,w = int(e), int(w)

# Notation:
# end state = 1, wall = -1; else = 0 (for other cells)
type_of_cell = [[0 for x in range(m)] for y in range(n)]
for i in range(e):
	a,b = raw_input().split()
	a,b = int(a), int(b)
	# utility_t[a][b] = rewards[a][b] # never changes again
	type_of_cell[a][b] = 1
for i in range(w):
	a,b = raw_input().split()
	a,b = int(a), int(b)
	# utility_t[a][b] = rewards[a][b] # never changes again
	type_of_cell[a][b] = -1
print type_of_cell
s1,s2 = raw_input().split()
s1,s2 = int(s1), int(s2)
unit_step_reward = float(raw_input())
lamda = 0.99
epsilon = 0.01
count = 0
while(True):
	count += 1
	delta = 0
	for i in range(n):
		for j in range(m):
			utility[i][j] = utility_t[i][j]
	directions = [['' for ii in range(4)] for jj in range(4)]
	for i in range(n):
		for j in range(m):
			u,l,r,d = 0,0,0,0 #for up,down,left,right
			# because of utility of wall,end state remains as it is
			if type_of_cell[i][j]==1:
				directions[i][j] = '*'
				continue
			if type_of_cell[i][j]==-1:
				directions[i][j] = '|'
				continue
			if i==0 or type_of_cell[i-1][j]==-1:
				u = utility[i][j]
			else:
				u = utility[i-1][j]
			if i==n-1 or type_of_cell[i+1][j]==-1:
				d = utility[i][j]
			else:
				d = utility[i+1][j]
			if j==0 or type_of_cell[i][j-1]==-1:
				l = utility[i][j]
			else:
				l = utility[i][j-1]
			if j==m-1 or type_of_cell[i][j+1]==-1:
				r = utility[i][j]
			else:
				r = utility[i][j+1]

			# values corresponding to each action
			up = u*0.8 + r*0.1 + l*0.1
			down = d*0.8 + r*0.1 + l*0.1
			left = l*0.8 + 0.1*u + 0.1*d
			right = r*0.8 + 0.1*u + 0.1*d
			maxi = max(up,down,left,right)
			utility_t[i][j] = unit_step_reward + rewards[i][j] + lamda*maxi
			if abs(utility[i][j] - utility_t[i][j]) > delta:
				delta = abs(utility[i][j] - utility_t[i][j])
			if maxi == up:
				directions[i][j] = 'U'
			if maxi == down:
				directions[i][j] = 'D'
			if maxi == left:
				directions[i][j] = 'L'
			if maxi == right:
				directions[i][j] = 'R'
	# print "for iteration",count, "delta",delta
	# for i in range(n):
	# 	for j in range(m):
	# 		print utility_t[i][j],
	# 	print
	if delta < (epsilon*(1-lamda)/lamda):
		for i in range(n):
			for j in range(m):
				print "%.3f" %float(utility_t[i][j]),
			print
		for i in range(4):
			for j in range(4):
				print directions[i][j],
			print
		break