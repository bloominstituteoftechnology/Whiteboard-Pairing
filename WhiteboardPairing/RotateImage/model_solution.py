"""
Iterative in-place solution using nested loops
"""
def rotate_image(image):
  for row in image:
    row.reverse()
  for i in range(len(image)):
    for j in range(i):
      image[i][j], image[j][i] = image[j][i], image[i][j]
  return image


# Some print tests
print(rotate_image([
  [1, 2],
  [3, 4]
]))  # should print [ [ 2, 4 ], [ 1, 3 ] ]

print(rotate_image([
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]))  # should print [ [ 9, 0, 1, 2, 3 ],
     #                [ 9, 0, 1, 2, 3 ],
     #                [ 5, 6, 7, 8, 9 ],
     #                [ 1, 2, 3, 4, 5 ],
     #                [ 1, 2, 3, 4, 5 ] ]