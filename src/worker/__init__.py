#!/usr/bin/env python2

from __future__ import absolute_import

from .interface import VisualCompass as VisualCompassInterface
from .binary import BinaryCompass
from .multiple import MultipleCompass


class VisualCompass(VisualCompassInterface):
    def __init__(self, config):
        self.compass = None
        self.compassType = None
        self.compassClasses = {
            "binary": BinaryCompass,
            "multiple": MultipleCompass
        }

        self.set_config(config)

    def process_image(self, image, resultCB=None, debugCB=None):
        return self.compass.process_image(image, resultCB, debugCB)

    def set_config(self, config):
        compass_type = config['compass_type']
        if compass_type == self.compassType:
            self.compass.set_config(config)
        else:
            self.compassType = compass_type
            if compass_type not in self.compassClasses:
                raise AssertionError(self.compassType + ": Compass not available!")
            compass_class = self.compassClasses[self.compassType]
            self.compass = compass_class(config)

    def set_truth(self, angle, image):
        return self.compass.set_truth(angle, image)

    def get_side(self):
        return self.compass.get_side()







