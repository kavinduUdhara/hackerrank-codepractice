def climbingLeaderboard(ranked, player):
    #take distinct values O(n) complexity
    rank_dict = {}
    rank_arr = []
    count = 0
    for rank in ranked:
        if rank not in rank_dict:
            count += 1
            rank_dict[rank] = count
            rank_arr.append(rank)
    
    result = []
    
    print(rank_arr)
    print(rank_dict)
    for play in player:
        start = 0
        end = len(rank_arr)
        print("______________________________________________")
        while(start != end):
            middle = (start + end) // 2
            print(f"s {start} | e {end} | m {middle} | rank_arr[middle] {rank_arr[middle]} | play {play}")
            if rank_arr[middle] == play:
                start = end
                result.append(rank_dict[play])
            elif rank_arr[middle] > play:
                start = middle + 1
            elif rank_arr[middle] < play:
                end = middle - 1
            if start == end or start == middle:
                print(f"s -- e : s {start} | e {end} | m {middle} | rank_arr[middle] {rank_arr[middle]} | play {play}")
                play_rank = rank_arr[middle]
                real_play_rank = rank_dict[play_rank]
                if play > play_rank:
                    if real_play_rank - 1 == 0:
                        result.append(real_play_rank)
                    else:
                        result.append(real_play_rank - 1)
                elif play < play_rank:
                    result.append(real_play_rank + 1)
                else:
                    result.append(real_play_rank)
                break
    print(result)

climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])