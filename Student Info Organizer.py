#problem A
std = '''STUDENT;SECTION;GRADE
Abordo;BSIT4A;2.25
Agustin;BSIT4A;1.75
Asiatico;BSIT4A;3.00
Asilo;BSIT4A;2.75
Bernabe;BSIT4A;2.25
Borja;BSIT4A;2.00
Botabara;BSIT4A;3.00
Cagoco;BSIT4A;3.00
Cariño;BSIT4A;3.00
Cruz;BSIT4A;3.00
Dapatnapo;BSIT4A;3.00
Darupan;BSIT4A;2.25
Delos Reyes;BSIT4A;3.00
Ono;BSIT4A;3.00
Torres;BSIT4A;2.50
Ugale;BSIT4A;2.25
Elpedes;BSIT4B;3.00
Endozo;BSIT4B;2.50
Estrada;BSIT4B;3.00
Evangelista;BSIT4B;2.75
Fernandez;BSIT4B;3.00
Flores;BSIT4B;3.00
Gayeta;BSIT4B;2.25
Gernale;BSIT4B;2.25
Guarino;BSIT4B;2.50
Lecaros;BSIT4B;3.00
Legarda;BSIT4B;2.50
Longcop;BSIT4B;2.75
Mabansag;BSIT4B;2.75
Malaluan;BSIT4B;2.50
Manaba;BSIT4B;2.25
Manarin;BSIT4B;3.00
Mengol;BSIT4B;3.00
Opriasa;BSIT4B;2.50
Pangan;BSIT4B;1.75
Cortez;BSIT4C;3.00
Pantilag;BSIT4C;2.25
Penuliar;BSIT4C;3.00
Relojo;BSIT4C;3.00
Reyes;BSIT4C;2.75
Salazar;BSIT4C;3.00
Santiago;BSIT4C;2.25
Seberre;BSIT4C;3.00
Suayan;BSIT4C;3.00
Sulit;BSIT4C;3.00
Tejada;BSIT4C;2.50
Tura;BSIT4C;2.25
Tuvieron;BSIT4C;1.75
Vicente;BSIT4C;2.25
Yacub;BSIT4C;2.75'''
with open('studs_grades.txt', 'w') as file:
    file.write(std)

#problem B 
with open("studs_grades.txt", "r") as file:
    lines = file.readlines()

studs_dict = {'STUDENT': [], 'SECTION': [], 'GRADE': []}

for line in lines[1:]:
    student, section, grade = line.strip().split(';')
    studs_dict['STUDENT'].append(student)
    studs_dict['SECTION'].append(section)
    studs_dict['GRADE'].append(float(grade))
#problem C
print("Grade|Count")
print("-----+-----")
for grade in sorted(set(studs_dict['GRADE'])):
    count = studs_dict['GRADE'].count(grade)
    print(f"{grade:.2f}| {count:>5}")
#problem D
def list_students(param_data, min_grade=None, max_grade=None, section=None):
    print("Student        |Section   |Grade  ")
    print("---------------+----------+-------")

    for student, sec, grade in zip(param_data['STUDENT'], param_data['SECTION'], param_data['GRADE']):
        if (min_grade is None or grade >= min_grade) and \
           (max_grade is None or grade <= max_grade) and \
           (section is None or sec == section):
            print(f"{student:15}|{sec:10}|{grade:7.2f}")

#problem E
list_students(studs_dict, min_grade=1.00, max_grade=1.75)
#problem F
list_students(studs_dict, min_grade=2.00, max_grade=2.75)
#problem G
list_students(studs_dict, min_grade=3.00, max_grade=3.00)
#problem H
list_students(studs_dict, section='BSIT4A')
