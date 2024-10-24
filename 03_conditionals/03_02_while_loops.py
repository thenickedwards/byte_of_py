# WHILE LOOP
n = 5
print("t minus")
while n > 0:
    print(n)
    n = n - 1
print("BLAST OFF 🚀")
print(n)

# BREAK STATEMENT
m = 4
while m > 1:
    print(m)
    m = m - 1
    if m == 2:
        print("BREAK!")
        break             # terminates current loop, resumes execution at next statement
print(f"m is {m}")

# CONTINUE STATEMENT
h = 5
while h > 1:
    h = h - 1
    if h == 2:
        continue            # skips remaining statements in current loop iteration (i.e. skips 2),
    print(h)                # continues normal execution at next iteration

# INFINTIE LOOP
'''
while True:
    print("Infintie Loop ∞")
'''
