from sys import argv

def input_analyzer(): #makes the data entered into the system accesible via indexing.
    with open(argv[1], 'r') as f:
        content = f.read() #content= given data
        lines = content.strip().split('\n')
    costs = [int(a) for a in lines[0].split()] #assign the first row of data as cost values
    map = [] #includes input data without cost values
    for l in lines[1:]:
        map.append([int(x) for x in l.split()])
    return costs, map

def cost_calculator(costs, map, x, y): #function that calculates the cost of the cell
    row = len(map)
    column = len(map[0])
    direction = [(-1,0),(1,0),(0,-1),(0,1)] #up,down,left,right
    diagonal = [(-1,-1),(-1,1),(1,-1),(1,1)] #top-left,top-right,bottom-left,bottom-right
    sinkhole = 0 #upper,lower,left,right sinkhole controller
    for a,b in direction:
        temp_x = x + a
        temp_y = y + b
        if 0 <= temp_x < row and 0 <= temp_y < column:
            if map[temp_x][temp_y] == 0:
                sinkhole = 1 #if there is a 0 in the right,left,bottom, or top, updates the sinkhole to 1
                break
    diagonal_sinkhole = 0 #diagonal sinkhole controller
    for a,b in diagonal:
        temp2_x = x + a
        temp2_y = y + b
        if 0 <= temp2_x < row and 0 <= temp2_y < column:
            if map[temp2_x][temp2_y] == 0:
                diagonal_sinkhole = 1 #if there is a 0 in the diagonal, updates diagonal_sinkhole to 1
                break
    if sinkhole == 1:
        return costs[2] # if there is a sinkhole in the right,left,bottom and top, it returns cost3
    elif diagonal_sinkhole == 1:
        return costs[1] #if there is a sinkhole in the diagonal, it returns cost2
    else:
        return costs[0] # else it returns cost1

def path_finder(costs, map, x, y, temporary_cost, min_cost, temporary_path, path, visited_cell): #function that finds the route
    column = len(map[0])
    row = len(map)
    first_cell_cost = cost_calculator(costs, map, x, y) #calculates the cost of the first cell of the line
    temporary_cost += first_cell_cost #temporary_cost includes total cost of the temporary path
    visited_cell.add((x, y))
    temporary_path.append((x, y)) #temporray_path includes all cells in the temporary route
    if y == column-1:
        if temporary_cost < min_cost[0]: #if temporary cost smaller than min_cost, assign it as  best toute until now and update min_cost
            min_cost[0] = temporary_cost
            path.clear()
            path.extend(temporary_path)
        visited_cell.remove((x, y))
        temporary_path.pop()
        return
    movement_order = [(0,1),(-1,0),(1,0),(0,-1)] #right,up,down,left
    for x1,y1 in movement_order: #it checks the right,up,down and left cells in order.
        new_x = x + x1
        new_y = y + y1
        if (
            0 <= new_x < row
            and 0 <= new_y < column
            and map[new_x][new_y] == 1
            and (new_x, new_y) not in visited_cell
        ):
            path_finder(costs, map, new_x, new_y, temporary_cost, min_cost, temporary_path, path, visited_cell)
            #if new cell is 1, hasn't been visited before and is within the index,it calls path_finder function for that cell.
            #it creates a recursion that performs the same operation for each cell.
    visited_cell.remove((x, y))
    temporary_path.pop()

def main():
    with open(argv[2], 'w') as output:
        costs, map = input_analyzer()
        rows = len(map)
        columns = len(map[0])
        min_cost = [float('inf')] #at the beginning min_cost has infinite value
        path = []
        for i  in range(rows):
            if map[i][0] == 1:
                visited_cell = {(i,0)}
                path_finder(costs, map, i, 0, 0, min_cost, [(i,0)], path, visited_cell)
        if not path: #if it can't find a route
            output.write("There is no possible route!")
        else:
            output.write(f"Cost of the route: {min_cost[0]}\n")
            for k in range(rows):
                for l in range(columns):
                    if (k,l) in path: #if this cell in the selected route, writes x instead of that
                        output.write("X ")
                    else:
                        output.write(f"{map[k][l]} ")
                if k != rows - 1:
                    output.write("\n") #satır atlar

if __name__ == "__main__":
    main()