print("NID Number Management System\n")
_NID_lst ={}


def view(_input):
    print("Here is a chart:\n")
    if len(_NID_lst) == 0:
        print("Empty")
    else:
        if len(_input) == 2:
            print(f"{_input[-1]} : {_NID_lst[_input[-1]]}")
        else:
            for _name, _NID in _NID_lst.items():
                print(f"{_name} : {_NID}")
    print("")

def insert(_input):
    global _NID_lst
    if len(_input) == 2:
        _input.append("0")
    _input[-1] = ''.join([x for x in _input[-1] if x.isnumeric()])
    if _input[-1] == '':
        print("Error!")
        return ""
    _NID_lst[_input[1]] = _input[-1]
    print("")


def discard(_input):
    global _NID_lst
    if _input[-1] == "All":
        _NID_lst = {}
    else:
        _NID_lst.pop(_input[1])
    print("")

def update(_input):
    global _NID_lst
    _NID_lst.update({_input[1] : ''.join([x for x in _input[-1] if x.isnumeric()])})
    print("")

while True:
    try:
        _input= input("Write down a command (Write 'Help' for a list of commands and its arrangement): ").strip()
        _input = _input.replace("/", "")
        _input = _input.replace("to", "")
        _input = _input.replace("with", "")
        _input = _input.split(" ")
        _iter = 0

        for _index in _input:
            if _index == '':
                _input.pop(_iter)
            else:
                pass
            _iter += 1
        _command = _input[0]

        if _command.lower() == "help":
            print("""[CmdName] : [Syntax] (what to write to execute. not case sensitive except for discard method. SPACING IS A MUST)
                   ____________________________________________________________________________________________________
                   | Help (Shows a list of Cmd) : Help; 
                   | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                   | About (about this management system) : About;
                   | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                   | View (Shows NID numbers with names) : (View /name/) or (View) to see all; (eg..  View Riddhi  ;  View)
                   | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                   | Insert (Inputs a NID number) : Insert /name/ with /Nid Number/; (eg..  Insert Riddhi with 01234   )
                   | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                   | Discard (Removes a specified NID number of a person) : (Discard /name/) or (Discard All) to erase all (can only be exactly "All" );
                   | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                   | Update (Updates a NID number into another number) : Update /Name/ into /Nid Number/ (eg   Update Riddhi to 012345   )
                   |___________________________________________________________________________________________________\n""")
        if _command.lower() == "view":
            view(_input)
        elif _command.lower() == "insert":
            insert(_input)
        elif _command.lower() == "discard":
            discard(_input)
        elif _command.lower() == "update":
            update(_input)
        elif _command.lower() == "about":
            print("""This is a NID management system that can do basic functions by writing a line of cmd. Filters are also installed. 
            Doesn't accept multiple equivalent values like name and name, nums and nums""")
        else:
            print("Something went wrong while nothing went wrong")

    except Exception as ex:
        print(f"Error [{ex}]")
