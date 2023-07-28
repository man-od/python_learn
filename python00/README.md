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

``00000254b208c0f43409d8dc00439896 ``
``0000085a34260d1c84e89865c210ceb4 ``
``0000071f49cffeaea4184be3d507086v ``

`` ~$ python blocks.py data_hashes_10lines.txt 10 ``

## Exercise 01: Decypher
To successfully complete the task, you need to write a Python script called "decypher.py" that can decrypt messages. The messages have a strange cipher, where each word is represented by the first letter of the original word.

Sample message: "The only way to get in touch with Brenda quickly is to explicitly deliver the products"

Encrypted message: "TowerrrBride"

You must write a script that takes an input message as a command-line argument and decodes it to output a single word response with no spaces.

An example of running a script:
`` ~$ python decypher.py "Have you delivered eggplant pizza at restored keep?" ``

## Exercise 02: Track and Capture
To successfully complete the task, you need to write a Python script named "mfinder.py" that can process a 2D "image" given as text in a file called "m.txt". The file contains five characters over three lines, forming a 3x5 pattern, and you need to identify if the pattern resembles the letter 'M' made out of stars ('*'). 

Your code should do the following:

1. Read the contents of the "m.txt" file, which represents the 2D image.
2. Check if the pattern matches the letter 'M' made out of stars ('*').
3. Print 'True' if the M-pattern exists in the given input image, or 'False' otherwise.
4. If the given pattern is not a 3x5 size, print 'Error'.

Examples:

For the input image:

```
*****
*****
*****
```

The output should be:

```
True
```

For the input image:

```
*****
*****
*****
*s*f*
**f**
*a***
```

The output should be:

```
False
```

For an invalid pattern:

```
*a*
*b*c
```

The output should be:

```
Error
```

After writing the code, name the file as "mfinder.py". Once you complete the task, Lestrade will upload the code to the police servers, and the cameras will be able to locate terrorists using the M-patterns.