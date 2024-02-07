import csv

# Open the space-separated CSV file and a new file for the comma-separated version
with open('comma_separated.csv', 'r') as infile, open('comma_separated_new.csv', 'w', newline='') as outfile:
    # Create a csv reader to read the space-separated file
    reader = csv.reader(infile, delimiter=' ')
    # Create a csv writer to write to the comma-separated file
    writer = csv.writer(outfile)
    
    # Read from the space-separated file and write to the comma-separated file
    for row in reader:
        writer.writerow(row)

