---
title: 'The Magnetometer Family Tree'
excerpt: 'A history of spacecraft magnetometers, tracing missions, sensor types, and boom designs from early lunar exploration to modern planetary missions.'
date: 2026-10-05
modified: "2026-10-05T19:59:39+02:00"
permalink: /posts/2026/10/mag-family-tree/
tags:
  - magnetometers
  - instrument genealogy
---

# Introduction

Think of the magnetic field at a given point in space as an arrow: its length represents the field's strength, and the way it points represents the field's direction. A **vector magnetometer** measures the field's components along three perpendicular axes, usually called x, y, and z. Together, these measurements tell us both how strong the field is and which way it points. A **scalar magnetometer** measures only the total field strength, giving us the arrow's length without its direction. We can also calculate that scalar strength from vector measurements by squaring the three components, adding them together, and taking the square root, as shown below.

<figure style="max-width: 480px;">
  <img src="{{ '/images/generic_vector_rep.png' | relative_url }}" alt="A magnetic field vector shown as a red arrow on three perpendicular axes labeled Bx, By, and Bz, with its magnitude calculated as the square root of Bx squared plus By squared plus Bz squared" width="480">
  <figcaption>The arrow represents the magnetic field vector; its length is the scalar field strength.</figcaption>
</figure>

# Methods

Vector and scalar describe what a magnetometer measures and the instrument type describes how it makes that measurement. Some instruments sense how a magnetic field affects a material, while others detect an electrical signal or the behavior of tiny magnetic moments inside atoms. Here are a few common techniques.

## Vector measurements

- **Fluxgate magnetometers** use coils to repeatedly magnetize a small magnetic core in opposite directions. The surrounding field makes the core's response uneven, and the instrument turns that imbalance into a measurement along one axis. Three perpendicular sensing axes give us the full vector, including steady fields and slow changes.

- **Search-coil magnetometers**, also called induction magnetometers, measure the voltage produced when a changing magnetic field passes through a coil of wire. Three perpendicular coils measure the changing vector components. These instruments are useful for detecting magnetic waves, but a stationary coil cannot measure a perfectly steady field.

- **Magnetoresistive magnetometers** use materials whose electrical resistance changes in response to a magnetic field. The instrument reads that change to measure a field component. Sensing elements arranged along different axes can provide vector measurements in a compact package.

- **SQUID magnetometers** use superconducting loops: materials cooled until they carry electrical current without resistance. A magnetic field passing through a sensing loop changes the instrument's electrical response, allowing it to detect very weak fields. Loops oriented along different axes can measure vector components, although the instrument needs cooling to work.

## Scalar measurements

- **Proton-precession magnetometers** contain a liquid rich in hydrogen, such as water. A magnetic pulse temporarily aligns the magnetic moments of the hydrogen nuclei, or protons. After the pulse ends, those moments wobble around the surrounding field like spinning tops. The wobble rate, called the precession frequency, tells us the total field strength.

- **Overhauser magnetometers** also measure proton-precession frequency, but use radio waves and special molecules to transfer magnetic alignment from electrons to protons. This strengthens the proton signal without needing the strong magnetic pulse used by a conventional proton-precession instrument. The result is still a scalar measurement.

- **Optically pumped magnetometers** use light to prepare atoms in a vapor, such as cesium, potassium, or helium, so their magnetic moments respond together. The instrument detects a magnetic resonance through changes in the light passing through the vapor. The resonance frequency tells us the total field strength. Some designs can also recover vector components by applying known magnetic fields and observing how the measurement changes.

# The Lost Art of Making Ring Cores

Some branches of the magnetometer family tree share the same stock of magnetic material. Many fluxgate sensors use a ring core made from thin ferromagnetic foil, whose intrinsic magnetic noise limits the instrument's sensitivity.[^miles-2019]

Many instruments have relied on Infinetics S1000 ring cores, which went out of production in 1996. Their manufacturing process grew out of military research in the 1960s and was insufficiently documented to reproduce their performance. Remarkably, virtually all the permalloy used in North American fluxgates appears to have come from a single batch, likely made by the Hamilton Watch Company around 1969. The alloy contained 6% molybdenum, 81.3% nickel, and the remainder iron.[^miles-2019]

