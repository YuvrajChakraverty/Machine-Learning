from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    
    feat_data = request.json
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    prediction = list(model.predict(df))
    return jsonify({'prediction': str(prediction)})

        

if __name__ == '__main__':

    def clean_df(data):
    
        data['MS SubClass']=data['MS SubClass'].apply(str)
        data= data.drop(['PID','Pool QC','Misc Feature','Alley','Fence'],axis=1)
        bsmt_num_cols = ['BsmtFin SF 1', 'BsmtFin SF 2', 'Bsmt Unf SF','Total Bsmt SF', 'Bsmt Full Bath', 'Bsmt Half Bath']
        data[bsmt_num_cols] = data[bsmt_num_cols].fillna(0)
        bsmt_str_cols =  ['Bsmt Qual', 'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 'BsmtFin Type 2']
        data[bsmt_str_cols] = data[bsmt_str_cols].fillna('None')
        data["Mas Vnr Type"] = data["Mas Vnr Type"].fillna("None")
        data["Mas Vnr Area"] = data["Mas Vnr Area"].fillna(0)
        gar_str_cols = ['Garage Type', 'Garage Finish', 'Garage Qual', 'Garage Cond']
        data[gar_str_cols] = data[gar_str_cols].fillna('None')
        data['Garage Yr Blt'] = data['Garage Yr Blt'].fillna(0)
        data['Fireplace Qu'] = data['Fireplace Qu'].fillna("None")
        data['Lot Frontage'] = data['Lot Frontage'].fillna(0) 
    
        return data

    model = joblib.load("Housing Prices Model.pkl") 
    col_names = joblib.load("Housing Prices Columns.pkl") 

    app.run(debug=True)