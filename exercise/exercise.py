import matplotlib.pyplot as plt

def main():

    # Select user
    user = input('Is this record for Daniel (d) or Gloria (g)? ')
    if user != 'g' and user != 'd':
        raise Exception('Invalid input')

    file_name = ''
    if user == 'g':
        file_name = 'recs_gloria.txt'
    else:
        file_name = 'recs_daniel.txt'

    # Prompt user to enter new record
    rec = input('Enter a new record: ')

    # Validate user input
    if rec.isnumeric() or rec == 'check':
        if rec.isnumeric():
            rec = int(rec)
            if rec < 1:
                raise Exception('Invalid input')

            # Write new record to file
            with open(file_name, 'a') as f:
                f.write('\n{}'.format(rec))

        # Read all records into list
        daniel_recs = []
        gloria_recs = []
        with open('recs_daniel.txt') as f:
            daniel_recs = f.read().splitlines()
        with open('recs_gloria.txt') as f:
            gloria_recs = f.read().splitlines()
        daniel_recs = [int(item) for item in daniel_recs]
        gloria_recs = [int(item) for item in gloria_recs]

        # Show data
        print('\nDaniel:', end=' ')
        for i in range(len(daniel_recs)):
            print(daniel_recs[i], end=' ')
        
        print('\n\nGloria:', end=' ')
        for i in range(len(gloria_recs)):
            print(gloria_recs[i], end=' ')

        # Plot the graph
        plt.plot(daniel_recs, label='Daniel')
        plt.plot(gloria_recs, label='Gloria')
        plt.xlabel('Days')
        plt.ylabel('Plank Duration (s)')
        plt.legend()
        plt.show()

    else:
        raise Exception('Invalid input')

if __name__ == "__main__":
    main()
