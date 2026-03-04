from dataclasses import dataclass

@dataclass
class PersonDC:
    name: str
    age: int
p = PersonDC("nejemddine", "23")
print(p)