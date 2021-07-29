class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder*10, abs(denominator))
            result.append(str(n))
        print(remainders)
        if remainder in remainders:
            idx = remainders[remainder]
            result.insert(idx, '(')
            result.append(')')
        print(remainders)
        return ''.join(result).rstrip(".")