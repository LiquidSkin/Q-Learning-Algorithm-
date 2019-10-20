from Dictionary import dict
states,actions = 16,4;
rewards_matrix = [[-10000 for x in range(actions)] for y in range(states)]


def create_rewardsmatrix_emptystates(g,w,f):
    for i in range(16):
        for j in range(4):
            if i == g or i == w or i == f:
                rewards_matrix[i][j] = 0


def create_rewardsmatrix_rewards(g,w,f):
    for i in range(16):
        for j in range(4):
            val = str(i) + '-' + str(j)
            if dict[val] == g:
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




def main():
    goal_number = int(input("Enter the Goal Number"))
    wall_number = int(input("Enter the cell number of the wall"))
    forbidden_number = int(input("Enter the forbidden cell's number"))
    variable_name = input("Enter p or q")
    variable_name = variable_name.strip()
    if variable_name == 'q':
       cell_number = int(input("Enter the cell number for which the q values must be found"))

    goal_number = goal_number - 1
    wall_number = wall_number - 1
    forbidden_number = forbidden_number - 1
    create_rewardsmatrix_emptystates(goal_number,wall_number,forbidden_number)
    create_rewardsmatrix_rewards(goal_number,wall_number,forbidden_number)
    create_rewardsmatrix_invalidstates()
    #print("printing the matrix indexes for testing")
    print(rewards_matrix)




if __name__ == "__main__":
    main()