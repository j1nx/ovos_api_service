
class Storage:
    def __init__(self):
        pass
        
    def set_api_connection_config(self):
        # read entry from file
        try:
            with open("/etc/wapi/wapi.conf", "r") as conf_file:
                return conf_file.read()
        except Exception as e:
            print(e)
            return " "
        
    def set_owm_api_config(self):
        # read entry from file
        try:
            with open("/etc/wapi/owm.conf", "r") as conf_file:
                return conf_file.read()
        except Exception as e:
            print(e)
            return " "

    def set_omdb_api_config(self):
        try:
            with open("/etc/wapi/omdb.conf", "r") as conf_file:
                return conf_file.read()
        except Exception as e:
            print(e)
            return " "

    def set_edamam_recipes_appid_config(self):
        try:
            with open("/etc/wapi/edamam-appid.conf", "r") as conf_file:
                return conf_file.read()
        except Exception as e:
            print(e)
            return " "

    def set_edamam_recipes_appkey_config(self):
        try:
            with open("/etc/wapi/edamam-appkey.conf", "r") as conf_file:
                return conf_file.read()
        except Exception as e:
            print(e)
            return " "