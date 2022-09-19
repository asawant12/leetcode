
input = {
    'A' : ['G','B', 'D'],
    'B' : ['C', 'E'],
    'C' : ['E', 'D'],
    'G' : ['C', 'B']
}

# 'E' --> 'D' --> 'C' --> 'B' --> 'G' --> 'A'


ans = []


#for package in input:

#for each dependency in package (def helper)
    #check if the dependency exists in input as key
        #if it exists in input as key:
            #helper(value)
        #if it doesn't exist in input as key:
            #if not in ans:
                #ans.append(val)
            #if in ans: 
                #dependency is met

                
def add_to_ans(x):
    for j, dependency in enumerate(input[x]):
        if dependency in input:
            add_to_ans(dependency)
        if dependency not in input:
            if dependency not in ans:
                ans.append(dependency)
    if x not in ans:
        ans.append(x)                
                
                
for i, pkg in enumerate(input):
   add_to_ans(pkg)

print(ans)




    

                
                
