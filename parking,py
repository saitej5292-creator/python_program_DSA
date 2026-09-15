class Vehicle:
    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type


class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def park(self, vehicle):
        if self.vehicle is None and self.spot_type == vehicle.vehicle_type:
            self.vehicle = vehicle
            return True
        return False

    def remove(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle


class ParkingLot:
    def __init__(self):
        self.spots = [
            ParkingSpot(1, "Car"),
            ParkingSpot(2, "Car"),
            ParkingSpot(3, "Bike")
        ]

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                print(f"{vehicle.number} parked at Spot {spot.spot_id}")
                return
        print("No suitable parking spot available.")

    def remove_vehicle(self, spot_id):
        for spot in self.spots:
            if spot.spot_id == spot_id:
                vehicle = spot.remove()
                if vehicle:
                    print(f"{vehicle.number} removed from Spot {spot_id}")
                else:
                    print("Spot is already empty.")


parking = ParkingLot()
car1 = Vehicle("TN38AB1234", "Car")
bike1 = Vehicle("TN38XY5678", "Bike")

parking.park_vehicle(car1)
parking.park_vehicle(bike1)
parking.remove_vehicle(1)