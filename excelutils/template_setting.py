
headers = {
    'A:O': ['Шифр главы', 'Шифр сборника', 'Шифр отдела', 'Шифр раздела', 'Шифр таблицы', 'Шифр расценки',
            'Наименование главы, сборника, отдела, раздела, таблицы, расценки', 'Измеритель',
            'Статистика применения по объектам жилищного строительства', 'Подлежит параметризации', 'Связанные расценки',
            'Шифры родительских расценок', 'алгоритм', 'элемент', 'материал'],

    'P:T': ['от', 'до', 'ед.изм.', 'шаг', 'тип'],

    'K1': 'Дополнительные расценки',
    'N1': 'Атрибуты',
    'P1': 'Название_параметра',

    'K': 'Связанные расценки',
    'L': 'Шифры родительских расценок',
    'M': 'Тип алгоритма',
    'N': 'элемент',
    'O': 'материал',
}

width_columns = {'A': 8, 'B': 10, 'C': 12, 'E': 15, 'F': 10, 'G': 80, 'H': 15, 'I': 16, 'J': 10, 'K': 15}


colors_styling = {'lavender': 'E6E6FA', 'thistle': '00D8BFD8', 'title_basic': "00FAFAE6", 'title_attributes': "00daeef3", 'title_parameter': "00fde9d9", 'c3': "0099CC00", 'c4': "00FFCC00", 'c5': "000066CC", 'c6': "00666699", 'c7': "00C0C0C0", 'c8': "00FF99CC"}

formats = [
    {
        'name':       'title_basic',
        'font':       {'name': 'Calibri', 'bold': True, 'size': 10},
        'alignment':  {'horizontal': 'center', 'vertical': 'bottom', 'wrap_text': True, 'shrink_to_fit': False, 'indent': 0},
        'fill':       {'patternType': "solid", 'fgColor': colors_styling['title_basic']},
        'border':     {'style': 'thin', 'color': "000000"}
    },
    {
        'name':       'title_parameter',
        'font':       {'name': 'Calibri', 'bold': False, 'size': 10},
        'alignment':  {'horizontal': 'center', 'vertical': 'bottom', 'wrap_text': True, 'shrink_to_fit': False, 'indent': 0},
        'fill':       {'patternType': "solid", 'fgColor': colors_styling['title_parameter']},
        'border':     {'style': 'thin', 'color': "000000"}
    },
    {
        'name':       'title_attributes',
        'font':       {'name': 'Calibri', 'bold': False, 'size': 10},
        'alignment':  {'horizontal': 'center', 'vertical': 'bottom', 'wrap_text': True, 'shrink_to_fit': False, 'indent': 0},
        'fill':       {'patternType': "solid", 'fgColor': colors_styling['title_attributes']},
        'border':     {'style': 'thin', 'color': "000000"}
    },
{
        'name':       'line_table',
        'font':       {'name': 'Calibri', 'bold': False, 'size': 10},
        'alignment':  {'horizontal': 'left', 'vertical': 'bottom', 'wrap_text': False, 'shrink_to_fit': False, 'indent': 0},
        'fill':       {'patternType': None, 'fgColor': colors_styling['title_attributes']},
        'border':     {'style': None, 'color': "000000"}
    },


]
