import vtk


def interpolate_solution(vtu_file_path, x, y, z):
    # Read the vtu file
    reader = vtk.vtkXMLUnstructuredGridReader()
    reader.SetFileName(vtu_file_path)
    reader.Update()

    # Get the solution field
    solution_array = reader.GetOutput().GetPointData().GetArray("Solution")

    # Create a vtkPoints object with the given coordinates
    point = vtk.vtkPoints()
    point.InsertNextPoint(x, y, z)

    # Create a vtkIdList to store the point id
    point_id_list = vtk.vtkIdList()
    point_id_list.InsertNextId(0)  # The point id we just inserted

    # Create a vtkCellLocator to find the cell that contains the point
    locator = vtk.vtkCellLocator()
    locator.SetDataSet(reader.GetOutput())
    locator.BuildLocator()

    # Find the cell that contains the point
    cell_id = vtk.mutable(0)
    sub_id = vtk.mutable(0)
    dist = vtk.mutable(0.0)
    locator.FindCell(point.GetPoint(0), 1e-10, cell_id, sub_id, dist)

    # Interpolate the solution at the given point
    interpolated_value = solution_array.GetTuple1(cell_id)

    return interpolated_value
