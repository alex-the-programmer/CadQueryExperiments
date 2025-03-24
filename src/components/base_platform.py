"""
Base platform component of the robot.
"""

import cadquery as cq
from typing import Tuple
import sys
import os

# Add parent directory to path to import config and base
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *
from components.base import ComponentBase

class BasePlatform(ComponentBase):
    def __init__(self):
        super().__init__()
        self.length = PLATFORM_LENGTH
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT
        self.wall_thickness = WALL_THICKNESS
        self.base_thickness = BASE_THICKNESS
        
    def create_base_plate(self) -> cq.Workplane:
        """Create the base plate with mounting holes."""
        return (cq.Workplane("XY")
                .box(self.length, self.width, self.base_thickness)
                .faces(">Z").workplane()
                .rect(self.length - 2*self.wall_thickness,
                     self.width - 2*self.wall_thickness,
                     forConstruction=True))
    
    def create_walls(self, base: cq.Workplane) -> cq.Workplane:
        """Create walls around the base plate."""
        return (base.faces(">Z").workplane()
                .rect(self.length, self.width)
                .rect(self.length - 2*self.wall_thickness,
                     self.width - 2*self.wall_thickness)
                .extrude(self.height - self.base_thickness))
    
    def create_battery_compartment(self, base: cq.Workplane) -> cq.Workplane:
        """Create the battery compartment."""
        compartment_pos = (-self.length/4, 0)  # Place in the rear quarter
        return (base.faces(">Z").workplane()
                .moveTo(*compartment_pos)
                .box(BATTERY_LENGTH + 2*TOLERANCE,
                    BATTERY_WIDTH + 2*TOLERANCE,
                    BATTERY_HEIGHT,
                    centered=True))
    
    def create_wheel_cutouts(self, base: cq.Workplane) -> cq.Workplane:
        """Create cutouts for the drive wheels."""
        wheel_positions = [(0, self.width/2), (0, -self.width/2)]
        cutout_width = DRIVE_WHEEL_WIDTH + 2*TOLERANCE
        cutout_height = DRIVE_WHEEL_DIAMETER/3  # Only cut out bottom third
        
        for pos in wheel_positions:
            base = (base.faces(">Z").workplane()
                   .moveTo(pos[0], pos[1])
                   .box(cutout_width,
                       DRIVE_WHEEL_DIAMETER + 2*TOLERANCE,
                       cutout_height,
                       centered=True))
        return base
    
    def create_caster_mounts(self, base: cq.Workplane) -> cq.Workplane:
        """Create mounting points for caster wheels."""
        mount_positions = [(self.length/2 - 50, 0),   # Front
                         (-self.length/2 + 50, 0)]    # Back
        mount_size = (80, 80, 10)  # Width, Length, Height
        
        for pos in mount_positions:
            base = (base.faces(">Z").workplane()
                   .moveTo(pos[0], pos[1])
                   .box(*mount_size, centered=True))
            # Add mounting holes
            hole_positions = [
                (pos[0] - mount_size[0]/4, pos[1] - mount_size[1]/4),
                (pos[0] - mount_size[0]/4, pos[1] + mount_size[1]/4),
                (pos[0] + mount_size[0]/4, pos[1] - mount_size[1]/4),
                (pos[0] + mount_size[0]/4, pos[1] + mount_size[1]/4)
            ]
            base = self.add_holes(base, hole_positions, HOLE_DIAMETER)
        return base
    
    def create_lift_rail_mount(self, base: cq.Workplane) -> cq.Workplane:
        """Create mounting point for the lift rail."""
        mount_width = LIFT_RAIL_WIDTH + 2*WALL_THICKNESS
        mount_length = 100  # Length of mounting area
        mount_height = 20   # Height above base platform
        
        return (base.faces(">Z").workplane()
                .moveTo(0, 0)  # Center of platform
                .box(mount_length, mount_width, mount_height, centered=True))
    
    def build(self) -> None:
        """Build the complete base platform."""
        # Create base structure
        base = self.create_base_plate()
        base = self.create_walls(base)
        
        # Add features
        base = self.create_battery_compartment(base)
        base = self.create_wheel_cutouts(base)
        base = self.create_caster_mounts(base)
        base = self.create_lift_rail_mount(base)
        
        # Add mounting holes and fillets
        base = self.add_mounting_holes(base, self.width, self.length, HOLE_DIAMETER)
        base = self.add_fillet(base, FILLET_RADIUS)
        
        self.model = base

if __name__ == "__main__":
    # Create and show the base platform
    platform = BasePlatform()
    platform.build()
    platform.show() 