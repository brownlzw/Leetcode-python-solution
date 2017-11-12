class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
      return False
    col = len(matrix[0]) - 1
    for row in matrix:
      while row[col] > target and col > 0:
        col -= 1
      if row[col] == target:
        return True
    return False

