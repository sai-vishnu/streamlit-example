import pandas as pd
import json
from datetime import date, timedelta
from flask import Flask
data = pd.read_csv('users.csv', low_memory=False)
df1 = pd.read_csv('feeds_comments.csv')
df2 = pd.read_csv('feeds_likes.csv')
output1 = pd.concat([df1, df2])

# app = Flask(__name__)

# @app.route('/', methods=['GET','POST'])
def getuser(start_date, end_date):
        mask = (data['created_date'] >= start_date) & (data['created_date'] <= end_date)
        selected_dataset = data.loc[mask]
        g = selected_dataset.groupby(["created_date"])["register_status"].count()
        g = g.to_json('users.json', indent=4)
        print(g)
        return;
getuser(start_date = "15/07/10", end_date = "15/10/08") 

def getmonth():
        data = pd.DataFrame({'created_date':['10-07-2015', '12-09-2015']})
        data['created_date'] = pd.to_datetime(data['created_date'])
        data['created_date'] = data['created_date'].dt.strftime('%b-%Y')
        print(data['created_date'])
        data = data.to_json('date.json', indent=4)
        return;
getmonth()

def gettoday():
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        print("d1 =", d1)
	
        d2 = today.strftime("%B %d, %Y")
        print("d2 =", d2)


        d3 = today.strftime("%m/%d/%y")
        print("d3 =", d3)

        d4 = today.strftime("%b-%d-%Y")
        print(d4)
        with open("gettoday.json", "w") as f:
                json.dump(d4, f)
gettoday()

def sevendays():
        drift = date.today() - timedelta(7)
        print("current date:",date.today())
        json_obj = json.loads(drift)
        with open("seven.json", 'w') as f :
                json.dumps(json_obj, f, indent=4)
sevendays()

def likcmd():
        g = output1.groupby(['created_on'])['liked_by', 'comment'].count()
        drt = g.sort_values(['liked_by', 'comment'], ascending=[False, False])
        print(drt)
        drt  = drt.to_json('likandcmd.json', indent=4)
        return;
likcmd()

# # if __name__ =='__main__':
# #         app.run(debug=True)
















