import csv
#path = input("Enter Path: ")


with open("data.csv","r") as fd:
    csv_read = csv.reader(fd)
    for lines in csv_read:
        print(lines)

# with open("data.csv","w",newline="") as anyfile:
    
#     csv_writer = csv.writer(anyfile, delimiter=",")
#     csv_writer.writerow(['NAME', 'Age', 'Class'])
#     csv_writer.writerow(['Zohaib', '25', 'AI'])
#     csv_writer.writerow(['Jasim', '26', 'cloud'])
#     csv_writer.writerow(['osama', '26', 'blockchain'])