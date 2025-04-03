def votes(lst):
    count_votes={}
    for name in lst:
        if name in count_votes:
            count_votes[name]+=1
        else:
            count_votes[name]=1 
    max_votes=max(count_votes.values());       
    winner=[key for key in count_votes if count_votes[key]==max_votes]
    print("Winner is ",min(winner))        
names=["Rahul","raminder","Rahul","raminder","Sam","John"]    
votes(names)