The resulting instruments kept working, but the supply of new cores did not keep growing. By 2021, NASA reported that stockpiles were so depleted that some providers were considering dismantling old flight-spare hardware to recover its cores. The manufacturing knowledge had been lost to the civilian community, leaving new missions dependent on a shrinking supply of decades-old components.[^nasa-ring-cores-2021]

Researchers including David Miles and B. Barry Narod published a replacement process: make a new alloy, cold-roll it into foil, insulate it, wind it around a supporting ring, and heat-treat the assembly. Their 2019 study demonstrated new cores with magnetic noise comparable to many legacy S1000 cores, restoring a manufacturing capability needed by future instruments.[^miles-2019]

# Spacecraft Missions

> **Authors Note:** Boom lengths are hand-wavey! In some cases, the reported value is the approximate distance between the magnetometer sensor and the spacecraft center rather than the physical boom length.

| Mission | Target / environment | Launch year | Number and type | Boom length / location |
|---|---|---:|---|---|
| Luna 1[^nasa-luna-1] | Lunar flyby / heliocentric | 1959 | 1 triaxial fluxgate | Spacecraft-mounted |
| Luna 10[^dolginov-1966] | Lunar orbit | 1966 | 1 triaxial fluxgate | Spacecraft-mounted |
| Explorer 35[^ness-1967] | Lunar orbit | 1967 | 2 triaxial fluxgates | GSFC sensor: 2.2 m from spin axis |
| Pioneer 10[^smith-1975] | Jupiter / interplanetary | 1972 | 1 triaxial helium (HVM) | \\(\sim 6.5\\) m from spacecraft center |
| Pioneer 11[^acuna-1973]<sup>,</sup>[^smith-1975] | Jupiter and Saturn | 1973 | 2: 1 triaxial helium (HVM) + 1 triaxial fluxgate (FGM) | HVM: \\(\sim 6.5\\) m from spacecraft center; FGM: experiment platform |
| Voyager 1/2[^miller-1979] | Outer planets / heliosphere | 1977 | 4 triaxial fluxgates (2 low-field + 2 high-field) | 13 m |
| AMPTE-CCE[^potemra-1985] | Geospace | 1984 | 2 triaxial fluxgates | 2.3 m |
| AMPTE-IRM[^luhr-1985] | Geospace | 1984 | 1 triaxial fluxgate | 2 m |
| AMPTE-UKS[^southwood-1985] | Geospace | 1984 | 1 triaxial fluxgate | 1 m |
| Giotto[^neubauer-1986]<sup>,</sup>[^neubauer-1987] | Comet Halley / interplanetary | 1985 | 2: 1 triaxial fluxgate + 1 biaxial fluxgate | Antenna tripod: MAG-1 outboard, MAG-4 inboard; no boom |
| Galileo[^kivelson-1992] | Jupiter system | 1989 | 2 triaxial fluxgates | 11 m |
| Ulysses[^balogh-1992] | Solar polar orbit | 1990 | 2: 1 triaxial fluxgate + 1 triaxial helium | 5.6 m |
| Mars Global Surveyor[^acuna-2001] | Mars orbit | 1996 | 2 triaxial fluxgates | Solar-array tips; \\(\sim 2\\)–\\(2.5\\) m |
| NEAR Shoemaker[^lohr-1997] | Near-Earth asteroid Eros | 1996 | 1 triaxial fluxgate | \\(\sim 1\\) m |
| ACE[^smith-1998] | Sun–Earth L1 | 1997 | 2 triaxial fluxgates | 4.19 m from spacecraft center |
| Cassini[^dougherty-2004] | Saturn system | 1997 | 2: 1 triaxial fluxgate + 1 vector/scalar helium | 11 m |
| Lunar Prospector[^lin-1998] | Lunar orbit | 1998 | 1 triaxial fluxgate | 0.8 m; \\(\sim 2.6\\) m total structure |
| Cluster[^balogh-2001]<sup>,</sup>[^cornilleau-wehrlin-1997] | Geospace | 2000 | 3: 2 triaxial fluxgates (FGM) + 1 triaxial search-coil (STAFF) | 5 m radial booms: FGM and STAFF on opposite booms |
| MESSENGER[^anderson-2007] | Mercury orbit | 2004 | 1 triaxial fluxgate | 3.6 m |
| THEMIS[^auster-2008]<sup>,</sup>[^roux-2008] | Geospace / Lunar orbit | 2007 | 2: 1 triaxial fluxgate (FGM) + 1 triaxial search-coil (SCM) | 1.2 m FGM; 1 m SCM |
| SELENE/Kaguya[^shimizu-2008]<sup>,</sup>[^takahashi-2009] | Lunar orbit | 2007 | 1 triaxial fluxgate | 12 m |
| Juno[^connerney-2017] | Jupiter orbit | 2011 | 2 triaxial fluxgates | \\(\sim 10\\)–\\(12\\) m solar-array boom |
| MAVEN[^connerney-2015] | Mars orbit | 2013 | 2 triaxial fluxgates | 0.66 m boomlets; sensors \\(\sim 5.6\\) m from center |
| Swarm[^friis-christensen-2008]<sup>,</sup>[^leger-2015] | Earth orbit | 2013 | 3: 1 triaxial fluxgate + 2 scalar helium (primary + backup) | 4.3 m |
| MMS[^russell-2016]<sup>,</sup>[^le-contel-2016] | Geospace | 2015 | 3: 2 triaxial fluxgates (AFG + DFG) + 1 triaxial search-coil (SCM) | 5 m FGM booms; SCM 4 m along the AFG boom |
| BepiColombo/MPO-MAG[^heyner-2021] | Mercury orbit | 2018 | 2 triaxial fluxgates | 2.8–2.9 m |
| BepiColombo/Mio-MGF[^baumjohann-2020] | Mercury orbit | 2018 | 2 triaxial fluxgates | 4.4 m |
| Parker Solar Probe[^bale-2016] | Solar corona / heliosphere | 2018 | 3: 2 triaxial fluxgates + 1 triaxial search-coil | 3.5 m |
| Solar Orbiter[^horbury-2020] | Solar orbit | 2020 | 2 triaxial fluxgates | 4.4 m |
| KPLO/Danuri[^jo-2023] | Lunar orbit | 2022 | 3 triaxial fluxgates | 1.2 m |
| JUICE[^grasset-2013]<sup>,</sup>[^esa-2023] | Jupiter system | 2023 | 3: 2 triaxial fluxgates + 1 scalar rubidium | 10.6 m |
| Europa Clipper[^kivelson-2023] | Jovian system / Europa | 2024 | 3 triaxial fluxgates | 7.9–8.5 m |

