class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return "0"

        result=[]
        while n!=0:
            remainder= n % -2
            n= n//-2

            if remainder<0:
                remainder+=2
                n+=1
            result.append(str(remainder))
        result.reverse()
        return ''.join(result)
        