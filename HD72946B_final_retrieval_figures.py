################################################################################
# The purpose of this script is to generate the "experiment" associated        #
# with Balmer et al. (in prep.) on HD 72946 B: test what influence a dyn.      #
# prior and stellar abundances has on the retrieved clouds and P-T params.     #
# for an L-type, fully convective brown dwarf. Here we assume clouds by        #
# enforcing their presence near the photosphere with the log_tau_cloud         #
# and fe_mgsio3_ratio parameters. We implement scattering, AMR for the         #
# pressure grid, and A&M clouds composed of MgSiO3 and Fe Crystalline,         #
# DHS (irregular shape) grains.      2023/05/23, W. Balmer                     #
# python HD72946B_init_species.py
# python HD72946B_final_retrieval_comparison.py
# python HD72946B_final_retrieval_figures.py
################################################################################
import os
import species

species.SpeciesInit()

database = species.Database()

##########################################################
### Molliere P-T, A&M Cloud, No mass prior, Free abund ###
##########################################################

output_folder = 'HD72946B-am-molliere-nomass-freeab-multinest'

tag = 'HD72946B-am-molliere-nomass-freeab'
if not os.path.isdir('./'+tag):
    os.makedirs('./'+tag)

database.get_retrieval_teff(tag=tag,
                            random=30)

try:
    species.plot_posterior(tag=tag,
                           offset=(-0.3, -0.35),
                           vmr=True,
                           inc_mass=True,
                           inc_pt_param=False,
                           output=tag+'/'+tag+'_posterior.pdf')
except:
    pass

samples, radtrans = database.get_retrieval_spectra(tag=tag,
                                                   random=30,
                                                   wavel_range=(0.5, 6.),
                                                   spec_res=500.)

species.plot_pt_profile(tag=tag,
                        random=100,
                        xlim=(0., 6000.),
                        offset=(-0.07, -0.14),
                        output=tag+'/'+tag+'_pt_profile.pdf',
                        radtrans=radtrans,
                        extra_axis='photosphere')

species.plot_opacities(tag=tag,
                       offset=(-0.1, -0.14),
                       output=tag+'/'+tag+'_opacities.pdf',
                       radtrans=radtrans)


best = database.get_probable_sample(tag=tag)

objectbox = database.get_object('HD 72946 B',
                                inc_phot=True)

objectbox = species.update_spectra(objectbox, best)

residuals = species.get_residuals(datatype='model',
                                  spectrum='petitradtrans',
                                  parameters=best,
                                  objectbox=objectbox,
                                  inc_phot=True,
                                  inc_spec=True,
                                  radtrans=radtrans)

modelbox = radtrans.get_model(model_param=best,
                              spec_res=500.,
                              plot_contribution=tag+'/'+tag+'_contribution.pdf')

no_clouds = best.copy()
no_clouds['log_tau_cloud'] = -100.
model_no_clouds = radtrans.get_model(no_clouds)

species.plot_spectrum(boxes=[samples, modelbox,
                             model_no_clouds,
                             objectbox],
                      filters=None,
                      plot_kwargs=[{'zorder':3,'ls': '-', 'lw': 0.1, 'color': 'gray'},
                                   {'zorder':3,'ls': '-', 'lw': 0.5, 'color': 'black'},
                                   {'zorder':3,'ls': '--', 'lw': 0.3, 'color': 'black'},
                                   {
                                    'GRAVITY': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': 'xkcd:brick', 'ls': 'none', 'alpha': 1, 'label': 'VLTI/GRAVITY'},
                                    'SPHERE': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': '#5f61b4', 'ls': 'none', 'capsize':2, 'alpha': 1, 'label': 'VLT/SPHERE'},
                                    'Paranal/SPHERE.IRDIS_D_H23_2': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2, 'label': 'VLT/SPHERE/IRDIS'},
                                    'Paranal/SPHERE.IRDIS_D_H23_3': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2},
                                    }],
                      residuals=residuals,
                      xlim=(0.95, 2.5),
                      # ylim=(0.15e-16, 1.15e-15),
                      ylim_res=(-5., 5.),
                      scale=('linear', 'linear'),
                      offset=(-0.6, -0.05),
                      figsize=(12, 6),
                      legend=[{'loc': 'upper right', 'fontsize': 8.}, {'loc': 'lower left', 'fontsize': 8.}],
                      output=tag+'/'+tag+'_spectrum.pdf')


#######################################################
### Molliere P-T, A&M Cloud, Mass prior, Free abund ###
#######################################################

output_folder = 'HD72946B-am-molliere-mass-freeab-multinest'

tag = 'HD72946B-am-molliere-mass-freeab'

