from random import randint

PERIOD = 1

####################################################################

def main():
    # Save records to list
    recs = []
    with open('recs.txt') as f:
        recs = f.read().splitlines()

    # Ask user whether to check records
    to_check = input('Do you want to check records? (y/n) ')
    check_empty(to_check)

    if to_check != 'y' and to_check != 'n':
        raise Exception("Invalid input. Enter 'y' or 'n'.")

    if to_check == 'y':
        rec_to_check = input('Enter the record name you want to check: ')
        check_empty(rec_to_check)

        if rec_to_check in recs:
            print('This record is already in file.')
        else:
            print('Record not found.')

    # Get the indicator
    indicator = recs[0]

    # Add new record
    if indicator[0] == 'a':
        new_rec = input("Please enter the new record name: ")
        check_empty(new_rec)
        
        if new_rec in recs:
            raise Exception('Record already exists.')

        recs.append(new_rec)
        recs[0] = 'c0'

        print('Records added successfully!')

    # Get random record
    elif indicator[0] == 'c':
        r = randint(1, len(recs) - 1)
        print(recs[r], 'has been chosen.')

        # Update number
        num = int(indicator[1:]) + 1
        if num > PERIOD - 1:
            recs[0] = 'a'
        else:
            recs[0] = 'c' + str(num)

    # Write records back to file
    with open('recs.txt', 'w') as f:
        f.write('\n'.join(recs))

####################################################################

def check_empty(user_input):
    if not user_input:
        raise Exception('Input cannot be empty.')

####################################################################

if __name__ == "__main__":
    main()
