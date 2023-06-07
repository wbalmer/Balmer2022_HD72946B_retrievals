import species
import pandas as pd

#################################################
### Add target and data to species.Database() ###
#################################################

species.SpeciesInit()

database = species.Database()

database.delete_data('objects/HD 72946 B')
Hphot = pd.read_csv('HD72946_SPHEREH_fluxcal_photometry_revised.dat', sep='\t', names=['l','f','fe'])
database.add_object('HD 72946 B',
                    parallax=(38.9809,0.0412), #gaia edr3
                    flux_density={'Paranal/SPHERE.IRDIS_D_H23_2':(Hphot['f'][0], Hphot['fe'][0]),
                                  'Paranal/SPHERE.IRDIS_D_H23_3':(Hphot['f'][1], Hphot['fe'][1])},
                    spectrum={'SPHERE':('HD72946_SPHEREYJ_fluxcal_spectrum_revised.dat', None, 50.),
                              'GRAVITY':(
                                         'HD72946B_GRAVITYK_fluxcal_spectrum_combined_cropped.fits',
                                         'HD72946B_GRAVITYK_fluxcal_spectrum_combined_cropped.fits',
                                         500.)},
                   )
