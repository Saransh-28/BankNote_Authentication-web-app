
# import the required modules
import pickle
import streamlit as st

# load the model 
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

# function to return the predicted value
def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if prediction == 0:
        prediction = 'Passed'
    else:
        prediction = "Failed"
    print(prediction)
    return str(prediction)

def main():
    st.title("Bank Note Authenticator")
    
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:grey;text-align:center;"> Bank Note Authenticator ML Web App </h2>
    </div>
    """
    
    st.markdown(html_temp , unsafe_allow_html=True)
    
    variance=(st.text_input("variance"))
    skewness=(st.text_input("skewness"))
    curtosis=(st.text_input("curtosis"))
    entropy=(st.text_input("entropy"))
    
    result = ""
    
    if st.button("Predict"):
        result = predict_note_authentication(float(variance),float(skewness),float(curtosis),float(entropy))
        
    st.success(f'The prediction is -> {result}')
    
if __name__=='__main__':
    main()
    
