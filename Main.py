from service.generate_small_files import SmallFilesProducer
from utils.file_utils import FileUtils
from repository.gerador_de_eventos import generate_event
import os


def gerar_massa(file_utils, files_producer):
    for c in range(2):
        small_file = file_utils.generate_file(path, 'xap')
        files_producer.write_events_to_file(small_file, generate_event, 50000)


if __name__ == '__main__':
    path = os.getcwdb().decode('utf-8') + '/eventos/'

    files_producer = SmallFilesProducer(path)
    file_utils = FileUtils()

    gerar_massa(file_utils, files_producer)



