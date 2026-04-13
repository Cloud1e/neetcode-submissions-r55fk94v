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

            if c in mappings:
                top_element = st.pop() if st else '#'
                if mappings[c] != top_element:
                    return False
            else:
                st.append(c)
        return not st