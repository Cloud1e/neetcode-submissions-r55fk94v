class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        st = [] 
        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if not st:
                st.append(c)
            else:
                if  c in mappings and mappings[c] == st[-1]:
                    st.pop()        
                else:
                    st.append(c)
        return not st