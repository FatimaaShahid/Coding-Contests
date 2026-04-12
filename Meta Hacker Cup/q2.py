# Open the input file for reading
file = open('temp.txt', 'r')

def decorrupt(s):
    s = str(s)
    count = 0
    ans = ""
    for char in s:
        if char == "?":
            ans += str(count)
            count += 1
        else:
            ans += char
    print(ans)
    return ans

def encode(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    i = 0
    while i < len(s):
        # Adjusted to prevent index out of range
        if i < len(s) - 1 and int(s[i:i+2]) < 27 and s[i:i+2] != "00":
            result += alpha[int(s[i:i+2]) - 1]
            i += 2
        else:
            result += alpha[int(s[i]) - 1]
            i += 1
    return result

def solve(input_string):
    # Apply the decorrupt and encode functions
    decorrupted = decorrupt(input_string)
    encoded = encode(decorrupted)
    return encoded

# Read the number of test cases
noOfTestCases = int(file.readline().strip())

# Open the output file for writing
with open('output.txt', 'w') as file2:
    for i in range(1, noOfTestCases + 1):
        # Read each input string for the test case
        input_string = file.readline().strip()
        # Call solve() and write the result
        result = solve(input_string)
        file2.write(f"Case #{i}: {result}\n")

# Close the input file
file.close()
