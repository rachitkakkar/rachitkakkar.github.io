def gen_row_permutations(width):
  permutations = []
  def subset(partial=[]):
    nonlocal permutations
    # Calculate all possible subsets give a (partially) complete wall and add to permutation list
    # For example, the incomplete wall [2, 2] has the possible subsets [2, 2, 3, 2] AND [2, 2, 2, 3]
    # Walls are stored as lists of where there edges are, so [2, 2, 3, 2] and [2, 2, 2, 3] are represented as [2, 4, 7, 9] and [2, 4, 6, 9]    
    if (partial[-1] == width-3 or partial[-1] == width-2): # Wall row is full (only one more 2x1 or)
      permutations.append(partial)
      return
    elif (partial[-1] == width-4): # Can only fit one or two additional 2x1 bricks
      subset([*partial, partial[-1]+2])
    else: # Can fit a 3x1 OR a 2x1 brick
      subset([*partial, partial[-1]+2])
      subset([*partial, partial[-1]+3])

  # Seeds for 2 and 3
  subset(partial=[2])
  subset(partial=[3])
  return permutations

def gen_possible_connections(all_rows):
  all_connections = []

  for i, row1 in enumerate(all_rows):
    connections = []
    for j, row2 in enumerate(all_rows):
      if (set(row1).isdisjoint(row2)):
        connections.append(j)
    all_connections.append(connections)
  return all_connections

def euler215(width, rows):
  all_rows = gen_row_permutations(width)
  all_connections = gen_possible_connections(all_rows)
  n_connections_per_depth = {}

  # print('All Possible Rows:', all_rows)
  # print('All Connections:', all_connections)
  
  # Calculate number of connections for depth of 2
  n_connections = []
  for connection in all_connections:
    n_connections.append(len(connection))
  print('Computed number of connections for a depth of 2')
  n_connections_per_depth[2] = n_connections

  for depth in range(3, rows+1):
    n_connections = []
    for i, row in enumerate(all_connections):
      n_connections_for_i = 0
      for j in all_connections[i]:
        n_connections_for_i += n_connections_per_depth[depth-1][j]
      n_connections.append(n_connections_for_i)
    print(f'Computed number of connections for a depth of {depth}')
    n_connections_per_depth[depth] = n_connections
  
  print('\n------------------------------------------------')
  print('Total Number of Possible Walls:', sum(n_connections_per_depth[depth]))

if __name__ == '__main__':
  euler215(32,10)
  