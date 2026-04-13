class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if not st:
                st.append(c)
            else:
                if c == ')' and st[-1] == '(':
                    st.pop()
                elif c == ']' and st[-1] == '[':
                    st.pop()
                elif c == '}' and st[-1] == '{':
                    st.pop()                
                else:
                    st.append(c)
        return not st