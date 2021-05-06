def selection_sort(first) :
    # This function sort list from Smallest to Greatest number.
    n = len(first)
    for i in range(n - 1) :
        small = i
        for j in range(i + 1, n) :
            if first[j] < first[small] :
                small = j
        if i != small :
            first[i], first[small] = first[small], first[i]
    return first
def selection_sort_2(first) :
    # This function sort list from Greatest number to Smallest number.
    n = len(first)
    for i in range(n - 1) :
        small = i
        for j in range(i + 1, n) :
            if first[j] > first[small] :
                small = j
        if i != small :
            first[i], first[small] = first[small], first[i]
    return first
def non_duplicate_list_function(user_list) :
    # This function sorts/removes duplicates from list and produce a non duplicate list(a list which contains no similar number, or to say it another way, only one of those numbers).
    duplicate_list = user_list[:]
    non_duplicate_list = []
    duplicate_check = False
    duplicate_check_2 = True
    for variable_1 in duplicate_list :
        if non_duplicate_list == [] :
            non_duplicate_list = non_duplicate_list + [variable_1]
        else :
            for variable_2 in non_duplicate_list :
                if variable_1 != variable_2 :
                    duplicate_check = True
                else :
                    duplicate_check = False
                    duplicate_check_2 = False
        if duplicate_check and duplicate_check_2 :
            non_duplicate_list = non_duplicate_list + [variable_1]
        duplicate_check_2 = True
    return non_duplicate_list
def even_odd_sort(user_list) :
    # This fuction depends on other function. Delete the line with hastag mark to make this function independent.
    even_list = []
    odd_list = []
    for x in user_list :
        remainder = x % 2
        if remainder == 0 :
            even_list = even_list + [x]
        else :
            odd_list = odd_list + [x]
    even_list = selection_sort(even_list)#
    odd_list = selection_sort(odd_list)#
    return even_list,odd_list
def prime_composite_sort(user_list) :
    # This fuction depends on other function. Delete the line with hastag mark to make this function independent.
    # This function do not consider Negative numbers for prime and composite sorting.
    prime_list = []
    composite_list = []
    for x in user_list :
        factors = 0
        for y in range(1,x+1,1) :
            remainder = x % y
            if remainder == 0 :
                factors = factors + 1
        if factors > 2 :
            composite_list = composite_list + [x]
        else :
            if factors == 2 :
                prime_list = prime_list + [x]
    prime_list = selection_sort(prime_list)#
    composite_list = selection_sort(composite_list)#
    return prime_list,composite_list
def main() :
    # This function takes the user input and run all the above functions by assigning it, to their formal parameter.
    # This function is just for the working demonstration of above functions.
    user_input = eval(input('>> Please enter numbers seperated by comma : '))
    first = list(user_input)
    a = first[:]
    b = first[:]
    result = selection_sort(a)
    print()
    print('Smallest to Greatest : ',result)
    print()
    result_2 = selection_sort_2(b)
    print('Greatest to Smallest : ',result_2)
    print()
    result_3 = non_duplicate_list_function(result)
    print('After Removing Duplicate Number/s ---->  ',result_3)
    print('Number of Duplicate Element/s found ----> ',len(first) - len(result_3),'Element/s')
    print()
    result_4,result_5 = even_odd_sort(first)
    print('Even Number/s : ',result_4)
    print()
    print('Odd Number/s : ',result_5)
    print()
    result_5,result_6 = prime_composite_sort(first)
    print('Prime Number/s : ',result_5)
    print()
    print('Composite Number/s : ',result_6)
    print()
main()
