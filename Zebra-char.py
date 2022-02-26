
s = "zebra"
          
class Solution:
    def zebraCase(self, s):
      
      for char in s:
          x = ord(char) - ord('a')
          print(x)

ans = Solution()
print(ans.zebraCase(s))