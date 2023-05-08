def valid_paranthesis(s):
    if not s or len(s) < 2:
        return False
    stack = []
    for p in s:
        if p in ["(", "[", "{"]:
            stack.append(p)
        else:
            if not stack:
                return False
            last = stack.pop()
            if last == "(" and p!= ")":
                return False
            if last == "{" and p!="}":
                return False
            if last == "[" and p != "]":
                return False
    return not stack


paranthesis_string = "(){[]"

print(valid_paranthesis(paranthesis_string))
