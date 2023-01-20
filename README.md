# sem-eds-qc

SEM EDS quality control program, in Jupyter Notebook

## Introduction

This repository is a part of my master's thesis, where I'm trying to improve SEM EDS.
This QC program is supposed to identify the status of a SEM EDS setup, so that the input parameters to a SEM EDS analysis can be adjusted accordingly.

As of 17.01.23, the idea is to calculate the following parameters:

- calibration (dispersion and offset)
- total counts (troughput)
- bg total counts
- fiori bg
- duane-hunt (when it goes to zero)
- energy resolution, Mn Ka (also at different DT?) (find formula from Egerton)
- peak positions
- peak shape / peak tailing (ICC)
- contamination / ice (K/L, how it change over time)
- Si Ka peak from detector
- how good the fit is - whole fit - low and high E seperated - bg fit
  _{ if using eg. NiO from Ted Pella, with possible stray signals }_
- source of stray radiation
- amount of stray
  _{ needs multiple spectra with different I_beam }_
- count rate linearity
  - increase I (increase incoming e) should be linear with detection count
- dispersion and E-res as a function of probe I (more counts, but the params should be constant)
- use X^2 with M spectra taken at time t/M to find the best settings [Ritchie, 2022]

These parameters are selected from the literature, primarily the DTSA-II QC program described in Goldstein et al. (2018), and also some of the routines used for TEM EDS QC (e.g. described in the Ted Pella information sheet on their NiOx sample).

## Idea

- One notebook taking in a spectrum, and calculating the parameters
  - The calculations must adapt to the materials (e.g. the NiOx sample from Ted Pella can give stray signals from Mo, while a pure Cu sample will not)
  - Give out all the parameters in a table, eventually make a plot
  - Warn about bad parameters (needs to be defined)
  - Save the parameters to a file
    - Both the parameters and the settings for the spectrum (also the spectrum?)
- Another notebook which take in multiple saved health checks (or raw spectra? I think not), and give some statistical overview of the setup.
  - Average values, change over time, last 10, etc.
  - Plot the parameters over time
  - Warn about specific parameters (like how a K/L change can indicate contamination)
  - Also compare the health check done with different settings and/or different materials, but at the same time

## Requirements for the spectrum files

The information needed to do proper QC would be:

- The spectrum
- V_acc, I_beam, time live, time real (or DT?), name of detector, material, working distance, angle(?), more detector properties(?), eventual contextual information, some thing else?

## Future work

After making a satisfactory QC program, I will try find a good standard sample for SEM EDS, which fills the following criteria:

- The sample should be cheap, and easily avaliable (e.g. not the Ted Pella NiOx sample)
- Must have peaks at low and high energy (e.g. fro 30 kV: round 10, 7-8, 5-6 kV, and lower E)
  - NB! Overvoltage
- Not magnetic
- Possibility for stray radiation as the TEM grids?
- Think about the potential users (semiconductor industry, mineralogy, biology, etc.)

Goldstein et al. (2018) and AZtec suggest Cu, which is good for calibrating dispersion, but not all the checks.
TED Pella suggests NiOx, which is good for stray radiation, but is not easily avaliable and is expensive. It is also a TEM sample.

Could put Cu on a GaAs wafer, cut it and look at the cross section. Then the strays can be detected, and the sample is cheap and easy to get.
GaAs, Cu and Ti/Sb would get the wanted peaks.

One possible outcome from this notebooks is an implementation in HyperSpy, but that depends on both the outcome of the thesis and the need for a QC program in HyperSpy.

## Data

The data in the `data/Skomedal_2022-03-23` folder is taken by Mari Skomedal as a part of her master's thesis. The data is from the SU9000 S(T)EM, where the different files on 30 kV are taken on different tilts (says Ton).
