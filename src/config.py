"""
Configuration file containing common parameters for the robot platform.
All dimensions are in millimeters unless otherwise specified.
"""

# Platform dimensions
PLATFORM_LENGTH = 457.2  # 1.5ft in mm
PLATFORM_WIDTH = 300.0   # Reasonable width for stability
PLATFORM_HEIGHT = 100.0  # Base platform height

# Material thicknesses
WALL_THICKNESS = 4.0     # Standard wall thickness for 3D printing
BASE_THICKNESS = 5.0     # Thicker base for better support

# Wheel dimensions
DRIVE_WHEEL_DIAMETER = 100.0
DRIVE_WHEEL_WIDTH = 30.0
CASTER_WHEEL_DIAMETER = 50.0
CASTER_WHEEL_WIDTH = 20.0

# Battery compartment
BATTERY_LENGTH = 150.0   # Example battery size
BATTERY_WIDTH = 100.0
BATTERY_HEIGHT = 50.0

# Lifting mechanism
LIFT_RAIL_WIDTH = 40.0
LIFT_RAIL_HEIGHT = 1000.0  # Maximum height (approximately human height)
LIFT_PLATFORM_WIDTH = 250.0
LIFT_PLATFORM_LENGTH = 300.0

# Load specifications
MAX_LOAD_KG = 1.36  # 3 lbs

# Common parameters
FILLET_RADIUS = 3.0  # Standard fillet radius for edges
HOLE_DIAMETER = 5.0  # Standard hole diameter for M5 screws
TOLERANCE = 0.2      # Standard tolerance for moving parts 