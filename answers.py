import csv

# Read the CSV file
with open('train.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    # Print the first line
    first_line = next(reader)
    print('First line:', first_line)
    
    # Ask the user which column to select
    column_index = int(input('Which column would you like to select? (0-based index): '))
    
    # Ask the user how many rows to convert
    num_rows = int(input('How many rows would you like to convert? '))
    
    # Iterate through the selected rows and create a new text file for each element
    for i, row in enumerate(reader):
        if i >= num_rows:
            break
        column_content = row[column_index]
        with open(f'models/{i}.txt', 'w') as outfile:
            outfile.write(column_content)
