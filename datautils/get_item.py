from data_bank_setting import data_bank


def get_table_line_from_data(row) -> tuple[str, str, str, str]:
    """ Получает кортеж информации по таблице из dataset. """
    cod = data_bank["tables"].get_cell_str_value(row, 1)
    title = data_bank["tables"].get_cell_str_value(row, 4)
    attributes = data_bank["tables"].get_cell_str_value(row, 5)
    parameters = data_bank["tables"].get_cell_str_value(row, 6)
    return cod, title, attributes, parameters
