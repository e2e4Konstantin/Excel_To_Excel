from excelutils import ExcelControl, headers, width_columns, formats
from openpyxl.styles import (NamedStyle, Font, Border, Side, PatternFill, Alignment)
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet import worksheet

from datautils import get_table_line_from_data


# https://stackoverflow.com/questions/27133731/folding-multiple-rows-with-openpyxl
#
def styles_add(this_book: Workbook):
    name_styles = {}
    for item in formats:
        name_styles[item['name']] = NamedStyle(name=item['name'])
        # header_style = NamedStyle(name=item['name'])
        name_styles[item['name']].font = Font(name=item['font']['name'], bold=item['font']['bold'],
                                              size=item['font']['size'])
        bd = Side(style=item['border']['style'], color=item['border']['color'])
        name_styles[item['name']].border = Border(left=bd, top=bd, right=bd, bottom=bd)
        name_styles[item['name']].fill = PatternFill(patternType=item['fill']['patternType'],
                                                     fgColor=item['fill']['fgColor'])
        name_styles[item['name']].alignment = Alignment(horizontal=item['alignment']['horizontal'],
                                                        vertical=item['alignment']['vertical'],
                                                        wrap_text=item['alignment']['wrap_text'],
                                                        shrink_to_fit=item['alignment']['shrink_to_fit'],
                                                        indent=item['alignment']['indent'])
        if not (item['name'] in this_book.named_styles):
            this_book.add_named_style(name_styles[item['name']])


def create_basic_header(operate_file: ExcelControl, sheet_name: str):
    sheet = operate_file.book[sheet_name]
    sheet.append(["."])
    headers["A:O"].extend(headers["P:T"])
    sheet.append(headers["A:O"])
    for column in range(1, len(headers["A:O"]) + 1):
        sheet.cell(row=2, column=column).style = 'title_basic'
    sheet.cell(row=1, column=operate_file.column_number['K']).value = headers['K1']
    sheet.cell(row=1, column=operate_file.column_number['K']).style = 'title_basic'
    sheet.merge_cells('K1:M1')

    sheet.cell(row=1, column=operate_file.column_number['N']).value = headers['N1']
    sheet.cell(row=1, column=operate_file.column_number['N']).style = 'title_basic'
    sheet.merge_cells('N1:O1')

    sheet.cell(row=1, column=operate_file.column_number['P']).value = headers['P1']
    sheet.cell(row=1, column=operate_file.column_number['P']).style = 'title_basic'
    sheet.merge_cells('P1:T1')

    for width in width_columns:
        sheet.column_dimensions[width].width = width_columns[width]


def range_decorating(operate_file: ExcelControl, sheet_name: str, row, columns: list[str], style_name: str):
    sheet = operate_file.book[sheet_name]
    for column in columns:
        sheet.cell(row=row, column=operate_file.column_number[column]).style = style_name


def create_table_header(operate_file: ExcelControl, sheet_name: str, table_info: tuple[str, str, str, str], row: int):
    sheet = operate_file.book[sheet_name]

    sheet.cell(row=row, column=operate_file.column_number['E']).value = table_info[0]  # код таблицы
    sheet.cell(row=row, column=operate_file.column_number['F']).value = ""
    sheet.cell(row=row, column=operate_file.column_number['G']).value = table_info[1]  # название таблицы
    sheet.cell(row=row, column=operate_file.column_number['H']).value = ""
    sheet.cell(row=row, column=operate_file.column_number['I']).value = ""
    sheet.cell(row=row, column=operate_file.column_number['J']).value = ""

    range_decorating(operate_file, sheet_name, row, ['E', 'F', 'G', 'H', 'I', 'J', ], 'line_table')

    column = operate_file.column_number['K']
    sheet.cell(row=row - 1, column=column).value = headers['K1']
    sheet.merge_cells(start_row=row - 1, start_column=column, end_row=row - 1, end_column=column + 2)

    sheet.cell(row=row, column=operate_file.column_number['K']).value = headers['K']
    sheet.cell(row=row, column=operate_file.column_number['L']).value = headers['L']
    sheet.cell(row=row, column=operate_file.column_number['M']).value = headers['M']

    column = operate_file.column_number['N']
    sheet.cell(row=row - 1, column=column).value = headers['N1']
    attributes = []
    if table_info[2]:
        attributes.extend(table_info[2].split(','))  # атрибуты
        attributes_length = len(attributes)
        for i, attribute in enumerate(attributes):
            sheet.cell(row=row, column=column + i).value = attribute
        if attributes_length > 1:
            sheet.merge_cells(start_row=row - 1, start_column=column, end_row=row - 1,
                              end_column=column + attributes_length - 1)
    else:
        sheet.cell(row=row, column=operate_file.column_number['N']).value = headers['N']
        sheet.cell(row=row, column=operate_file.column_number['O']).value = headers['O']
        sheet.merge_cells(start_row=row - 1, start_column=column, end_row=row - 1, end_column=column + 1)

    if table_info[3]:
        column += len(attributes)
        parameters = table_info[3].split(',')  # параметры
        parameters_length = len(parameters)
        if parameters_length > 0:
            d = 0
            for i in range(parameters_length):
                sheet.cell(row=row - 1, column=column + i+d).value = parameters[i]  # название параметра
                parameter_tile_len = len(headers['P:T'])
                for j in range(parameter_tile_len):  # таблица: 'от', 'до', 'ед.изм.', 'шаг', 'тип'
                    sheet.cell(row=row, column=column + d + i + j).value = headers['P:T'][j]
                sheet.merge_cells(start_row=row - 1, start_column=column + i, end_row=row - 1,
                                  end_column=column + i + parameter_tile_len - 1)
                d += parameter_tile_len
    sheet.append(["."])


def prepare_file_template(file_name: str = None, file_path: str = None, sheets_name: list[str] = None):
    """ Подготовка выходного файла. Удаляет все содержимое и создает шапку таблицы. """
    output_file = ExcelControl(file_name, file_path)
    with output_file as ex:
        ex.delete_all_sheets()
        ex.create_sheets(sheets_name)
        print(output_file)
        print(type(ex.book))
        styles_add(ex.book)
        create_basic_header(ex, 'name')
        z = 0
        for r in range(4, 6):
            table = get_table_line_from_data(r)

            create_table_header(ex, 'name', table, 6+z)
            z += 3


if __name__ == "__main__":
    fln = "template_x_xx.xlsx"
    sheets = ["name", "stat"]
    prepare_file_template(fln, "../output", sheets)
