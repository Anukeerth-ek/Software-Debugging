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

print(remove_html_markup("<b>foo</b>"))   # And we got the desired result, that is foo. 

# But we need to make sure that if it works for everything. And we have one on error. If we check '<a href=">"></a>' in this we will get "foo. That is not the
# result we want so we need to add some changes to this. 
