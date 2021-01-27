import matplotlib.pyplot as plt
from datetime import date, datetime, timedelta

def main():

    # Select mode
    mode = input("Select mode ('a' for add, 'c' for check): ")
    if mode != 'a' and mode != 'c':
        raise Exception("Invalid input. 'a' or 'c' are only valid modes. ")

    # Read recs list
    recs = []
    with open('aaa.txt') as f:
        recs = f.read().splitlines()

    # Add a new rec
    if mode == 'a':

        # Enter date difference
        days_diff = input('Enter the date difference: ')
        if not days_diff.isnumeric():
            raise Exception('Invalid input. <days_diff> must be an int')
        
        days_diff = int(days_diff)
        if days_diff < 0:
            raise Exception('Invalid input. <days_diff> must be non-negative')

        # Calculate date difference
        this_day = date.today() - timedelta(days=days_diff)
        last_day = datetime.fromisoformat(recs[0]).date()
        diff = (this_day - last_day).days

        if diff < 0:
            raise Exception('Invalid input. <diff> must be non-negative')

        # Modify recs
        recs[0] = str(this_day)
        recs.append(str(diff))

        # Write changes to file
        with open('aaa.txt', 'w') as f:
            f.write('\n'.join(recs))

    # Show data
    for i in range(len(recs)):
        print(recs[i], end=' ')

    # Make the plot
    recs = [int(item) for item in recs[1:]]
    plt.plot(recs)
    plt.xlabel('Instances')
    plt.ylabel('Days Between')
    plt.show()

if __name__ == "__main__":
    main()
