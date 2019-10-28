from Dictionary import dict
from Dictionary import direct_dict
import random

states,actions = 16,4;
rewards_matrix = [[-10000 for x in range(actions)] for y in range(states)]
Qvalue_matrix = [[0 for x in range(actions)] for y in range(states)]
start_state = 1
gamma = 0.1
alpha = 0.1
flag = None
route_path = []
first_goal_path = []
second_goal_path = []

def create_rewardsmatrix_emptystates(g1,g2,w,f):
    for i in range(16):
        for j in range(4):
            if i == g1 or i == g2 or i == w or i == f:
                rewards_matrix[i][j] = 0


def create_rewardsmatrix_rewards(g1,g2,w,f):
    for i in range(16):
        for j in range(4):
            val = str(i) + '-' + str(j)
            if dict[val] == g1 or dict[val] == g2:
                rewards_matrix[i][j] = 100
            elif dict[val] == w:
                rewards_matrix[i][j] = -0.1
            elif dict[val] == f:
                rewards_matrix[i][j] = -100


def create_rewardsmatrix_invalidstates():
    for i in range(16):
        for j in range(4):
            val = str(i) + '-' + str(j)
            if dict[val] == -1:
                rewards_matrix[i][j] = None


def create_rewardsmatrix_livingstates():
    for i in range(16):
        for j in range(4):
            if rewards_matrix[i][j] == -10000:
                rewards_matrix[i][j] = -0.1


def calculate_Individual_QValue(start_state,next_state):

    next_state_list = []
    val = str(start_state) + '-' + str(next_state)
    print(val)
    key_val = direct_dict[val]
    print("printing the direction of the transition")
    print(key_val)
    print("printing q value matrix of transition direction")
    print(Qvalue_matrix[start_state][key_val])
    qvalue_transition = Qvalue_matrix[start_state][key_val]
    print("printing reward value of the transition")
    print(rewards_matrix[start_state][key_val])
    q_val = (1-alpha) * (qvalue_transition)
    next_val = str(next_state) + '-'
    next_not_val = str(1) + str(next_state) + '-'
    for key in dict:
        if next_val in key and  next_not_val not in key and dict[key] != -1:
            next_state_list.append(dict[key])

    print("printing next state in the second function")
    print(next_state)


    max  = -100000
    for item in next_state_list:
        print("printing next next states")
        val = str(next_state) + '-' + str(item)
        print(val)
        qvalue_direction = direct_dict[val]
        print(qvalue_direction)
        qvalue_matrix = Qvalue_matrix[next_state][qvalue_direction]
        if qvalue_matrix > max:
            max = qvalue_matrix

    print("the max value is")
    print(max)
    print("printing rewards matrix values")
    print(rewards_matrix[start_state][key_val])
    reward_transition = rewards_matrix[start_state][key_val]
    print(reward_transition)
    q_val_sub = alpha * (reward_transition + (gamma * max))
    print("the second part of the q value equation")
    print(q_val_sub)
    q_val = round(q_val + q_val_sub,2)
    print("printing the Q Value of the state after transition")
    print(q_val)
    return q_val


def calculate_individual_qvalues(g1,g2,w,f):
    for i in range(10000):
     print("printing the value of i")
     print(i)
     list=[]
     next_list = []
     start_new = str(start_state) + '-'
     # Get the neighbours of the start state.
     for key in dict:
         if start_new in key and '11-' not in key:
             if dict[key] != -1:
                 list.append(dict[key])

     print(list)
     if w in list:
         list.remove(w)
     print("printing the start state")
     print(start_state)
     next_state = random.choice(list)


     print("printing next state from start")
     print(next_state)
     #Get the Direction of Transition from the start state to next state from the direction matrix.
     val = str(start_state) + '-' + str(next_state)
     val_direct_dict = direct_dict[val]
         #Calculate the Q Value of the transition from the start state to the next state
     q_value = calculate_Individual_QValue(start_state,next_state)
     Qvalue_matrix[start_state][val_direct_dict] = q_value
     print("printing the coordinates of the q value matrix")
     print(start_state)
     print(val_direct_dict)
     print("The Q Value of the transition from start to next state")
     print("The two goal states and the next_state are")
     print(next_state)
     print(q_value)
     #Terminate if the immediate next state is either of the two goals.
     if next_state != g1 and next_state != g2:
         while True:
             print("Coming inside the while statement")
             print("printing the next state inside the while loop")
             print(next_state)
             #Added an extra check to see whether the next state
             if next_state == g1 or next_state == g2:
                 print("reached the goal at the very next step" + " "  + str(next_state))
                 break

             next_state_str  = str(next_state) + '-'
             #print(next_state_str)
             next_not_state =  str(1) + str(next_state) + '-'
             #print(next_not_state)
             #Get the next possible transitions from the next state
             list =[]
             for key in dict:
                 if next_state_str in key and next_not_state not in key and dict[key] != -1:
                     list.append(dict[key])


             print(list)
             if w in list:
                 list.remove(w)

             #Choose a random next transition
             next_next_state = random.choice(list)
             print("printing next next state")
             print(next_next_state)
             print(i)
             print("the current and next states are")
             print(next_state)
             print(next_next_state)
             val = str(next_state) + '-' + str(next_next_state)
             print(val)
             val_direct_dict = direct_dict[val]
             print("The direction of the transition to the next state")
             print(val_direct_dict)

             #Calculate the Q Value of the transition from the next state which is assigned as current state and the next state of the next state
             q_val = calculate_Individual_QValue(next_state,next_next_state)

             #Assign the Q Value to the transition
             Qvalue_matrix[next_state][val_direct_dict] = q_val
             #Important Step = assign the next transition of the next state as the next state so that the loop keeps repeating until the goal is reached
             next_state = next_next_state

             #If the next state of the next state is the goal, break the loop
             if next_next_state == g1 or next_state == g2:
                 print("reached the goal" + " " + str(next_next_state))
                 break

             #Clear the list to eliminate all the values.
             list.clear()
            #count = count + 1
            #print("printing after clearing list")
            #print(list)

