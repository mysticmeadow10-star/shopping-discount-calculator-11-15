while True:
    try:
        bill = float(input("Enter the total shopping bill: "))
        discount = float(input("Enter the discount percentage: "))
        people = int(input("Enter the number of people: "))

        discount_amount = bill * (discount / 100)
        final_bill = bill - discount_amount
        per_person = final_bill / people

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except ZeroDivisionError:
        print("Number of people cannot be zero! Try again.")
    else:
        print("Final bill after discount:", final_bill)
        print("Each person pays:", per_person)
        break
    finally:
        print("Calculation attempt finished.")