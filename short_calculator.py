while True:
    op = input("\n+ - * / or q: ")
    if op == 'q': break
    a, b = float(input("A: ")), float(input("B: "))
    print("=", a+b if op=="+" else a-b if op=="-" else a*b if op=="*" else a/b if op=="/" and b!=0 else "Error")