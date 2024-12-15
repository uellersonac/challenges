# Function to rotate the image anticlockwise
def rotate_image(size, img):
	# Write your code here
	new_img = []
	if img == []:
		return
	for column in range(size-1,-1,-1):
		new_row=[]
		for row in range(size):
			new_row.append(img[row][column]) 
		new_img.append(new_row)
	return new_img

# Call rotate_image and display the result
print(rotate_image(3,[[1, 2, 3],[4, 5, 6],[7, 8, 9]]))