from pyamaze import maze, agent, textLabel

treasure_hunt = maze(5,5) #size 
treasure_hunt.CreateMaze()


def search_algorithm(treasure_hunt, algorithm_choice):
    if algorithm_choice == "DFS":
        start = (treasure_hunt.rows, treasure_hunt.cols)
        closed = [start] 
        open_set = [start] 
        search_path = {}
        dSearch = []
        while len(open_set) > 0:
            current_node = open_set.pop()
            dSearch.append(current_node)
            if current_node == (1, 1):
                break
            for user_input_direction in 'NSEW':
                if treasure_hunt.maze_map[current_node][user_input_direction]:
                    if user_input_direction == 'N':
                        child = (current_node[0] - 1, current_node[1])
                    if user_input_direction == 'S':
                        child = (current_node[0] + 1, current_node[1])
                    if user_input_direction == 'E':
                        child = (current_node[0], current_node[1] + 1)
                    if user_input_direction == 'W':
                        child = (current_node[0], current_node[1] - 1)
                    if child in closed:
                        continue
                    closed.append(child)
                    open_set.append(child)
                    search_path[child] = current_node
                    print(search_path)
                    
        reverse_path = {}
        node = (1, 1)
        while node != start:
            reverse_path[search_path[node]] = node
            node = search_path[node]
            print(node)
        return search_path, reverse_path

    elif algorithm_choice == "BFS":
        start = (treasure_hunt.rows, treasure_hunt.cols)
        closed = [start]
        open_set = [start]
        search_path = {}
        dSearch = []
        while len(open_set) > 0:
            current_node = open_set.pop(0)
            dSearch.append(current_node)
            if current_node == (1,1):
                break
            for user_input_direction in 'NSEW':
                if treasure_hunt.maze_map[current_node][user_input_direction]:
                    if user_input_direction == 'N':
                        child = (current_node[0] - 1, current_node[1])
                    if user_input_direction == 'S':
                        child = (current_node[0] + 1, current_node[1])
                    if user_input_direction == 'E':
                        child = (current_node[0], current_node[1] + 1)
                    if user_input_direction == 'W':
                        child = (current_node[0], current_node[1] - 1)
                    if child in closed:
                        continue
                    closed.append(child)
                    open_set.append(child)
                    search_path[child] = current_node
                    print(search_path)
        reverse_path = {}
        node = (1,1)
        while node != start:
            reverse_path[search_path[node]] = node
            node = search_path[node]
            print(node)
        return search_path, reverse_path

    else:
        print("Invalid algorithm choice.")
        return None, None


algorithm_choice = input("Enter the algorithm choice (DFS or BFS): ")
search_path, reverse_path = search_algorithm(treasure_hunt, algorithm_choice)

search_path_treasure = agent(treasure_hunt,1,1,goal=(5,5),footprints=True,filled=treasure_hunt, color="yellow")
reversPath_treasure = agent(treasure_hunt,5,5,footprints=True,color="black")

treasure_hunt.tracePath({search_path_treasure:search_path})
treasure_hunt.tracePath({reversPath_treasure:reverse_path})
l=textLabel(treasure_hunt,'You found treasure_hunt, via Length of Shortest Path',len(reverse_path)+1)

treasure_hunt.run()