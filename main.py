def preview(a):
	print("=================================================================================")
	print("\t", end="")
	for k in range(0, n):
		print(" ────── ", end="")
	for ii in range(0, n):
		print()
		for j in range(0, n + 2):
			if (j == a[ii]):
				print(" ▓▓▓▓▓", end="")
			else:
				print("\t█", end="")
		print()
		for j in range(0, n + 2):
			if (j == a[ii]):
				print(" ▓▓▓▓▓", end="")
			else:
				print("\t█", end="")
		print()
		print("\t", end="")
		for k in range(0, n):
			print(" ────── ", end="")

	print("\n=================================================================================")

n=int(input("n :"))
answer=[0]*n
Row=0
while(Row<n and Row>=0):
    if(answer[Row]<n):
        answer[Row]=answer[Row]+1
        for k in range(0,Row):
            if(answer[k]==answer[Row] or abs(Row-k)==abs(answer[Row]-answer[k])):
                Row=Row+20
                break
        if(Row>20):
            Row=Row-21
        elif(Row==n-1):
            preview(answer)
            input()
            Row=(n-2)
        else:
            answer[Row+1]=0
    else:
        Row=Row-2
    Row=Row+1
