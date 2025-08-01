def solution(arr):
    n = len(arr)
    def check_same(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    return False
        return True
    
    def compress(x, y, size):
        if check_same(x, y, size):
            if arr[x][y] == 0:
                return (1, 0)
            else:
                return (0, 1)
            
        half = size //2
        top_left = compress(x, y, half)
        top_right = compress(x + half, y, half)
        bottom_left = compress(x, y + half, half)
        bottom_right = compress(x + half, y + half, half)
        
        zeros = top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0]
        ones = top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]
        
        return (zeros, ones)
        
    
    return list(compress(0, 0, n))

        

print(solution([[1, 1, 0, 0], 
                [1, 0, 0, 0], 
                [1, 0, 0, 1], 
                [1, 1, 1, 1]]))

print(solution([[1, 1, 1, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 1, 1, 1, 1], 
                [0, 1, 0, 0, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0, 1, 1], 
                [0, 0, 0, 0, 0, 0, 0, 1], 
                [0, 0, 0, 0, 1, 0, 0, 1], 
                [0, 0, 0, 0, 1, 1, 1, 1]]))