"""
Question:

Display by order of speed (fastest to slowest), all the bipedal dinosaurus.

speed = (length of leg * stride) + SquareRoot(length of legs * g)
g = 9,81 m*s^-2

file1.csv contains:

Name,length of leg,diet
Abelisaurus,1.2,herbivore
Achelousaurus,2,carnivore
Albertosaurus,1,herbivore
Avaceratops,2.5,carnivore
Avimimus,0.8,herbivore
Aragosaurus,3,carnivore


file2.csv contains:
Name,stride,number of legs
Abelisaurus,1,bipedal
Achelousaurus,2,bipedal
Albertosaurus,1.5,bipedal
Avaceratops,4,quadrupedal
Avimimus,1.6,quadrupedal
Ankylosaurus,0.9,bipedal
"""
import math

dinos = {}

with open("file1.csv") as f:
    for line in f.readlines()[1:]:
        line = line.split(",")
        dinos[line[0]] = {"lenght": float(line[1])}

with open("file2.csv") as f:
    for line in f.readlines()[1:]:
        line = line.split(",")
        try:
            dinos[line[0]]["stride"] = float(line[1])
            dinos[line[0]]["legs"] = line[2]
        except KeyError:
            pass


def speed(length, stride):
    return (length * stride) + math.sqrt(length * 9.81)


dino_list = [{"name": name, "speed": speed(info["lenght"], info["stride"])}
             for name, info in dinos.items() if info.get("legs") == "bipedal"]

sorted_list = sorted(dino_list, key=lambda k: k["speed"])

for dino in reversed(sorted_list):
    print("{} : {} m/s".format(dino["name"], dino["speed"]))
