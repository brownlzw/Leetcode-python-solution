class Solution(object):
  def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    #freq = # of tasks, max = maximum number, (max-1)*(n+1) + 1
    # A B C D IDLE A B C IDLE IDLE A
    # A B C A D IDLE A (MAX-1)*N
    freq = [0 for i in range(26)]
    for task in tasks:
      freq[ord(task) - ord('A')] += 1
    freq.sort()
    max_num = freq.count(freq[-1])
    return max(len(tasks), (freq[-1] - 1) * (n + 1) + max_num)

  """
  public class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] map = new int[26];
        for (char c: tasks)
            map[c - 'A']++;
        Arrays.sort(map);
        int max_val = map[25] - 1, idle_slots = max_val * n;
        for (int i = 24; i >= 0 && map[i] > 0; i--) {
            idle_slots -= Math.min(map[i], max_val);
        }
        return idle_slots > 0 ? idle_slots + tasks.length : tasks.length;
    }
}
  """