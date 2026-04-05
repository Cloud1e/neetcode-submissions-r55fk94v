class Solution:

    def encode(self, strs: List[str]) -> str:

        return ''.join([s.replace('#', '##') + '#,' for s in strs])
    def decode(self, s: str) -> List[str]:

        res = s.replace('##', '#').split('#,')[:-1]
        print(res)
        return res