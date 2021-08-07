def run():
  word = lambda text: text == text[::-1]
  print(word('jorge'))

if __name__ == '__main__':
  run()