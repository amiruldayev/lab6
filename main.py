def get_keys_with_value_true(input_dict):
    true_keys = [key for key, value in input_dict.items() if value is True]
    return true_keys
my_dict = {
    "a": True,
    "b": False,
    "c": True,
}

result = get_keys_with_value_true(my_dict)
print(result)
