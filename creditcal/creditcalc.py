import argparse
import sys
import math
parser = argparse.ArgumentParser(description='loan calculater with two option')
parser.add_argument('-t', '--type', type=str, choices=['diff', 'annuity'])
parser.add_argument('-p', '--periods', type=int, required=False)
parser.add_argument('-i', '--interest', type=float)
parser.add_argument('--principal', type=float, required=False)
parser.add_argument('--payment', type=int, required=False)
args = parser.parse_args()

dic = vars(args)
flag = None

if (dic["type"] == None or dic["interest"] == None or (dic["type"] == "diff" and ( dic["payment"]))):
    print("Incorrect parameters")
    sys.exit(0)
# print ("ok")
for i in dic:
    if (type(dic[i]) == int and dic[i] <= 0):
        print("Incorrect parameters")
        sys.exit(0)
    if (not dic[i]):
        if (not flag):
            flag = i
            # print (flag,dic[i])
            #print(i)
        else:
            print("Incorrect parameters")
            sys.exit(0)

if (flag == None):
    print("Incorrect parameters")
    sys.exit(0)

pp = args.principal
pd = args.periods
itt = args.interest/(12*100)
pay = args.payment


def get_principal():
    ans = math.floor(((1+itt)**pd-1)*pay/(itt*(1+itt)**pd))
    print("Your loan principal = {:d}!".format(ans))
    print("Overpayment = {:d}".format(pd*pay-ans))


def get_periods():
    n = math.ceil(math.log(pay/(pay-itt*pp), 1+itt))
    year = n//12
    month = n-12*year

    if (year > 0):
        if (month == 0):
            print("It will take {:d} {:s} to repay this loan!".format(
                year, "year "if year == 1 else "years"))
        else:
            print("It will take {:d} {:s} {:s} {:d} {:s} to repay this loan!".format(
                year, "year "if year == 1 else "years", month, "months"if month > 1 else "month"))
    else:
        print("It will take {:d} {:s} to repay this loan!".format(
            month, "months"if month > 1 else "month"))
    pd=n
    print("Overpayment = {:.0f}".format(pd*pay-pp))

def get_payment():
    pay=math.ceil(pp*(itt*(1+itt)**pd)/((1+itt)**pd-1))
    print("Your annuity payment = %.0f!"%(pay))
    print("Overpayment = {:.0f}".format(pd*pay-pp))

if (dic["type"] == "annuity"):
    if (flag == "principal"):
        get_principal()
    elif (flag == "periods"):
        get_periods()
    elif (flag=="payment"):
        get_payment()
    else:
        print("Incorrect parameters")
        sys.exit(0)

else :
    # print (pp,pd,itt)
    sum=0
    for i in range (1,pd+1):
        ans=math.ceil(pp/pd+itt*(pp-pp*(i-1)*1.0/pd))
        sum+=ans
        print ("Month %d: payment is %d"%(i,ans))
    print ();print("Overpayment = %d"%(sum-pp))
