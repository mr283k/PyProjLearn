def format_name(f_name,l_name):
    output = f_name.lower().title() + " " + l_name.lower().title()
    return output

x = format_name('aBc','xYz')
print(x)