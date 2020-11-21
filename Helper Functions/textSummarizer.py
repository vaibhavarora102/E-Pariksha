from summarizer import Summarizer
model = Summarizer()

def textSumamryPredictor(text):
    result = model(text)
    full = ''.join(result)
    return full


print(textSumamryPredictor('''Science in Everyday Life
Science is a great blessing to mankind. Nothing better has happened in the history of man than advent of science in human life. The world into which science came was a world of ignorance, suffering and hardship. Science has come to relieve us to sufferings, to remove our ignorance and to lighter our toil.

Science is a faithful servant of man. It serves us in all walks of life. It is our servant in the home, in the field and in the factory. Science has transformed our daily life. Gone are the days when only the rich men could afford luxuries. Science has made them cheap and has brought them within the reach of everybody. Science has produced goods on a large market. These are sold at cheap rates in every market. Books, music and all other forms of entertainment have been brought to our door. Radio, television, cinema help us in passing our time and also provide education to us.

Science is our most faithful medical attendant. It shows every care for our health. Because of science we are cured of many diseases. It has given us the power to reduce epidemics. No longer are cholera, plague and small pox the scourge of mankind. Science has helped in reducing the death rate and has also enhanced the living age of humans.

Science has reduced distance and made travelling a pleasure. Science has annihilated time and space. Trains roar through deserts, jungles and mountains while aeroplanes fly across thousands of kilometers in a matter of hours. The work of months and years can now be completed in hours.

Science is the greatest blessing to the poor housewife. A thousand devices have been placed at her disposal to lighter her toil. There is electricity run kitchens in which cooking is pleasure. There is no dirt, no smoke and cooking with the help of gas and electricity can be done in the twinkling of an eye. Electricity helps her in washing and pressing clothes and even in cleaning floors.

Science has provided us with computers and machines which have greatly increased our efficiency. We are better connected to people today and information is only a click of the mouse away. Man no longer needs to do the back breaking job of digging into mines with bare hands or tilling the soil with animals. Every factory is a standing tribute from the care and comforts that science has brought into our life.

Science educates us in many ways. Large printing presses produce number of books at cheap rates. News is brought to us from every corner of the world through the newspaper, radios and television.

However science has done a great disservice to mankind in the field of armaments. Weapons of mass destruction, nuclear weapons and sophisticated armament have endangered our lives and threaten to destroy the world. However it is upto us whether we will destroy our world or make is more beautiful and comfortable with the help of science.'''))
