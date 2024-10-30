from pupils import Pupil

pupils = []

def print_all():
   print("Список студентів")
   for pupil in pupils:
      print(pupil.name, pupil.surname, str(pupil.mark))

with open("pupils.txt", "r", encoding="utf-8") as file:
   for line in file:
      data = line.split(" ")
      new_pupil = Pupil(data[0], data[1], int(data[2]))
      pupils.append(new_pupil)

print_all()
