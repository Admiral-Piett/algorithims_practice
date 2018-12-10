stations = {}
stations["107.1"] = set(["id", "nv", "ut"])
stations["108.1"] = set(["wa", "id", "mt"])
stations["109.1"] = set(["or", "nv", "ca"])
stations["110.1"] = set(["nv", "ut"])
stations["111.1"] = set(["ca", "az"])

final_stations = set()

states_needed = set(["id", "nv", "ut", "wa", "mt", "or", "ca", "az"])

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
print(states_needed)