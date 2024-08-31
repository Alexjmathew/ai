def vacuum_world():
    final_goal_state = {'A': '0', 'B': '0'}
    cost = 0
    
    print("****WELCOME TO THE VACUUM WORLD****")
    
    location_input = input("Enter Location of Vacuum (A/B): ").upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ")
    status_input_complement = input(f"Enter status of other room (0 for Clean, 1 for Dirty): ")
    
    print("Here is MY status")
    
    if location_input == 'A':
        goal_state = {'A': status_input, 'B': status_input_complement}
        print("My Initial Location Condition is " + str(goal_state))
        
        if status_input == '1':
            print("I find location A is dirty so the dirt need to be sucked")
            print("SUCKING THE DIRT.....PLEASE WAIT...")
            cost += 1
            print("The cost after sucking the dirt in A is", str(cost))
            
            if status_input_complement == '1':
                print("I find B is dirty so the dirt need to be sucked")
                print("SUCKING THE DIRT.....PLEASE WAIT...")
                cost += 1
                print("B is clean now .... ")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
            else:
                print("Location B is clean so hence I am moving to A")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
        else:
            print("Location A is not dirty so moving to location B")
            if status_input_complement == '1':
                print("I find B is dirty so the dirt need to be sucked")
                print("SUCKING THE DIRT.....PLEASE WAIT...")
                cost += 1
                print("B is clean now .... ")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
            else:
                print("Location B is clean so hence I am moving to A")
                print("As both the rooms were clean i had no work..the goal state is already reached..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
    else:
        goal_state = {'A': status_input_complement, 'B': status_input}
        print("Initial Location Condition" + str(goal_state))
        
        if status_input == '1':
            print("I find location B is dirty so the dirt need to be sucked")
            print("SUCKING THE DIRT.....PLEASE WAIT...")
            cost += 1
            print("The cost after sucking the dirt in B is", str(cost))
            
            if status_input_complement == '1':
                print("I find A is dirty so the dirt need to be sucked")
                print("SUCKING THE DIRT.....PLEASE WAIT...")
                cost += 1
                print("A is clean now .... ")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
            else:
                print("Location A is clean so hence I am moving to B")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
        else:
            print("Location B is not dirty so moving to location A")
            if status_input_complement == '1':
                print("I find A is dirty so the dirt need to be sucked")
                print("SUCKING THE DIRT.....PLEASE WAIT .. ")
                cost += 1
                print("A is clean now .... ")
                print("I have completed the goal you have given me...the goal state is..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
            else:
                print("Location A is clean so hence I am moving to B")
                print("As both the rooms were clean i had no work..the goal state is already reached..", final_goal_state)
                print("So the total cost /the total performance measure is", str(cost))
                print("THANK YOU")
