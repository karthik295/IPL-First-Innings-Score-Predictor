from  flask import Flask,render_template,request,url_for
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('dt_reg.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/PREDICT',methods=['POST'])
def PREDICT():
    final=[]
    if request.method=='POST':
        Season=int(request.form['Season'])
        final=final+[Season]
        Toss_Decision=request.form['Toss_Decision']
        if Toss_Decision=='field':
            final=final+[1]
        else:
            final=final+[0]
        Toss_Winner=request.form['Toss_Winner']
        if Toss_Winner=='DC':
            final=final+[1,0,0,0,0,0,0]
        elif Toss_Winner=='KKR':
            final=final+[0,1,0,0,0,0,0] 
        elif Toss_Winner=='KingsXI':
            final=final+[0,0,1,0,0,0,0]
        elif Toss_Winner=='MI':
            final=final+[0,0,0,1,0,0,0] 
        elif Toss_Winner=='RCB':
            final=final+[0,0,0,0,1,0,0]
        elif Toss_Winner=='RR':
            final=final+[0,0,0,0,0,1,0]
        elif Toss_Winner=='SRH':
            final=final+[0,0,0,0,0,0,1]
        else:
            final=final+[0,0,0,0,0,0,0]
        Batting_Team=request.form['Batting_Team']
        if Batting_Team=='DC':
            final=final+[1,0,0,0,0,0,0]
        elif Batting_Team=='KKR':
            final=final+[0,1,0,0,0,0,0] 
        elif Batting_Team=='KingsXI':
            final=final+[0,0,1,0,0,0,0]
        elif Batting_Team=='MI':
            final=final+[0,0,0,1,0,0,0] 
        elif Batting_Team=='RCB':
            final=final+[0,0,0,0,1,0,0]
        elif Batting_Team=='RR':
            final=final+[0,0,0,0,0,1,0]
        elif Batting_Team=='SRH':
            final=final+[0,0,0,0,0,0,1]
        else:
            final=final+[0,0,0,0,0,0,0]
        Bowling_Team=request.form['Bowling_Team']
        if Bowling_Team==Batting_Team:
            return 'Both Bowling and Batting cannot be same team'
        elif Bowling_Team=='DC':
            final=final+[1,0,0,0,0,0,0]
        elif Bowling_Team=='KKR':
            final=final+[0,1,0,0,0,0,0] 
        elif Bowling_Team=='KingsXI':
            final=final+[0,0,1,0,0,0,0]
        elif Bowling_Team=='MI':
            final=final+[0,0,0,1,0,0,0] 
        elif Bowling_Team=='RCB':
            final=final+[0,0,0,0,1,0,0]
        elif Bowling_Team=='RR':
            final=final+[0,0,0,0,0,1,0]
        elif Bowling_Team=='SRH':
            final=final+[0,0,0,0,0,0,1]
        else:
            final=final+[0,0,0,0,0,0,0]
        if (Toss_Winner not in Batting_Team) and (Toss_Winner not in Bowling_Team):
            return 'The Toss Winner is not in either batiing or bowling teams'
        Extra_runs=int(request.form['Extra_runs'])
        Batting_power_play=int(request.form['Batting_power_play'])
        Expected_Death_overs_Score=int(request.form['Expected_Death_overs_Score'])
        final=final+[Extra_runs,Batting_power_play,Expected_Death_overs_Score]
        Venues=request.form['Venues']
        if Venues=='Sheikh Zayed Stadium':
            final=final+[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Sharjah Cricket Stadium':
            final=final+[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Dubai International Cricket Stadium':
            final=final+[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Rajiv Gandhi International Stadium, Uppal':
            final=final+[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='M Chinnaswamy Stadium':
            final=final+[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Wankhede Stadium':
            final=final+[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Holkar Cricket Stadium':
            final=final+[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Eden Gardens':
            final=final+[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Feroz Shah Kotla':
            final=final+[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Punjab Cricket Association IS Bindra Stadium, Mohali':
            final=final+[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Punjab Cricket Association Stadium, Mohali':
            final=final+[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Sawai Mansingh Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='MA Chidambaram Stadium, Chepauk':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Dr DY Patil Sports Academy':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Newlands':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=="St George's Park":
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Kingsmead':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='SuperSport Park':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Buffalo Park':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='New Wanderers Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='De Beers Diamond Oval':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='OUTsurance Oval':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Brabourne Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Sardar Patel Stadium, Motera':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Himachal Pradesh Cricket Association Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Subrata Roy Sahara Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif Venues=='Shaheed Veer Narayan Singh International Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif Venues=='JSCA International Stadium Complex':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif Venues=='Barabati Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif Venues=='Maharashtra Cricket Association Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif Venues=='Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif Venues=='M. A. Chidambaram Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif Venues=='Feroz Shah Kotla Ground':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif Venues=='M. Chinnaswamy Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif Venues=='Rajiv Gandhi Intl. Cricket Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif Venues=='IS Bindra Stadium':
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        else:
            final=final+[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        data=np.array([final])
        output=model.predict(data)[0]
        lb=np.floor(output-10)
        ub=np.floor(output+10)
        return render_template('index.html',ans='Predicted First Innings Score is {}-{}'.format(int(lb),int(ub))) 
                 
if __name__=='__main__':
    app.run(debug=True)
