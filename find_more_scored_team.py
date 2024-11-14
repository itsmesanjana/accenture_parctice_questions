def find_winning_team(goals):
    goal_list=goals.split()

    teamA_goals=goal_list.count("TeamA")
    teamB_goals=goal_list.count("TeamB")

    if teamA_goals>teamB_goals:
        return "TeamA"
    elif teamB_goals>teamA_goals:
        return "TeamB"
    else:
        return "Draw"  # or return None, depending on your requirements

goals="TeamA TeamB TeamB TeamA TeamB TeamA TeamB"
print("The team that scored more goals is:", find_winning_team(goals))
    
    