import math


class Building:
    def __init__(self, production, price) -> None:
        self.production = production
        self.price = price

    def __repr__(self):
        return f"Building: Production: {self.production}, Price: {self.price}"


def main():
    num_of_buildings = int(input("Antal byggnader ? "))
    mega_pickle_price = int(input("Kostnad av Megapickeln ? "))

    types_of_buildings = []
    for building in range(num_of_buildings):
        building_info = input(
            f"Produktionshastighet och pris för byggnad {building +1} ? "
        ).split()
        building_production, building_price = tuple(building_info)
        new_building = Building(
            production=int(building_production), price=int(building_price)
        )
        types_of_buildings.append(new_building)

    owned_buildings = [types_of_buildings[0]]

    seconds = 1
    pickles = 0
    while pickles < mega_pickle_price:
        pickles += calculate_pickles(owned_buildings)
        # print(owned_buildings)
        # print(pickles)
        seconds += 1
        time_to_buy_mega_pickle = calculate_time_for_item(
            owned_buildings, mega_pickle_price, pickles
        )
        # print(time_to_buy_mega_pickle)
        best_building = find_which_building_to_buy(
            owned_buildings,
            types_of_buildings,
            pickles,
            time_to_buy_mega_pickle,
            mega_pickle_price,
            seconds,
        )

        if best_building != 0 and best_building.price <= pickles:
            owned_buildings.append(best_building)
            pickles -= best_building.price
    print(seconds)


def find_which_building_to_buy(
    owned_buildings,
    type_buildings,
    available_pickles,
    current_time_until_mega_pickle,
    mega_pickle_price,
    current_time,
):
    best_building = 0
    smallest_time = current_time_until_mega_pickle
    for building in type_buildings:
        # print(building)
        if building.price > available_pickles:
            time_until_it_can_be_bought = calculate_time_for_item(
                owned_buildings, building.price, available_pickles
            )
            # print(
            #     "Available pickles: ",
            #     available_pickles,
            #     "Building: ",
            #     building,
            #     "Time: ",
            #     time_until_it_can_be_bought,
            #     "Current Time: ",
            #     current_time,
            # )
            time_until_mega_pickle_with_new_building = (
                calculate_time_for_item(
                    owned_buildings + [building], mega_pickle_price, available_pickles
                )
                + time_until_it_can_be_bought
            )
            if time_until_mega_pickle_with_new_building + 3 < smallest_time:
                best_building = building
                smallest_time = time_until_mega_pickle_with_new_building
        elif available_pickles >= building.price:
            # print(building.price)
            potential_buildings = owned_buildings + [building]
            potential_time = calculate_time_for_item(
                potential_buildings,
                mega_pickle_price,
                available_pickles - building.price,
            )
            # print(building, potential_time, smallest_time)
            if potential_time < smallest_time:
                # print("lol")
                best_building = building
                smallest_time = potential_time
    # print(best_building)
    return best_building


def time_to_save_up_to_building(building, available_pickles, production_per_second):
    time = math.ceil((building.price - available_pickles) / production_per_second)
    return time


def determine_if_saving_pickles(
    available_pickle,
    owned_buildings,
    production_per_second,
    type_buildings,
    best_building,
    time_to_buy_mega_pickle,
):
    for building in type_buildings:
        pass
    pass


def calculate_time_for_item(buildings, item_price, current_pickles):
    production_per_second = sum([building.production for building in buildings])
    time_to_get_item = math.ceil((item_price - current_pickles) / production_per_second)
    return time_to_get_item


def calculate_pickles(buildings):
    sum_pickles = 0
    for building in buildings:
        sum_pickles += building.production

    return sum_pickles


main()
