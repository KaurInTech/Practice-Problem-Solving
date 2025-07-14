class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[temperatures[0],0]]
        i = 1
        length = len(temperatures)
        res = [0] * length
        while i < length:
            while stack and temperatures[i] > stack[-1][0]:
                element = stack.pop()
                index = i - element[1]
                res[element[1]] = index
            stack.append([temperatures[i],i])
            i+=1
        return res
            
        