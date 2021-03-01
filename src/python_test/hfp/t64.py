from athletemodel import *

the_files = ["../../datasets/sarah2.txt",
             "../../datasets/james2.txt",
             "../../datasets/julie2.txt",
             "../../datasets/mikey2.txt"
             ]

data = put_to_store(the_files)
print(data)
for athlete in data:
    print(data[athlete].name + ' ' + data[athlete].dob)
