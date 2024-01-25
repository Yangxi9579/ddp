def count_case(s):
    lowcount = 0
    upcount = 0
    for i in s:
        if i >= 'a' and i <= 'z':
            lowcount = lowcount+1
        elif i >='A' and i <= 'Z':
            upcount = upcount+1
    print(f"There have {lowcount} lowcount, and {upcount} upcount.")
xxx=input("Please enter text:")
count_case(xxx)
