while True:
    op=int(input("Choose operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\n"))
    if op==1:
        a,b=map(int,input("Enter two numbers:").split())
        result=a+b
        print(f"{a}+{b}={result}")
    elif op==2:
        a,b=map(int,input("Enter two numbers:").split())
        result=a-b
        print(f"{a}-{b}={result}")
    elif op==3:
        a,b=map(int,input("Enter two numbers:").split())
        result=a*b
        print(f"{a}*{b}={result}")
    elif op==4:
        a,b=map(float,input("Enter two numbers:").split())
        if b==0:
            print("Division by zero not possible.\n")
        else:
            result=a/b
            print(f"{a}/{b}={result}")
    elif op==5:
        print("Exiting...\n")
        break
    else:
        print("Invalid choice\n")