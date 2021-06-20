
import numpy as np     
import networkx as nx 
import nltk 
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

stop_words = stopwords.words('english')
sample_input = '''There are times when the night sky glows with bands of color. The bands may
begin as cloud shapes and then spread into a great arc across the entire sky. They
may fall in folds like a curtain drawn across the heavens. The lights usually grow
brighter, then suddenly dim. During this time the sky glows with pale yellow, pink,
green, violet, blue, and red. These lights are called the Aurora Borealis. Some
people call them the Northern Lights. Scientists have been watching them for
hundreds of years. They are not quite sure what causes them. In ancient times people were afraid of the Lights. They imagined that they saw fiery dragons in the
sky. Some even concluded that the heavens were on fire. '''


# Summarize using Cosine Similarity

class cosine_summary:
    
    def extract_vector(self, sentence, all_words, stop_words):
        
        extracted_vector = [0] * len(all_words)
        for word in sentence:
            if word in stop_words:
                continue
            extracted_vector[all_words.index(word)] += 1
        return extracted_vector
    
    def sentence_similarity(self, s1, s2, stop_words):

        s1 = [word.lower() for word in s1]
        s2 = [word.lower() for word in s2]

        all_words = list(set(s1 + s2))

        v1 = self.extract_vector(s1, all_words, stop_words)
        v2 = self.extract_vector(s2, all_words, stop_words)

        return 1 - cosine_distance(v1, v2)
    
    
    def summarise_text(self, ranked_sentences, threshold):
        summary = []
        max_len = len(ranked_sentences)

        for i in range(max_len):
            if(ranked_sentences[i][0]< 0.02):
                break
            summary.append(" ".join(ranked_sentences[i][1]))

        summary = ". ".join(summary)

        return summary
    
    
    
    def summariser(self, text):
        #Breaking Down text to Sentences
        sentences = []
        
        #STOP Words
        stop_words = stopwords.words('english')
        split_text = text.split(". ")
        
        for sentence in split_text:
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        
        sentences.pop()
        
        #Similarity Matrix Building
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for i1, sentence1 in enumerate(sentences):
            for i2, sentence2 in enumerate(sentences):
                if sentence1 == sentence2:
                    similarity_matrix[i1][i2] = 0
                    continue
                similarity_matrix[i1][i2] = self.sentence_similarity(sentence1, sentence2, stop_words)
                
        #Ranking sentences
        similarity_network = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(similarity_network)
        
        # Sorting the Sentences with scores in descending order
        i = 0
        ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
        
        summary = self.summarise_text(ranked_sentences, 10)
        
        return summary, ranked_sentences


summ = cosine_summary()
summerised_text, ranked_sentences = summ.summariser(sample_input)

print(len(summerised_text))
print(len(sample_input))

print(summerised_text)