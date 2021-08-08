def words(word):
  try:
    if len(word) == 0:
      raise ValueError("not found")
    return word == word[::-1]
  except ValueError as ve:
    print(ve)
    return False

def run():
  try:
    print(words(''))
  except TypeError:
    print("Error capturado")

if __name__ == '__main__':
  run()