# this is a file for helper functions
import hyperspy.api as hs
import numpy as np
import pandas as pd


def elementlines(element, all=True, give_return=False):
    """
    Given an element, return the x-ray lines using the HyperSpy library.

    Parameters
    ----------
    element : str
        Element symbol
    all : bool, optional
        Give all lines or jst La, Lb, Ka, and Kb, by default True
    """
    d = hs.material.elements[element].Atomic_properties.Xray_lines.as_dictionary()
    lines = []
    for key in d.keys():
        if all:
            lines.append([d[key]["energy (keV)"], key])
        if key == "La" or key == "Lb" or key == "Ka" or key == "Kb":
            lines.append([d[key]["energy (keV)"], key])
    lines.sort(key=lambda x: x[0])
    if give_return:
        return lines
    print(element)
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
    pd.DataFrame
        df of closest x-ray lines, closest first
    """
    lines = hs.eds.get_xray_lines_near_energy(energy)
    energies = [theoretical_energy(line) for line in lines]
    df = pd.DataFrame({'line': lines, 'energy [keV]': energies})
    df.set_index('line', inplace=True)
    df['delta [eV]'] = (df['energy [keV]'] - energy) * 1000
    return df



def theoretical_energy(line):
    """
    Return the theoretical energy of a given x-ray line.

    Parameters
    ----------
    line : str
        X-ray line, e.g. 'Ga_Ka'

    Returns
    -------
    float
        Energy of the x-ray line in keV
    """
    element = line.split('_')[0]
    line_name = line.split('_')[1]
    return hs.material.elements[element]['Atomic_properties']['Xray_lines'][line_name]['energy (keV)']