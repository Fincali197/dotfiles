import sys

output = sys.stdin.read()

# Process the output
for i in range(8):
    output = output[output.find(":")+1:]

processed_output = output[:output.index("active")-4]

# Print the processed output
print(processed_output)
