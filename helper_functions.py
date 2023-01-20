# this is a file for helper functions
import hyperspy.api as hs
import numpy as np


def elementlines(element, all=True):
    """
    Given an element, return the x-ray lines using the HyperSpy library.

    Parameters
    ----------
    element : str
        Element symbol
    all : bool, optional
        Give all lines or jst La, Lb, Ka, and Kb, by default True
    """
    print(element)
    d = hs.material.elements[element].Atomic_properties.Xray_lines.as_dictionary()
    lines = []
    for key in d.keys():
        if all:
            lines.append([d[key]["energy (keV)"], key])
        if key == "La" or key == "Lb" or key == "Ka" or key == "Kb":
            lines.append([d[key]["energy (keV)"], key])
    lines.sort(key=lambda x: x[0])
    for line in lines:
        print(f"{line[1]:5} {line[0]:.4f}")


def nearestlines(energy):
    """
    Given an energy in keV, return the nearest x-ray lines using the HyperSpy library.

    Parameters
    ----------
    energy : float
        energy in keV

    Returns
    -------
    list
        list of closest x-ray lines, closest first
    """
    return hs.eds.get_xray_lines_near_energy(energy)


