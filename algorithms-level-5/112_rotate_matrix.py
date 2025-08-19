def solution(rows, colunmns, queries):
    matrix = [[0] * colunmns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(colunmns):
            matrix[i][j] = num
            print(f'matrix[{i}][{j}] = {num}')
            num += 1

    result = []
    for query in queries:
        x1, y1, x2, y2 = query
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        
        top_left = matrix[x1][y1]
        min_value = top_left
        
        # Move left column down
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])
        
        # Move bottom row left
        for j in range(y1, y2):
            matrix[x2][j] = matrix[x2][j + 1]
            min_value = min(min_value, matrix[x2][j])
        
        # Move right column up
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])
        
        # Move top row right
        for j in range(y2, y1, -1):
            matrix[x1][j] = matrix[x1][j - 1]
            min_value = min(min_value, matrix[x1][j])
        
        # Place the top-left value at the end of the top row
        matrix[x1][y1 + 1] = top_left
        
        result.append(min_value)

    return result
    
    
    

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # Output: [8,10,25]
print(solution(3, 3, [[1,1,2,2], [1,2,2,3], [2,1,3,2], [2,2,3,3]])) # Output: [1,1,5,3]
#print(solution(100, 97, [[1,1,100,97]]))  # Output: [1]  
    