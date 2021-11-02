"""Generate sales report showing total melons each salesperson sold."""

# creates an empty list for sales people that will be updated later.
# should have "_" to separate words as it is standard practice
salespeople = []
melons_sold = []


# setting "f" as variable for the text file that is being opened
# should set variable with more descriptive name, such as "sales_report_file"
f = open('sales-report.txt')
# this will go through each line
for line in f:
    # removes trailing whitespace and redifines "line" to be without the trailing whitespace
    line = line.rstrip()
    # this will separate out the data on each line. the "|" indicates a new piece of data in the text file
    # also assigns the data to entries and saves as a list
    entries = line.split('|')
    # assigns the salesperson to the first item in every line before the |
    salesperson = entries[0]
    # assigns the salesperson to the third item to melons
    # naming should be better, such as num_of_melons
    melons = int(entries[2])

    # checks to see if the variable salesperson is in the list salespeople
    if salesperson in salespeople:
        # if so, then setting variable "position" to the index of where that person is
        position = salespeople.index(salesperson)
        # adds melons to the index that salesperson was at
        melons_sold[position] += melons
    else:
        # if not in sales people then it will add the salesperson
        salespeople.append(salesperson)
        # adds the melons sold by that person
        melons_sold.append(melons)

# this will iterate over the lenth of the list "salespeople"
for i in range(len(salespeople)):
    # prints the salesperson then the melons they sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
