class ZoneManager(object):
    #zone creations

    def __init__(self):
        # initialize list to contain zones
        self.zones = []
    #hanle creaton
    def create_new_zone(self,parent, name):
        zone_holder = {}
        if name:
            zone_holder[parent] = name
            self.zones.append(zone_holder)
            return "success"
        else:
            return "blank_entry"


    #handle return of the zones
    def return_zones(self):
        return self.zones

    def delete_zone(self,parent, name):
        counter=0
        default=""
        for i in self.zones:
            if i.get(parent, default)==name:
                self.zones.pop(counter)
                return "success"
            counter=counter+1
        return "error"
