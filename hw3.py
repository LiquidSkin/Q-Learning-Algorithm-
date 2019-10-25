from Dictionary import dict
from Dictionary import direct_dict
import random

states,actions = 16,4;
rewards_matrix = [[-10000 for x in range(actions)] for y in range(states)]
Qvalue_matrix = [[0 for x in range(actions)] for y in range(states)]
start_state = 1
gamma = 0.1
alpha = 0.1


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
    print("printing the value of the transition")
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
        qvalue = direct_dict[val]
        print(qvalue)
        qvalue_matrix = Qvalue_matrix[next_state][qvalue]
        if qvalue_matrix > max:
            max = qvalue_matrix

    print("the max value is")
    print(max)
    reward_transition = rewards_matrix[start_state][key_val]
    q_val_sub = alpha * (reward_transition + (gamma * max))
    print("the second part of the q value equation")
    print(q_val_sub)
    q_val = q_val + q_val_sub
    print("printing the Q Value of the state after transition")
    print(q_val)
    return q_val







def calculateQvalues(g1,g2,w,f):

    list=[]
    next_list = []
    start_new = str(start_state) + '-'
    for key in dict:
        if start_new in key and '11-' not in key:
            if dict[key] != -1:
                list.append(dict[key])

    print(list)
    print("printing the start state")
    print(start_state)
    next_state = random.choice(list)
    print("printing next state from start")
    print(next_state)
    val = str(start_state) + '-' + str(next_state)
    val_direct_dict = direct_dict[val]
    q_value = calculate_Individual_QValue(start_state,next_state)
    Qvalue_matrix[start_state][val_direct_dict] = q_value
    print("printing the coordinates of the q value matrix")
    print(start_state)
    print(val_direct_dict)

    print("The Q Value of the transition from start to next state")
    print("The two goal states and the next_state are")
    print(g1)
    print(g2)
    print(next_state)
    print(q_value)

    if next_state != g1 and next_state != g2:
        count = 0
        while
            print("Coming inside the while statement")
            next_state_str  = str(next_state) + '-'
            #print(next_state_str)
            next_not_state =  str(1) + str(next_state) + '-'
            #print(next_not_state)
            list =[]
            for key in dict:
                if next_state_str in key and next_not_state not in key and dict[key] != -1:
                    list.append(dict[key])

            #print(list)
            next_state = random.choice(list)
            print("printing next state")
            print(next_state)
            if next_state == g1 or next_state == g2:
                break
            list.clear()
            count = count + 1
            #print("printing after clearing list")
            #print(list)



def main():
    goal_number_one = int(input("Enter the first Goal Number"))
    goal_number_two = int(input("Enter the second Goal Number"))
    wall_number = int(input("Enter the cell number of the wall"))
    forbidden_number = int(input("Enter the forbidden cell's number"))
    variable_name = input("Enter p or q")
    variable_name = variable_name.strip()
    if variable_name == 'q':
       cell_number = int(input("Enter the cell number for which the q values must be found"))

    g1 = goal_number_one - 1
    g2 = goal_number_two - 1

    w = wall_number - 1
    f = forbidden_number - 1
    create_rewardsmatrix_emptystates(g1,g2,w,f)
    create_rewardsmatrix_rewards(g1,g2,w,f)
    create_rewardsmatrix_invalidstates()
    create_rewardsmatrix_livingstates()
    #print("printing the matrix indexes for testing")
    print(rewards_matrix)
    print("printing the Q Value Matrix")
    calculateQvalues(g1,g2,w,f)
    print(Qvalue_matrix)





if __name__ == "__main__":
    main()