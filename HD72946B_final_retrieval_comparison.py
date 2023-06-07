################################################################################
# The purpose of this script is to generate the "experiment" associated        #
# with Balmer et al. (in prep.) on HD 72946 B: test what influence a dyn.      #
# prior and stellar abundances has on the retrieved clouds and P-T params.     #
# for an L-type, fully convective brown dwarf. Here we assume clouds by        #
# enforcing their presence near the photosphere with the log_tau_cloud         #
# and fe_mgsio3_ratio parameters. We implement scattering, AMR for the         #
# pressure grid, and A&M clouds composed of MgSiO3 and Fe Crystalline,         #
# DHS (irregular shape) grains.      2023/05/23, W. Balmer                     #
################################################################################
import os
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"
import species

species.SpeciesInit()

database = species.Database()

##########################################################
### Molliere P-T, A&M Cloud, No mass prior, Free abund ###
##########################################################

output_folder = 'HD72946B-am-molliere-nomass-freeab-multinest'

tag = 'HD72946B-am-molliere-nomass-freeab'

# retrieve = species.AtmosphericRetrieval(object_name='HD 72946 B',
#                                         line_species=['CO_all_iso_HITEMP', 'H2O_HITEMP', 'CH4', 'NH3', 'CO2', 'Na_allard', 'K_allard', 'TiO_all_Exomol', 'VO_Plez', 'FeH', 'H2S'],
#                                         cloud_species=['MgSiO3(c)_cd', 'Fe(c)_cd'],
#                                         scattering=True, #False if no clouds
#                                         output_folder=output_folder,
#                                         wavel_range=(0.9, 3.),
#                                         inc_spec=['SPHERE', 'GRAVITY'],
#                                         inc_phot=True,
#                                         pressure_grid='clouds',#'standard' 'clouds'
#                                         weights=None)
#
# retrieve.run_multinest(bounds={'logg': (2.5, 6.0),
#                                'c_o_ratio': (0.1, 1.5),
#                                'metallicity': (-3., 3.),
#                                'radius': (0.5, 2.),
#                                'fsed': (0., 20.),
#                                'log_kzz': (2., 15.),
#                                'sigma_lnorm': (1.2, 5.)},
#                                # 'mgsio3_fraction':(-3.,1.), # if clouds work w/out enforcement
#                                # 'fe_fracton':(-3.,1.), # if clouds work w/out enforcement
#                                'log_tau_cloud': (-2., 1.), # if result should be cloudy but is not, set this
#                                'fe_mgsio3_ratio': (-2., 2.), # if result ...
#                               },
#                        prior={},
#                        chemistry='equilibrium',
#                        quenching=None,
#                        pt_profile='molliere',
#                        fit_corr=['SPHERE'],
#                        n_live_points=1000, #500-1000
#                        resume=True, # if running on cluster/intermediate results
#                        plotting=False, # testing plots
#                        pt_smooth=0.)



database.add_retrieval(tag=tag,
                       output_folder=output_folder,
                       inc_teff=True)

#######################################################
### Molliere P-T, A&M Cloud, Mass prior, Free abund ###
#######################################################

output_folder = 'HD72946B-am-molliere-mass-freeab-multinest'

tag = 'HD72946B-am-molliere-mass-freeab'

