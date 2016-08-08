#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import lorem
import random
from dummy_data.data import Folder, File


def random_structure(path, top_ceiling, levels):
    # create root
    folder = Folder(path, [])
    # create x subfolders and create x files
    rand = random_value(top_ceiling)

    for i in range(0, rand):
        rand_type = random.randint(0, 1)
        if (rand_type == 1 and levels > 0):
            item = random_structure("Folder " + str(i), top_ceiling, levels-1)
        else:
            text = lorem.text()
            title = random.choice(text.split())
            item = File(title + str(i) + ".txt", text)

        folder.content.append(item)

    return folder


def random_value(avg):
    rand = random.uniform(0, 1)
    rand = math.floor(rand*avg)
    print(rand)
    return int(rand)
