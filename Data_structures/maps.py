locations = {'North America': {'USA': ['Mountain View', 'California']}}

for key, value in locations.copy().items():
    if key == "North America":
        for key_2, value_2 in value.items():
            if key_2 == 'USA':
                value_2.append('Atlanta')
    if 'Africa' not in locations:
        locations['Africa'] = {"Egypt":['Cairo']}
    if 'Asia' not in locations:
        locations['Asia'] = {"China":['Shanghai']}
        for key, value in locations.items():
            if key == "Asia":
                locations['Asia']['India'] = ['Banglore']
            
                    


def cities(locations):
    for key, value in locations.items():
        if key == 'North America':
            for key_2, value_2 in value.items():
                if key_2 == 'USA':
                    for i in range(len(value_2)):
                        for j in range(len(value_2)):
                            if value_2[i] < value_2[j]:
                                value_2[i], value_2[j] = value_2[j], value_2[i]
            print("1")
            for val in value_2:
                print(val)

        elif key == "Asia":
            print("2")
            for key_, val in value.items():
                for val2 in val:
                    print(f"{val2} - {key_}")

cities(locations)  

  
                           
                        
            
        