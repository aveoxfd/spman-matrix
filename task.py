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

def method_disagreement(matrix, normalized = True): #disagreement method
    R = get_spearman_matrix(matrix)
    n = len(R)
    if normalized:
        return [[(1 - R[i][j]) / 2 for j in range(n)] for i in range(n)]
    else:
        return [[1 - R[i][j] for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # print column headers
    print("   ", end="")
    for j in range(len(matrix)):
        print(alpha[j], end="   ")
    print()
    # print rows
    for i in range(len(matrix)):
        print(alpha[i], end=" ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

if __name__ == "__main__":
    matrix = [
        [1, 3, 1, 1],
        [2, 2, 3, 3],
        [5, 4, 4, 5],
        [4, 5, 5, 4],
        [3, 1, 2, 2]
        ]
    print_matrix(get_spearman_matrix(matrix))