from datautils.data_setting import SourceData
from common_data import data_bank
import gc


def get_tables(file_name: str = None, file_path: str = None, sheet_name: str = None,
               skip_rows: int = 0) -> SourceData | None:
    src_data = SourceData("Tables", file_name, file_path, sheet_name, skip_rows=skip_rows, what_columns="B:H")
    if not src_data.df.empty:
        column_names = ["show_number", "number", "attribute_count", "parameter_count", "table_name",
                        "attributes", "parameters"]
        c_types = {"attribute_count": int, "parameter_count": int}
        src_data.set_columns_name_type_column_data(column_names, c_types)
        # print(data.df.info())
        return src_data
    return None


def get_quotes(file_name: str = None, file_path: str = None, sheet_name: str = None,
               skip_rows: int = 0) -> SourceData | None:
    src_data = SourceData("Quotes", file_name, file_path, sheet_name, skip_rows=skip_rows, what_columns="B:I")
    if not src_data.df.empty:
        column_names = ["table", "cod", "title", "measure", "stat", "flag", "basic_slave", "link_cod"]
        c_types = {"stat": int, }
        src_data.set_columns_name_type_column_data(column_names, c_types)
        print(src_data.df.info())
        print(src_data.df.to_string())
        return src_data
    return None


def get_attributes(file_name: str = None, file_path: str = None, sheet_name: str = None,
                   skip_rows: int = 0) -> SourceData | None:
    src_data = SourceData("Attributes", file_name, file_path, sheet_name, skip_rows=skip_rows, what_columns="B:D")
    if not src_data.df.empty:
        column_names = ["quote", "name", "value"]
        src_data.df.columns = column_names
        # print(src_data.df.info())
        return src_data
    return None


def get_parameters(file_name: str = None, file_path: str = None, sheet_name: str = None,
                   skip_rows: int = 0) -> SourceData | None:
    src_data = SourceData("Options", file_name, file_path, sheet_name, skip_rows=skip_rows, what_columns="B:H")
    if not src_data.df.empty:
        column_names = ["quote", "name", "left", "right", "measure", "step", "type"]
        c_types = {}  # "type": int,
        src_data.set_columns_name_type_column_data(column_names, c_types)
        src_data.df.set_index(['quote'])
        print(src_data.df.index)
        print(src_data.df.head())

        # src_data.df.columns = column_names
        # print(src_data.df.info())

        return src_data
    return None


def get_data_from_file(file_name: str = None, file_path: str = None):
    data_bank["tables"] = get_tables(file_name, file_path, sheet_name="Tables", skip_rows=1)
    data_bank["quotes"] = get_quotes(file_name, file_path, sheet_name="Quote", skip_rows=1)
    data_bank["attributes"] = get_attributes(file_name, file_path, sheet_name="Attributes", skip_rows=1)
    data_bank["parameters"] = get_parameters(file_name, file_path, sheet_name="Options", skip_rows=1)


def free_data_bank():
    for db in data_bank.values():
        print(db.df.info()) if db else print("пусто")
        del db
        gc.collect()


if __name__ == "__main__":
    path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex\src"
    file = r"template_all_output_xxx.xlsx"

    get_data_from_file(file, path)
    print(f"<< {'-' * 70} >>")
    free_data_bank()
