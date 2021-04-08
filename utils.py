import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Plots galaxies in 3d space using the plotly library
def plot_galaxies_in_3d_space(data):
  column_names = data.dtype.names

  better_data = []
  for row in data:
    better_data.append(list(row))
  data = np.array(better_data)

  x_index = column_names.index('x')
  y_index = column_names.index('y')
  z_index = column_names.index('z')

  x_data = data[:, x_index]
  y_data = data[:, y_index]
  z_data = data[:, z_index]

  fig = go.Figure(data=[go.Scatter3d(
    x=x_data, y=y_data, z=z_data,
    mode='markers'
  )])
  fig.show()

def plot_galaxies_and_voids(data, voids):
  column_names = data.dtype.names

  better_data = []
  for row in data:
    better_data.append(list(row))
  data = np.array(better_data)

  x_index = column_names.index('x')
  y_index = column_names.index('y')
  z_index = column_names.index('z')

  x_data = data[:, x_index]
  y_data = data[:, y_index]
  z_data = data[:, z_index]

  void_x = voids[:, 0]
  void_y = voids[:, 1]
  void_z = voids[:, 2]
  fig = go.Figure(data=[go.Scatter3d(
    name="Void",
    x=void_x, y=void_y, z=void_z,
    mode='markers',
    marker=dict(
      size=12,
      color="red",
      opacity=0.5
    )
  )])

  fig.add_scatter3d(name="Galaxy", x=x_data, y=y_data, z=z_data, mode='markers', marker=dict(
    size=5,
    color="blue",
    opacity=1
  ))

  fig.update_layout(
    title="Mini-millennium galaxy plot",
    xaxis_title="x - 1/h Mpc",
    yaxis_title="y - 1/h Mpc",
    legend_title="Legend"
  )
  fig.show()