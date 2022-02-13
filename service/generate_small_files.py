import os
from datetime import datetime
from utils.mainframe_utils import MainFrameUtils


class SmallFilesProducer:

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        self.mainframe_utils = MainFrameUtils()

    def write_event_to_file(self, file, event, mainframe_book):
        file.write(self.mainframe_utils.to_mainframe_layout(event, mainframe_book) + '\n')

    def write_events_to_file(self, file, events, number_of_events):
        for c in range(number_of_events):
            print(f'Evento n°{c+1} registrado - hora: {datetime.now()}')
            self.write_event_to_file(file, events(), [30, 26, 10, 10, 15])
