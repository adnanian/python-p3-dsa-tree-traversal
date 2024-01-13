class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    pass
    node = self.root
    nodes_to_visit = [node]
    
    while len(nodes_to_visit) > 0:
      if node['id'] == id:
        return node
      node = nodes_to_visit.pop(0)
      nodes_to_visit = node['children'] + nodes_to_visit
    return None
      
  
def breadth_first_traversal(node):
    result = []
    nodes_to_visit = [node]
    
    while len(nodes_to_visit) > 0:
      # traverse our node
        
      # 1. Remove the first node from the nodes_to_visit list
      node = nodes_to_visit.pop(0)
      # 2. Add its value to the result list
      result.append(node['value'])
      # 3. Add its children (if any) to the END of the 'nodes_to_visit' lsit
      nodes_to_visit = nodes_to_visit + node['children']
    return result
  
def depth_first_traversal(node, result = []):
  # visit each node (add it to the list of results)
  result.append(node['value'])
  for child in node['children']:
    # visit each child node
    depth_first_traversal(child, result)

  return result

child_1 = {
  'value': 2,
  'children': []
}

child_2 = {
  'value': 3,
  'children': []
}

child_3 = {
  'value': 4,
  'children': []
}

root = {
  'value': 1,
  'children': [child_1, child_2, child_3]
}

print(breadth_first_traversal(root))