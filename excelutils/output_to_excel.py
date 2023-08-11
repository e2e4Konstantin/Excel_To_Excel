from excelutils.excel_tools_setting import ExcelControl
from excelutils.templates import styles_add, create_basic_header, put_table_to_sheet, put_quote_to_sheet
from datautils import get_all_tables_from_data, get_all_quotes_for_tables_from_data


def data_out_to_excel(file_name: str = None, file_path: str = None, sheets_name: list[str] = None, grid: bool = True):
    """ Подготовка выходного файла. Удаляет все содержимое и создает шапку таблицы. """
    output_file = ExcelControl(file_name, file_path)
    with output_file as ex:
        ex.delete_all_sheets()
        ex.create_sheets(sheets_name)
        print(output_file)

        styles_add(ex.book)
        ex.sheet = ex.book['name']
        ex.set_sheet_grid(grid=grid)
        create_basic_header(ex.sheet)

        # ex.sheet.sheet_properties.outlinePr.summaryBelow = False

        start_table_row = 6
        step_table_row = 3
        next_table_row = 0
        table_row = start_table_row

        # прочитать данные о всех таблицах
        tables = get_all_tables_from_data()
        for table in tables:
            # print(table_row, table)
            put_table_to_sheet(ex.sheet, table, table_row)

            table_cod = table[0]
            quotes = get_all_quotes_for_tables_from_data(table_cod)
            quote_row = table_row+1
            for quote in quotes:
                put_quote_to_sheet(ex.sheet, quote, quote_row)
                quote_row += 1
            table_row = quote_row + step_table_row

