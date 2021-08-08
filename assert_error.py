def divisor(num):
  divisors = []
  for i in range(1, num+1):
    if num %i == 0:
      divisors.append(i)
  return divisors

def run():
  try:
    num = input("numero: ")
    assert num.isnumeric(), "Debes ingresar un positivo"
    print(divisor(int(num)))
    print("---")
  except ValueError:
    print("debes ingresar un numero")

if __name__ == "__main__":
  run()