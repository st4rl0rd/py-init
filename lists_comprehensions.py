def run():
  # squares = []
  # for i in range(1,101):
  #   if i % 3 != 0:
  #     squares.append(i**2)

  squares = [ i**2 for i in range(1,101) if i % 3 != 0]
  print(squares)

def multiplos():
  values = [ i for i in range(1,9999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
  print(values)

if __name__ == '__main__':
  # run()
  multiplos()