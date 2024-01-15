class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        binary = ""
        carry = 0 
        
        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if a[i] == '1' else 0 
            r += 1 if b[i] == '1' else 0 
            
            binary = ('1' if r % 2 == 1 else '0') + binary
            carry = 0 if r < 2 else 1 
        if carry != 0:
            binary = '1' + binary

        return binary
