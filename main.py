class Node:
    def __init__(self, label="#", flag=[], children=[]):
        self.label = label
        self.flag = flag
        self.children = children
def addString(pattern, pattern_index):
    currentNode = root
    for index in xrange(len(pattern)):
        existChildNode = next((child for child in currentNode.children if child.label==pattern[index]), None)
        if existChildNode == None:
            currentNode.children.append(Node(label=pattern[index],flag=[],children=[]))
            currentNode = currentNode.children[-1];
        else:
            currentNode = existChildNode
    currentNode.flag.append(pattern_index)
def findString(keyword):
    currentNode = root
    suggestions = []
    for index in xrange(len(keyword)):
        if any(child.label==keyword[index] for child in currentNode.children) == False:
            return suggestions
        currentNode = [child for child in currentNode.children if child.label==keyword[index]][0]
    return getFlagsFromCurrentNode(currentNode)
def getFlagsFromCurrentNode(currentNode):
    flags = []
    if(len(currentNode.flag)>0):
        flags.extend(currentNode.flag)
    if(len(currentNode.children)>0):
        for childNode in currentNode.children:
            flags.extend(getFlagsFromCurrentNode(childNode))
    return flags

patterns = ["maf", "mixyzu", "mw"]
root = Node()
for index in xrange(len(patterns)):
    addString(patterns[index], index)
print(findString("mw"))