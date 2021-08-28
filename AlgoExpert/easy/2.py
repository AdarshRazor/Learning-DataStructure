# Average: O(Log(n)) | O(log(n))
# Worst: O(n) time | O(n) space

def findClosetValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest < tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

# Average: O(Log(n)) time | O(1) space 
# Worst: O(n) time | O(1) space

def findClosetValueInBst1(tree, target):
    return findClosestValueInBstHelper1(tree, target, float("inf"))

def findClosestValueInBstHelper1(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else:
            break
    return closest

'''
Check for the value in the root node 
If the value match then return or compare
if the closest if bigger than the difference of current node and target = move right
if the closest if smaller than the difference of current node and target = move left


            10
        5       15
    2       5 13    22
1               14

1. closest = inf | abs(node-target) = abs(10-12)=2
2. inf > 2 = move right = 15 and closest=2
3. abs(15-12)=3 > closest =2 | move left
4. abs(13-12)=1 < closest =2 | move right
'''