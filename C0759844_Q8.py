#Name:Prashanth Chintala,CNumber:C0759844,Question:08,Date:11/5/2019

#Initializing variables
sqFeetOfWallToPaint = 0
priceOfPaintPerGallon = 0
noOfGallonsOfPaintReq = 0
hoursOfLabour = 0
costOfPaint = 0
labourCharges = 0
totalCostOfPaintJob = 0

#Initializing constants
LABOURCHARGES = 35
HOURSPER112FT = 8
SQFTWALLFOR8HOURS = 112
SqFTWALLFOR1HOUR = 14


#main function
def main():
   sqFeetOfWallToPaint,priceOfPaintPerGallon =getInputs()  #getting inputs from the getinputs function
   noOfGallonsOfPaintReq,hoursOfLabour,costOfPaint,labourCharges,toalCostOfPaintJob = calculateData(sqFeetOfWallToPaint,priceOfPaintPerGallon) #getting calculated values from the calculateData function
   print("No of gallons of paint required are ",format(noOfGallonsOfPaintReq,'.2f'))
   print("Hours of labour required are ",format(hoursOfLabour,'.2f'))
   print("Cost of paint is ",format(costOfPaint,'.2f'))
   print("Labour Charges are ",format(labourCharges,'.2f'))
   print("Total cost of paint job is ",format(toalCostOfPaintJob,'.2f'))

#This function will take inputs from the user and passes back to main function
def getInputs():
    sqFeetOfWallToPaint = float(input("Please enter the square feet of wall space to be painted: "))
    priceOfPaintPerGallon = float(input("Please enter the price of the paint per gallon: "))
    return sqFeetOfWallToPaint,priceOfPaintPerGallon;

#this function calculates all values and returns result back to main function
def calculateData(sqFeetOfWallToPaint,priceOfPaintPerGallon):
    noOfGallonsOfPaintReq = sqFeetOfWallToPaint / SQFTWALLFOR8HOURS #calculating number of gallons of paint required
    hoursOfLabour = sqFeetOfWallToPaint / SqFTWALLFOR1HOUR          #Calculating hours of labour required
    costOfPaint = noOfGallonsOfPaintReq * priceOfPaintPerGallon     #calculating cost of paint
    labourCharges = LABOURCHARGES * hoursOfLabour                   #calculating labour charges
    toalCostOfPaintJob = costOfPaint + labourCharges                #calculating total cost for paint job
    return noOfGallonsOfPaintReq,hoursOfLabour,costOfPaint,labourCharges,toalCostOfPaintJob


main()
