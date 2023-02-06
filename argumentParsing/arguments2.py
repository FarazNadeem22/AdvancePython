import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(f"opts: {opts}\nargs: {args}")
# input expected $python arguments2.py -f myfile.txt -m This is my file