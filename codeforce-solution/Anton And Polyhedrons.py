import sys

# Read all lines from standard input for fast I/O
input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    polyhedrons = input_data[1:]
    
    # Map each shape name to its number of faces
    faces_map = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }
    
    # Sum the faces for all polyhedrons in the collection
    total_faces = sum(faces_map[shape] for shape in polyhedrons)
    print(total_faces)
