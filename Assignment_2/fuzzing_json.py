import random
import string
import sys

def random_data_generator():
    """
    Generates random data to be used for differential fuzzing.
    """
    sys.setrecursionlimit(20000)
    while True:
        data_type = random.choice(["string", "number", "boolean", "null", "list", "dict", "tuple", "unicode"])
        match data_type:
            case "string":
                yield random_string_generator(100000, 1000000)
            case "number":
                yield random.uniform(100000000, 1000000000000)
            case "boolean":
                yield random.choice([True, False])
            case "null":
                yield None
            case "list":
                depth = random.randint(1500, 2000)
                yield nested_list_generator(depth)
            case "dict":
                depth = random.randint(1500, 2000)
                yield nested_dict_generator(depth)
            case "tuple":
                depth = random.randint(1500, 2000)
                yield nested_tuple_generator(depth)
            case "unicode":
                yield random_unicode_generator(10000, 100000)

def random_unicode_generator(upper_bound, lower_bound):
    """
    Generates a random unicode character.
    """
    data = []
    for _ in range(random.randint(upper_bound, lower_bound)):
        char = random.randint(0, 1114111)
        data.append(chr(char))
    return "".join(data)

def random_string_generator(lower_bound, upper_bound):
    """
    Generates a random string of a given length.
    """
    length = random.randint(lower_bound, upper_bound)
    return "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))

def random_nest_function(depth):
    return random.choice([nested_list_generator, nested_dict_generator, nested_tuple_generator])(depth)

def nested_list_generator(depth):
    """
    Generates a nested list of a given depth and length.
    """
    if depth <= 1:
        return [random_string_generator(20, 50),
                random_unicode_generator(20, 50)]
    else:
        return [random_nest_function(depth-1)]

def nested_dict_generator(depth):
    """
    Generates a nested dictionary of a given depth and size.
    """
    if depth <= 1:
        return {random_string_generator(20, 50): random_string_generator(20, 50),
                random_unicode_generator(20, 50): random_data_generator()}
    else:
        return {random_string_generator(10, 20): random_string_generator(10, 20),
                random_string_generator(20, 50): random_nest_function(depth-1)}

def nested_tuple_generator(depth):
    """
    Generates a nested tuple of a given depth and size.
    """
    if depth <= 1:
        return (random_string_generator(20, 50),
                random_unicode_generator(50, 100))
    else:
        return (random_string_generator(10, 20), random_nest_function(depth-1))

# import random
# import string

# # def random_data_generator():
# #     while True:
# #         data_type = random.choice(["string", "number", "boolean", "null", "list", "dict", "tuple", "unicode"])
# #         if data_type == "string":
# #             length = random.randint(100, 1000)
# #             data = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))
# #         case "number":
# #             data = random.uniform(-100, 100)
# #         case "boolean":
# #             data = random.choice([True, False])
# #         case "null":
# #             data = None
# #         case "list":
# #             length = random.randint(5, 10)
# #             depth = random.randint(20, 50)
# #             data = nested_list_generator(depth, length)
# #         case "dict":
# #             length = random.randint(5, 10)
# #             depth = random.randint(20, 50)
# #             data = nested_dict_generator(depth, length)
# #         case "tuple":
# #             length = random.randint(5, 10)
# #             depth = random.randint(20, 50)
# #             data = nested_tuple_generator(depth, length)
# #         case "unicode":
# #             length = random.randint(1000, 10000)
# #             data = "".join(random.choice(string.printable) for _ in range(length))
# #         yield data

# def random_data_generator():
#     while True:
#         data = {}
#         data_type = random.choice(["string", "number", "boolean", "null", "list", "dict", "tuple", "unicode"])
#         if data_type == "string":
#             length = random.randint(10, 100)
#             data = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))
#         case "number":
#             data = random.uniform(-100, 100)
#         case "boolean":
#             data = random.choice([True, False])
#         case "null":
#             data = None
#         case "list":
#             depth = random.randint(3, 5)
#             length = random.randint(3, 5)
#             stack = [(nested_list_generator(depth, length),)]
#             data = []
#             while stack:
#                 curr, *rest = stack
#                 if isinstance(curr, tuple):
#                     if curr:
#                         stack = [*curr, rest]
#                         stack[-2] = curr[0]
#                     else:
#                         data.append([])
#                 else:
#                     for item in reversed(curr):
#                         stack = [(item, *rest)] + stack
#         case "dict":
#             depth = random.randint(3, 5)
#             size = random.randint(3, 5)
#             stack = [(nested_dict_generator(depth, size),)]
#             data = {}
#             while stack:
#                 curr, *rest = stack
#                 if isinstance(curr, tuple):
#                     if curr:
#                         stack = [*curr, rest]
#                         stack[-2] = curr[0]
#                     else:
#                         data[""] = {}
#                 else:
#                     for key, value in curr.items():
#                         stack = [("", key, *rest), (value,)]
#         case "tuple":
#             depth = random.randint(3, 5)
#             size = random.randint(3, 5)
#             stack = [(nested_tuple_generator(depth, size),)]
#             data = ()
#             while stack:
#                 curr, *rest = stack
#                 if isinstance(curr, tuple):
#                     if curr:
#                         stack = [*curr, rest]
#                         stack[-2] = curr[0]
#                     else:
#                         data += ()
#                 else:
#                     data += (curr,)
#         case "unicode":
#             length = random.randint(10, 100)
#             data = "".join(random.choice(string.printable) for _ in range(length))
#         yield data

# def nested_list_generator(depth):
#     length = random.randint(10, 20)
#     if depth <= 1:
#         return [random_data_generator()]
#     else:
#         return [random_nest_function(depth-1)]

# def nested_dict_generator(depth):
#     if depth <= 1:
#         length = random.randint(10, 20)
#         key = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))
#         return {key: random_data_generator()}
#     else:
#         length = random.randint(10, 20)
#         key = "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))
#         return {key: random_nest_function(depth-1)}

# def nested_tuple_generator(depth):
#     if depth <= 1:
#         size = random.randint(10, 20)
#         return tuple(random_data_generator())
#     else:
#         return tuple(random_nest_function(depth-1))
