def get_size(matrix):
    return int(len(matrix) ** (1/2))

def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix - строку, в которой строки матрицы 
    разделены переносом строки, а элементы строки разделены пробелами.
    :param matrix: list
    :return: string
    """
    size = get_size(matrix)
    string = ""
    for i in range(size):
        if i:
            string += '\n'
        for j in range(size):
            if j:
                string += ' '
            string += str(matrix[i*size + j])
    return string

def add_element(element, matrix):
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: string
    :param matrix: list
    :return: list
    """
    if element == None:
        return matrix
    size = get_size(matrix)
    for i in range(size - 1):
        for j in range(size):
            if matrix[i * size + j] == None:
                matrix[i * size + j] = element
                return matrix
    matrix[(size - 1) * size] = element
    size += 1
    for _ in range(2 * size - 1):
        matrix.append(None)
    return matrix

def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное 0).
    :param size: int > 0
    :return: list 
    """
    return [None for _ in range(size * size)]