from configparser import ConfigParser 
  
config = ConfigParser() 
print (config.read('config/config.ini')) 

attibute_list = {}

try:
    env = os.environ.get('ENV')
    print("env",env)
    for key in config[env]:  
        attibute_list[key] =  config[env][key]
except:
    for key in config['MAIN']:  
        attibute_list[key] =  config['MAIN'][key]

print(attibute_list)