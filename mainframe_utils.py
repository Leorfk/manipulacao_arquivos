def validate_field_size(item, size):
    if len(str(item)) > size:
        raise Exception('Valor maior que o do campo')

def concat_zeros_to_left(item, size):
    return '0' * (size-len(str(item))) + str(item)

def concat_spaces_to_right(item, size):
    return item + ' ' * (size-len(item))