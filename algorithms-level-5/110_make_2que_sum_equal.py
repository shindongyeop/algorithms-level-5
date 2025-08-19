def solution(queue1, queue2):
    # Make copies so original input lists aren't modified
    q1 = queue1[:]
    q2 = queue2[:]
   
    # Calculate the initial sums of each queue
    sum1 = sum(q1)
    sum2 = sum(q2)
   
    # The target sum each queue should have for balance
    target = (sum1 + sum2) // 2
    
    # Operation counter
    count = 0
    
    # Pointers for the front of each queue
    i, j = 0, 0

    # Store original lengths — important so the stop condition isn't affected by appending
    n1 = len(q1)
    n2 = len(q2)
    
    # The loop will run at most (n1 + n2) * 3 times, a safe upper bound for this problem
    # Also ensures we don't run past the available elements in either queue
    while count < (n1 + n2) * 3 and i < len(q1) and j < len(q2):
        # If sums are balanced, return the operation count
        if sum1 == target:
            return count
        
        # If queue1's sum is too large, move from q1 to q2
        elif sum1 > target:
            sum1 -= q1[i]         # Decrease q1's sum
            sum2 += q1[i]         # Increase q2's sum
            q2.append(q1[i])      # Append element to q2's end
            i += 1                # Move q1's pointer forward
        
        # Otherwise, move from q2 to q1
        else:
            sum2 -= q2[j]         # Decrease q2's sum
            sum1 += q2[j]         # Increase q1's sum
            q1.append(q2[j])      # Append element to q1's end
            j += 1                # Move q2's pointer forward
           
        # Count each move
        count += 1

    # If we exit the loop without balancing, return -1
    return -1

print(solution([3,2,7,2], [4,6,5,1])) # result 2
print(solution([1,2,1,2], [1,10,1,2])) # result 7
print(solution([1,1], [1,5])) # result -1