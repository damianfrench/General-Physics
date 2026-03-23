import numpy as np
class CTM_model:

    ## need to deal with the boundary cells seperately

    def __init__(self,cell_widths_initialise,density_initialise,jam_density_init,max_flow_init,v_free_init):
        self.density=density_initialise
        self.cells_widths=cell_widths_initialise
        self.history=[self.density.copy()]
        self.v_free=v_free_init
        self.jam_density=jam_density_init
        self.max_flow=max_flow_init
        q_max=self.density*self.velocity_greenshields()  # v_free * rho_jam / 4
        rho_crit=self.jam_density/2
        self.w=q_max/(self.jam_density-rho_crit)  # = v_free / 2 for Greenshields
        self.step_width =0.9*np.min(self.cells_widths)/self.v_free  # use smallest cell for safety

        

        # initialise D and S from starting density
        q = self.density * self.velocity_greenshields()
        self.D = self.calculate_D(q)
        self.S = self.calculate_S()
        self.y = self.calculate_y()
        
    

    def calculate_D(self,flow):
        return np.minimum(flow,np.full(len(flow),self.max_flow))
    
    def calculate_S(self):
        return np.minimum(self.max_flow,self.w*(self.jam_density-self.density))
    
    def velocity_greenshields(self):
        return self.v_free * (1 - self.density / self.jam_density)
    
    
    def calculate_y(self):
        return np.minimum(self.D[:-1],self.S[1:])

    def recursive_stepping(self,current_step,inlet_density,total_steps=100):
        q=self.density*self.velocity_greenshields()
        self.D=self.calculate_D(q)
        self.S=self.calculate_S()
        self.y=self.calculate_y()
        jump=(self.step_width/self.cells_widths[1:-1])*(self.y[:-1]-self.y[1:])
        self.density[1:-1]=self.density[1:-1]+jump

        self.density[0] = inlet_density             # fixed inlet density
        self.density[-1] = self.density[-2]     # free outflow

        self.history.append(self.density.copy())
        while current_step!=total_steps:
            return self.recursive_stepping(current_step+1,inlet_density,total_steps)
        return 
    
    def travel_time(self, start_cell, end_cell):
        x = np.sum(self.cells_widths[:start_cell])  # physical position of start cell
        
        for t, density_snapshot in enumerate(self.history):
            cell = np.searchsorted(np.cumsum(self.cells_widths), x)
            cell = np.clip(cell, 0, len(density_snapshot) - 1)
            
            v = self.v_free * (1 - density_snapshot[cell] / self.jam_density)
            x += v * self.step_width
            
            if cell >= end_cell:
                return t * self.step_width
        
        return None




