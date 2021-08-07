def run():
  my_list = [1,"ccc", True, 4.5]
  my_dic = {"firstname":"Wil", "lastname":"iba"}

  super_list = [
    {"firstname":"Wil", "lastname":"iba"},
    {"firstname":"Wil1", "lastname":"iba1"},
    {"firstname":"Wil2", "lastname":"iba2"},
    {"firstname":"Wil3", "lastname":"iba3"},
    {"firstname":"Wil4", "lastname":"iba4"},
  ]

  super_dic = {
    "numbers": [1,2,3,4,5],
    "integers": [-1,-2,-3,-4],
    "float": [1.1,2.3,4.2,2.5]
  }

  for key, value in super_dic.items():
    print(key, "-", value)

if __name__ == '__main__':
  run()