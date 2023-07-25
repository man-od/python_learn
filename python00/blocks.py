import sys

def filter_lines(file_path, filter_1, num_lines):
  with open(file_path, 'r') as f:
    count = 0
    for line in f:
      line = line.strip()
      if line.startswith(filter_1) and len(line) == 32 and line[5] != '0':
        print(line)
        count += 1
        if count == num_lines:
          break

if (len(sys.argv) != 3 and sys.argv[2].isnumeric()):
  print("Usage: python blocks.py <file_path> <num_lines>")
else:
  file_path = sys.argv[1]
  filter_1 = '00000'
  num_lines = int(sys.argv[2])
  filter_lines(file_path, filter_1, num_lines)

#  python blocks.py data_hashes_10lines.txt 5