# Plan for general physics project - Time to leave for labs
Aidan Hughes - 11/03 


## Overview

A poster showing the time you must leave to get to labs by bus/walking and if it is quicker to walk or bus.

Are we going to do guarateed times to get to schuster(eg 3 std) or just avg arrival is before 9?

What is the scope(eg how far away from labs and which bus routes)?
Fallowfield and rusholme?

## Coding
People - 

To model travel time, need to model both walking time (to uni and to nearest bus stop) and bus time.


[LWR Model](https://www.researchgate.net/profile/Dede-Tarwidi/publication/304775982_Numerical_Simulation_of_Traffic_Flow_via_Fluid_Dynamics_Approach/links/577a2f4308aece6c20fbbff7/Numerical-Simulation-of-Traffic-Flow-via-Fluid-Dynamics-Approach.pdf) with
[Cell Transition Model(CTM)](https://doi.org/10.1016/0191-2615(94)90002-7) for the buses, and (?) for walking,
coded in python and/or jupyter notebook. 

Data needed for buses:
- Bus routes and stops, [MappingGM](https://mappinggm.org.uk/maps/exploregm/)
- Distances between bus stops
- Traffic data, [gov](https://roadtraffic.dft.gov.uk/local-authorities/E08000003)
- Traffic lights?? 

Data for walking:
- Distance to nearest bus stop or to uni
- Average walking speed
- Traffic lights??

### Potential plan for coding
#### 13/03 to 19/03 - Minimal working version

After first week of coding, aim to have a bus model that can get a time to travel from a bus stop to uni stop with these assumptions:
1. Single lane road
2. No traffic lights
3. Constant time stopped at bus stop

And a walking model / time calcualtor.
#### 21/03 to 26/03 - Add additional features
1. Expand to entire area we want to model for
2. Add additional routes (50, 111)?
3. Multiple lanes and bus lanes
4. Traffic lights
5. Model time at bus stop (dependant on bus stop)
6. Time waiting for bus, [this](https://friedmanroy.github.io/blog/2023/Entropy/) article looks interesting and could be the source of another idea
6. Tues vs Thurs
7. Add side streets?

## Poster

People - 

Using Canva/Publisher/Powerpoint?

Link clearly to physics and our course. 
- Fluid mechanics (it is a compressible flow, so explaining how that changes the ones we have learned)
- Waves (the speed we find is essentially a wave speed for the traffic)

Research on Godunov's scheme, which is the numerical method the CTM is based in.

