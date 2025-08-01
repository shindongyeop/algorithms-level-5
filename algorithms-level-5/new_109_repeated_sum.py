def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = None
    
    while right < len(sequence):
        if current_sum == k:
            if best_range is None or (right - left) < (best_range[1] - best_range[0]):
                best_range = (left, right)
            elif (right - left) == (best_range[1] - best_range[0]) and left < best_range[0]:
                best_range = left, right
        if current_sum >= k:
            current_sum -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
                    
    return [best_range[0], best_range[1]] 
                
        
        


print(solution([1, 2, 3, 4, 5], 7))  # Output: [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))  # Output: [6, 6]
print(solution([2, 2, 2, 2, 2], 6))  # Output: [0, 2]