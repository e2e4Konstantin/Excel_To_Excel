from excelutils import create_file_template
from datautils import data_preparation


def main():
    path = r"C:\Users\kazak.ke\PycharmProjects\Quotes_Parsing\output"
    file = r"template_all_output.xlsx"
    data_preparation(file, path)
    print(f"<< {'-' * 70} >>")

    file = "template_x_xx.xlsx"
    create_file_template(file, "./output", ["name", "stat"])





if __name__ == "__main__":
    main()
