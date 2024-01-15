# for 4 bits

class Solution:
    def reverseBits(self, n: int, bit_size: int) -> int:
        reversed_bits = 0
        for bit_index in range(bit_size):
            if n >> bit_index & 1:
                reversed_bits |= 1 << (bit_size - 1) - bit_index
        return reversed_bits

binary_string = "1100"
binary_integer = int(binary_string, 2)
used_solution = Solution()
reversed_bits = used_solution.reverseBits(binary_integer, 4)
print(reversed_bits)
