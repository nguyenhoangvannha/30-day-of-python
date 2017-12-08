import csv
with open('data.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Title','Description'])
	writer.writerow(['Row 1', 'Some desc'])
with open('data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)