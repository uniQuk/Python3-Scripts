import re

# TODO: Only match correct length.
isMobileNumber = re.compile(r"07\d{9}|447\d{10}")

# TODO: Read in a file, local drive and extract mobile numbers
message = input("> ")
output = isMobileNumber.findall(message)

# TODO: output file names and lines number is located on

print(output)
