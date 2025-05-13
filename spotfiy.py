AllMuusika = [{"title": "shbs", "artist": "guy"}]

def otsi_muusikat(item):
    if not item:
        print("Sisend on tühi!")

        tulemused = []
        for laul in AllMuusika:
            if item in laul["title"] or item in laul["artist"]: 
                tulemused.append(laul)
            
        if tulemused:
            print("Leitud laulud ")
            for i in tulemused:
                print(i['artist'], ' - ', i["title"])

        else:
            print("Ei leia laulu")

otsi_muusikat("shbs")