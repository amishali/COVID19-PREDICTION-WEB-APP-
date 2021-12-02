import  joblib

#is aframework that allows u to create this app and easy to use 
import streamlit as st  
 #import our model name it as classifier
import os
from pathlib import Path
current_directory = Path(__file__).parent #Get current directory
file = open(os.path.join(current_directory, 'svc.pkl'), 'rb')
#classifier = joblib.load(open('svc.pkl' , 'rb')) #load the model u want , #rb = read bytes because we are reading the file
classifier =joblib.load(file)
def  prediction_generator(cough ,fever , sore_throat , shortness_of_breath , head_ache , age_60_and_above  ,gender , test_indication): #colums are its argument 
    
    prediction = classifier.predict([[cough ,fever , sore_throat , shortness_of_breath , head_ache , age_60_and_above  ,gender , test_indication]])
    if prediction ==0 :
        output='negative'
    else:
                output = 'positive'
    return output 

def main():
    st.title('COVID_19  PREDICTION  APP')  
    cough= float(st.number_input('COUGH :    ( 0 negetive , 1 :positive)'))
    fever = float(st.number_input( '    FEVER :      (0 negetive , 1 :positive) '))
    sore_throat = float(st.number_input(' SORE _THROAT :      (0 negetive , 1 :positive )'))
    shortness_of_breath = float(st.number_input('SHORTNESS_OF_BREATH:     ( 0 negetive , 1 :positive)'))
    head_ache= float(st.number_input('HEADACHE  :      (0 negetive , 1 :positive)'))
    age_60_and_above  = float(st.number_input('AGE > 60 :      ( No: 0 , Yes :1 ,None :2)'))
    gender = float(st.number_input('GENDER:                ( female :0 , male :1 , None:2)'))
    test_indication= float(st.number_input('TEST_INDICATION :             (Other: 0 , Abroad:1 , Contact with confirmed :2)'))


    result = ' '
    if st.button('Predict'):
        result = prediction_generator(cough ,fever , sore_throat , shortness_of_breath , head_ache , age_60_and_above  ,gender , test_indication)
        st.success(f'Corona result is  {result}')

if __name__ =='__main__' :
    main()      
