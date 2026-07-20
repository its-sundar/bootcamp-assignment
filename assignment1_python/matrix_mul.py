r1 = int(input("Rows of first matrix: "))
c1 = int(input("Columns of first matrix: "))

A = []
print("Enter first matrix:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Rows of second matrix: "))
c2 = int(input("Columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible.")
else:
    B = []
    print("Enter second matrix:")
    for i in range(r2):
        row = list(map(int, input().split()))
        B.append(row)

    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Product Matrix:")
    for row in result:
        print(row)