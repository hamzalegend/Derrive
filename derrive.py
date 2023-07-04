def Hsplit(inp : str, tokens : list):
    lst = []
    temp = ""
    for j, ch in enumerate(inp):
        for t in tokens:
            if t == ch and inp[j-1] != "*":
                lst.append(temp)
                temp = ""
        if ch != ' ':temp += ch
    lst.append(temp)
    return lst

def derrive(fx):
    parts = Hsplit(fx, ['+', '-'])
    
    dx = "" #output
    for j, part in enumerate(parts):
        part = part.strip()
        if not 'x' in part: continue # to remove the 'thabet'
        
        # us
        if part[-1] == 'x': us = 1
        else: us = float(part.split("*")[-1]) # take all digits from * till end
        
        #mu3amel
        for i in range(len(part)):
            if not part[i] == 'x': continue
            if i == 0: m = us #if x is the first element then the mu3aml is 1, and us*1=us;
            else: m = float(part[:i]) * us # take all digits from beggingin till find 'x'
        if m > 0 and j > 0:
            dx += "+"
        dx += str(m) #dx = m
        
        
        # x & us
        if us-1 != 0: 
            dx += "x" #dx = mx
            if us-1 != 1: 
                dx += "**" + str(us-1)  #dx= mx**us
        
    return dx

def main():
    # fx = "6.3x**3.1 -7.8x**2.9 +5.11x +9.0"
    fx = input("f(x) = ")
    print(f"f(x) = {fx}")
    dx = derrive(fx)
    print(f"f`(x) = {dx}")
    

main()

