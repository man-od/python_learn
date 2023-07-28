import sys

def check_m_pattern(image):
  if len(image) != 3 or any(len(row) != 5 for row in image):
    return 'Error'
  if ( image[0][0] == '*' and image[0][4] == '*' and
       image[1][0] == '*' and image[1][2] == '*' and image[1][4] == '*' and
       image[2][0] == '*' and image[2][2] == '*' and image[2][3] == '*' and image[2][4] == '*' ):
    return 'True'
  else:
    return 'False'

if len(sys.argv) != 2:
  print("Usage: python mfinder.py <filename>")
  sys.exit(1)

filename = sys.argv[1]

try:
  with open(filename, 'r') as file:
    image = [line.strip() for line in file]

  result = check_m_pattern(image)
  print(result)

except FileNotFoundError:
  print(f"Файл '{filename}' не найден.")
