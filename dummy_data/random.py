#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import lorem
from random import uniform, randint, choice
from dummy_data.data import Folder, File


def random_structure(path, top_ceiling, levels):
    # create root
    folder = Folder(path, [])
    # create x subfolders and create x files
    rand = random(top_ceiling)

    for i in range(0, rand):
        rand_type = randint(0, 1)
        if (rand_type == 1 and levels > 0):
            item = random_structure("Folder " + str(i), top_ceiling, levels-1)
        else:
            text = lorem.text()
            title = choice(text.split())
            item = File(title + str(i) + ".txt", text)

        folder.content.append(item)

    return folder


def random(avg):
    rand = uniform(0, 1)
    rand = math.floor(rand*avg)
    return rand
