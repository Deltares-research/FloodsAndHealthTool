User manual - general
=====

Overview
-----

The Floods and Health tool uses flood maps produced by SFINCS and WFLOW as part of the HydroMT package and transforms it into the requested format for the health assessment (.netcdf).
The input data includes the severity (depth, area), as well as demographic information about the affected population (age, social status, sex). 
Additionally, concentrations of different pathogens in floodwater (E.coli, V. cholerae, Cryptosporidium) and exposure scenario’s of adults and children are provided in two separate YAML files. 
These files can be configurated to adjust the pathogen concentrations or ingested volumes per exposure group. 

For more information regarding specific parameters see the pages 'Input parameters' or 'Output parameters'.

.. figure:: ./figures/UserManualOverview.png
   :width: 800px
   :align: center

   Overview of the data stream with input data, source and type, as well as potential nice-to-haves.¶
	
Example of floodshealth.inp **still from sfincs**
-----

.. code-block:: text

	x0              = 0
	y0              = 0	
	mmax            = 100
	nmax            = 100
	dx              = 100
	dy              = 100
	rotation        = 0
	
	tref            = 20221116 000000
	tstart          = 20221116 180000
	tstop           = 20221116 235959
	
	depfile         = sfincs.dep
	mskfile         = sfincs.msk
	indexfile       = sfincs.ind

	bndfile         = sfincs.bnd
	bzsfile         = sfincs.bzs
	spwfile         = sfincs.spw
	srcfile         = sfincs.src
	disfile         = sfincs.dis

	advection	    = 0
	alpha           = 0.75
	huthresh	    = 0.05
	manning         = 0.04	
	theta 		    = 1.0
	qinf            = 0.0

	dtout           = 3600
	dtmaxout        = 86400	
	dthisout        = 600

	inputformat     = bin
	outputformat    = net	
	
	obsfile         = sfincs.obs  	

Domain
-----


Grid characteristics
^^^^^
**from sfincs**
   
.. code-block:: text
	
	e.g. in sfincs.inp:
	
	x0              = 0
	y0              = 0	
	mmax            = 250
	nmax            = 150
	dx              = 100
	dy              = 100
	rotation        = 45
	

	
Index file
^^^^^

Input format 
^^^^^

.. code-block:: text

	inputformat = net

Output format
^^^^^

The main map output is in netcdf.

.. code-block:: text

	outputformat = net

Output files **from sfincs**
^^^^^

In case of netcdf output the map output will be named 'sfincs_map.nc', in case observation points are provided also a second file will be created with observation point output named 'sfincs_his.nc'.

For more information about the variables saved to the netcdf output files, see the 'Output description' section.

For binary or ascii files the output will be written to separate files, of which the named can be changed:

.. code-block:: text

	hmaxfile 	= hmax.dat
	zsfile 		= zs.dat
	vmaxfile 	= vmax.dat

Numerical parameters **from sfincs**
^^^^^

**huthresh**

'huthresh' is the flow depth limiter in SFINCS, by default set to 0.05 meters, controlling what minimal water depth should be exceeded to call a cell wet, and start calculating fluxes.
It is recommended to use values within the range [0.001 <> 0.1].

**alpha**

'alpha' is the additional time step limiter besides the courant criteria.
By default this is set to 0.75, in case model simulations become instable for some reason this value can be reduced.
It is recommended to use values within the range [0.1 <> 0.75].

**theta**

'theta' sets the implicitness of the numerical scheme of SFINCS.
The default value is 1.0 which is recommended for the regular version of SFINCS, however if more smoothing in you model result is needed because it might become unstable for some reason, you could set this to theta=0.9..

**advection**

'advection' sets what version of the advection term to use in the momentum equation, varying between the default of no advection at all (advection = 0), 1D advection terms (advection = 1) and full 2D advection terms (advection = 2).
Generally it is only needed to turn on advection in case of modelling waves or super-critical flow.

.. code-block:: text

	huthresh 	= 0.05
	alpha 		= 0.75
	theta 		= 1.0
	advection 	= 0

**viscosity**

'viscosity' turns on the viscosity term in the momentum equation (viscosity = 1).
The recommended value of viscosity 'nuvisc' to add to your model (only advised to use when you set theta = 1.0), depends on your grid size.
For ease, SFINCS internally automatically determines the optimal value for you, which is displayed when running the model:	'Turning on process: Viscosity, with nuvisc=   0.5000000'. In this example corresponding to a grid resolution of 50 meters.
In case you would want to increase the viscosity term, you can either specify the exact value you want 'nuvisc = XXX', or e.g. multiply it by a factor 2: 	nuviscdim = 2.0 (default = 1.0, dimensionless).
By default the value of nuvisc is determined like this:

	dx = 50 > nuvisc = 0.5
	
        dx = 100 > nuvisc = 1.0
	
        dx = 500 > nuvisc = 5.0	
	
.. code-block:: text

	viscosity 	= 1
	nuviscdim 	= 1.0 (default)
	nuvisc 		= XXX (automatically determined, or specify a value yourself that overrules this)
	
**Drag Coefficients:**

The wind drag coefficients are varying with wind speed and implemented as in Delft3D. 
The default values are based on Vatvani et al. (2012). 
There is specified for how many points 'cd_nr' a velocity 'cd_wnd' and a drag coefficient 'cd_val' is specified, the following are the default values:

.. code-block:: text

	cd_nr 		= 3 

	cd_wnd 		= 0 28 50 

	cd_val 		= 0.0010 0.0025 0.0015 
	

