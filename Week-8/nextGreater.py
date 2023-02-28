from collections import deque

def nextGreaterElement(a):
    s = deque()
    for i in range(len(a)):
        # If the stack is empty, push the current element.
        if len(s) == 0:
            s.append(a[i])
            continue
        while s and s[-1] < a[i]:
            print(str(s[-1]), "-->", str(a[i]))
            s.pop()

        s.append(a[i])
    """
    pop all the elements from the stack and print -1 as the next greater element for them.
    """
    while len(s) > 0:
        print(str(s[-1]), "--> -1")
        s.pop()


if __name__ == "__main__":
    a = [11, 13, 21, 3]
    print("The list of the next greater element is :")
    nextGreaterElement(a)
        ### Time Complexity: O(N) and Space: O(N)