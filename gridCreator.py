import numpy as np
import io
import libconf

'''
In this file we will create a regular cuboidal mesh of fixed dimensions
'''


def createMesh():
    with open('settings.cfg') as f:

        config = libconf.load(f)

        '''
        Load the settings.cfg file
        '''

        meshArray = []

        # Read the settings.cfg file

        H = config['H']
        L = config['L']
        W = config['W']
        RESX = config['RESX']
        RESY = config['RESY']
        RESZ = config['RESZ']

        Xs = np.linspace(0, L, RESX)
        Ys = np.linspace(0, W, RESY)
        Zs = np.linspace(0, H, RESZ)

        '''
        Create the Mesh
        '''
        for _i in Xs:
            for _j in Ys:
                for _k in Zs:
                    meshArray.append([_i, _j, _k, 0.0])

        return meshArray
