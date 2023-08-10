from excelutils import data_out_to_excel
from datautils import data_preparation, get_table_line_from_data
# from data_bank_setting import data_bank



def main():
    # path = r"C:\Users\kazak.ke\PycharmProjects\Quotes_Parsing\output"
    # path = r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\Python_projects\Ex_to_Ex\src"
    path = r"C:\Users\kazak.ke\PycharmProjects\Excel_To_Excel\src"

    file = r"template_all_output_xxx.xlsx"
    data_preparation(file, path)
    print(f"<< {'-' * 70} >>")

    file = "template_x_xx.xlsx"
    data_out_to_excel(file, "./output", ["name", "stat"])




if __name__ == "__main__":
    main()
