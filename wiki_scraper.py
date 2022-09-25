import wikipedia
def search_wikipedia(name):
    wikipage = wikipedia.summary(name)
    # print(wikipage)
    return wikipage

# if __name__=="__main__":
#     search_wikipedia("walt disney")