"""Problem 6.3 Sort array of 0's,1's and 2's
Given an array of size N containing only 0s, 1s, and 2s; 
sort the array in ascendingorder. 
Example 1:Input:N = 5arr[]= {0 2 1 2 0}
Output:0 0 1 2 2
Explanation: 0's 1's and 2's are segregated into ascending order.
Example 2:Input:N = 3arr[] = {0 1 0}
Output:0 0 1Explanation: 0s 1s and 2s are segregated into ascending order.
Time Complexity: O(N)Expected Auxiliary Space: O(1)Constraints: 1 <= N <= 10^6 0 <= A[i] <= 2"""
def sortNumbers(A):
    left=current=0
    right = len(A) - 1

    while current < right:
        if A[current] == 0:
            A[current], A[left] = A[left], A[current]
            left = left + 1
            current = current + 1
        elif A[current] == 2:
            A[current], A[right] = A[right], A[current]
            right = right - 1
        else:
            current = current + 1

if __name__ == '__main__':
    A=[2,1,0,1,2,1,0]
    sortNumbers(A)
    print(A)