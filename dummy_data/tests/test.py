"""#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ...dummy_data
from .dummy_data.Models import Folder, File

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
        Folder("Pasta2",[]),
        File("Ficheiro.txt", "COiso e tal")
    ]
)

dummy_data.print_data(tree)"""
