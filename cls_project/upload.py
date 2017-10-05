import csv
import re
import json


def main():
    num = 0


    #Text file containing University name, league, and roster URL
    f_read = open("ivy.csv", "rt")
    data = []
    player_model = {}
    data = []
    player_data = {}
    #Create single JSON output file
    total_output = open("ivy_player_data.json", "w")

    #CSV object of University text file
    reader = csv.reader(f_read)

    #Iterates through each University included in the original text file
    for indx_0, line in enumerate(reader):
        th_titles = []
        td_titles = []
        #Write a player's University and League to dictionary variable
        player_data['school'] = line[12].strip()
        player_data['hs_type'] = line[9].strip()
        player_data['high_school'] = line[8].strip()
        player_data['city'] = line[6].strip()
        try:
            player_data['weight'] = int(line[5].strip())
        except:
            pass
        player_data['name'] = line[1].strip()
        player_data['number'] = line[0].strip()
        player_data['state'] = line[7].strip()
        player_data['height'] = line[4].strip()
        player_data['position'] = line[3].strip()
        player_data['year'] = line[2].strip()
        
        """
        f_state = open("states.csv", "rt")
        states = csv.reader(f_state)
        for state in states:
            for name in state:
                #Looks for State name or abbreviation in stripped table data cell
                state_check = None
                #print(name)
                if name == player_data['state']:
                    player_data['state'] = state[0]
                    break
        """       
        
        a_pos = re.search(r'a$|A$|Attack$|attack$', str(player_data['position']))
        d_pos = re.search(r'd$|D$|Defense$|defense$', str(player_data['position']))
        g_pos = re.search(r'g$|G$|GK$|Gk$|gk$|Goalie$', str(player_data['position']))
        m_pos = re.search(r'm$|M$|Middie$|middie$', str(player_data['position']))
        lsm_pos = re.search(r'LSM$|lsm$', str(player_data['position']))
        am_pos = re.search(r'A\/M$|a\/m$\M\/A$|m\/a$', str(player_data['position']))
        fo_pos = re.search(r'F\/O|Face-off$|Face-Off$|FO$|FO\/M$|M\/FO$', str(player_data['position']))
        if a_pos:
            player_data["position"] = "atk"
        elif d_pos:
            player_data["position"] = "def"
        elif g_pos:
            player_data["position"] = "gl"
        elif m_pos:
            player_data["position"] = "mid"
        elif lsm_pos:
            player_data["position"] = "lsm"
        elif am_pos:
            player_data["position"] = "am"
        elif fo_pos:
            player_data["position"] = "fo"
        else:
            player_data["position"] = ""

        fr_year = re.search(r'fr\.$|Fr\.$|fr$|Fr$|^freshman$|^Freshman$', str(player_data['year']))
        so_year = re.search(r'so\.$|So\.$|so$|So$|^sophomore$|^Sophomore$', str(player_data['year']))
        jr_year = re.search(r'jr\.$|Jr\.$|jr$|Jr$|^junior$|^Junior$', str(player_data['year']))
        sr_year = re.search(r'sr\.$|Sr\.$|Sr$|Sr$|^Senior$|^Senior$', str(player_data['year']))
        if fr_year:
            player_data["year"] = "fr"
        elif so_year:
            player_data["year"] = "so"
        elif jr_year:
            player_data["year"] = "fr"
        elif sr_year:
            player_data["year"] = "sr"
        else:
            player_data["year"] = ""

        try:
            height_match = re.search(r'^(\d)-(\d{1,2})$', str(player_data['height']))
            feet = int(height_match.group(1))
            inches = int(height_match.group(2))
            total_height = (feet * 12) + inches
            player_data['height'] = int(total_height)
        except:
            pass




        if player_data['school'] == "Harvard University":
            player_data['school'] = 1
        elif player_data['school'] == "Brown University":
            player_data['school'] = 2
        elif player_data['school'] == "Yale University":
            player_data['school'] = 3
        elif player_data['school'] == "Cornell University":
            player_data['school'] = 4
        elif player_data['school'] == "Princeton University":
            player_data['school'] = 5
        elif player_data['school'] == "Dartmouth College":
            player_data['school'] = 6

        if player_data['weight'] == "":
            player_data['weight'] = None
        elif player_data['height'] == "":
            player_data['height'] = None

        num += 1
        player_model = {"pk": num,
                        "model": "rosters.Player",
                        "fields": player_data.copy()}
        data.append(player_model.copy())


    json.dump(data, total_output, sort_keys=True, indent=4)








if __name__ == "__main__":
    main()

"""

"""
