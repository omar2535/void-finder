import math
import numpy as np

# Calculate average density of galaxies
# Assumes that region is a square
def calculate_average_density(data, min_position, max_position):
  num_galaxies = data.shape[0]
  volume = math.pow(max_position - min_position, 3)
  return num_galaxies / volume

# Go through each region from MIN_POSITION to MAX_POSITION for x,y,z and for the radius we
# are using, determine the number of galaxies that should be in the region
def get_list_of_void_positions(data, min_position, max_position, average_density, void_radius):
  void_positions = []

  for x in range(min_position, max_position):
    print(x)
    for y in range(min_position, max_position):
      print(y)
      for z in range(min_position, max_position):
        num_galaxies_in_range = count_number_of_galaxies_in_radius(data, x, y, z, void_radius)
        if is_void(num_galaxies_in_range, average_density, void_radius):
          void_positions.append((x, y, z))
  return void_positions

# For each galaxy, check if it's in an under-dense region
def get_galaxies_in_voids(data, average_density, void_radius):
  column_names = data.dtype.names
  x_index = column_names.index('x')
  y_index = column_names.index('y')
  z_index = column_names.index('z')
  galaxies = []

  for index, galaxy in enumerate(data):
    x = galaxy[x_index]
    y = galaxy[y_index]
    z = galaxy[z_index]
    num_galaxies_in_range = count_number_of_galaxies_in_radius(data, x, y, z, void_radius)
    if is_void(num_galaxies_in_range, average_density, void_radius):
      galaxies.append((x, y, z))
  
  return np.array(galaxies)

# Counts number of galaxies within radius of sphere at a given point and given radius
def count_number_of_galaxies_in_radius(data, x, y, z, radius):
  count = 0
  column_names = data.dtype.names
  x_index = column_names.index('x')
  y_index = column_names.index('y')
  z_index = column_names.index('z')
  for galaxy in data:
    galaxy_x = galaxy[x_index]
    galaxy_y = galaxy[y_index]
    galaxy_z = galaxy[z_index]

    distance = distance_between_points(x, y, z, galaxy_x, galaxy_y, galaxy_z)
    if distance < radius:
      count+=1
  return count

# Returns distance between two points
# sqrt((x-x0)^2 + (y-y0)^2 + (z-z0)^2)
def distance_between_points(x1, y1, z1, x2, y2, z2):
  return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1)**2))

# Assumes spherical void
# Determines if number of galaxies in sphere is smaller than average density
def is_void(num_galaxies_in_range, average_density, radius):
  volume_of_sphere = 4/3 * (math.pi * math.pow(radius, 3))
  threshold_num_galaxies = volume_of_sphere * average_density
  return num_galaxies_in_range < threshold_num_galaxies

# TODO: Simplify the list of voids
# Combines void lists for those that are similar
def simplify_void_list(list_of_void_points, radius):
  pass
