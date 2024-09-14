def is_valid(s: str) -> bool:
        choices = {"{": "}", "[":"]", "(":")"}
        stack = []
        for char in s:
            if stack and stack[-1] in choices and choices[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        return not stack    

