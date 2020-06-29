# Strain-Gauge-Rosette-Calculations

This was a short program written to aid in performing a mechanics of materials lab.

The strain in the x and y directions and shear strain, as well as strain at 60* were 
calculated at various pressures given a set of experimental data collected in a thin 
wall pressure vessel with both open end and closed end conditions.

The following set of equations were used in the calculations:

strain_a = strain_x*(cos(theta_a))^2 + strain_y*(sin(theta_a))^2 +shear_strain*sin(theta_a)*cos(theta_a)
strain_b = strain_x*(cos(theta_b))^2 + strain_y*(sin(theta_b))^2 +shear_strain*sin(theta_b)*cos(theta_b)
strain_c = strain_x*(cos(theta_c))^2 + strain_y*(sin(theta_c))^2 +shear_strain*sin(theta_c)*cos(theta_c)

where a, b, and c are the strains in the a*, b*, and c* directions, respectively.  
