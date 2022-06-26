import pathlib
from pathlib import Path

import streamlit as st
from fastai.vision.all import *
from fastai.vision.widgets import *



learn_inf = load_learner('model.pkl')

class Predict:
    def __init__(self, filename):
        st.title('Sprawdź gatunek swojego grzyba!')
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Prześlij zdjęcie",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(250,250), caption='Przesłane zdjęcie')

    def get_prediction(self):

        if st.button('Klasyfikuj'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            if(pred == 'Boletus edulis'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Borowik szlachetny jest jednym z najsmaczniejszych i najbogatszych w wartości odżywcze grzybów występujących w polskich lasach.')
                st.write('Prawdziwek wyróżnia się dostojnym wyglądem, pięknym zapachem i wybornym smakiem.')
                st.write('Doskonale nadaje się zarówno do gotowania, jak i smażenia, pieczenia i suszenia. ')
                st.write('Na zbiory tego grzyba o pękatym kapeluszu można wybrać się zarówno latem, jak i jesienią.')
                st.write('https://www.ekologia.pl/styl-zycia/zdrowa-zywnosc/borowik-szlachetny-opis-wystepowanie-i-zdjecia-grzyb-borowik-szlachetny-ciekawostki,23347.html')
            if(pred == 'Cantharellus cibarius Fr.'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Pieprznik jadalny jest smacznym grzybem jadalnym.')
                st.write('W Polsce jest bardzo pospolity – należy do najczęściej występujących grzybów w lasach.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/pieprznik-jadalny')
            if (pred == 'Lactarius deliciosus'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Mleczaj rydz jest grzybem jadalnym. Uważany za jeden ze smaczniejszych grzybów. W Polsce jest pospolity.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/mleczaj-rydz')
            if (pred=='Russula sanguinea'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Gołąbek krwisty należy do grzybów mikoryzowych, które wchodzą w symbiozę z roślinami.')
                st.write('Strzępki grzyba wnikają w komórki miękiszu kory pierwotnej korzeni rośliny.')
                st.write('Grzyb w tym oddziaływaniu przekazuje roślinie sole mineralne i wodę z witaminami.')
                st.write('Natomiast od rośliny pobiera niezbędne do rozwoju węglowodany.')
                st.write('Ze względu na swój cierpki smak uznaje się go za gatunek niejadalny.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/golabek-krwisty')
            if(pred =='Cortinarius cinnamomeus'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Zasłonak cynamonowy jest grzybem niejadalnym.')
                st.write('Nazwa gatunku sugeruje jego zabarwienie kapelusza, które u innych gatunków z rodziny zasłonakowatych może niewiele się różnić.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/zaslonak-cynamonowy')
            if (pred == 'Amanita phalloides'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Muchomor sromotnikowy jest jednym z najsilniej trujących grzybów.')
                st.write(' W Polsce jest bardzo pospolity, spotkać go można na całym terytorium naszego kraju.')
                st.write('Wśród biologów znany jest także pod nazwą muchomor zielonawy.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/muchomor-sromotnikowy')
            if (pred == 'Amanita pantherina'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Muchomor plamisty jest grzybem silnie trującym.')
                st.write('Posiada te same substancje toksyczne, co muchomor czerwony, tylko w większym stężeniu.')
                st.write('W Polsce jest dość pospolity.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/muchomor-plamisty')
            if(pred == 'Amanita muscaria'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Muchomor czerwony, zwany bedłką lub muchomorem pospolitym, to najsłynniejszy gatunek grzybów z rodziny muchomorowatych.')
                st.write(' Miąższ tego grzyba kryje w sobie substancje o właściwościach toksycznych.')
                st.write('https://www.ekologia.pl/srodowisko/przyroda/muchomor-czerwony-opis-wystepowanie-i-zdjecia-grzyb-muchomor-czerwony-ciekawostki,23511.html')
            if(pred=='Rubroboletus satanas'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Borowik szatański, zwany diablikiem, szatanem, smoczym łbem lub trucicielem, jest toksycznym gatunkiem grzybów należących do rodziny borowikowatych.')
                st.write('Rubroboletus satanas jest rzadkością w naszych lasach.')
                st.write('Dzięki temu do zatruć dochodzi stosunkowo rzadko.')
                st.write('https://www.ekologia.pl/srodowisko/przyroda/borowik-szatanski-opis-wystepowanie-i-zdjecia-grzyb-borowik-szatanski-ciekawostki,23584.html')
            if(pred=='Hypholoma fasciculare'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Maślanka wiązkowa to grzyb trujący.')
                st.write('To jeden z najbardziej pospolicie występujących grzybów blaszkowych.')
                st.write('https://www.ekologia.pl/wiedza/grzyby/maslanka-wiazkowa')
            if(pred=='Boletus badius'):
                st.subheader(f'**Predykcja**: {pred}')
                st.subheader(f'**Prawdopodobieństwo**: {probs[pred_idx]*100:.02f}%')
                st.write('Podgrzybek brunatny stanowi jeden z najbardziej poszukiwanych leśnych skarbów.')
                st.write(' Ma aromatyczny, delikatny smak, który świetnie wzbogaci takie potrawy, jak pierogi, zapiekanki czy risotto.')
                st.write('Występujący powszechnie w lasach iglastych.')
                st.write('https://www.ekologia.pl/srodowisko/przyroda/podgrzybek-brunatny-opis-wystepowanie-i-zdjecia-grzyb-podgrzybek-brunatny-ciekawostki,23382.html')
            if (pred =='Random'):
                st.subheader('**Predykcja**: Nieznany')
                st.write('Nie udało się rozpoznać grzyba na zdjęciu')
        else: 
            st.write(f'Kliknij aby sklasyfikować') 

if __name__=='__main__':

    file_name='model.pkl'
predictor = Predict(file_name)
