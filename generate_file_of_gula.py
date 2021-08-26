from generate_small_files import gerador_de_massa
import os
from os import walk
# começou a brincadeira
gerador_de_massa()

path = os.getcwdb().decode('utf-8')
file_path = path + '/arquivinhos/'
guloso = path + '/guloso/'

if not os.path.exists(guloso):
    os.mkdir(guloso)

if os.path.exists(guloso+'guloso.csv'):
    os.remove(guloso+'guloso.csv')

file_names = []
for (dirpath, dirnames, filenames) in walk(file_path):
    file_names.extend(filenames)
    break

with open(guloso + 'guloso.csv', 'w') as outfile:
    for fname in file_names:
        with open(file_path+fname) as infile:
            for line in infile:
                outfile.write(line)

print('hora do delete')
for file in file_names:
    os.remove(file_path+file)
print(f'arquivos no direitório {file_path} foram deletados')