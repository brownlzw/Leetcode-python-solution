class Solution(object):
  def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if not matrix or not matrix[0]:
      return
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
      for j in range(i, n):  # i or i+1 both work
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
