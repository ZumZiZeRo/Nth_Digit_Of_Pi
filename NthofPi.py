#chudnovsky algorith Worked!! 

from decimal import Decimal as Dec, getcontext as gc

def nthOfPI(iteration=70, precision=1008, display=1007): # parameter defaults chosen to gain 1000+ digits within a few seconds
    gc().prec = precision
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409 #the values defined here are part of constants of Chudnovsky Algorithm

    for k in range(1, iteration+1):             #Algorithm Implemented 

        M = (K**3 - 16*K) * M // k**3           
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    pi = Dec(str(pi)[:display]) # drop few digits of precision for accuracy
    print("PI(Loop={} iterations, context precision={}, display={} digits) =\n{}".format(iteration, precision, display, pi))
    return pi

print("Welcome!")
print("We will Use Chudnovsky Algorithm to Calculate The Nth Digit of Pi")

nth_digit = int(input("Please Determine Up to Which Digit Of The Pi You Want: \t"))

precision = nth_digit + 10                       #This Plus Ten is to make sure in low percisions , we will get high accuracy

calculated_pi = nthOfPI(70,precision,nth_digit+2)#we keep iterations at 70 times because i dont think anybody 
                                                #gonna that much of percision and accuracy
