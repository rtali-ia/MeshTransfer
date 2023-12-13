import meshio
from utils import timeit


@timeit
def pltToVTK(pltFile, vtkFile):
    # Read the PLT file
    mesh = meshio.read(pltFile)

    # Write the mesh data to VTK format
    meshio.write(vtkFile, mesh, file_format='vtk')

    return vtkFile
