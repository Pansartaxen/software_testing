import json
import orjson
import msgspec
import random
import string
import time

def random_data_generator():
    """
    Generates random data to be used for differential fuzzing.
    """
    while True:
        data = {}
        data_type = random.choice(["string", "number", "boolean", "null", "list", "dict"])

        if data_type == "string":
            length = random.randint(0, 10)
            data = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        elif data_type == "number":
            data = random.uniform(-1000, 1000)
        elif data_type == "boolean":
            data = random.choice([True, False])
        elif data_type == "null":
            data = None
        elif data_type == "list":
            length = random.randint(0, 5)
            data = [random_data_generator() for _ in range(length)]
        elif data_type == "dict":
            length = random.randint(0, 5)
            for _ in range(length):
                key_length = random.randint(1, 100)
                key = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(key_length))
                data = {}
                data[key] = random_data_generator()
        yield data

def compare_json_encodings(json_data, orjson_data, msgspec_data):
    if json_data != orjson_data:
        print("\nJSON and orjson produce different encodings:")
        print(f"json: {json_data}")
        print(f"orjson: {orjson_data}")
    if json_data != msgspec_data:
        print("\nJSON and msgspec produce different encodings:")
        print(f"json: {json_data}")
        print(f"msgspec: {msgspec_data}")
    if orjson_data != msgspec_data:
        print("\norjson and msgspec produce different encodings:")
        print(f"orjson: {orjson_data}")
        print(f"msgspec: {msgspec_data}")

def main():
    for i in range(1000):
        # Generate random data
        data = random_data_generator()

        # Test encoding and decoding with JSON
        json_data = json.dumps(data)
        try:
            decoded_json_data = json.loads(json_data)
        except Exception as e:
            print(f"JSON exception: {e}")

        # Test encoding and decoding with orjson
        orjson_data = orjson.dumps(data)
        try:
            decoded_orjson_data = orjson.loads(orjson_data)
        except Exception as e:
            print(f"orjson exception: {e}")

        # Test encoding and decoding with msgspec
        msgspec_data = msgspec.json.encode(data)
        try:
            decoded_msgspec_data = msgspec.json.decode(msgspec_data)
        except Exception as e:
            print(f"msgspec exception: {e}")

        # Compare encodings
        compare_json_encodings(json_data, orjson_data, msgspec_data)


if __name__ == "__main__":
    main()
