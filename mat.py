def scalar_multiply(matrix, scalar):
    lst = []
    for element in matrix:
        row = []
        for i in element:
            new_value = i*scalar
            row.append(new_value)
        lst.append(row)
    return lst


# Example usage
matrix_c = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
scalar_value = 3
result_scalar_multiply = scalar_multiply(matrix_c, scalar_value)


with open("new.txt", "w")as file:
    matstr = ""
    for element in result_scalar_multiply:
        rowstr = ""
        for i in element:
            rowstr = rowstr+str(i)+" "
            # 6 12 18
        rowstr = rowstr+"\n"
        matstr = matstr+rowstr
    

    file.write(matstr)
    

mat={
    "size":6,
    (1,2):2,
    (1,3):1,
    (1,2):10
}
my_mat=[]
for i in range(5):
    my_row=[]
    for j in range(5):
        my_row.append(0)
    my_mat.append(my_row)

my_mat[0][2]=2
my_mat[1][1]=1
my_mat[3][0]=1



def create_mat_txt(m):
    # m deyerine gore yeni matrix yaranmalidir
    # yaradilan matrix eyni formada txt faylinin icine yazdirilmalidir
    
    pass

create_mat_txt(mat)
# result : [[0, 0, 2, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# eyni zaman