if not os.path.isdir('./'+tag):
    os.makedirs('./'+tag)

database.get_retrieval_teff(tag=tag,
                            random=30)

try:
    species.plot_posterior(tag=tag,
                           offset=(-0.3, -0.35),
                           vmr=True,
                           inc_mass=True,
                           inc_pt_param=False,
                           output=tag+'/'+tag+'_posterior.pdf')
except:
    pass

samples, radtrans = database.get_retrieval_spectra(tag=tag,
                                                   random=30,
                                                   wavel_range=(0.5, 6.),
                                                   spec_res=500.)

species.plot_pt_profile(tag=tag,
                        random=100,
                        xlim=(0., 6000.),
                        offset=(-0.07, -0.14),
                        output=tag+'/'+tag+'_pt_profile.pdf',
                        radtrans=radtrans,
                        extra_axis='photosphere')

species.plot_opacities(tag=tag,
                       offset=(-0.1, -0.14),
                       output=tag+'/'+tag+'_opacities.pdf',
                       radtrans=radtrans)


best = database.get_probable_sample(tag=tag)

objectbox = database.get_object('HD 72946 B',
                                inc_phot=True)

objectbox = species.update_spectra(objectbox, best)

residuals = species.get_residuals(datatype='model',
                                  spectrum='petitradtrans',
                                  parameters=best,
                                  objectbox=objectbox,
                                  inc_phot=True,
                                  inc_spec=True,
                                  radtrans=radtrans)

modelbox = radtrans.get_model(model_param=best,
                              spec_res=500.,
                              plot_contribution=tag+'/'+tag+'_contribution.pdf')

no_clouds = best.copy()
no_clouds['log_tau_cloud'] = -100.
model_no_clouds = radtrans.get_model(no_clouds)

species.plot_spectrum(boxes=[samples, modelbox,
                             model_no_clouds,
                             objectbox],
                      filters=None,
                      plot_kwargs=[{'zorder':3,'ls': '-', 'lw': 0.1, 'color': 'gray'},
                                   {'zorder':3,'ls': '-', 'lw': 0.5, 'color': 'black'},
                                   {'zorder':3,'ls': '--', 'lw': 0.3, 'color': 'black'},
                                   {
                                    'GRAVITY': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': 'xkcd:brick', 'ls': 'none', 'alpha': 1, 'label': 'VLTI/GRAVITY'},
                                    'SPHERE': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': '#5f61b4', 'ls': 'none', 'capsize':2, 'alpha': 1, 'label': 'VLT/SPHERE'},
                                    'Paranal/SPHERE.IRDIS_D_H23_2': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2, 'label': 'VLT/SPHERE/IRDIS'},
                                    'Paranal/SPHERE.IRDIS_D_H23_3': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2},
                                    }],
                      residuals=residuals,
                      xlim=(0.95, 2.5),
                      # ylim=(0.15e-16, 1.15e-15),
                      ylim_res=(-5., 5.),
                      scale=('linear', 'linear'),
                      offset=(-0.6, -0.05),
                      figsize=(12, 6),
                      legend=[{'loc': 'upper right', 'fontsize': 8.}, {'loc': 'lower left', 'fontsize': 8.}],
                      output=tag+'/'+tag+'_spectrum.pdf')


#####################################################################
### Molliere P-T, A&M Cloud, No mass prior, Fix abund. to Stellar ###
#####################################################################

output_folder = 'HD72946B-am-molliere-nomass-fixab-multinest'

tag = 'HD72946B-am-molliere-nomass-fixab'

if not os.path.isdir('./'+tag):
    os.makedirs('./'+tag)

database.get_retrieval_teff(tag=tag,
                            random=30)

try:
    species.plot_posterior(tag=tag,
                           offset=(-0.3, -0.35),
                           vmr=True,
                           inc_mass=True,
                           inc_pt_param=False,
                           output=tag+'/'+tag+'_posterior.pdf')
except:
    pass

samples, radtrans = database.get_retrieval_spectra(tag=tag,
                                                   random=30,
                                                   wavel_range=(0.5, 6.),
                                                   spec_res=500.)

species.plot_pt_profile(tag=tag,
                        random=100,
                        xlim=(0., 6000.),
                        offset=(-0.07, -0.14),
                        output=tag+'/'+tag+'_pt_profile.pdf',
                        radtrans=radtrans,
                        extra_axis='photosphere')

species.plot_opacities(tag=tag,
                       offset=(-0.1, -0.14),
                       output=tag+'/'+tag+'_opacities.pdf',
                       radtrans=radtrans)


best = database.get_probable_sample(tag=tag)

objectbox = database.get_object('HD 72946 B',
                                inc_phot=True)

