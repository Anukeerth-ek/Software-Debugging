# In this firstly we created a python program to remove the html markup and return only the content. This program have successfully return the desired result.
# We can check with all the HTML element and make sure this program is working fine with all of those.

def remove_html_markup(s):
    tag = False
    out = " "

    for c in s: 
        if c == '<':      # Start of markup
            tag = True
        elif c == '>':    # End of markup
            tag = False
        elif not tag:
            out = out + c
    
    return out

print(remove_html_markup("<b>foo</b>"))