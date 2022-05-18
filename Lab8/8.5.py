import xlsxwriter
from catalog import read_data, cust_sort, find_len, calc_media


def write_xls(lst: list):
    workbook = xlsxwriter.Workbook('catalog.xlsx')
    worksheet = workbook.add_worksheet('Lab_8.5')
    bold = workbook.add_format({'bold': True})
    num_format = workbook.add_format({'num_format': '#,##0.00'})
    worksheet.set_column('A:A', find_len(lst))
    worksheet.set_column('B:B', 5)
    worksheet.write('A1', 'Elev', bold)
    worksheet.write('B1', 'Media', bold)

    row_cnt = 1
    for item in lst:
        worksheet.write(row_cnt, 0, item[0])
        worksheet.write(row_cnt, 1, item[1], num_format)
        row_cnt += 1
    workbook.close()


catalog = read_data('../Lab7/note.txt')
srt_cat = cust_sort(calc_media(catalog))
write_xls(srt_cat)

