cur_char = ''

get_char = None

def get_token():
    global cur_char
    if cur_char == '<':
        cur_char = get_char()
        if cur_char == '/':
            return end_tag()
        elif cur_char == '!':
            cur_char = get_char()
            if cur_char == '-':
                skip_comment()
            else:
                print(1)
        else:
            return start_tag()
    elif cur_char == '>':
        cur_char = get_char()
        if cur_char != '\n':
            return data()
        else: 
            skip_whitespace()
    elif cur_char == -1:
        return ('eof', )
    elif cur_char == '\n':
        skip_whitespace()

def start_tag():
    tag = ""
    global cur_char
    while cur_char != '>':
        tag += cur_char
        cur_char = get_char()
    # cur_char = get_char()
    return('start', tag)

def end_tag():
    tag = ""
    global cur_char
    while cur_char != '>':
        tag += cur_char
        cur_char = get_char()
    return('end', tag)

def data():
    data = ""
    global  cur_char
    while cur_char != '<':
        data += cur_char
        cur_char = get_char()
    return('data', data)

def skip_comment():
    while cur_char != '>':
        cur_char = get_char()
    cur_char = get_char()

def skip_whitespace():
    global cur_char
    while cur_char != '<':
        cur_char = get_char()

if __name__ == '__main__':
    print("Test tokens")
    f = open("sample html.html")

    def getch():
        global cur_char
        return f.read(1)

    get_char = getch
    cur_char = get_char()
    for i in range(100):
        borg = get_token()
        if borg != None:
            print(borg)
    f.close()