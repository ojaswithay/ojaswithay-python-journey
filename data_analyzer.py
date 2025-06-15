print("📊Welcome to Mini Data Analyzer!")
data_input = input("Enter 5 numbers seperated by commas:")

data_list = data_input.split(",")
numbers = [int(num) for num in data_list]

Average = sum(numbers) / len(numbers)
Minimum = min(numbers)
Maximum = max(numbers)

if max(numbers) - min(numbers) < 10:
  balance = "This data is quite balanced."
else:
  balance = "This data is varied"

print("\n Data Summary Report")
print("Numbers:", numbers)
print("Average:", Average)
print("Minimum:", Minimum)
print("Maximum:", Maximum)
print("Balance:", balance)
