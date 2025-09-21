"""
ARBEIDSKRAV 1 i PY1010.
Programmet skal regne ut årlige kostnader for elbil og bensinbil, samt 
differansen.

Silje Marie Andreassen (silje@sesela.no)
Oppdatert: 2025 09 21
"""

Elbil = 5000 + (8.38*365) + (10000*0.2*2) + (0.1*10000)   #regner ut årlige kostnader for elbil
print("Årlige kostnader elbil:",Elbil)                    #viser resultatet
Bensin = 7500 + (8.38*365) + (10000*1) + (0.3*10000)      #regner ut årlige kostnader for bensinbil
print("Årlige kostnader bensinbil:",Bensin)               #viser resultatet

print("Differanse:",Bensin-Elbil)                         #regner ut og viser differansen

