from exceptions.FileException import FieldSizeException


class MainFrameUtils:

    def validate_field_size(self, item, size):
        if len(str(item)) > size:
            raise FieldSizeException('Valor maior que o do campo')

    def concat_zeros_to_left(self, item, size):
        return '0' * (size-len(str(item))) + str(item)

    def concat_spaces_to_right(self, item, size):
        return item + ' ' * (size-len(item))

    def to_mainframe_layout(self, event, mainframe_book):
        row = ''
        count = 0
        for k, v in event.items():
            if type(v) is str:
                row += self.concat_spaces_to_right(v, mainframe_book[count])
            else:
                row += self.concat_zeros_to_left(v, mainframe_book[count])
            count += 1
        return row