objectbox = species.update_spectra(objectbox, best)

residuals = species.get_residuals(datatype='model',
                                  spectrum='petitradtrans',
                                  parameters=best,
                                  objectbox=objectbox,
                                  inc_phot=True,
                                  inc_spec=True,
                                  radtrans=radtrans)

modelbox = radtrans.get_model(model_param=best,
                              spec_res=500.,
                              plot_contribution=tag+'/'+tag+'_contribution.pdf')

no_clouds = best.copy()
no_clouds['log_tau_cloud'] = -100.
model_no_clouds = radtrans.get_model(no_clouds)

species.plot_spectrum(boxes=[samples, modelbox,
                             model_no_clouds,
                             objectbox],
                      filters=None,
                      plot_kwargs=[{'zorder':3,'ls': '-', 'lw': 0.1, 'color': 'gray'},
                                   {'zorder':3,'ls': '-', 'lw': 0.5, 'color': 'black'},
                                   {'zorder':3,'ls': '--', 'lw': 0.3, 'color': 'black'},
                                   {
                                    'GRAVITY': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': 'xkcd:brick', 'ls': 'none', 'alpha': 1, 'label': 'VLTI/GRAVITY'},
                                    'SPHERE': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': '#5f61b4', 'ls': 'none', 'capsize':2, 'alpha': 1, 'label': 'VLT/SPHERE'},
                                    'Paranal/SPHERE.IRDIS_D_H23_2': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2, 'label': 'VLT/SPHERE/IRDIS'},
                                    'Paranal/SPHERE.IRDIS_D_H23_3': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2},
                                    }],
                      residuals=residuals,
                      xlim=(0.95, 2.5),
                      # ylim=(0.15e-16, 1.15e-15),
                      ylim_res=(-5., 5.),
                      scale=('linear', 'linear'),
                      offset=(-0.6, -0.05),
                      figsize=(12, 6),
                      legend=[{'loc': 'upper right', 'fontsize': 8.}, {'loc': 'lower left', 'fontsize': 8.}],
                      output=tag+'/'+tag+'_spectrum.pdf')



#####################################################################
### Molliere P-T, A&M Cloud, No mass prior, Fix abund. to Stellar ###
#####################################################################

output_folder = 'HD72946B-am-molliere-nomass-fixab-multinest'

tag = 'HD72946B-am-molliere-nomass-fixab'

if not os.path.isdir('./'+tag):
    os.makedirs('./'+tag)

database.get_retrieval_teff(tag=tag,
                            random=30)

try:
    species.plot_posterior(tag=tag,
                           offset=(-0.3, -0.35),
                           vmr=True,
                           inc_mass=True,
                           inc_pt_param=False,
                           output=tag+'/'+tag+'_posterior.pdf')
except:
    pass

samples, radtrans = database.get_retrieval_spectra(tag=tag,
                                                   random=30,
                                                   wavel_range=(0.5, 6.),
                                                   spec_res=500.)

species.plot_pt_profile(tag=tag,
                        random=100,
                        xlim=(0., 6000.),
                        offset=(-0.07, -0.14),
                        output=tag+'/'+tag+'_pt_profile.pdf',
                        radtrans=radtrans,
                        extra_axis='photosphere')

species.plot_opacities(tag=tag,
                       offset=(-0.1, -0.14),
                       output=tag+'/'+tag+'_opacities.pdf',
                       radtrans=radtrans)


best = database.get_probable_sample(tag=tag)

objectbox = database.get_object('HD 72946 B',
                                inc_phot=True)

objectbox = species.update_spectra(objectbox, best)

residuals = species.get_residuals(datatype='model',
                                  spectrum='petitradtrans',
                                  parameters=best,
                                  objectbox=objectbox,
                                  inc_phot=True,
                                  inc_spec=True,
                                  radtrans=radtrans)

modelbox = radtrans.get_model(model_param=best,
                              spec_res=500.,
                              plot_contribution=tag+'/'+tag+'_contribution.pdf')

no_clouds = best.copy()
no_clouds['log_tau_cloud'] = -100.
model_no_clouds = radtrans.get_model(no_clouds)

