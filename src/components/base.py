"""
Base class for robot components with common operations.
"""

import cadquery as cq
from typing import Union, Tuple, List

class ComponentBase:
    def __init__(self):
        self.model = None
        
    def add_holes(self, 
                 workplane: cq.Workplane,
                 positions: List[Tuple[float, float]],
                 diameter: float,
                 depth: Union[float, str] = "thru") -> cq.Workplane:
        """Add holes at specified positions.
        
        Args:
            workplane: CadQuery workplane
            positions: List of (x, y) coordinates for holes
            diameter: Hole diameter
            depth: Hole depth or "thru" for through holes
            
        Returns:
            Modified workplane
        """
        for pos in positions:
            workplane = workplane.faces(">Z").workplane() \
                                .moveTo(pos[0], pos[1]) \
                                .hole(diameter, depth)
        return workplane
    
    def add_fillet(self,
                  workplane: cq.Workplane,
                  radius: float,
                  edges_selector: str = ">Z") -> cq.Workplane:
        """Add fillets to selected edges.
        
        Args:
            workplane: CadQuery workplane
            radius: Fillet radius
            edges_selector: Edge selector string
            
        Returns:
            Modified workplane
        """
        return workplane.edges(edges_selector).fillet(radius)
    
    def add_mounting_holes(self,
                         workplane: cq.Workplane,
                         width: float,
                         length: float,
                         hole_diameter: float,
                         edge_offset: float = 10.0) -> cq.Workplane:
        """Add mounting holes in corners.
        
        Args:
            workplane: CadQuery workplane
            width: Width of the part
            length: Length of the part
            hole_diameter: Diameter of mounting holes
            edge_offset: Offset from edges
            
        Returns:
            Modified workplane
        """
        positions = [
            (length/2 - edge_offset, width/2 - edge_offset),
            (length/2 - edge_offset, -width/2 + edge_offset),
            (-length/2 + edge_offset, width/2 - edge_offset),
            (-length/2 + edge_offset, -width/2 + edge_offset)
        ]
        return self.add_holes(workplane, positions, hole_diameter)
    
    def export_stl(self, filename: str) -> None:
        """Export the model to STL format.
        
        Args:
            filename: Output filename
        """
        if self.model is None:
            raise ValueError("No model to export")
        
        cq.exporters.export(self.model, filename)
    
    def show(self) -> None:
        """Display the model in CQ-editor."""
        if self.model is None:
            raise ValueError("No model to display")
        
        show_object(self.model)  # type: ignore # This is defined in CQ-editor 