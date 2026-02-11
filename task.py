#матрица экспертов (согласия между экспертами)

def spearman(x, y):
    n = len(x)
    sum = 0
    for i in range(n):
        d = x[i] - y[i]
        sum += d**2
    return 1 - (6*sum)/(n**3 - n)

def get_spearman_matrix(matrix):
    n_object = len(matrix)
    n_experts = len(matrix[0])

    experts = [[matrix[i][j] for i in range(n_object)] for j in range(n_experts)]
    result = [[0 for _ in range(n_experts)] for _ in range(n_experts)]

    for i in range(n_experts):
        for j in range(n_experts):
            result[i][j] = spearman(experts[i], experts[j])

    return result

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    matrix = [
        [3, 3, 1, 3],
        [1, 1, 4, 4],
        [2, 5, 5, 5],
        [5, 2, 2, 1],
        [4, 4, 3, 2]
        ] #из практической работы 1, задание 1
    print_matrix(get_spearman_matrix(matrix))