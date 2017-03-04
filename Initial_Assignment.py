import operator

#Multiplies 2 matrices
def multiply(M,N):
	a = M[0]*N[0] + M[1]*N[2]
	b = M[0]*N[1] + M[1]*N[3]
	c = M[2]*N[0] + M[3]*N[2]
	d = M[2]*N[1] + M[3]*N[3]
	M[0] = a
	M[1] = b
	M[2] = c
	M[3] = d
	#print M

#Get power of a matrix
def get_power(rem_mat, number):
	n = number
	if (n == 0 or n == 1):
		return
	const_mat = [1,1,1,0]
	get_power(rem_mat,n//2)
	multiply(rem_mat, rem_mat)
	if (n%2 != 0):
		multiply(rem_mat, const_mat)

#Compute the new matrix
def compute(number,prev_matrix):
	rem_mat = [1,1,1,0]
	get_power(rem_mat, number)
	if number == 0:
		return prev_matrix
	multiply(rem_mat,prev_matrix)
	return rem_mat




if __name__ == "__main__":
	t = int(input("No. of test cases: "))
	n = dict()
	print "Enter ",t,"numbers " 
	i = 0
	while i < t:
		n[i] = int(input())
		i = i + 1

	sorted_n = sorted(n.items(), key=operator.itemgetter(1))

	output = dict()
	prev_matrix = [2,1,1,1]
	prev_num = 1
	power_ = (10 ** 9) + 7
	i = 0
	while i < len(sorted_n):
		now_num = sorted_n[i][1]
		new_matrix = compute(now_num - prev_num, prev_matrix)
		output[sorted_n[i][0]] = new_matrix[0] % power_
		prev_num = now_num
		prev_matrix = new_matrix
		i = i + 1

	i = 0	
	while i < len(output):
		print output[i]
		i = i + 1

		

