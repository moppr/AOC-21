with open("10.in") as f:
    lines = [ln.strip() for ln in f.readlines()]
    
    pts = 0
    ptmap = {')':3, ']':57, '}':1197, '>':25137}
    cmap = {'(':1, '[':2, '{':3, '<':4}
    
    cptsl = []
    for line in lines:
        cpts = 0
        stack = []
        for ch in line:
            if ch in '([{<':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    break
                p = stack.pop()
                if (p == '(' and ch != ')') or (p == '[' and ch != ']') or \
                        (p == '{' and ch != '}') or (p == '<' and ch != '>'):
                    pts += ptmap[ch]
                    stack = []
                    break
        if len(stack) > 0:
            for ch in reversed(stack):
                cpts *= 5
                cpts += cmap[ch]
        if cpts:
            cptsl.append(cpts)
    
    print(sorted(cptsl)[len(cptsl)//2])