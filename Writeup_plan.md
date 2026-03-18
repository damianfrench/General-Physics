# Theory- LWR Model of traffic flow
## ~ 200-220 words
The Lighthill-Whitham_Richards (LWR) models traffic flow in a 1D description, similar to the analysis of an compressible fluid, dictated by mass conservation. Traffic is treated as having a macroscpic density $\rho$ and flow rate $q$, governed by the core principles of conservation laws and the flow-density relation. The former can be derived directly from the continuity equation

$\frac{\partial\rho}{\partial t} + \nabla \cdot (\rho u) = 0 $

over a 1D road segment. Imposing vehicles to act as the mass and density being vehicles per unit length yields

$\frac{\partial\rho}{\partial t} +\frac{\partial q}{\partial x} =0$, 
the conservation law disctating the LWR model. However, this equation contains unknowns, making it undetermined. A relationship used between $q$ and $\rho$ here is known as the fundamental diagram. Acting as as the experimentally obtained relation of traffic, this shows increasing flow  with density to a critical point; after which congestion occurs causing reduced flow.

The Greenshields model assumes a linear speed-density relation, yielding the fundamental diagram 

$q = \rho u = v_{max} \rho (1-\frac{\rho}{\rho_{max}})$ .

Applying this witht the conservation condition gives a PDE describing characteristic wavespeed

$\frac{dq}{d \rho} = v_{max}(1-\frac{2\rho}{\rho_{max}})$ ,

highlighting the pertubations that propogate at speeds that depend on a local density. This forms shock waves that act as density discontinuities; defining the LWR model as a whole.


