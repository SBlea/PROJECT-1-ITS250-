lettergrade = " "
raw_input = " "
credit = 0.0
totalcal = 0.0
caltimes = 0.0
totalcredit = 0.0
A = 4.0
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D = 1.0
F = 0.0

for i in range (0,4):
    lettergrade = input("What is the letter grade: ")
    credit = input ("What is the credit: ")
    if  lettergrade == "A" or "a":
        caltimes = float(credit) * A
    elif lettergrade == "A-" or "a-":
        caltimes = float(credit) * A_minus
    elif lettergrade == "B+" or "b+":
        caltimes = float(credit) * B_plus
    elif lettergrade == "B" or "b":
        caltimes = float(credit) * B
    elif lettergrade == "B-" or "b-":
        caltimes = float(credit) * B_minus
    elif lettergrade == "C+" or "c+":
        caltimes = float(credit) * C_plus
    elif lettergrade == "C" or "c":
        caltimes = float(credit) * C
    elif lettergrade == "C-" or "c-":
        caltimes = float(credit) * C_minus
    elif lettergrade == "D" or "d":
        caltimes = float(credit) * D
    elif lettergrade == "F" or "f":
        caltimes = float(credit) * F

    totalcredit = totalcredit + float(credit)
    totalcal = totalcal + caltimes

finalgpa = totalcal / totalcredit
print ("GPA:" +str(finalgpa))


