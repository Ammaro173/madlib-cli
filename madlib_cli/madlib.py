import re
# import regex


def read_template(path):
    """
    This Function Takes a path as an argument
    """
    try:
        file = open(path, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError('File Not Found \'-_-')


def welcome():
    """
    show welcome message
    """
    print("\n************************\nWelcome!!\nThis is a Madlib Game\nAll you Have to do is insert the words as you wish and we will handle the rest :D\n************************")
    pass


def parse_template(script):
    """
    This function takes a template(string) and extract all the
    phrases within any curly brackets {}
    """
    # bring {and what`s inside of it`}
    parsed = re.findall(r'\{.*?\}', script)
    removed_brackets = []
    # then we slice out the brackets!
    for i in parsed:
        brackets_slicer = (i[1:-1])
        removed_brackets.append(brackets_slicer)
    # to return the string obtained by replacing the leftmost non-overlapping occurrences of the regex pattern in string with repl.
    replace_sub_string = re.sub(r'\{.*?\}', "{}", script)

    return replace_sub_string, tuple(removed_brackets)


def merge(script, inputs):
    """
    inserts th user input inputs and returns them + Also creates a new text file
    """
    txt = open('madlib_cli/assets/new_text.txt', 'w')
    txt.write(script.format(*inputs))
    return script.format(*inputs)


def madlib_It():
    """this function run madlib game(all functions)"""
    welcome()
    new_template = read_template('madlib_cli/assets/template.txt')
    script, inserts = parse_template(new_template)
    inputs = [input(f"\nInsert a/an {i}: ") for i in inserts]
    return merge(script, inputs)


if __name__ == "__main__":
    print(madlib_It())


# print("check", parse_template())
