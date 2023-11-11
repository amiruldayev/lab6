from datetime import datetime


def task1():
    def get_keys_with_value_true(input_dict):
        true_keys = []
        for key, value in input_dict.items():
            if value is True:
                true_keys.append(key)
        return true_keys


    my_dict = {
        "a": True,
        "b": False,
        "c": True
    }

    result = get_keys_with_value_true(my_dict)
    print(result)

def task2():
    def get_unique_elements(list):
        num_list = []
        for i in list:
            if list.count(i) <=1:
                num_list.append(i)
        return num_list

    print(get_unique_elements([1, 2, 3, 1, 2, 4]))


def task3():
    def get_date_in_format(input_date):
        date_object = datetime.strptime(input_date, '%Y.%m.%d')

        formatted_date = date_object.strftime('%d.%m.%Y')
        return formatted_date


    print(get_date_in_format('2023.10.23'))


def task4():
    def get_elements_with_no_more_than_two_occurrences(list):
        num_list = []
        for i in list:
            if not num_list.count(i):
                if list.count(i) > 1:
                    num_list.append(i)
        return num_list

    print(get_elements_with_no_more_than_two_occurrences([1, 2, 3, 1, 2, 4]))

def task5():
    def get_words_from_string(string):
        print(string.split())

    string = "This a string with a several words."
    get_words_from_string(string)


def task6():
    def get_unique_elements_with_count(list):
        unique_elem = {}
        for i in list:
            if i in unique_elem:
                unique_elem[i] += 1
            else:
                unique_elem[i] = 1
        return unique_elem
    print(get_unique_elements_with_count([1, 2, 3, 1, 2, 4, 1, 2]))


def task7():
    def get_prime_numbers(n):
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    # Example usage:
    print(get_prime_numbers(100))


def task8():
    def get_prime_numbers_in_list(list):
        primes = []
        for num in list:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    print(get_prime_numbers_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]))


def task9():
    def get_difference_between_dates(date1, date2):
        date1_obj = datetime.strptime(date1, "%Y.%m.%d")
        date2_obj = datetime.strptime(date2, "%Y.%m.%d")

        date_dif = date2_obj - date1_obj

        return date_dif.days

    date_str1 = "2023.10.23"
    date_str2 = "2023.10.24"
    print(get_difference_between_dates(date_str1, date_str2))



def task10():
    def get_decimal_number_from_binary_string(binary_string):
        return int(binary_string, 2)

    binary_input = "10110011"
    print(get_decimal_number_from_binary_string(binary_input))



def task11():
    def is_expression_true(expression):
        def is_perfect_square(number):
            return int(number ** 0.5) ** 2 == number

        return all(is_perfect_square(num) for num in expression)



    print(is_expression_true([4, 25, 81]))


def task12():
    def sort_by_price(shopping_list):
        return sorted(shopping_list, key=lambda x: x['price'])

    # Example usage:
    shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]

    print(sort_by_price(shopping_list))


def task13():
    def get_words_starting_with_vowel(words):
        vowels = "aeiouAEIOU"
        vowel_words = []
        for word in words:
            if word[0] in vowels:
                vowel_words.append(word)
        return vowel_words


    print(get_words_starting_with_vowel(["apple", "banana", "orange", "bear", "cat"]))


task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()
task12()
task13()
