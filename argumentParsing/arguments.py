import sys


# Printing to screen
writeThis = ''

print(sys.argv[0], sys.argv[1], sys.argv[2])
print(sys.argv)
for argument in sys.argv:
    if argument == sys.argv[0] or argument == sys.argv[0]:
        pass
    else:
        writeThis += argument
        print(argument, end=" ")

# Writing to a file 
filename = sys.argv[1]

with open(filename, 'w+') as f:
    f.write(writeThis)

