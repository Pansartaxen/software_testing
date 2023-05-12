import random
import string
import sys

def random_data_generator() -> dict:
    """
    Generates random data to be used for differential fuzzing.
    """
    # Sets the recursion limit to 50000 to allow for deeper trees
    sys.setrecursionlimit(50000)
    while True:
        data = None
        # Chooses a random data type
        data_type = random.choice(["string", "int", "boolean", "null", "list", "dict", "tuple", "binary", "hex"])
        # Generates data of the chosen data type
        match data_type:
            case "string":
                data = random_string_generator(1, 1000000)
            case "int":
                # Test if small and big numbers are handled correctly
                data = random.uniform(0.000000000001, 1000000000000)
            case "boolean":
                data = random.choice([True, False])
            case "null":
                data = None
            case "list":
                depth = random.randint(1, 1000)
                data = nested_list_generator(depth)
            case "dict":
                depth = random.randint(1, 1000)
                data = nested_dict_generator(depth)
            case "tuple":
                depth = random.randint(1, 1000)
                data = nested_tuple_generator(depth)
            case "binary":
                data = bin(random.randint(1, 100000000000))
            case "hex":
                data = hex(random.randint(1, 100000000000))
        yield {random_string_generator(100, 200): data}

def random_string_generator(lower_bound: int, upper_bound: int) -> str:
    """
    Generates a random string of a random length in a given range.
    """
    length = random.randint(lower_bound, upper_bound)
    return "".join(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace) for _ in range(length))

def random_nest_function(depth: int):
    """
    Calls a random generator function.
    """
    return random.choice([nested_list_generator, nested_dict_generator, nested_tuple_generator])(depth)

def nested_list_generator(depth: int) -> list:
    """
    Adds a list to the nest and calls the
    random generator function to add another
    data type if the depth is greater than 1,
    otherwise returns a list of random strings.
    """
    if depth <= 1:
        # If the depth is 1 or less the tree is done and a list of random strings is returned
        return [random_string_generator(0, 50)]
    else:
        # Floor division to ensure the result is an int
        # and devide by 5 to ensure the depth is not too big
        # since the tree will grow exponentially
        return [random_nest_function(depth//5) for _ in range(5)]

def nested_dict_generator(depth: int) -> dict:
    """
    Adds a dict to the nest and calls the
    random generator function to add another
    data type if the depth is greater than 1,
    otherwise returns a dict of random strings.
    """
    if depth <= 1:
        # If the depth is 1 or less the tree is done and a dict of random strings is returned
        return {random_string_generator(20, 50): random_string_generator(20, 50)}
    else:
        # Same thing here as in the nested_list_generator, the depth is limited
        # by using floor division to avoid geting a too big tree and saving some RAM :)
        return {random_string_generator(0, 50): random_nest_function(depth-1),
                random_string_generator(0, 50): random_nest_function(depth//10),
                random_string_generator(0, 50): random_nest_function(depth//5),
                random_string_generator(0, 50): random_nest_function(depth//2),
                random_string_generator(0, 50): random_nest_function(depth//4)}

def nested_tuple_generator(depth: int) -> tuple:
    """
    Adds a tuple to the nest and calls the
    random generator function to add another
    data type if the depth is greater than 1,
    otherwise returns a dict of random strings.
    """
    if depth <= 1:
        # If the depth is 1 or less the tree is done and a tuple of random strings is returned
        return (random_string_generator(20, 50))
    else:
        # Once again floor division to ensure the result is an int
        # and devide by 5 to ensure the depth is not too big
        return (random_nest_function(depth//5) for _ in range(5))
