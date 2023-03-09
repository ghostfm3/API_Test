from take_api import InfomationWeather
from collections import Counter
from wordcloud import WordCloud
import ginza
import matplotlib.pyplot as plt
import pandas as pd
import spacy
import japanize_matplotlib

def ja_ginza_token(word):
    nlp = spacy.load('ja_ginza')
    ginza.set_split_mode(nlp, 'C')
    doc = nlp(word)
    return doc

def wordcloud_result(color,path_1,width,height,text):
    wordcloud = WordCloud(background_color=color, font_path=path_1, width=width, height=height).generate(text)    
    wordcloud.to_file("./result1.png")

def plt_counter(count):
    for word, num in count.most_common(10):
        plt.bar(word, num)
    
    plt.grid(axis='y')
    plt.xlabel('単語')
    plt.ylabel('頻度')
    plt.savefig('./count_result.png')

def main():
    locate_list = ["130010","130020","130030","130040","260010","260020","160010","160020","170010","170020","180010","180020","220010","471010","471020","474020"]
    day_list = [0,1,2]
    sentence_list = []
    result_list = []
    font_path = './ipaexm.ttf'
    for d_list in day_list: 
        for l_list in locate_list:
            info_weather = InfomationWeather(l_list)
            weather_sentence = info_weather.info_datail_weather(d_list)
            sentence_list.append(weather_sentence)
    
    text = ''.join(sentence_list)
    doc_1 = ja_ginza_token(text)

    for sent in doc_1.sents:
        result_list = result_list + [[token.text, token.lemma_, token.pos_, token.tag_] for token in sent]
    df = pd.DataFrame(result_list, columns = ['単語', '句', '品詞', '品詞タグ'])
    text2 = ' '.join(df[df['品詞タグ'].str.startswith('名詞','動詞')]['単語'].to_list())
    counter = Counter(df[df['品詞タグ'].str.startswith('名詞','動詞')]['単語'].to_list())
    plt_counter(counter)
    wordcloud_result('white',font_path,500,400,text2)
    df.to_csv("./ginza_result.csv")

       
if __name__ == "__main__":
    main()
