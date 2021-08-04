# This program reads all numbers from numbers.txt
# and calculates the average. Error exception is handled
# for ValueErrors and IOErrors

def main():
    try:
        # Open and read numbers.txt file
        infile = open('numbers.txt', 'r')

        # Initialize count for all values in the file
        count = 0

        #Initialize the total numbers to be counted
        total = 0

        print("Here are the values from the file \"numbers.txt\"")

        # Get values of all numbers in file
        for line in infile:
            all = int(line)
            count += 1

            # Display all values from the file
            print(all, sep='')
            total += all

            # Determine average of all values
            average = total/count

        print()
        print("The average of all values is:", average)

        # Close numbers.txt        
        infile.close()

    # Exception if unable to locate file
    except IOError:
        print("ERROR. Program stopped")
        print("Unable to read or fine file location")

    # Exception if all values are not numbers
    except ValueError:
        print("ERROR. Program stopped")
        print("All values must be numbers")

# Call main function
main()
