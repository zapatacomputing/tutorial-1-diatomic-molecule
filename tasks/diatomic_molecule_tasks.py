import json
from diatomicmolecule import create_diatomic_molecule_geometry


def create_diatomic_molecule(species1, species2, bond_length):
    geometry = create_diatomic_molecule_geometry(species1, species2, bond_length)
    geometry["schema"] = "molecular_geometry"
    with open("molecule.json", "w") as f:
        f.write(json.dumps(geometry))
