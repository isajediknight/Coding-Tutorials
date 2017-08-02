my_list = ['Monday','Tuesday']
my_list.append('Wednessday')

my_dict = {}
my_dict['Goku'] = 'Green'
my_dict['Vegita'] = 'Blue'
my_dict['Freeza'] = 'Red'
my_dict['Gohan'] = 'Yellow'

my_tuple = (('May',31),('June',30),('July',31))

my_string = 'Hello World!'

my_int = 10

my_float = 7.6

def how_to_loop_through_datatypes(my_data,loop_type):
    """
    Example of how to loop through and print the data
    """
    my_type = type(my_data)
    if(loop_type == 'for'):
        if(my_type == type((''))):
            for x in range(len(my_data)):
                print(my_data[x],end='')
            print('')
        elif(my_type == type((0,0))):
            for x in range(len(my_data)):
                print(my_data[x])
        elif(my_type == type([])):
            which = input("1) my_data[x]\n2) my_data.pop(0)\n3) my_data.pop(-1)\n--------------\nChoice: ")
            print("")
            if(which == '1'):
                for x in range(len(my_data)):
                    print(my_data[x])
            elif(which == '2'):
                for x in range(len(my_data)):
                    print(x,' ',end='')
                    print(my_data.pop(0))
            elif(which == '3'):
                for x in range(len(my_data)):
                    print(x,' ',end='')
                    print(my_data.pop(-1))
        elif(my_type == type({})):
            which = input("Loop through as?\n1) Keys\n2) List of Keys\n3) Print Keys Alphabetically\n--------------\nChoice: ")
            if(which == '1'):
                for x in my_dict.keys():
                    print('Key: ',x,'\t\tValue:\t',my_dict[x])
            elif(which == '2'):
                for x in list(my_dict.keys()):
                    print('Key: ',x,'\t\tValue:\t',my_dict[x])
            elif(which == '3'):
                for x in sorted(list(my_dict.keys())):
                    print('Key: ',x,'\t\tValue:\t',my_dict[x])
    print('--------------')

def index_check(my_data):
    if(my_type == type({})):
        search = input('Enter Key to search for: ')
        
# pass by value vs pass by reference
