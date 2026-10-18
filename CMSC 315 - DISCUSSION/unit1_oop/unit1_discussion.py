"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""
import copy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.
class AerialVehicle:
    """Represents a standard base aerial device."""
    # Class-level variable (shared namespace attribute)
    fleet_type = "Autonomous Fleet"

    def __init__(self, vehicle_id: str, battery_pct: float, baseline_logs: list):
        self.vehicle_id = vehicle_id          # Instance variable
        self.battery_pct = battery_pct        # Instance variable
        self.logs = baseline_logs             # Mutable nested structure

    def monitor_systems(self) -> str:
        """Returns telemetry health data."""
        return f"[{self.vehicle_id}] Battery: {self.battery_pct}% | Status: NOMINAL"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.
class PackageDeliveryDrone(AerialVehicle):
    """Represents a specialized cargo delivery vehicle."""

    def __init__(self, vehicle_id: str, battery_pct: float, baseline_logs: list, max_payload: float):
        # Use super() to call the parent constructor
        super().__init__(vehicle_id, battery_pct, baseline_logs)
        # TODO: Add new attributes specific to child class
        self.max_payload = max_payload
        self.current_payload = 0.0

    def monitor_systems(self) -> str:
        base_status = super().monitor_systems()
        return f"{base_status} | Payload: {self.current_payload}/{self.max_payload} kg"

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.
def main():
    print("--- 1. Testing Objects and Inheritance ---")
    shared_log = ["System Booted"]

    base_craft = AerialVehicle("AV-100", 95.0, shared_log)
    drone_craft = PackageDeliveryDrone("DEL-402", 88.5, shared_log, 15.0)

    print(base_craft.monitor_systems())
    print(drone_craft.monitor_systems())

    # TODO 3:
    # Create a function that demonstrates class namespaces and instance namespaces.
    #
    # Your function should:
    # - Create at least two objects of the child class.
    # - Access a class variable through the class itself.
    # - Access the same class variable through an object.
    # - Add a new attribute to only one object after it is created.
    # - Display each object's namespace using __dict__.
    # - Display information about the class namespace.
    print("\n--- 2. Namespace Demonstration ---")
    print(f"Class namespace fleet_type: {AerialVehicle.fleet_type}")
    print(f"Base craft namespace fleet_type: {base_craft.fleet_type}")
    print(f"Drone craft namespace fleet_type: {drone_craft.fleet_type}")

    print("\nModifying AerialVehicle.fleet_type at the class level...")
    AerialVehicle.fleet_type = "Global Drone Net"
    print(f"Base craft fleet_type (updated via class lookup): {base_craft.fleet_type}")
    print(f"Drone craft fleet_type (updated via class lookup): {drone_craft.fleet_type}")

    print("\nModifying fleet_type directly on drone_craft instance...")
    drone_craft.fleet_type = "Express Delivery Only"
    print(f"Base craft fleet_type (unchanged class level): {base_craft.fleet_type}")
    print(f"Drone craft fleet_type (shadowed local level): {drone_craft.fleet_type}")

    # TODO 4:
    # Create a function that demonstrates shallow copying and deep copying.
    #
    # Requirements:
    # - Create an object that contains nested mutable data.
    # - Create a shallow copy.
    # - Create a deep copy.
    # - Modify the original object's nested data.
    # - Display the original object, shallow copy, and deep copy.
    # - Use comments to explain the difference between shallow and deep copying.
    print("\n--- 3. Shallow Copy vs. Deep Copy Demonstration ---")
    shallow_drone = copy.copy(drone_craft)
    deep_drone = copy.deepcopy(drone_craft)

    print(f"Original drone logs before update: {drone_craft.logs}")

    print("\nAppending 'GPS Lock Acquired' directly to drone_craft.logs...")
    drone_craft.logs.append("GPS Lock Acquired")

    print(f"Original drone logs: {drone_craft.logs}")
    print(f"Shallow copy logs (references leaked): {shallow_drone.logs}")
    print(f"Deep copy logs (completely isolated): {deep_drone.logs}")


if __name__ == "__main__":
    main()
