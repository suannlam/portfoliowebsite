

class Solution:



    def smallerNumbersThanCurrentTEST(self) -> None: #since printing is not the same as returning
        # 12348 -> 0, 1, 2, 3, 4
        test1 = [1,2,8,4,3] 
        # 0,1,2,3,3
        test2 = [1,8,8,4,3]
        # 0,0,0,0,0
        test3 = [6,6,6,6,6]
        # 0,0,2,3,3
        test4 = [8,2,8,2,3]

        print(Solution().smallerNumbersThanCurrent(test1))
        print(Solution().smallerNumbersThanCurrent(test2))
        print(Solution().smallerNumbersThanCurrent(test3))
        print(Solution().smallerNumbersThanCurrent(test4))
        
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        # sort out the list - set or check if key already, to take duplicates into account => can't do set since duplicates are still valid
        sortedNums = sorted(nums)
        # make a hashmap to store the less ints - check for dupes!!!
        mp = {}
        less = []
        for i, v in enumerate(sortedNums):
            if v not in mp.keys():
                mp[v] = i
        # for loop, access hashmap, get value, add it to list that is to be returned
        for n in nums:
            less.append(mp[n])
       

        # return how many nums is smaller than it [int, int, int]

        return less


    # CAN THERE BE DUPLICATES?
    # are the duplicates counted as valid numbers for them to be <, ie. do they have to be the number of elems, or number of UNIQUE elems less than
        
    
    def evalRPN(self, tokens: list[str]) -> int: 
        stack = []
        validOperators = {
            "+":lambda x, y : x + y,
             "-": lambda x, y : x - y, 
             "*": lambda x, y : x * y, 
             "/": lambda x, y : x / y
        }
        
        for vals in tokens:
            tok = vals

            if vals in validOperators.keys():
                v2 = stack.pop()
                v1 = stack.pop()
                tok = validOperators[vals](v1, v2)

            
            stack.append(int(tok))

        return stack.pop()
    
    def evalRPNTesting(self) -> int: 
        test1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        print(Solution().evalRPN(test1))

if __name__== "__main__":
    sol = Solution()
    # sol.smallerNumbersThanCurrentTEST() => array + hashmap based leet
    sol.evalRPNTesting()

    
    print("adfgadg")

