import xlsxwriter

# Create a new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
black_cell = workbook.add_format({'bg_color': 'black'})
# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# Insert an image.
worksheet.write('B5', '', black_cell)
worksheet.set_column('B:B', 45)
worksheet.set_row(4, height=45)
worksheet.insert_image('B5', 'fasttrackit.png')

workbook.close()
