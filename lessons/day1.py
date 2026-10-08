print("DNA SEQUENCE ANALYSIS")

seq = input("input your seq : ")
x = len(seq)
sequence = seq.upper()
g = sequence.count("G")
c = sequence.count("C")
g_content = f"Number of G = {g}"
c_content = f"Number of C = {c}"
Gccontent = (g + c) / x * 100
ans = f"Your sequence is {x} bases long"
ans1 = f"The GC content is {Gccontent:.2f}%"
print(g_content)
print(c_content)
print(ans)
print(ans1)

