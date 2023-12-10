def power(base, exponent):
    # Base case: any number raised to the power of 0 is 1
    if exponent == 0:
        return 1
    # Recursive case: base^exponent = base * base^(exponent-1)
    else:
        return base * power(base, exponent - 1)

def main():
    try:
        # Input: Get base and exponent from the user
        base = float(input("Enter the base (a): "))
        exponent = int(input("Enter the exponent (n): "))

        # Check if the exponent is non-negative
        if exponent < 0:
            print("Error: Exponent should be a non-negative integer.")
        else:
            # Output: Calculate and display the result
            result = power(base, exponent)
            print(f"{base}^{exponent} = {result}")

    except ValueError:
        print("Error: Please enter valid numeric values for the base and exponent.")

if __name__ == "__main__":
    main()
