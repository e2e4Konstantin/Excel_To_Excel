from common_data import data_bank, QuoteInfo, AttributeInfo, ParameterInfo


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


def get_attribute_from_data(row) -> AttributeInfo:
    """ Получает кортеж информации атрибута из dataset в строке row. """
    quote_cod = data_bank["attributes"].get_cell_str_value(row, 0)
    title = data_bank["attributes"].get_cell_str_value(row, 1)
    value = data_bank["attributes"].get_cell_str_value(row, 2)
    return AttributeInfo((quote_cod, title, value))


def get_all_attributes_for_quote_from_data(quote_cod: str) -> list[AttributeInfo]:
    attributes_list: list[AttributeInfo] = []
    attributes = data_bank["attributes"]
    for row in range(attributes.row_max + 1):
        if attributes.get_cell_str_value(row, 0) == quote_cod:
            attributes_list.append(get_attribute_from_data(row))
    return attributes_list


def _get_parameter_from_data(row) -> ParameterInfo:
    """ Получает словарь информации параметра из dataset в строке row. """
    # "cod", "name", "left", "right", "measure", "step", "type"
    parameter: ParameterInfo = dict()
    # parameter["cod"] = data_bank["parameters"].get_cell_str_value(row, 0)
    # parameter["name"] = data_bank["parameters"].get_cell_str_value(row, 1)
    parameter["left"] = data_bank["parameters"].get_cell_str_value(row, 2)
    parameter["right"] = data_bank["parameters"].get_cell_str_value(row, 3)
    parameter["measure"] = data_bank["parameters"].get_cell_str_value(row, 4)
    parameter["step"] = data_bank["parameters"].get_cell_str_value(row, 5)
    parameter["type"] = data_bank["parameters"].get_cell_str_value(row, 6)
    return parameter


def _get_parameter_from_tuple(src_data: tuple[str, str, str, str, str]) -> ParameterInfo:
    """ Получает словарь информации параметра из dataset в строке row. """
    # "cod", "name", "left", "right", "measure", "step", "type"
    parameter: ParameterInfo = dict()
    parameter["left"], parameter["right"], parameter["measure"], parameter["step"], parameter["type"] = src_data
    return parameter


def get_all_parameters_for_quote_from_data(quote_cod: str) -> dict[str: ParameterInfo]:
    parameters: dict[str: ParameterInfo] = dict()
    parameters_data = data_bank["parameters"]

    slim = parameters_data.df.loc[parameters_data.df["quote"] == quote_cod, ["quote", "name", "left", "right", "measure", "step", "type"]]
    # print(slim.to_records().tolist())
    # d = {x[2]: x[3:] for x in slim.to_records().tolist()}
    parameters = {x[2]: _get_parameter_from_tuple(x[3:]) for x in slim.to_records().tolist()}
    # print(d)



    # print(x.shape[0])
    # for i in range(x.shape[0]):
    #     v = x.iloc[[i]]
    #     print(type(v), x.iloc[[i]]) #x.iat[i, 1]


    #
    # y = parameters_data.df.loc[parameters_data.df["quote"] == quote_cod].tolist()
    # print("\t\t-->>>> ", y)


    # col_one_list = parameters_data["quote"].tolist()

    # for row in range(parameters_data.row_max + 1):
    #     if parameters_data.get_cell_str_value(row, 0) == quote_cod:
    #         parameters[parameters_data.get_cell_str_value(row, 1)] = _get_parameter_from_data(row)
    return parameters
