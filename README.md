# Differential Drive Robot Platform

This project contains the CAD models for a differential drive robot platform using CadQuery. The robot consists of:

1. Base Platform

   - Houses batteries
   - Two large driving wheels in the middle
   - Two coaster wheels (front and back)
   - Total length: 1.5ft (457.2mm)

2. Lifting Platform
   - Mounted on a rail in the middle of the base platform
   - Can be raised from base level to human height
   - Includes mounting points for robotic arm (future)
   - Includes tray for object placement

## Specifications

- Maximum load capacity: 3 lbs (1.36 kg)
- 3D printing material: PLA
- Maximum print bed size: 220mm x 220mm

## Project Structure

```
.
├── src/
│   └── components/     # Individual component models
├── tests/             # Test files
└── docs/              # Documentation
```

## Dependencies

- Python 3.11
- CadQuery 2.4
- Additional dependencies in requirements.txt

## Usage

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Run CQ-editor:

```bash
cq-editor
```

3. Open the desired component file from the src/components directory.

## License

MIT License
