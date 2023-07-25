# python_learn

## Exercise 00: Blockchain

- Create a Python script (let's call it "blocks.py") that can read input from standard input.
- The input will consist of multiple lines of data.
- The script should process the input and print out only the lines that meet the following criteria:
- a. The line is exactly 32 characters long.
- b. The line starts with exactly 5 zeroes ('0').
- c. Any line starting with more than 5 zeroes is not considered valid.
- d. Any line starting with less than 5 zeroes is not considered valid.
- The script should be able to handle a specified number of lines as an argument when run.
- If the number of lines in the input is smaller than the specified argument, the program should not produce an error but may hang.
- In summary, the Python script "blocks.py" should filter and print lines that are 32 characters long and start with exactly 5 zeroes, and it should accept the number of lines to be processed as an argument.

So, for the example above your script should print:

`` 00000254b208c0f43409d8dc00439896 ``
``0000085a34260d1c84e89865c210ceb4 ``
``0000071f49cffeaea4184be3d507086v ``

`` ~$ python blocks.py data_hashes_10lines.txt 10 ``