"""#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dummy_data import print_data, create
from dummy_data.random import random_structure
from dummy_data.data import Folder, File

# Create User Tree
tree = Folder(
    "C:\\Test",
    [
        Folder(
            "Pasta1",
            [
                Folder("Pasta12"),
                File("F.txt", "0")
            ]
        ),
        Folder("Pasta2", []),
        File("Ficheiro.txt", "COiso e tal")
    ]
)

create(tree)

# Create random Tree
f = random_structure("C:\\Testtt", 10, 2)
print_data(f)
# create(f)
"""
