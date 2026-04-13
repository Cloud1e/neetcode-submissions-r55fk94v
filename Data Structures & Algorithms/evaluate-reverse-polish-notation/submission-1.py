class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            print(st)                
            if token in {"+", "-", "*", "/"}:
                num2 = st.pop()
                num1 = st.pop()
                if token == '+':
                    st.append(num1 + num2)
                elif token == '-':
                    st.append(num1 - num2)
                elif token == '*':
                    st.append(num1 * num2)
                elif token == '/':
                    st.append(int(num1 / num2))
            else:
                st.append(int(token))
        return st[0]