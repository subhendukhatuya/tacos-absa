import pandas as pd

# Load the review data
df_reviews = pd.read_csv('./Itza_Reviews_SIGIR - Positive.csv')
all_review_sentences = []
for index, review_rows in df_reviews.iterrows():
    review_id = review_rows['review_id']
    review_body = review_rows['review_body']
    review_sentences = review_body.split('.')
    '''
    keep only non empty sentences. 
    Append review_id with each review sentences, start index of sentence is 1.
    e.g:
    review_id: Itza_POS_2
    review_body: Must do as early morning trip
    result: Itza_POS_2_1: Must do as early morning trip .
    '''
    review_sentences_with_id = [review_id + '_' + str(sentence_index + 1) + ': ' + sentence for sentence_index, sentence
                                in
                                enumerate(review_sentences) if len(sentence) > 0]
    for review_sentence in review_sentences_with_id:
        all_review_sentences.append(review_sentence)
    # Create a DataFrame object
df = pd.DataFrame(all_review_sentences,
                  columns=['sentences'])
df.to_csv('review_sent.csv', index=False)
#print(df)
print(all_review_sentences)
