#! /usr/bin/python

def main():
    filename = "prob022.txt"
    total_points = 0;
    alph = 'abcdefghijklmnopqrstuvwxyz'

    #Retrieve the list of names from filename, and sort them
    names = quick_sort(get_names(filename))
    for i in xrange(len(names)):
        name_total = 0
        for letter in names[i]:
            name_total += (alph.find(letter.lower()) + 1) #Gets total points for each name
        total_points += name_total * (i + 1) #Accumulates total points for each name
    print "Total points for each name and it's index:", total_points

def get_names(filename):
    """Reads in filename, splits the CSV at the commas, and then removes the double quotes at the beginning
       and end of the word. Returns the newly generated list of these values. """

    with open(filename, "r") as readFile:
        names = [each.split(',') for each in readFile] #Split at the commas
        names = list(names[0]) #Retrieves the list of names within the list names
        names = [each.strip("\"") for each in names] #Strips each name of the double quotes
    return names

def quick_sort(list):
    """Uses list comprehension to concatenate a sorted list around the pivot.
    Returns the sorted list argument."""

    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = quick_sort([x for x in list[1:] if x < pivot])
        greater = quick_sort([x for x in list[1:] if x > pivot])
        return lesser + [pivot] + greater

if __name__ == '__main__':
    main()
