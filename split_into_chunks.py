

THE_LONG_STRING = "Loremipsumdolorsitamet,consectetueradipiscingelit.Aeneancommodoligulaegetdolor.Aenean massa.Cumsociisnatoquepenatibusetmagnisdisparturientmontes"

if __name__ == "__main__":
    n = 10
    chunks = [THE_LONG_STRING[i:i+n] for i in range(0, len(THE_LONG_STRING), n)]
    print('\n'.join(chunks))    
    
        
    