from .excel_tools_setting import ExcelControl
from .templates import styles_add, create_basic_header, create_table_header
from datautils import get_table_line_from_data


def data_out_to_excel(file_name: str = None, file_path: str = None, sheets_name: list[str] = None):
    """ Подготовка выходного файла. Удаляет все содержимое и создает шапку таблицы. """
    output_file = ExcelControl(file_name, file_path)
    with output_file as ex:
        ex.delete_all_sheets()
        ex.create_sheets(sheets_name)
        print(output_file)
        print(type(ex.book))

        styles_add(ex.book)
        sheet = ex.book['name']
        create_basic_header(sheet)

        z = 0
        for r in range(0, 6):
            table = get_table_line_from_data(r)

            create_table_header(sheet, table, 6+z)
            z += 3