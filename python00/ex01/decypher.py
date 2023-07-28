import sys
if (len(sys.argv) > 1):
    word = sys.argv[1:]
    for arg in word:
        first_letter = arg[0]
        print(first_letter, end='')
else:
    print("ERROR! Usage: python decypher.py <words>")

# python decypher.py Have you delivered eggplant pizza at restored keep?