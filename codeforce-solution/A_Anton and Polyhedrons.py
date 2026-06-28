import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    face_map = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }
    
    polyhedrons = input_data[1:]
    total_faces = sum(face_map[name] for name in polyhedrons)
    
    print(total_faces)

if __name__ == '__main__':
    solve()
