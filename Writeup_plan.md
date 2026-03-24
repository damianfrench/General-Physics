# Theory- LWR Model of traffic flow
## ~ 200-220 words
The Lighthill-Whitham_Richards (LWR) models traffic flow in a 1D description, similar to the analysis of a compressible fluid, dictated by mass conservation. Traffic is treated as having a macroscpic density $\rho$ and flow rate $q$, governed by the core principles of conservation laws and the flow-density relation. The former can be derived directly from the continuity equation

$\frac{\partial\rho}{\partial t} + \nabla \cdot (\rho u) = 0 $

over a 1D road segment. Imposing that vehicles act as a mass and treating density as vehicles per unit length yields

$\frac{\partial\rho}{\partial t} +\frac{\partial q}{\partial x} =0$, 

the conservation law disctating the LWR model. However, this equation contains unknowns, making it undetermined. A relationship used between $q$ and $\rho$ here is known as the fundamental diagram, acting as as the theoreitcal assumption of the model's behaviour.

The Greenshields model assumes a linear speed-density relation, yielding the fundamental diagram 

$q = \rho u = v_{max} \rho (1-\frac{\rho}{\rho_{max}})$ .

Applying this with the conservation condition gives a PDE describing characteristic wavespeed

$\frac{dq}{d \rho} = v_{max}(1-\frac{2\rho}{\rho_{max}})$ ,

highlighting the pertubations that propogate at speeds that depend on a local density. Free flow is where $\rho < \rho_{max}/2, providing a positive wavespeed propogating infomation forward with the traffic. Whereas, in congestion - where $\rho > \rho_{max}/2$ - the negative wavespeed forces disturbances to flow upstream and captures the backwards growth of traffic jams.

Using the LWR-Greenshields model now makes it possible to determine how traffic density evolves with time. Prediciting the behaviour and estimating travel time between two given points requires a numerical solution of the PDE shown above. The Cell Transmission Model (CTM) provides a framework using discrete cells, meaning real traffic data can be applied to the LWR model, acting as a numerical solution to the characteristic wave behaviour.


# CTM MODEL
## ~ 100 Words

The road can be divided into discrete cells, and using discreet time steps yields 

$$ \Delta \rho_{i} = \rho_{i} (t+\Delta t) - \rho_{i}(t) = \frac{\Delta t}{\Delta x}[y_{i-1}(t) - y_i(t)] $$,

acting as the update equation. This describes the flux, $y_i(t)$ from cell $i$ to $i+1$ at a time t. $\Delta x$ describes the width of the cell where $\Delta t$ is the time jump. The flux between each cell is then defined as 

$y_i = min(D_i, S_{i+1})$

where $D_i$ is the demand of the sending cell and $S_{i+1}$ the supply of the reveiving cell, both being derived from the Greenshields fundamental diagram.

The system is initialized by starting each cell with a density quoted from real traffic data, resetting the inflow and outflow parameters of each cell and allowing a computation of $y_i(0)$. Iteratively applying the update equation for each cell computes the forward step in time which results in many fluxes changing over the whole 1D road. This makes calculating the discrete velocity possible through taking the ratio of flux $y_i(t)$ and density $\rho_i(t)$ per each cell.
It is then possible to determine the travel time for a vehicle between two positions using

$$ T = \sum_{t=0}^{t_{end}} \Delta t, if       x_v(t_{end}) \leq x_{end} $$

where $x_v(t_{end})$, the updated vehicle position is given by 

$$ x_v(t+\Delta t) = x_v(t) + v_i(t) \Delta t $$

for each time step, $\Delta t$.


