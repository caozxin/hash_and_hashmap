
class Solution:
    def isHappy(self, n: int) -> bool:

        def refine_num (num: int, visited: list, digit_squared:list) -> bool:
            if num == 1:
                return True

            str_num = str(num)
            #base exit:
            
            curr_sum = 0
            for each_dgt in str_num:
                each_dgt = int(each_dgt)
                curr_sum += digit_squared[each_dgt]
            print("curr_sum", curr_sum)
            if curr_sum == 1:
                print("true")
                return True 
            if curr_sum in visited:
                return False
            visited.append(curr_sum)
            refine_num(curr_sum, visited, digit_squared)
            
            print(curr_sum, "here")
        
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        digit_squared = {}
        for each_dgt in digits:
            digit_squared[each_dgt] = each_dgt ** 2


        visited = []
        return refine_num(n, visited, digit_squared)
