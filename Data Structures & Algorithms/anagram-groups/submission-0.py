class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has={}
        for index,st in enumerate(strs):
            so="".join(sorted(st))
            if so in has:
                has[so].append(st)
            else:
                has[so]=[st]
        return list(has.values())