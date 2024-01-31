class Solution:
    def binary(self, n: int) -> int: 
        number_of_1_bits = 0
        
        for bit_index in range(31, -1, -1):
            
            bit_value = (n >> bit_index) & 1
            print(bit_value, end=" ")
            
        return number_of_1_bits

# defined binary valued used 0b
n = 0b00000000000000000000000000011100
checker = Solution()

checker.binary(n)
