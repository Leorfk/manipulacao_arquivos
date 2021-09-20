from datetime import datetime
import os


class FileUtils:

    def generate_file(self, file_path, file_name):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        return open(f'{file_path}{file_name}_{str(datetime.now().timestamp())}.csv', 'x')

    def get_files_in_dir(self, file_path):
        list_of_files = []
        for (dirpath, dirnames, filenames) in os.walk(file_path):
            list_of_files.extend(filenames)
            break
        return list_of_files

    def concat_content_of_files(self, big_file, file_names, file_path):
        for fname in file_names:
            with open(file_path+fname) as infile:
                for line in infile:
                    big_file.write(line)

    def delete_files_in_dir(self, file_path, file_names):
        print('hora do delete')
        for file in file_names:
            os.remove(file_path + file)
        print(f'arquivos no direitório {file_path} foram deletados')

    def delete_file_in_dir(self, file_path, file_name):
        os.remove(file_path+file_name)
