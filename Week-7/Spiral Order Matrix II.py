""" Problem 6.2 Spiral Order Matrix II
Problem Description Given a matrix of m * n elements (m rows, n columns), 
return allelements of the matrix in spiral order.Example: 
Given the following matrix: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] 
You should return[1, 2, 3, 6, 9, 8, 7, 4, 5]"""
class Solution:
	def spiralTraverse(array):
		result=[]
		startRow,endRow=0,len(array)-1
		startCol,endCol=0,len(array[0])-1
		while startRow<=endRow and startCol<=endCol:
			for col in range(startCol,endCol+1):
				result.append(array[startRow][col])
			for row in range(startRow+1,endRow+1):
				result.append(array[row][endCol])
			for col in reversed(range(startCol,endCol)):
				if startRow==endRow:
					break
				result.append(array[endRow][col])
			for row in reversed(range(startRow+1,endRow)):
				if startCol==endCol:
					break
				result.append(array[row][startCol])
			startRow+=1
			endRow-=1
			startCol+=1
			endCol-=1
    	return result
if __name__ == '__main__':
    array=[ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
    res=spiralTraverse(array)
    print(res)


