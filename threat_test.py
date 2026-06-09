from threat_engine import get_threat_level

objects = [
    "person",
    "car",
    "truck",
    "motorcycle",
    "chair"
]

for obj in objects:
    threat = get_threat_level(obj)
    print(f"{obj} -> {threat}")