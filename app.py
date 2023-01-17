import sys

def printPairs(numbers, target_sum):

    hashmap = {}
    for i in range(0, len(numbers)):
        temp = target_sum-numbers[i]

        if (temp in hashmap):
            print(','.join([str(numbers[i]), str(temp)]))

        hashmap[numbers[i]] = i
 
if __name__ == "__main__":
    try:
        numbers = [int(x) for x in sys.argv[1].split(",")]
        target_sum = int(sys.argv[2])
        printPairs(numbers, target_sum)
    except:
        print("Error: Please, enter the correct arguments according to de README")