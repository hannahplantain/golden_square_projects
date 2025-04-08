#A function called make_snippet that takes a string as an argument 
# and returns the first five words and then a '...' if there are more than that.

def make_snippet(string):
        if len(string) <= 5:
            return string
        else:
            snippet_string = " ".join(string.split()[:5])
            return snippet_string + "..."