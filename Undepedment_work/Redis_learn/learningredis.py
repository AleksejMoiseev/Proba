import redis

r = redis.Redis(host="localhost", port=6379, db=0)
# my_value = r.get(name="current_bbaab69f-f0cd-4b72-bd08-6068a86fb415")
# print(my_value.decode(encoding='utf-8'))


class Ship:
    def __init__(self, coordinates, hit_coordinates):
        self.coordinates = coordinates
        self.hit_coordinates = hit_coordinates

    def to_json(self):
        return {'coordinates': self.coordinates, 'hit_coordinates': self.hit_coordinates}

    def __str__(self):
        return f"'coordinates': {self.coordinates}, 'hit_coordinates': {self.hit_coordinates}"

    def check_hit(self, coordinate):
        if not (coordinate in self.coordinates):
            return 'mimo'
        if not (coordinate in self.hit_coordinates):
            self.hit_coordinates.append(coordinate)
        if len(self.coordinates) == len(self.hit_coordinates):
            return "killed"
        return "ranen"

    def killed(self):
        if len(self.coordinates) == len(self.hit_coordinates):
            return True
        return False

ship_list = [{'coordinates': ['A3'], 'hit_coordinates': []}, {'coordinates': ['A5'], 'hit_coordinates': []}, {'coordinates': ['A9', 'B9'], 'hit_coordinates': []}, {'coordinates': ['E2', 'E3', 'E4'], 'hit_coordinates': []}, {'coordinates': ['C6', 'C5', 'D6', 'E7'], 'hit_coordinates': []}]
al = [{'coordinates': ['A5'], 'hit_coordinates': ['A5']}, {'coordinates': ['A9', 'B9'], 'hit_coordinates': ['A9', 'B9']}]

def get_array_ships(list_json_objects):
    harborArr = []
    for json_object in list_json_objects:
        ship = Ship(coordinates=json_object['coordinates'], hit_coordinates=json_object['hit_coordinates'])
        harborArr.append(ship)
    return harborArr


def ships_to_json(arrship_object):
    arr_to_json = []
    for ship in arrship_object:
        arr_to_json.append(ship.to_json())
    return arr_to_json



def check_hit(harbor, coordinate):
    for ship in harbor:
        hit_result = ship.check_hit(coordinate=coordinate)
        if hit_result == "ranen":
            return "ranen"
        if hit_result == "killed":
            return "killed"
    return 'mimo'

def check_winner(arr_ships):
    for ship in arr_ships:
        if not ship.killed():
            return False
    return True



if __name__ == '__main__':
    # arr = get_array_ships(ship_list)
    # print(arr)
    # hit_result = check_hit(harbor=arr, coordinate='E4')
    # print(hit_result)
    # for i in arr:
    #     print(i)
    # arr_ready_save_to_database = ships_to_json(arrship_object=arr)
    # print(arr_ready_save_to_database)
    # arr = get_array_ships(list_json_objects=arr_ready_save_to_database)
    # hit_result = check_hit(harbor=arr, coordinate='A5')
    # print(hit_result)
    # for i in arr:
    #     print(i)
    # arr_ready_save_to_database = ships_to_json(arrship_object=arr)
    # print(arr_ready_save_to_database)
    # print(str(arr_ready_save_to_database).encode())
    # content = str({ 'coordinate': 'A5', 'hit_result': hit_result}).encode()
    # print(content)
    arr1 = get_array_ships(al)
    print(check_winner(arr_ships=arr1))


