from typing import List


def min_refills(distance: int, max_run: int, gas_stations: List[int]) -> int:
    stops: int = 0
    last_stop_value: int = 0
    index: int = 0
    gas_stations.append(distance)
    while index < len(gas_stations):
        if gas_stations[index] - last_stop_value <= max_run:
            index += 1
            continue
        elif gas_stations[index] - gas_stations[index-1] > max_run or index == 0:
            return -1
        else:
            last_stop_value = gas_stations[index-1]
            stops += 1
    return stops
