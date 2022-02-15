from matrix import Matrix

mat1 = Matrix([
        [5, 2],
        [0, 3],
        ])

mat2 = Matrix([
        [7, 3],
        [9, 1],
        ])

print(mat1.determinant())
print("______________________")
print(mat1.trace())
print("______________________")
print(mat1.inverse())
print("______________________")
print(mat2.T())
print("______________________")
print(mat1 + mat2)
print("______________________")
# print(-(mat1))
print("______________________")
# print(mat1 - mat2)
# print(5*mat1)

# print("______________________")
# print(mat1 * mat2)

