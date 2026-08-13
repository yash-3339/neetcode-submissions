class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        so=sorted(s)
        to=sorted(t)
        return so==to