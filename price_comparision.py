Lease = 0
PurchaseTotal = 0
LeaseYears = 0
LoopsYear = 0
PurchaseValue =0
LeaseValue = 0

Counter = 0

PurchasePrice = float(input("Please enter the purchase price "))
LoanPercentage = float(input("Please enter the loan percentage(%) "))
LoanDuration = int(input(("Please enter the loan duration(Years) ")))
#MonthlyCost = float("Please enter monthly cost of purchase")
NoOfMonths = LoanDuration * 12

Taxes = (0.13*PurchasePrice)
PriceAfterTaxes = PurchasePrice + Taxes

print("--------------------Buying the car----------------------------")

print("Price after taxes ",PriceAfterTaxes)


MonthlyCost = (((LoanPercentage/100)/12) * PriceAfterTaxes)/(1-(1+(LoanPercentage/100)/12)**-NoOfMonths)

print("Monthly cost of purchase is ",MonthlyCost)

print("\n----------------Leasing the car----------------------------")

MonthlyLeasePrice = float(input("Please enter the monthly lease price "))
Taxes = (0.13*MonthlyLeasePrice)
print("Taxes are ",Taxes)
PriceAfterTaxes = MonthlyLeasePrice + Taxes
print("Total monthly lease cost ",PriceAfterTaxes)

print("\n ----------------------------COMPARISON--------------------------------")

LeaseYears = int(input("Please enter the duration you plan on keeping the car(Years) "))

print("Year     Month    Lease  Purchase Total")


print(LoanDuration,LeaseYears)

if(LeaseYears>=LoanDuration):
    LoopsYear = LeaseYears
    #print("Lease greater",LoopsYear)
else:
    LoopsYear = Loanduration
    #print(LoopsYear)

    
for Years in range(LoopsYear):
    for Months in range(12):
        #print(Counter+(Months+1))
        PurchaseTotal = MonthlyCost * (Counter+(Months+1))
        Lease = PriceAfterTaxes * (Counter+(Months+1))

        if(LoanDuration<Years+1):
            PurchaseValue = ""
        else:
            PurchaseValue = format(PurchaseTotal,'.2f')

        if(LeaseYears<Years+1):
            LeaseValue = ""
        else:
            LeaseValue =format(Lease,'.2f')
        
        print(Years+1,"   ",Months+1,"    ",LeaseValue,"    ",PurchaseValue)
    #print(PurchaseTotal,Lease)
    #MonthlyCost = PurchaseTotal + MonthlyCost
    #PriceAfterTaxes = Lease + PriceAfterTaxes
    Counter = (Months+1)*(Years+1)
    #print(Counter)
     
    
