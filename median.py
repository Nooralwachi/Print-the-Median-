import os.path
def median(filename):
	total=0
	with open(filename, 'r') as f:
		for line in f:
			total +=1
		f.seek(0)
		for line in range(total//2):
			tmp= f.readline()
		if total %2==0 :
			print(tmp, end='')
		print(f.readline(), end='')

median('input.txt')