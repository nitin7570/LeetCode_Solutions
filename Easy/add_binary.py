'''
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

'''

class Solution:
    def addBinary(self, a, b):
        return bin(int(a, 2)+int(b, 2)).replace("0b","")
        
    
if __name__ == '__main__':
    a = input()
    b = input()
    solution = Solution()
    print(solution.addBinary(a, b))