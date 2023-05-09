import random

import json
import orjson
import msgspec

from tqdm import tqdm

from fuzzing_json import random_data_generator

def main():
    random.seed(9001)
    data_generator = random_data_generator()
    exeptions = []
    mismatches = []
    for _ in tqdm(range(1000)):
        data = next(data_generator)
        try:
            output_json = json.dumps(data, indent=None, separators=(',', ':'), ensure_ascii=False).encode('utf8')
            output_orjson = orjson.dumps(data)
            output_mesgspec = msgspec.json.encode(data)
        except Exception as exception:
            exeptions += [(exception, data)]
        else:
            if not output_json == output_orjson == output_mesgspec:
                print(output_json, output_orjson, output_mesgspec)
                mismatches += [data]
    print(f'{len(exeptions)} exceptions and {len(mismatches)} mismatches found')


if __name__ == '__main__':
    main()
