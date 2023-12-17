from icecream import ic
import aoc_utils
from pathlib import Path

day = int(Path(__file__).name.split('_')[1])
tf = aoc_utils.get_day_input(day)



def get_seeds():
    # line 1 of tf
    line = tf[0].split(":")[1].strip()
    return [int(el) for el in line.split(" ") if el]

def get_mappings():
    res = dict()
    for line in tf[2:]:
        if line and line[0].isalpha():
            mapping = line.split(":")[0].split(" ")[0]
            res[mapping] = list()
    
        elif line:
            dest, source, range_ = [int(el)  for el in line.split(" ")]
            res[mapping].append([dest, source, range_])

    for key in res:
        res[key] = sorted(res[key], key=lambda x: x[0])

    return res

def find_map_for_val_in_mapping(val, mapping):
    for dest, source, range_ in mapping:
        if source <= val < (source + range_):
            ic(source, dest, range_)
            delta = val - source
            return dest + delta
    ic("val not in range, return", val)
    return val

if __name__ == "__main__":
    seeds = get_seeds()
    mappings = get_mappings()
    ic.disable()
    ic(mappings)
    locations = list()
    for seed in seeds:
        ic(seed)
        soil = ic(find_map_for_val_in_mapping(seed, mappings['seed-to-soil']))
        fertilizer = ic(find_map_for_val_in_mapping(soil, mappings['soil-to-fertilizer']))
        water = ic(find_map_for_val_in_mapping(fertilizer, mappings['fertilizer-to-water']))
        light = ic(find_map_for_val_in_mapping(water, mappings['water-to-light']))
        temperature = ic(find_map_for_val_in_mapping(light, mappings['light-to-temperature']))
        humidity = ic(find_map_for_val_in_mapping(temperature, mappings['temperature-to-humidity']))
        location = ic(find_map_for_val_in_mapping(humidity, mappings['humidity-to-location']))

        locations.append(location)
    ic(locations)
    print(min(locations))

    