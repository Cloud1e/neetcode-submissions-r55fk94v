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
                if c in mappings:
                    if mappings[c] != st.pop():
                        return False
                
                else:
                    st.append(c)
        return not st