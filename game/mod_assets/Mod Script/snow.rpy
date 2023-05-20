init python:
    
    #################################################################
    # Here we use a random module for some random materials (since we 
    # do not want Ren'Py to store random numbers, we will generate them).
    import random
    
    # random number initialization
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates a snow effect. You should use this function instead of instantiating
        SnowFactory directly (Well, it doesn't really matter, but it will save typing, 
        if you use the default values =D)
        
        image:
            This is the image used as the snowflakes. It should always be an image file
            or im object, since we will be applying im transformations on it.
        
        max_particles:
            Maximum number of particles on the screen at one time.
            
        speed:
            The basic vertical speed of the particles. The higher the value, the faster the particles
            The higher the value, the faster the particles will fall.
            Values below 1 will be rescaled to 1
            
        wind:
            Maximum wind force that will be applied to particles.
            
        xborder:
            Horizontal range boundary. A random value between these two will be applied
            When creating particles.
            
        yborder:
            Vertical range boundary. A random value between these two will be applied
            when creating particles.
            The higher the values, the further away from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles used in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize factory. The parameters are the same as those of the Snow function.
            """            
            # the maximum number of particles that can be on the screen at the same time
            self.max_particles = max_particles
            
            # particle velocity
            self.speed = speed
            
            # wind speed
            self.wind = wind
            
            # horizontal/vertical range for particle creation
            self.xborder = xborder
            self.yborder = yborder
            
            # is the maximum depth of the screen. The highest values result in more 
            # particle size, but they also use more memory. 10 is the default value 
            # and should be fine for most games,
            # because particle sizes are calculated as a percentage of this value.
            self.depth = kwargs.get("depth", 10)
            
            # initialize images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            Called from inside each Particles object frame to create new particles.
            We will simply create new particles if the number of particles on the screen is less than the 
            maximum number of particles that can be.
            """
            # If we create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for a particle
                depth = random.randint(1, self.depth)
                
                # We assume that particles falling far away from the screen will move slower
                # than those falling close to the screen. So we change the velocity of the particles based on
                # their depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                    random.uniform(-self.wind, self.wind)*depth_speed,  # wind power 
                                    self.speed*depth_speed,  # vertical velocity of the particle
                                    random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                    random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                    ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            Creates a list of images with different sizes, so we can
            anticipate them all and use cached versions to make 
            them more efficient for memory.            
            """
            rv = [ ]
            
            # creates an array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            This is an internally invoked Particles object for predicting used 
            particle images. It expects to return an image list for prediction.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents each particle on the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes snow particles. Called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o.)
            # If the vertical velocity of the particles is lower than 1, we use 1.
            # Prevents particles from getting stuck on the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind speed
            self.wind = wind
            
            # particle velocity
            self.speed = speed

            # The last time the particle was updated (used to calculate unexpected
            # delays between updates, otherwise known as lag)
            self.oldst = None
            
            # horizontal/vertical particle positions
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called inside each frame to update the particle.
            """
            
            # lag calculation
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # position update
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # checks to see if the particle is out of the screen, you can destroy it.
            if self.ypos > renpy.config.screen_height or\
            (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ## outputs "Dead"
                return None
                
            # returns the particle as a tuple (xpos, ypos, time, image)
            # since it assumes that the horizontal and vertical positions are integers, 
            # we have to convert them (internal positions use float for smooth moves =D)
            return int(self.xpos), int(self.ypos), st, self.image
init:
    image snow = Snow("gui/menu_particle.png", max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400))

    