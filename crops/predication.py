from main.settings import BASE_DIR
import numpy as np
import pickle


model = pickle.load(open(f'{BASE_DIR}/crops/ai_models/model.pkl','rb'))
sc = pickle.load(open(f'{BASE_DIR}/crops/ai_models/standscaler.pkl','rb'))
mx = pickle.load(open(f'{BASE_DIR}/crops/ai_models/minmaxscaler.pkl','rb'))


def model_predict(nitrogen, potassium, phosphorus, temperature, humidity, ph_level, rainfall):
    
    feature_list = [nitrogen, potassium, phosphorus, temperature, humidity, ph_level, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    mx_features = mx.transform(single_pred)
    sc_mx_features = sc.transform(mx_features)
    prediction = model.predict(sc_mx_features)

    crop_dict = {
        1: "Rice", 
        2: "Maize", 
        3: "Jute", 
        4: "Cotton", 
        5: "Coconut", 
        6: "Papaya", 
        7: "Orange",
        8: "Apple", 
        9: "Muskmelon", 
        10: "Watermelon", 
        11: "Grapes", 
        12: "Mango", 
        13: "Banana",
        14: "Pomegranate", 
        15: "Lentil", 
        16: "Blackgram", 
        17: "Mungbean", 
        18: "Mothbeans",
        19: "Pigeonpeas", 
        20: "Kidneybeans", 
        21: "Chickpea", 
        22: "Coffee"
    }
    
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = f"{crop} is the best crop to be cultivated right there"
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return result