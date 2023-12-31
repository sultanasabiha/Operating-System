
def SCAN(arr, head, direction):
 
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
    # Appending end values
    # which has to be visited
    # before reversing the direction
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)
 
    for i in range(n):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    # Sorting left and right vectors
    left.sort()
    right.sort()
 
    # Run the while loop two times.
    # one by one scanning right
    # and left of the head
    run = 2
    print("Tracks Traversed\tDifference between Tracks")

    while (run != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
 
                # Appending current track to
                # seek sequence
                seek_sequence.append(cur_track)
 
                # Calculate absolute distance
                distance = abs(cur_track - head)
                print("\t",cur_track,"\t\t\t",distance) 
                # Increase the total count
                seek_count += distance
 
                # Accessed track is now the new head
                head = cur_track
             
            direction = "right"
     
        elif (direction == "right"):
            for i in range(len(right)):
                cur_track = right[i]
                 
                # Appending current track to seek
                # sequence
                seek_sequence.append(cur_track)
 
                # Calculate absolute distance
                distance = abs(cur_track - head)
                print("\t",cur_track,"\t\t\t",distance) 
                # Increase the total count
                seek_count += distance
 
                # Accessed track is now new head
                head = cur_track
             
            direction = "left"
         
        run -= 1
    print("Seek Sequence is:",seek_sequence)
    print("Total number of seek operations =",
          seek_count)

 

 
# Driver code
disk_size=int(input("Enter Disk Size:"))
head=int(input("Enter Head Position:"))
n=int(input("Enter no. of tracks:"))
print("Enter Track Positions:")
arr=[]
for i in range(n):
	arr.append(int(input()))
direction=input("Enter Direction:")
SCAN(arr, head, direction)

