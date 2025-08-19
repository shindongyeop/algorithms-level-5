def solution(n):
    # Step 1: Create an empty triangle with all values set to 0
    triangle = [[0] * (i + 1) for i in range(n)]
    
    # Step 2: Define movement directions: Down, Right, Up-Left
    directions = [(1, 0), (0, 1), (-1, -1)]
    
    # Step 3: Initialize variables
    num = 1  # Number to fill in
    x, y = 0, 0  # Starting position
    direction = 0  # Current direction (start by moving down)
    
    while num <= (n * (n + 1)) // 2:  # Total numbers to fill
        print(f'num = {num}')
        triangle[x][y] = num  # Fill current position
        print(f'x = {x}, y = {y}, triangle[x][y] = {triangle[x][y]}')
        num += 1
        
        # Calculate next position
        nx, ny = x + directions[direction][0], y + directions[direction][1]
        
        # Check if we need to change direction
        if nx < 0 or nx >= n or ny < 0 or ny >= len(triangle[nx]) or triangle[nx][ny] != 0:
            # Safe debug print that won't cause IndexError
            if 0 <= nx < n and 0 <= ny < len(triangle[nx]):
                print(f'nx = {nx}, ny = {ny}, len(triangle[nx]) = {len(triangle[nx])}, triangle[nx][ny] = {triangle[nx][ny]}')
            else:
                print(f'nx = {nx}, ny = {ny} is out of bounds')
            
            direction = (direction + 1) % 3  # Change direction
            print(f'direction = {direction}')
            nx, ny = x + directions[direction][0], y + directions[direction][1]
        
        # Move to the next position
        x, y = nx, ny
        print(f'Next position: x = {x}, y = {y}')
    
    # Step 4: Flatten the triangle into a single list
    result = []
    for row in triangle:
        result.extend(row)  # Add each row's numbers to the result list
    
    return result



print(solution(4)) # result [1,2,9,3,10,8,4,5,6,7]
#print(solution(5)) # result [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
#print(solution(6)) # result [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]