def getQValues(cell_no):
    cell_no = cell_no - 1
    for i in range(16):
        for j in range(4):
            if i == cell_no and j == 0:
                print("Going Up" + " " + str(Qvalue_matrix[cell_no][j]))
            if i == cell_no and j == 1:
                print("Going Down" + " " + str(Qvalue_matrix[cell_no][j]))
            if i == cell_no and j == 2:
                print("Going Left(<-)" + " " + str(Qvalue_matrix[cell_no][j]))
            if i == cell_no and j == 3:
                print("Going Right(->)" + " " + str(Qvalue_matrix[cell_no][j]))


def get_best_path_one(start_state,g1,w):
    first_goal_path.append(start_state)
    print("Printing the goal state inside the function")
    print(g1)
    best_path = []
    best_path.append(start_state)
    max = -10000
    nextval = None
    for i in range(1,2):
        for j in range(4):
            if(i == 1):
                value = Qvalue_matrix[1][j]
                if value > max and j != 1 and dict[str(1) + '-' + str(j)] != w:
                    max = value
                    nextval = j

    best_path_val = dict[str(start_state) + '-' + str(nextval)]
    best_path.append(best_path_val)
    first_goal_path.append(best_path_val)
    route_path.append(str(start_state) + '-' + str(nextval))
    route_path.append(nextval)
    print("printing the route part")
    print(route_path)
    print(best_path)
    max = -1000000000
    count = 0
    path_trace= []
    while True:
        print("coming inside path tracer")
        for i in range(best_path_val,best_path_val+1):
            for j in range(4):
                if i == best_path_val:
                    value = Qvalue_matrix[best_path_val][j]
                    if value > max and dict[str(best_path_val) + '-' + str(j)] != -1 and dict[str(best_path_val) + '-' + str(j)] not in path_trace and dict[str(best_path_val) + '-' + str(j)] != w:
                        max = value
                        nextval = j
                        print("the direction to go is")
                        print(nextval)

        print("printing the best path value and the next value")
        print(best_path_val)
        if best_path_val == g1:
            break
        path_trace.append(best_path_val)
        print(nextval)
        best_val = dict[str(best_path_val) + '-' + str(nextval)]
        print("The next state from previous state is")
        print(best_val)
        first_goal_path.append(best_val)
        best_path_val = best_val
        max = -100000

def get_best_path_two(start_state,g2,w):
    print("Printing the second goal state inside the function")
    print(g2)
    best_path = []
    best_path.append(start_state)
    max = -10000
    nextval = None
    for i in range(1,2):
        for j in range(4):
            if(i == 1):
                value = Qvalue_matrix[1][j]
                if value > max and j != 1:
                    max = value
                    nextval = j

    best_path_val = dict[str(start_state) + '-' + str(nextval)]
    best_path.append(best_path_val)
    route_path.append(str(start_state) + '-' + str(nextval))
    route_path.append(nextval)
    print("printing the route part")
    print(route_path)
    print(best_path)
    max = -1000000000
    count = 0
    path_trace= []
    while True:
        print("coming inside path tracer")
        for i in range(best_path_val,best_path_val+1):
            for j in range(4):
                if i == best_path_val:
                    value = Qvalue_matrix[best_path_val][j]
                    if value > max and dict[str(best_path_val) + '-' + str(j)] != -1 and dict[str(best_path_val) + '-' + str(j)] not in path_trace and  dict[str(best_path_val) + '-' + str(j)] != w:
                        max = value
                        nextval = j
                        print("the direction to go is")
                        print(nextval)

        print("printing the best path value and the next value")
        print(best_path_val)
        if best_path_val == g2:
            break
        path_trace.append(best_path_val)
        print(nextval)
        best_val = dict[str(best_path_val) + '-' + str(nextval)]
        print("The next state from previous state is")
        print(best_val)
        best_path_val = best_val
        max = -100000
        count = count + 1





def main():
    # Enter the Inputs
    goal_number_one = int(input("Enter the first Goal Number"))
    goal_number_two = int(input("Enter the second Goal Number"))
    wall_number = int(input("Enter the cell number of the wall"))
    forbidden_number = int(input("Enter the forbidden cell's number"))
    variable_name = input("Enter p or q")
    variable_name = variable_name.strip()
    if variable_name == 'q':
       cell_number = int(input("Enter the cell number for which the q values must be found"))

    # Subtraction to align with indices of arrays and matrices
    g1 = goal_number_one - 1
    g2 = goal_number_two - 1
    w = wall_number - 1
    f = forbidden_number - 1

    #Create Rewards Matrix from the inputs obtained
    create_rewardsmatrix_emptystates(g1,g2,w,f)
    create_rewardsmatrix_rewards(g1,g2,w,f)
    create_rewardsmatrix_invalidstates()
    create_rewardsmatrix_livingstates()
    #print("printing the matrix indexes for testing")
    print(rewards_matrix)
    #Calculate Q Values from the given inputs
    calculate_individual_qvalues(g1,g2,w,f)
    print(Qvalue_matrix)
    if variable_name == 'q':
        print("printing the input Q Values of all the four states")
        getQValues(cell_number)
    if variable_name == 'p':
        print("Printing the best path from the start to the goal states")
        get_best_path_one(start_state,g1,w)
        print(first_goal_path)
        #get_best_path_two(start_state,g2,w)





if __name__ == "__main__":
    main()