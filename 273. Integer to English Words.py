class Solution(object):
  def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
      return "Zero"
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]
    words = []
    # 2147483647
    i = 0
    while num != 0:
      mod = num % 1000
      if mod != 0:
        words.append(THOUSANDS[i])
      tens = mod % 100
      if tens < 20:
        words.append(LESS_THAN_20[tens])
      else:
        words.append(LESS_THAN_20[tens % 10])
        words.append(TENS[tens / 10])
      if mod / 100 != 0:
        words.append("Hundred")
        words.append(LESS_THAN_20[mod / 100])
      num /= 1000
      i += 1
    words = [word for word in words if word != ""]
    words.reverse()
    return " ".join(words)