# retrieve = species.AtmosphericRetrieval(object_name='HD 72946 B',
#                                         line_species=['CO_all_iso_HITEMP', 'H2O_HITEMP', 'CH4', 'NH3', 'CO2', 'Na_allard', 'K_allard', 'TiO_all_Exomol', 'VO_Plez', 'FeH', 'H2S'],
#                                         cloud_species=['MgSiO3(c)_cd', 'Fe(c)_cd'],
#                                         scattering=True, #False if no clouds
#                                         output_folder=output_folder,
#                                         wavel_range=(0.9, 3.),
#                                         inc_spec=['SPHERE', 'GRAVITY'],
#                                         inc_phot=True,
#                                         pressure_grid='clouds',#'standard' 'clouds'
#                                         weights=None)
#
# retrieve.run_multinest(bounds={'logg': (2.5, 6.0),
#                                'c_o_ratio': (0.1, 1.5),
#                                'metallicity': (-3., 3.),
#                                'radius': (0.5, 2.),
#                                'fsed': (0., 20.),
#                                'log_kzz': (2., 15.),
#                                'sigma_lnorm': (1.2, 5.)},
#                                # 'mgsio3_fraction':(-3.,1.), # if clouds work w/out enforcement
#                                # 'fe_fracton':(-3.,1.), # if clouds work w/out enforcement
#                                'log_tau_cloud': (-2., 1.), # if result should be cloudy but is not, set this
#                                'fe_mgsio3_ratio': (-2., 2.), # if result ...
#                               },
#                        prior={'mass':(69.5,0.5),
#                              },
#                        chemistry='equilibrium',
#                        quenching=None,
#                        pt_profile='molliere',
#                        fit_corr=['SPHERE'],
#                        n_live_points=1000, #500-1000
#                        resume=True, # if running on cluster/intermediate results
#                        plotting=False, # testing plots
#                        pt_smooth=0.)



database.add_retrieval(tag=tag,
                       output_folder=output_folder,
                       inc_teff=True)

#####################################################################
### Molliere P-T, A&M Cloud, No mass prior, Fix abund. to Stellar ###
#####################################################################

output_folder = 'HD72946B-am-molliere-nomass-fixab-multinest'

tag = 'HD72946B-am-molliere-nomass-fixab'

# retrieve = species.AtmosphericRetrieval(object_name='HD 72946 B',
#                                         line_species=['CO_all_iso_HITEMP', 'H2O_HITEMP', 'CH4', 'NH3', 'CO2', 'Na_allard', 'K_allard', 'TiO_all_Exomol', 'VO_Plez', 'FeH', 'H2S'],
#                                         cloud_species=['MgSiO3(c)_cd', 'Fe(c)_cd'],
#                                         scattering=True, #False if no clouds
#                                         output_folder=output_folder,
#                                         wavel_range=(0.9, 3.),
#                                         inc_spec=['SPHERE', 'GRAVITY'],
#                                         inc_phot=True,
#                                         pressure_grid='clouds',#'standard' 'clouds'
#                                         weights=None)
#
# retrieve.run_multinest(bounds={'logg': (2.5, 6.0),
#                                'c_o_ratio': (0.512, 0.047), # from stellar analysis
#                                'metallicity': (0.036, 0.023), # from stellar analysis
#                                'radius': (0.5, 2.),
#                                'fsed': (0., 20.),
#                                'log_kzz': (2., 15.),
#                                'sigma_lnorm': (1.2, 5.)},
#                                # 'mgsio3_fraction':(-3.,1.), # if clouds work w/out enforcement
#                                # 'fe_fracton':(-3.,1.), # if clouds work w/out enforcement
#                                'log_tau_cloud': (-2., 1.), # if result should be cloudy but is not, set this
#                                'fe_mgsio3_ratio': (-2., 2.), # if result ...
#                               },
#                        prior={},
#                        chemistry='equilibrium',
#                        quenching=None,
#                        pt_profile='molliere',
#                        fit_corr=['SPHERE'],
#                        n_live_points=1000, #500-1000
#                        resume=True, # if running on cluster/intermediate results
#                        plotting=False, # testing plots
#                        pt_smooth=0.)



database.add_retrieval(tag=tag,
                       output_folder=output_folder,
                       inc_teff=True)


#####################################################################
### Molliere P-T, A&M Cloud, No mass prior, Fix abund. to Stellar ###
#####################################################################

output_folder = 'HD72946B-am-molliere-nomass-fixab-multinest'

tag = 'HD72946B-am-molliere-nomass-fixab'

