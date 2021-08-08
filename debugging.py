def divisor(num):
  divisors = []
  for i in range(1, num+1):
    if num %i == 0:
      divisors.append(i)
  return divisors

def run():
  try:
    num = int(input("numero: "))
    try:
      if num < 0:
        raise ValueError("Debes ingresar un positivo")
      print(divisor(num))
      print("---")
    except ValueError as ve:
      print(ve)
  except ValueError:
    print("debes ingresar un numero")

if __name__ == "__main__":
  run()