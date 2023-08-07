

headers = {
    'A2': ['Шифр главы', 'Шифр сборника', 'Шифр отдела', 'Шифр раздела', 'Шифр таблицы', 'Шифр расценки',
           'Наименование главы, сборника, отдела, раздела, таблицы, расценки', 'Измеритель',
           'Статистика применения по объектам жилищного строительства', 'Подлежит параметризации',
           'Связанные расценки', 'Шифры родительских расценок', 'Тип алгоритма',
           'Наименование элемента', 'Наименование материала', 'от', 'до (включительно)', 'Ед. изм.',
           'Шаг'],

    'K1': 'Дополнительные расценки',
    'N1': 'Атрибуты',
    'P1': 'Название_параметра',

    'K': 'Связанные расценки',
    'L': 'Шифры родительских расценок',
    'M': 'Тип алгоритма',
    'N': 'Наименование элемента',
    'O': 'Наименование материала',
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




]

#
#
#
#
# title_format = workbook.add_format({
#     'text_wrap': True,
#     'bold': True,
#     'align': 'center',
#     'valign': 'vcenter',
#     'border': 1
# })
#
# default_text = workbook.add_format({
#     'text_wrap': True,
#     'align': 'left'
# })
#
# default_cell = workbook.add_format({
#     'text_wrap': True,
#     'align': 'center',
#     'valign': 'vcenter'
# })
#
# grey_color_text = workbook.add_format({
#     'bg_color': '#f2f2f2',
#     'text_wrap': True,
#     'align': 'left'
# })
#
# dark_color_text = workbook.add_format({
#     'bg_color': '#8e8e8e',
#     'text_wrap': True,
#     'align': 'left'
# })
#
# dark_color_cell = workbook.add_format({
#     'bg_color': '#8e8e8e',
#     'text_wrap': True,
#     'align': 'center',
#     'valign': 'vcenter'
# })
#