species.plot_spectrum(boxes=[samples, modelbox,
                             model_no_clouds,
                             objectbox],
                      filters=None,
                      plot_kwargs=[{'zorder':3,'ls': '-', 'lw': 0.1, 'color': 'gray'},
                                   {'zorder':3,'ls': '-', 'lw': 0.5, 'color': 'black'},
                                   {'zorder':3,'ls': '--', 'lw': 0.3, 'color': 'black'},
                                   {
                                    'GRAVITY': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': 'xkcd:brick', 'ls': 'none', 'alpha': 1, 'label': 'VLTI/GRAVITY'},
                                    'SPHERE': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': '#5f61b4', 'ls': 'none', 'capsize':2, 'alpha': 1, 'label': 'VLT/SPHERE'},
                                    'Paranal/SPHERE.IRDIS_D_H23_2': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2, 'label': 'VLT/SPHERE/IRDIS'},
                                    'Paranal/SPHERE.IRDIS_D_H23_3': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2},
                                    }],
                      residuals=residuals,
                      xlim=(0.95, 2.5),
                      # ylim=(0.15e-16, 1.15e-15),
                      ylim_res=(-5., 5.),
                      scale=('linear', 'linear'),
                      offset=(-0.6, -0.05),
                      figsize=(12, 6),
                      legend=[{'loc': 'upper right', 'fontsize': 8.}, {'loc': 'lower left', 'fontsize': 8.}],
                      output=tag+'/'+tag+'_spectrum.pdf')



##################################################################
### Molliere P-T, A&M Cloud, Mass prior, Fix abund. to Stellar ###
##################################################################

output_folder = 'HD72946B-am-molliere-mass-fixab-multinest'

tag = 'HD72946B-am-molliere-mass-fixab'

if not os.path.isdir('./'+tag):
    os.makedirs('./'+tag)

database.get_retrieval_teff(tag=tag,
                            random=30)

try:
    species.plot_posterior(tag=tag,
                           offset=(-0.3, -0.35),
                           vmr=True,
                           inc_mass=True,
                           inc_pt_param=False,
                           output=tag+'/'+tag+'_posterior.pdf')
except:
    pass

samples, radtrans = database.get_retrieval_spectra(tag=tag,
                                                   random=30,
                                                   wavel_range=(0.5, 6.),
                                                   spec_res=500.)

species.plot_pt_profile(tag=tag,
                        random=100,
                        xlim=(0., 6000.),
                        offset=(-0.07, -0.14),
                        output=tag+'/'+tag+'_pt_profile.pdf',
                        radtrans=radtrans,
                        extra_axis='photosphere')

species.plot_opacities(tag=tag,
                       offset=(-0.1, -0.14),
                       output=tag+'/'+tag+'_opacities.pdf',
                       radtrans=radtrans)


best = database.get_probable_sample(tag=tag)

objectbox = database.get_object('HD 72946 B',
                                inc_phot=True)

objectbox = species.update_spectra(objectbox, best)

residuals = species.get_residuals(datatype='model',
                                  spectrum='petitradtrans',
                                  parameters=best,
                                  objectbox=objectbox,
                                  inc_phot=True,
                                  inc_spec=True,
                                  radtrans=radtrans)

modelbox = radtrans.get_model(model_param=best,
                              spec_res=500.,
                              plot_contribution=tag+'/'+tag+'_contribution.pdf')

no_clouds = best.copy()
no_clouds['log_tau_cloud'] = -100.
model_no_clouds = radtrans.get_model(no_clouds)

species.plot_spectrum(boxes=[samples, modelbox,
                             model_no_clouds,
                             objectbox],
                      filters=None,
                      plot_kwargs=[{'zorder':3,'ls': '-', 'lw': 0.1, 'color': 'gray'},
                                   {'zorder':3,'ls': '-', 'lw': 0.5, 'color': 'black'},
                                   {'zorder':3,'ls': '--', 'lw': 0.3, 'color': 'black'},
                                   {
                                    'GRAVITY': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': 'xkcd:brick', 'ls': 'none', 'alpha': 1, 'label': 'VLTI/GRAVITY'},
                                    'SPHERE': {'zorder':1,'marker': '', 'ms': 5., 'mew': 0., 'color': '#5f61b4', 'ls': 'none', 'capsize':2, 'alpha': 1, 'label': 'VLT/SPHERE'},
                                    'Paranal/SPHERE.IRDIS_D_H23_2': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2, 'label': 'VLT/SPHERE/IRDIS'},
                                    'Paranal/SPHERE.IRDIS_D_H23_3': {'zorder':1,'marker': '', 'ms': 5., 'color': 'xkcd:dark orange', 'ls': 'none', 'capsize':2},
                                    }],
                      residuals=residuals,
                      xlim=(0.95, 2.5),
                      # ylim=(0.15e-16, 1.15e-15),
                      ylim_res=(-5., 5.),
                      scale=('linear', 'linear'),
                      offset=(-0.6, -0.05),
                      figsize=(12, 6),
                      legend=[{'loc': 'upper right', 'fontsize': 8.}, {'loc': 'lower left', 'fontsize': 8.}],
                      output=tag+'/'+tag+'_spectrum.pdf')



#############
### Done! ###
#############
