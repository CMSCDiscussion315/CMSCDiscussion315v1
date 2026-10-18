# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Implementation

### Design Approach & Architecture
This program implements an object-oriented taxonomy for handling asset tracking across complex hardware grids:
* **Parent Class (AerialVehicle)**: Encapsulates primitive tracking parameters including standard identification metrics (vehicle_id), battery statuses (battery_pct), and structural telemetry logs (logs).
* **Child Class (PackageDeliveryDrone)**: Models functional expansion. It inherits baseline flight tracking definitions from the parent using super().__init__(), adds unique physical cargo boundaries (max_payload, current_payload), and overrides the telemetry monitoring mechanics (monitor_systems) to track cargo capacities in real time without replicating core code.

### Namespace & Scope Analysis
* **Class Namespace**: Variables declared inside the class block (like `fleet_type`) remain bound to the class dictionary structure and act as shared layout scopes across all instantiated objects. When modified globally via `AerialVehicle.fleet_type`, all instances reflect the change via the lookup chain.
* **Instance Namespace**: Unique attributes declared using `self` belong explicitly to that targeted instance object context. Overriding a class variable using `drone_craft.fleet_type = value` injects that key directly into the instance's unique dictionary (`__dict__`). This shadows the class default locally without altering the global class blueprint.

### Memory Allocation: Shallow vs. Deep Copying
* **Shallow Copy (copy.copy)**: Clones the outer structural frame of the object but copies raw *memory references* to nested data blocks (like the mutable logs list). Mutating a log statement on the original drone breaks structural boundaries, leaking edits straight into the shallow clone because they share a pointer.
* **Deep Copy (copy.deepcopy)**: Recursively copies both the frame *and* its nested contents into entirely fresh memory addresses. This provides strict data encapsulation and isolates state environments completely, preventing cross-object data contamination.

----------------------------------------------------

## Verified Runtime Output

    1. Testing Objects and Inheritance ---
[AV-100] Battery: 95.0% | Status: NOMINAL
[DEL-402] Battery: 88.5% | Status: NOMINAL | Payload: 0.0/15.0 kg

    2. Namespace Demonstration ---
Class namespace fleet_type: Autonomous Fleet
Base craft namespace fleet_type: Autonomous Fleet
Drone craft namespace fleet_type: Autonomous Fleet

Modifying AerialVehicle.fleet_type at the class level...
Base craft fleet_type (updated via class lookup): Global Drone Net
Drone craft fleet_type (updated via class lookup): Global Drone Net

Modifying fleet_type directly on drone_craft instance...
Base craft fleet_type (unchanged class level): Global Drone Net
Drone craft fleet_type (shadowed local level): Express Delivery Only

    3. Shallow Copy vs. Deep Copy Demonstration ---
Original drone logs before update: ['System Booted']

Appending 'GPS Lock Acquired' directly to drone_craft.logs...
Original drone logs: ['System Booted', 'GPS Lock Acquired']
Shallow copy logs (references leaked): ['System Booted', 'GPS Lock Acquired']
Deep copy logs (completely isolated): ['System Booted']