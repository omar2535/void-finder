from os import name
from void_finding_utils import calculate_average_density, get_galaxies_in_voids, get_list_of_void_positions
from utils import plot_galaxies_and_voids, plot_galaxies_in_3d_space
import numpy as np
import eagleSqlTools as sql
from matplotlib import pyplot as plt
import plotly.express as px
import time

'''Constants to be used in the program'''
DB_USERNAME = "xyz"
DB_PASSWORD = "abc"
DB_URL = "http://virgodb.dur.ac.uk:8080/Millennium/"

MIN_POSITION = 0
MAX_POSITION = 20
REDSHIFT = 0
VOID_RADIUS = 5

def main():
  start_time = time.time()
  print("Starting void finder program")

  connection = sql.connect(user=DB_USERNAME, password=DB_PASSWORD, url=DB_URL)

  query = (f"SELECT * "
           f"FROM millimil..DeLucia2006a "
           f"WHERE Redshift = {REDSHIFT} "
           f"AND x BETWEEN {MIN_POSITION} AND {MAX_POSITION} "
           f"AND y BETWEEN {MIN_POSITION} AND {MAX_POSITION} "
           f"AND z BETWEEN {MIN_POSITION} AND {MAX_POSITION};")

  data = connection.execute_query(query)
    
  """Calculate the average density of galaxies"""
  average_density = calculate_average_density(data, MIN_POSITION, MAX_POSITION)

  """Calculate void positions"""
  # list_of_voids = get_list_of_void_positions(data, MIN_POSITION, MAX_POSITION, average_density, VOID_RADIUS)
  list_of_voids = get_galaxies_in_voids(data, average_density, VOID_RADIUS)
  
  print("--- %s seconds ---" % (time.time() - start_time))

  """For plotting the galaxies in 3d space"""
  # plot_galaxies_in_3d_space(data)
  plot_galaxies_and_voids(data, list_of_voids)

  print("Ending void finder program")

if __name__ == "__main__":
  main()
