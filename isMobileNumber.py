import re


matches = []
# Only match correct length.

isMobileNumber = re.compile(r'((\+?447|07)\d{9})[ ]')

# TODO: Read in a file, local drive and extract mobile numbers
message = input("> ")
output = isMobileNumber.findall(message)

for hits in output:
    matches.append(hits[0])

# TODO: output file names and lines number is located on (currently N/A)

print(matches)
