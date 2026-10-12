class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mem = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(list(s)))
            print(key)
            mem[key].append(s)
        
        result = []
        for key, vals in mem.items():
            result.append(vals)
        print(result)
        
        return result