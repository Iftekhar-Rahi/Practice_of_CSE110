credit=int(input("Enter the credit :"))
cgpa=float(input("Enter your CGPA: "))
if credit>=30 and cgpa>=3.8:
    if cgpa>=3.8 and cgpa<=3.89:
        print("25 percent")
    elif cgpa>=3.9 and cgpa<=3.94:
        print("50 percent")
    elif cgpa>=3.95 and cgpa<=3.99:
        print("75 percent")
    elif cgpa>=4:
        print("100 percent")

