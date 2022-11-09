#Nombre de protocole : 135 => pour les graphes (on represente les 20 plus importants )
import json
dict={"nb_attacks": 321283,
"nb_state":13,
"nb_service":16,
"nb_protocole": 135}
import json 
      

 
json_object = json.dumps(dict, indent = 4) 
print(json_object)

with open("sample.json","w") as outfile:
    json.dump(dict,outfile)