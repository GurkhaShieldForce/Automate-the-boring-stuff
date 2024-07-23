import openpyexcel

# Create a new workbook and get the active sheet
workbook = openpyexcel.Workbook()
sheet = workbook.active

# Create some data in column A
for row in range(1, 11):
    sheet[f'A{row}'] = row

# Create a reference object for the data in column A
data_ref = openpyexcel.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# Create a series object for the data
series = openpyexcel.chart.Series(data_ref, title='First series')

# Create a bar chart object
chart = openpyexcel.chart.BarChart()
chart.title = 'My Chart'
chart.append(series)

# Add the chart to the sheet
sheet.add_chart(chart, 'C5')

# Save the workbook to a file
workbook.save('sampleChart.xlsx')