'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph.keys():
        from_member_dict = social_graph.get(from_member)
        from_member_following_list = from_member_dict.get("following")
        to_member_dict = social_graph.get(to_member)
        to_member_following_list = to_member_dict.get("following")
        if to_member in from_member_following_list and from_member in to_member_following_list:
            return "friends"
        if to_member in from_member_following_list:
            return "follower"
        if from_member in to_member_following_list:
            return "followed by"  
        else:
            return "no relationship"
        
def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    rows = len(board)
    counter_list = list(range(0,rows))
    characters = ["X","O"]
    
    column1X = 0
    column2X = 0
    column3X = 0
    column4X = 0
    column5X = 0
    column6X = 0
    column1O = 0
    column2O = 0
    column3O = 0
    column4O = 0
    column5O = 0
    column6O = 0

    Xs=[column1X,column2X,column3X,column4X,column5X,column6X]
    Os=[column1O,column2O,column3O,column4O,column5O,column6O]

    for row in board:
        if row.count("X") == rows:
            return "X"
        if row.count("O") == rows:
            return "O"

    for row in board:
        if rows > 0:
            if row[0] == "X":
                column1X += 1
            if row[0] == "O":
                column1O += 1
        if rows > 1:
            if row[1] == "X":
                column2X += 1
            if row[1] == "O":
                column2O += 1
        if rows > 2:
            if row[2] == "X":
                column3X += 1
            if row[2] == "O":
                column3O += 1
        if rows > 3:
            if row[3] == "X":
                column4X += 1
            if row[3] == "O":
                column4O += 1
        if rows > 4:
            if row[4] == "X":
                column5X += 1
            if row[4] == "O":
                column5O += 1
        if rows > 5:
            if row[5] == "X":
                column6X += 1
            if row[5] == "O":
                column6O += 1
                
    if column1X == rows:
        return "X"
    if column2X == rows:
        return "X"
    if column3X == rows:
        return "X"
    if column4X == rows:
        return "X"
    if column5X == rows:
        return "X"
    if column6X == rows:
        return "X"
    if column1O == rows:
        return "O"
    if column2O == rows:
        return "O"
    if column3O == rows:
        return "O"
    if column4O == rows:
        return "O"
    if column5O == rows:
        return "O"
    if column6O == rows:
        return "O"

    diagonal1 = ["d00","d11","d22","d33","d44","d55"]
    if rows == 6:
        diagonal2 = ["d05","d14","d23","d32","d41","d50"]
    if rows == 5:
        diagonal2 = ["d04","d13","d22","d31","d40"]
    if rows == 4:
        diagonal2 = ["d03","d12","d21","d30"]
    if rows == 3:
        diagonal2 = ["d02","d11","d20"]

    diagonal1X = 0
    diagonal1O = 0
    diagonal2X = 0
    diagonal2O = 0

    count = 1
    

    for item in diagonal1:
        row = int(item[1])
        column = int(item[2])
        if board[row][column] == "X":
            diagonal1X += 1
        if board[row][column] == "O":
            diagonal1O += 1
        count += 1
        if count > rows:
            break

    for item in diagonal2:
        row = int(item[1])
        column = int(item[2]) 
        if board[row][column] == "X":
            diagonal2X += 1
        if board[row][column] == "O":
            diagonal2O += 1
        count += 1

    if diagonal1X == rows:
        return "X"
    if diagonal2X == rows:
        return "X"
    if diagonal1O == rows:
        return "O"
    if diagonal2O == rows:
        return "O"
    else:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    # if route is only one stop
    input_tuple = (first_stop, second_stop)
    if input_tuple in route_map:
        return route_map[input_tuple]["travel_time_mins"]

    # if route will take multiple stops
    start = []
    end = []
    times = []
    time = 0
    count = 0
    for stops in route_map.keys():
        start.append(stops[0])
    for stops in route_map.keys():
        end.append(stops[1])
    for duration in route_map.values():
        times.append(duration["travel_time_mins"])
    
    first_stop_num = start.index(first_stop)
    second_stop_num = end.index(second_stop)

    if second_stop_num < first_stop_num:
        second_stop_num += len(start)
        start += start
        end += end
        times += times

    length_of_trip = second_stop_num - first_stop_num + 1
    start_time = first_stop_num

    if length_of_trip == 0:
        for item in times:
            time += item
    
    while count < length_of_trip:
        time += times[start_time]
        start_time += 1
        count += 1
    
    return(time)