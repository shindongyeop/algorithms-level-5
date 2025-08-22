def solution(places):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    two_space_moves = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    result = []
    # Change element of place to list
    
    for place in places:
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    for dx, dy in directions:
                        if 0 < r + dx < 5 and 0< c + dy <5 and place[r + dx][c + dy] == 'P':
                            result.append(0)
                    
                for dx, dy in diagonals:
                    if 0 < r + dx <5 and 0 < c + dy <5 and place[r + dx][c + dy] == 'P':
                        if place[r + dx][c] == '0' or place[r][c + dy] == '0':
                            result.append(0)
                
                for dx, dy in two_space_moves:
                    if 0< r + dx <5 and 0 < c + dy <5 and place[r + dx][c + dy] == 'P':
                        if place[r + dx // 2][c + dy // 2] == '0':
                            result.append(0)
        result.append(1)
        
    return result




print(solution([["P000P", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))  # result [1,0,1,1,1]