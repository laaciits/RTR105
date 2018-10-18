score = float(input("Enter score between 0.0 and 1.0   "))
if 0.0 <= score <= 1.0:
    if score >= 0.9:
        results="A"
    elif 0.9<= score <= 0.8:
        results="B"
    elif 0.8<= score <= 0.7:
        results="C"
    elif 0.7<= score <= 0.6:
        results="D"
    elif score <= 0.6:
        results="F"
    else:
        print("ERROR")
print (results)