# retrieve = species.AtmosphericRetrieval(object_name='HD 72946 B',
#                                         line_species=['CO_all_iso_HITEMP', 'H2O_HITEMP', 'CH4', 'NH3', 'CO2', 'Na_allard', 'K_allard', 'TiO_all_Exomol', 'VO_Plez', 'FeH', 'H2S'],
#                                         cloud_species=['MgSiO3(c)_cd', 'Fe(c)_cd'],
#                                         scattering=True, #False if no clouds
#                                         output_folder=output_folder,
#                                         wavel_range=(0.9, 3.),
#                                         inc_spec=['SPHERE', 'GRAVITY'],
#                                         inc_phot=True,
#                                         pressure_grid='clouds',#'standard' 'clouds'
#                                         weights=None)
#
# retrieve.run_multinest(bounds={'logg': (2.5, 6.0),
#                                'c_o_ratio': (0.512, 0.047), # from stellar analysis
#                                'metallicity': (0.036, 0.023), # from stellar analysis
#                                'radius': (0.5, 2.),
#                                'fsed': (0., 20.),
#                                'log_kzz': (2., 15.),
#                                'sigma_lnorm': (1.2, 5.)},
#                                # 'mgsio3_fraction':(-3.,1.), # if clouds work w/out enforcement
#                                # 'fe_fracton':(-3.,1.), # if clouds work w/out enforcement
#                                'log_tau_cloud': (-2., 1.), # if result should be cloudy but is not, set this
#                                'fe_mgsio3_ratio': (-2., 2.), # if result ...
#                               },
#                        prior={},
#                        chemistry='equilibrium',
#                        quenching=None,
#                        pt_profile='molliere',
#                        fit_corr=['SPHERE'],
#                        n_live_points=1000, #500-1000
#                        resume=True, # if running on cluster/intermediate results
#                        plotting=False, # testing plots
#                        pt_smooth=0.)



database.add_retrieval(tag=tag,
                       output_folder=output_folder,
                       inc_teff=True)


##################################################################
### Molliere P-T, A&M Cloud, Mass prior, Fix abund. to Stellar ###
##################################################################

output_folder = 'HD72946B-am-molliere-mass-fixab-multinest'

tag = 'HD72946B-am-molliere-mass-fixab'

# retrieve = species.AtmosphericRetrieval(object_name='HD 72946 B',
#                                         line_species=['CO_all_iso_HITEMP', 'H2O_HITEMP', 'CH4', 'NH3', 'CO2', 'Na_allard', 'K_allard', 'TiO_all_Exomol', 'VO_Plez', 'FeH', 'H2S'],
#                                         cloud_species=['MgSiO3(c)_cd', 'Fe(c)_cd'],
#                                         scattering=True, #False if no clouds
#                                         output_folder=output_folder,
#                                         wavel_range=(0.9, 3.),
#                                         inc_spec=['SPHERE', 'GRAVITY'],
#                                         inc_phot=True,
#                                         pressure_grid='clouds',#'standard' 'clouds'
#                                         weights=None)
#
# retrieve.run_multinest(bounds={'logg': (2.5, 6.0),
#                                'c_o_ratio': (0.512, 0.047), # from stellar analysis
#                                'metallicity': (0.036, 0.023), # from stellar analysis
#                                'radius': (0.5, 2.),
#                                'fsed': (0., 20.),
#                                'log_kzz': (2., 15.),
#                                'sigma_lnorm': (1.2, 5.)},
#                                # 'mgsio3_fraction':(-3.,1.), # if clouds work w/out enforcement
#                                # 'fe_fracton':(-3.,1.), # if clouds work w/out enforcement
#                                'log_tau_cloud': (-2., 1.), # if result should be cloudy but is not, set this
#                                'fe_mgsio3_ratio': (-2., 2.), # if result ...
#                               },
#                        prior={'mass':(69.5,0.5),},
#                        chemistry='equilibrium',
#                        quenching=None,
#                        pt_profile='molliere',
#                        fit_corr=['SPHERE'],
#                        n_live_points=1000, #500-1000
#                        resume=True, # if running on cluster/intermediate results
#                        plotting=False, # testing plots
#                        pt_smooth=0.)



database.add_retrieval(tag=tag,
                       output_folder=output_folder,
                       inc_teff=True)

#############
### Done! ###
#############
