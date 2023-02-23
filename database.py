from sqlalchemy import create_engine
from sqlalchemy import text

#print(sqlalchemy.__version__)

# create_engine
URL = "mysql+pymysql://txm2ie3t5qgljsgnzvfh:pscale_pw_Iu3WakflVl8CCrVGXBoSjjkngq93lcYyWT6qoQNkStS@us-east.connect.psdb.cloud/joviancareers?charset=utf8mb4"
#Establish connectivity
engine = create_engine(URL,
                       echo=True,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

#print("type: result", type(result))
#print("type: result_all", type(result_all))
#print("type: result_all[0]", type(result_all[0]))

#print("result_dicts:", result_dicts)
#first_result_dict = result_all[0].__lt__
#print("type: first_result_dict", type(first_result_dict))
#print(first_result_dict)
