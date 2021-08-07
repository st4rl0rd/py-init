DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
  all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
  all_work_workers = [worker["name"] for worker in DATA if worker["organization"] == "Rappi"]
  all_adults = list(filter(lambda worker: worker["age"] > 18  , DATA))
  all_adults = list(map(lambda worker: worker["name"], all_adults))
  # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

  list_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
  list_python_devs = list(map(lambda worker: worker["name"], list_python_devs))
  list_workers = list(filter(lambda worker: worker["organization"] == "Rappi", DATA))
  list_workers = list(map(lambda worker: worker["name"], list_workers))
  list_olds = [worker["name"] for worker in DATA if worker["age"] > 18]
  list_old2 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

  for w in list_old2:
    print(w)


if __name__ == '__main__':
  run()