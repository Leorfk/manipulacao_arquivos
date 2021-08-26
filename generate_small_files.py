import os
from event import generate_event
from datetime import datetime
from mainframe_utils import concat_spaces_to_right, concat_zeros_to_left

mainframe_book = [50, 30, 10, 10, 15]
file_path = os.getcwdb().decode('utf-8') + '/arquivinhos/'

if not os.path.exists(file_path):
    os.mkdir(file_path)

def generate_file(file_name):
    #f = open(file_name + '.csv', 'x')
    f = open(f'{file_path}{file_name}_{str(datetime.now().timestamp())}.csv', 'x')
    return f

def to_mainframe_layout(event, mainframe_book):
    row = ''
    count = 0
    for k,v in event.items():
        if type(v) is str:
            row += concat_spaces_to_right(v, mainframe_book[count])
        else:
            row += concat_zeros_to_left(v, mainframe_book[count])
        count += 1
    return row

def write_events_to_file(file):
    for c in range(100):
        file.write(to_mainframe_layout(generate_event(), mainframe_book) + '\n')

def gerador_de_massa():
    for c in range(200):
        print(f'{(c+1)/2}% hora: {datetime.now()}')
        file = generate_file('toma')
        write_events_to_file(file)