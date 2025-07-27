import sys

if len(sys.argv) != 3:
    print("Please provide exactly two numbers as command line arguments.")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

result = num1 + num2

print("Sum =", result)
