f = open('24-2-3.txt').read().split('\n')

tree_data = f

bst = []
tree = {}
for statement in tree_data:
    branch, subbranches = statement.split(":")
    branch = branch.strip()
    subbranches = [sub.strip() for sub in subbranches.split(",")]
    tree[branch] = subbranches

def find_at_sign(tree):
    stack = [['RR',0,'R']] 
    while stack:
        node = stack.pop()
        for subbranch in tree.get(node[0], []):    
            if((subbranch != 'ANT') and (subbranch != 'BUG')):
                if subbranch in tree:                
                    if(subbranch != '@'):
                        stack.append([subbranch,node[1]+1,node[2]+subbranch[0]])
                if(subbranch == '@'):       
                    bst.append([node[1],node[2] +'@'])
                    
    
    return "No '@' found in the tree"

result = find_at_sign(tree)
best = -1
for i in range(len(bst)):    
    ct = 0
    for j in range(len(bst)):
        if(i != j):
            if(bst[i][0] == bst[j][0]):
                ct += 1
    if (ct == 0):        
        best = i

print('part 3 - ',bst[best][1])
