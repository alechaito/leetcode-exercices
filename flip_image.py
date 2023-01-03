
# https://leetcode.com/problems/flipping-an-image/description/
image = [[1,1,0],[1,0,1],[0,0,0]]

for row in image:
    for x in range((len(row)+1)//2):
        row[x], row[~x] = row[~x] ^ 1, row[x] ^ 1
    
print(image)

# trick: use invertion bit op and xor op