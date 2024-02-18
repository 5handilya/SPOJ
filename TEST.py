broken = False
while not broken:
    inp = int(input())
    if inp != 42:
        print(inp)
    else:
        broken = True