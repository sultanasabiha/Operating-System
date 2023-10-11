
def FCFS(arr, head, n):
	seek_count = 0
	distance=0
	cur_track = 0
	print("Tracks Traversed\tDifference between Tracks")
	for i in range(n):
		cur_track = arr[i]
		distance = abs(cur_track - head)
		print("\t",cur_track,"\t\t\t",distance)
		seek_count += distance
		head = cur_track
		
	print("Seek Sequence is:",arr)
	print("Total number of seek operations = ",seek_count)


if __name__ == '__main__':

	head=int(input("Enter Head Position:"))
	n=int(input("Enter no. of tracks:"))
	print("Enter Track Positions:")
	arr=[]
	for i in range(n):
		arr.append(int(input()))

	FCFS(arr, head, n)

