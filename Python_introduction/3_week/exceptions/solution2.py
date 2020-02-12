import csv
import os.path

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        #if os.path.splitext(photo_file_name)[1]:
        #    self.photo_file_name = photo_file_name
        #else:
        #    raise ValueError("Wrong photofile")
        self.photo_file_name = photo_file_name
        #if carrying >= 0.0:
        #    self.carrying = carrying
        #else:
        #    raise ValueError("Wrong carrying value")
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
    
    def __repr__(self):
        return str(self.__dict__)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        if body_whl:
            whl = list(map(float, body_whl.split(sep = 'x')))
            if len(whl) != 3:
                raise ValueError("Wrong weight/height/lenght data")
            self.body_width, self.body_height, self.body_length = tuple(whl)
        else:
            self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) != 7:
                continue
            try:
                if row[0] == 'car':
                    car_list.append(Car(
                        row[1],
                        row[3],
                        float(row[5]), 
                        int(row[2])
                    ))
                elif row[0] == 'truck':
                    car_list.append(Truck(
                        row[1],
                        row[3], 
                        float(row[5]),
                        row[4]
                    ))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(
                        row[1], 
                        row[3], 
                        float(row[5]),
                        row[6]
                    ))
                else:
                    continue
            except Exception:
                continue
    return car_list


#print(get_car_list("week3_cars.csv"))