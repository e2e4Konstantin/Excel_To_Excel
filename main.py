from datautils import get_data_from_file
from excelutils import data_out_to_excel


def main():
    # path = r"C:\Users\kazak.ke\PycharmProjects\Quotes_Parsing\output"
    path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex\src"
    # path = r"C:\Users\kazak.ke\PycharmProjects\Excel_To_Excel\src"
    file = r"template_all_output_xxx.xlsx"

    get_data_from_file(file, path)
    print(f"<< {'-' * 70} >>")

    file = "template_x_xx.xlsx"
    data_out_to_excel(file, "./output", ["name", "stat"], grid=False)


if __name__ == "__main__":
    main()
