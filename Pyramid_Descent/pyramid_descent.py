def convert_to_list(pyramid):
    for i in range(len(pyramid)):
        pyramid[i] = pyramid[i].replace('\n', '').replace(',', ' ')

        #Using split():
        # pyramid[i] = pyramid[i].split()
        # pyramid[i] = [int(num) for num in pyramid[i]]

        #Manual parsing and cast to int
        curr_list = []
        length = len(pyramid[i])
        num = ''
        for j in range(length):
            curr = pyramid[i][j]
            if curr != ' ' and j != length-1:
                num += curr
            elif j == length-1:
                num += curr
                curr_list.append(int(num))
                num = ''
            elif curr == ' ':
                curr_list.append(int(num))
                num = ''
        pyramid[i] = curr_list
    return pyramid

def pyramid_Descent(path, pyramid, target, row, col, val):
    #Calculate the product of running product and current node
    val *= pyramid[row][col]
    
    #If on the last row, check if the new val == target
    if row == len(pyramid)-1:
        #Return correct path if value is correct
        if val == target:
            return True, path
        #Invalidate outcome if incorrect
        else:
            return False, []
    
    #If product is greater than target, invalidate path
    if val > target:
        return False, []
    
    #Test left with 'L' added to path; don't decrement col for left b/c each succeeding row has 1 more value at the end of the list
    valid_left, left_path = pyramid_Descent(path+['L'], pyramid, target, row+1, col, val)
    #Test right with 'R' added to path
    valid_right, right_path = pyramid_Descent(path+['R'], pyramid, target, row+1, col+1, val)
    
    if valid_left:
        return True, left_path
    if valid_right:
        return True, right_path
    return False, []

def main():
    #Read in the pyramid from a file named pyramid_input.txt with the target value and pyramid
    with open('pyramid_input.txt') as input_file:
        pyramid = input_file.readlines()
    #Extract the target value from the 1st line of input
    target = int(pyramid[0][8:])
    #Remove target line from pyramid
    pyramid = pyramid[1:]
    #Remove newlines and make each layer into list of ints
    convert_to_list(pyramid)
    #Perform pyramid descent
    path = []
    val = 1
    row = col = 0
    path_found, path = pyramid_Descent(path, pyramid, target, row, col, val)
    #If path exists, print path to standard output and create an output file with the path named pyramid_output.txt
    if path_found:
        print(path)
        output_file = open('pyramid_output.txt', 'w+')
        for node in path:
            output_file.write(node)
        output_file.close()

main()