class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n
        for i, temp in enumerate(temperatures):
            while st and temp > temperatures[st[-1]]:
                prev_temp_index = st[-1]
                st.pop()
                res[prev_temp_index] = i - prev_temp_index
            st.append(i)
        return res