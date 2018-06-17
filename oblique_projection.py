class ObliqueProjection():
    def __init__(self,v0=30,theta=30):
        self.v0 = v0
        self.theta = math.radians(theta)
        self.v0_x = self.v0 * math.cos(self.theta)
        self.v0_y = self.v0 * math.sin(self.theta)
        self.g = 9.8

    def get_velocity(self,t):
        self.v_x = self.v0 * math.cos(self.theta)
        self.v_y = -1.0 * self.g * t + self.v0 * math.sin(self.theta)
        return [self.v_x,self.v_y]


    def get_position(self,t):
        self.x = v0 * math.cos(theta) * t
        self.y = -0.5 * self.g * t**2  + self.v0 * math.sin(theta) * t
        return [self.x,self.y]

    def get_positionX(self,t):
        self.x = v0 * math.cos(theta) * t
        return self.x

    def get_positionY(self,t):
        self.y = -0.5 * self.g * t**2 + self.v0 * math.sin(self.theta) * t
        return self.y

    def get_top_time(self):
        t = self.v0 * math.sin(self.theta) / self.g
        return t

    def get_landing_time(self):
        return self.get_top_time() * 2

    def get_landing_x(self):
        return self.get_positionX(self.get_landing_time())

    def draw(self,start_t,end_t):
        list_x = []
        list_y = []
        for i in np.linspace(start_t,end_t,30):
            list_x.append(self.get_positionX(i))
            list_y.append(self.get_positionY(i))
        plt.plot(list_x,list_y)
        plt.show()