Counts refer to sensor heads per spacecraft within the cited investigations, including backup heads.

Giotto's dust shield was designed to protect the spacecraft during its fast encounter with Comet Halley, so an exposed magnetometer boom was not included. Both sensors were mounted on the antenna tripod and comparing their readings helped assess interference from the spacecraft's own magnetic fields. Giotto carried two magnetometer sensor heads: the outboard triaxial MAG-1 and the inboard biaxial MAG-4. MAG-2 was the electronics box. The instrument paper's hardware inventory does not mention MAG-3, I have not found a satisfying source for why they were named this way.

## References

[^acuna-1973]: Acuña, M. H., & Ness, N. F. 1973, The Pioneer 11 high-field fluxgate magnetometer, NASA-TM-X-70467 (Greenbelt, MD: NASA GSFC), [NASA report](https://ntrs.nasa.gov/citations/19730022673)

[^acuna-2001]: Acuña, M. H., Connerney, J. E. P., Wasilewski, P., et al. 2001, Magnetic field of Mars: Summary of results from the aerobraking and mapping orbits, *J. Geophys. Res. Planets*, 106, 23403, [doi:10.1029/2000je001404](https://doi.org/10.1029/2000je001404)

[^anderson-2007]: Anderson, B. J., Acuña, M. H., Lohr, D. A., et al. 2007, The Magnetometer Instrument on MESSENGER, *Space Sci. Rev.*, 131, 417, [doi:10.1007/s11214-007-9246-7](https://doi.org/10.1007/s11214-007-9246-7)

[^auster-2008]: Auster, H. U., Glassmeier, K. H., Magnes, W., et al. 2008, The THEMIS Fluxgate Magnetometer, *Space Sci. Rev.*, 141, 235, [doi:10.1007/s11214-008-9365-9](https://doi.org/10.1007/s11214-008-9365-9)

[^bale-2016]: Bale, S. D., Goetz, K., Harvey, P. R., et al. 2016, The FIELDS Instrument Suite for Solar Probe Plus: Measuring the Coronal Plasma and Magnetic Field, Plasma Waves and Turbulence, and Radio Signatures of Solar Transients, *Space Sci. Rev.*, 204, 49, [doi:10.1007/s11214-016-0244-5](https://doi.org/10.1007/s11214-016-0244-5)

[^balogh-1992]: Balogh, A., Beek, T. J., Forsyth, R. J., et al. 1992, The magnetic field investigation on the Ulysses mission: Instrumentation and preliminary scientific results, *A&AS*, 92, 221, [instrument-team publication](https://www.imperial.ac.uk/space-and-atmospheric-physics/research/missions-and-projects/space-missions/ulysses/magnetometer/)

[^balogh-2001]: Balogh, A., Carr, C. M., Acuña, M. H., et al. 2001, The Cluster Magnetic Field Investigation: overview of in-flight performance and initial results, *Ann. Geophys.*, 19, 1207, [doi:10.5194/angeo-19-1207-2001](https://doi.org/10.5194/angeo-19-1207-2001)

[^baumjohann-2020]: Baumjohann, W., Matsuoka, A., Narita, Y., et al. 2020, The BepiColombo–Mio Magnetometer en Route to Mercury, *Space Sci. Rev.*, 216, 125, [doi:10.1007/s11214-020-00754-y](https://doi.org/10.1007/s11214-020-00754-y)

[^connerney-2015]: Connerney, J. E. P., Espley, J., Lawton, P., et al. 2015, The MAVEN Magnetic Field Investigation, *Space Sci. Rev.*, 195, 257, [doi:10.1007/s11214-015-0169-4](https://doi.org/10.1007/s11214-015-0169-4)

[^connerney-2017]: Connerney, J. E. P., Benn, M., Bjarno, J. B., et al. 2017, The Juno Magnetic Field Investigation, *Space Sci. Rev.*, 213, 39, [doi:10.1007/s11214-017-0334-z](https://doi.org/10.1007/s11214-017-0334-z)

[^cornilleau-wehrlin-1997]: Cornilleau-Wehrlin, N., Chauveau, P., Louis, S., et al. 1997, The Cluster Spatio-Temporal Analysis of Field Fluctuations (STAFF) Experiment, *Space Sci. Rev.*, 79, 107, [doi:10.1023/a:1004979209565](https://doi.org/10.1023/a:1004979209565)

[^dolginov-1966]: Dolginov, Sh. Sh., Eroshenko, E. G., Zhuzgov, L. N., & Pushkov, N. V. 1966, Magnetic field measurement in the Moon's neighbourhood at the Luna-10 satellite, *Dokl. Akad. Nauk SSSR*, 170, 574, [journal archive](https://www.mathnet.ru/php/archive.phtml?jrnid=dan&option_lang=eng&paperid=32585&wshow=paper)

[^dougherty-2004]: Dougherty, M. K., Kellock, S., Southwood, D. J., et al. 2004, The Cassini Magnetic Field Investigation, *Space Sci. Rev.*, 114, 331, [doi:10.1007/s11214-004-1432-2](https://doi.org/10.1007/s11214-004-1432-2)

[^esa-2023]: ESA 2023, Quantum-based MAGSCA aboard Juice (Paris: ESA), [instrument description](https://www.esa.int/ESA_Multimedia/Images/2023/11/Quantum-based_MAGSCA_aboard_Juice)

[^friis-christensen-2008]: Friis-Christensen, E., Lühr, H., Knudsen, D., & Haagmans, R. 2008, Swarm – An Earth Observation Mission investigating Geospace, *Adv. Space Res.*, 41, 210, [doi:10.1016/j.asr.2006.10.008](https://doi.org/10.1016/j.asr.2006.10.008)

[^grasset-2013]: Grasset, O., Dougherty, M. K., Coustenis, A., et al. 2013, JUpiter ICy moons Explorer (JUICE): An ESA mission to orbit Ganymede and to characterise the Jupiter system, *Planet. Space Sci.*, 78, 1, [doi:10.1016/j.pss.2012.12.002](https://doi.org/10.1016/j.pss.2012.12.002)

[^heyner-2021]: Heyner, D., Auster, H.-U., Fornaçon, K.-H., et al. 2021, The BepiColombo Planetary Magnetometer MPO-MAG: What Can We Learn from the Hermean Magnetic Field?, *Space Sci. Rev.*, 217, 52, [doi:10.1007/s11214-021-00822-x](https://doi.org/10.1007/s11214-021-00822-x)

[^horbury-2020]: Horbury, T. S., O’Brien, H., Carrasco Blazquez, I., et al. 2020, The Solar Orbiter magnetometer, *A&A*, 642, A9, [doi:10.1051/0004-6361/201937257](https://doi.org/10.1051/0004-6361/201937257)

[^jo-2023]: Jo, W., Jin, H., Park, H., et al. 2023, Korea Pathfinder Lunar Orbiter Magnetometer Instrument and Initial Data Processing, *J. Astron. Space Sci.*, 40, 199, [doi:10.5140/jass.2023.40.4.199](https://doi.org/10.5140/jass.2023.40.4.199)

[^kivelson-1992]: Kivelson, M. G., Khurana, K. K., Means, J. D., Russell, C. T., & Snare, R. C. 1992, The Galileo magnetic field investigation, *Space Sci. Rev.*, 60, 357, [doi:10.1007/bf00216862](https://doi.org/10.1007/bf00216862)

[^kivelson-2023]: Kivelson, M. G., Jia, X., Lee, K. A., et al. 2023, The Europa Clipper Magnetometer, *Space Sci. Rev.*, 219, 48, [doi:10.1007/s11214-023-00989-5](https://doi.org/10.1007/s11214-023-00989-5)

[^le-contel-2016]: Le Contel, O., Leroy, P., Roux, A., et al. 2016, The Search-Coil Magnetometer for MMS, *Space Sci. Rev.*, 199, 257, [doi:10.1007/s11214-014-0096-9](https://doi.org/10.1007/s11214-014-0096-9)

[^leger-2015]: Léger, J.-M., Jager, T., Bertrand, F., et al. 2015, In-flight performance of the Absolute Scalar Magnetometer vector mode on board the Swarm satellites, *Earth Planets Space*, 67, 57, [doi:10.1186/s40623-015-0231-1](https://doi.org/10.1186/s40623-015-0231-1)

[^lin-1998]: Lin, R. P., Mitchell, D. L., Curtis, D. W., et al. 1998, Lunar Surface Magnetic Fields and Their Interaction with the Solar Wind: Results from Lunar Prospector, *Science*, 281, 1480, [doi:10.1126/science.281.5382.1480](https://doi.org/10.1126/science.281.5382.1480)

[^lohr-1997]: Lohr, D. A., Zanetti, L. J., Anderson, B. J., et al. 1997, NEAR Magnetic Field Investigation, Instrumentation, Spacecraft Magnetics and Data Access, *Space Sci. Rev.*, 82, 255, [doi:10.1023/a:1005089829882](https://doi.org/10.1023/a:1005089829882)

[^luhr-1985]: Lühr, H., Klöcker, N., Ölschlägel, W., Häusler, B., & Acuña, M. 1985, The IRM Fluxgate Magnetometer, *IEEE Trans. Geosci. Remote Sens.*, GE-23, 259, [doi:10.1109/tgrs.1985.289524](https://doi.org/10.1109/tgrs.1985.289524)

[^miller-1979]: Miller, D. C. 1979, The Voyager magnetometer boom, in *The 12th Aerospace Mechanisms Symposium*, NASA-CP-2080 (Moffett Field, CA: NASA Ames Research Center), 51, [NASA proceedings](https://ntrs.nasa.gov/citations/19790013187)

[^miles-2019]: Miles, D. M., Ciurzynski, M., Barona, D., et al. 2019, Low-noise permalloy ring cores for fluxgate magnetometers, *Geosci. Instrum. Method. Data Syst.*, 8, 227, [doi:10.5194/gi-8-227-2019](https://doi.org/10.5194/gi-8-227-2019)

[^nasa-luna-1]: NASA Space Science Data Coordinated Archive n.d., Luna 1, spacecraft record 1959-012A (Greenbelt, MD: NASA GSFC), accessed 2026 October 5, [mission record](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=1959-012A)

[^nasa-ring-cores-2021]: NASA Science Editorial Team 2021, Rediscovering the Lost Art of Fluxgate Magnetometer Cores, July 6, [NASA technology highlight](https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/rediscovering-the-lost-art-of-fluxgate-magnetometer-cores/)

[^ness-1967]: Ness, N. F., Behannon, K. W., Scearce, C. S., & Cantarano, S. C. 1967, Early results from the magnetic field experiment on lunar Explorer 35, *J. Geophys. Res.*, 72, 5769, [doi:10.1029/jz072i023p05769](https://doi.org/10.1029/jz072i023p05769)

[^neubauer-1986]: Neubauer, F. M., Acuña, M. H., Burlaga, L. F., et al. 1986, The Giotto magnetic-field investigation, in *The Giotto Mission: Its Scientific Investigations* (Noordwijk: ESA), [ESA instrument paper](https://archives.esac.esa.int/psa/ftp/GIOTTO/GRE/GIO-C-GRE-3-RDR-HALLEY-V1.0/DOCUMENT/GIOMAG.PDF)

[^neubauer-1987]: Neubauer, F. M., Acuña, M. H., Burlaga, L. F., et al. 1987, The Giotto magnetometer experiment, *J. Phys. E: Sci. Instrum.*, 20, 714, [doi:10.1088/0022-3735/20/6/030](https://doi.org/10.1088/0022-3735/20/6/030)

[^potemra-1985]: Potemra, T. A., Zanetti, L. J., & Acuña, M. H. 1985, The AMPTE CCE Magnetic Field Experiment, *IEEE Trans. Geosci. Remote Sens.*, GE-23, 246, [doi:10.1109/tgrs.1985.289521](https://doi.org/10.1109/tgrs.1985.289521)

[^roux-2008]: Roux, A., Le Contel, O., Coillot, C., et al. 2008, The Search Coil Magnetometer for THEMIS, *Space Sci. Rev.*, 141, 265, [doi:10.1007/s11214-008-9455-8](https://doi.org/10.1007/s11214-008-9455-8)

[^russell-2016]: Russell, C. T., Anderson, B. J., Baumjohann, W., et al. 2016, The Magnetospheric Multiscale Magnetometers, *Space Sci. Rev.*, 199, 189, [doi:10.1007/s11214-014-0057-3](https://doi.org/10.1007/s11214-014-0057-3)

[^shimizu-2008]: Shimizu, H., Takahashi, F., Horii, N., et al. 2008, Ground calibration of the high-sensitivity SELENE lunar magnetometer LMAG, *Earth Planets Space*, 60, 353, [doi:10.1186/bf03352800](https://doi.org/10.1186/bf03352800)

[^smith-1998]: Smith, C. W., L'Heureux, J., Ness, N. F., et al. 1998, The ACE Magnetic Fields Experiment, *Space Sci. Rev.*, 86, 613, [doi:10.1023/a:1005092216668](https://doi.org/10.1023/a:1005092216668)

[^smith-1975]: Smith, E. J., Connor, B. V., & Foster, G. T., Jr. 1975, Measuring the magnetic fields of Jupiter and the outer solar system, *IEEE Trans. Magn.*, 11, 962, [doi:10.1109/tmag.1975.1058779](https://doi.org/10.1109/tmag.1975.1058779)

[^southwood-1985]: Southwood, D. J., Mier-Jedrzejowicz, W. A. C., & Russell, C. T. 1985, The Fluxgate Magnetometer for the AMPTE UK Subsatellite, *IEEE Trans. Geosci. Remote Sens.*, GE-23, 301, [doi:10.1109/tgrs.1985.289531](https://doi.org/10.1109/tgrs.1985.289531)

[^takahashi-2009]: Takahashi, F., Shimizu, H., Matsushima, M., et al. 2009, In-orbit calibration of the lunar magnetometer onboard SELENE (KAGUYA), *Earth Planets Space*, 61, 1269, [doi:10.1186/bf03352979](https://doi.org/10.1186/bf03352979)
