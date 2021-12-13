
def getBMIcategory (Height, Weight):
    MetricHeight = 0.0254 * Height
    MetricWeight = 0.453592 * Weight
    
    BMI = MetricWeight / (MetricHeight * MetricHeight)
    
    Category = ""
    
    if BMI < 18.5:
        Category = "Underweight"
    elif BMI < 25:
        Category = "Normalweight"
    elif BMI < 29:
        Category = "Overweight"
    else:
        Category = "Obesity"
        
    return BMI, Category

def printkarvonen (Age, restHR):

    print ("Excercise Intensity Heart Rates: ")
    print ("Intensity          Maximum Heart Rate")
    print ("  ")


    for Intensity in range (50, 100, 5):
        i_percent = Intensity / 100


        t_t_zone = (((220 - Age) - restHR) * i_percent) + restHR

        print ("{0:.2f}                {1}".format(i_percent, int (t_t_zone)))

def main():
    
    print ("Please enter the following values for the user..." )
    print (" ")
    ValidInt = True

    while ValidInt:
        try:
            Height = int(input("Height in inches: "))
            break
        except ErrorCheck:
            print ("Height must be a number")
            
    while ValidInt:
        try:
            Weight = int (input("Weight in pounds: "))
            break
        except ErrorCheck:
            print("Weight must be a number")

        while ValidInt:
            ValidInt = True
            
    while ValidInt:
        try:
            Age = int(input("Please enter your age "))
            break
        except ErrorCheck:
            print("Age must be a number")
    while ValidInt:
        try:
            restHR = int(input("Enter resting heart rate: "))
            break
        except ErrorCheck:
            print("Enter valid")
    BMI, WeightCatt = getBMIcategory (Height, Weight)

    print(" ")
    print("Result")
    print(" ")
    print("Your BMI is: {0: .2f}--- {1}".format(BMI, WeightCatt))
    printkarvonen(Age, restHR)
main()      

