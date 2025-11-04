# from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = []
        groupping = {}
        res = []


        for each in strs:
            # curr_cout = Counter(each)
            uni_each = sorted(list(each))
            new_key = "".join(uni_each)
            # print(uni_each, new_key)
            if new_key not in groupping:
                groupping[new_key] = [each]
            else:
                groupping[new_key].append(each)
            # print(groupping)
            # exit()
        
        for each_group in groupping.values():
            res.append(each_group)
        # print(res)
        return res
        # exit()
