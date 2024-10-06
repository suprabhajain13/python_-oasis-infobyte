#BMI Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("BMI Calculator")
    
    try:
        # User inputs for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)
        
        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Based on your BMI, you are classified as: {category}")
    
    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()
