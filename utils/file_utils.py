from datetime import datetime


class FileUtils:

    def generate_file(self, file_path, file_name):
        return open(f'{file_path}{file_name}_{str(datetime.now().timestamp())}.csv', 'x')
