def store_highscore_in_file(dictionary, fn = "sauvegarde/high_score.txt", top_n=0):
    """Store the dict into a file, only store top_n highest values."""
    with open(fn,"w") as f:
        for idx,(name,pts) in enumerate(sorted(dictionary.items(), key= lambda x:-x[1])):
            f.write(f"{name}:{pts}\n")
            if top_n and idx == top_n-1:
                break

def load_highscore_from_file(fn = "sauvegarde/high_score.txt"):
    """Retrieve dict from file"""
    hs = {}
    try:
        with open(fn,"r") as f:
            for line in f:
                name,_,points = line.partition(":")
                if name and points:
                    hs[name]=int(points)
    except FileNotFoundError:
        return {}
    return hs

def sauvegarde(name,points):
    file = load_highscore_from_file()
    if file.get(name, 0) < points:
        file[name]=points                  # add some highscores to dict
    store_highscore_in_file(file, top_n=5) # store file, only top 5
    fileOk = load_highscore_from_file()    # load back into new dict