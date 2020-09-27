#(Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
#their weight in pounds and their height in feet and inches. For example, if a person
#is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches. Here is a sample
#run:
#BMI Interpretation
#Below 18.5 Underweight
#18.5–24.9 Normal
#25.0–29.9 Overweight
#Above 30.0 Obese

#one pound is 0.45359237 kilograms and one inch is 0.0254 meters
#BMI = weight / height ^ 2

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weight = eval(input("Enter weight in pounds: "))
feet = eval(input("Enter feet (5' 8\" = 5): "))
inches = eval(input("Enter inches (5' 8\" = 8): "))

heightInMeters = (inches + 12 * feet) * METERS_PER_INCH
weightInKilograms = weight * KILOGRAMS_PER_POUND

bmi = weightInKilograms / heightInMeters ** 2
formattedBMI = str(int(bmi * 100) / 100)
bmiStatus = ''
if bmi < 18.5:
    bmiStatus = 'Underweight'
elif bmi < 25:
    bmiStatus = 'Normal'
elif bmi < 30:
    bmiStatus = 'Overweight'
else:
    bmiStatus = 'Obese'

print("BMI: " + formattedBMI)
print("BMI Interpretation: " + bmiStatus)