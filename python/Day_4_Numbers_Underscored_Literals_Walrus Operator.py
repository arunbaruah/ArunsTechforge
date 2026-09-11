# Mock input to provide simulated values and prevent the script from timing out
simulated_inputs = ["10.5", "20.0", "done"]

def input(prompt=""):
    if simulated_inputs:
        val = simulated_inputs.pop(0)
        print(f"{prompt}{val}")
        return val
    return "done"

total = 0.0
while (user_input := input("Enter a number (or 'done' to exit): ")) != 'done':
    total += float(user_input)
print(f"Total sum: {total}")