from common_data import data_bank, QuoteInfo


def get_table_from_data(row) -> tuple[str, str, str, str]:
    """ Получает кортеж информации по таблице из dataset. """
    cod = data_bank["tables"].get_cell_str_value(row, 1)
    title = data_bank["tables"].get_cell_str_value(row, 4)
    attributes = data_bank["tables"].get_cell_str_value(row, 5)
    parameters = data_bank["tables"].get_cell_str_value(row, 6)
    return cod, title, attributes, parameters


def get_quote_from_data(row) -> QuoteInfo:
    """ Получает кортеж информации по расценке из dataset. """
    table_cod = data_bank["quotes"].get_cell_str_value(row, 0)
    cod = data_bank["quotes"].get_cell_str_value(row, 1)
    title = data_bank["quotes"].get_cell_str_value(row, 2)
    unit_of_measure = data_bank["quotes"].get_cell_str_value(row, 3)
    statistics = data_bank["quotes"].get_cell_str_value(row, 4)
    return QuoteInfo((table_cod, cod, title, unit_of_measure, statistics))


def get_all_tables_from_data() -> list[tuple[str, str, str, str]]:
    tables_list = []
    for row in range(data_bank["tables"].row_max + 1):
        tables_list.append(get_table_from_data(row))
    return tables_list


def get_all_quotes_for_tables_from_data(table_cod: str) -> list[QuoteInfo]:
    quotes_list: list[QuoteInfo] = []
    quotes = data_bank["quotes"]
    for row in range(quotes.row_max + 1):
        if quotes.get_cell_str_value(row, 0) == table_cod:
            quotes_list.append(get_quote_from_data(row))
    return quotes_list
