def backspace_compare(first: str, second: str):

    def backspace(line: str):
        if '#' in line:
            if line.startswith('#'):  # remove all leading sharps with recursion
                line_changed = line.replace('#', '', 1)
                backspace(line_changed)

            line_list = list(line)  # convert string to list
            for key, value in enumerate(line_list):  # deletion algorithm before sharps
                if value == '#':
                    line_list[key-1] = ''
                    line_list[key] = ''
            line_list.remove('')
            return ''.join(line_list)  # return list convert to string
        else:
            return line

    return backspace(first) == backspace(second)