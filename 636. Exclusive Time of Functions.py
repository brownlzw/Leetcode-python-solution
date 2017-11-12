class Solution(object):
  def exclusiveTime(self, n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """
    stack = []
    # total = 0
    time = [0] * n
    for log in logs:
      log_id, typ, t = log.split(':')
      log_id, t = int(log_id), int(t)
      if typ == 'start':
        stack.append((log_id, t))
      else:
        log_id, s_t = stack.pop()
        duration = t - s_t + 1
        time[log_id] += duration
        if stack:
          time[stack[-1][0]] -= duration
    return time

