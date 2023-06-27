import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import numpy as np
documents=json.load(open('cran_docs.json','r'))
doc_ids,docs=[item['id'] for item in documents],[item['body'] for item in documents]
query=json.load(open('cran_queries.json','rb'))
query_ids,queries=[item['query number'] for item in query],[item['query'] for item in query]
doc_corpus=[]
stop_words=stopwords.words('english')
for doc in docs:
    words=word_tokenize(doc)
    for word in words:
        if word not in stop_words:
            doc_corpus.append(word)
doc_corpus

class InformationRetrieval:
    def __init__(self,documents,queries) -> None:
        self.stop_words=stopwords.words('english')
        self.documents=documents
        self.queries=queries
        self.doc_ids,self.doc_content=[item['id'] for item in documents],[item['body'] for item in documents]
        self.query_ids,self.query_content=[item['query number'] for item in query],[item['query'] for item in query]
        self.doc_corpus=[]
        for doc in self.doc_content:
            words=word_tokenize(doc)
            for word in words:
                if word not in self.stop_words:
                    self.doc_corpus.append(word)
    def get_doc_index(self):
        return self.doc_ids
    def get_query_index(self):
        return self.query_ids
    def get_idf(self,word):
        idf_count=0
        for doc in self.doc_content:
            words=word_tokenize(doc)
            if word in words:
                idf_count+=1
        return np.log(len(self.doc_ids)/idf_count)
    def get_tf(self,word,doc):
        rel_words=[]
        word_count=0
        words=word_tokenize(doc)
        for word in words:
            if (word not in self.stop_words)&(word not in string.punctuation):
                rel_words.append(word)
        word_count=[]
        for i in rel_words:
            if i==word:word_count+=1
        return word_count/len(rel_words)
    def get_tf_idf(self,word,doc):
        return self.get_tf(word,doc)*self.get_idf(word)
    def vectorizer(self,doc,query):
        words_in_doc=[]
        words_in_query=[]
        words=word_tokenize(doc)
        qwords=word_tokenize(query)
        common_words=[]
        doc_vector=[]
        query_vector=[]
        for word in words:
            if (word not in self.stop_words)&(word not in string.punctuation):
                words_in_doc.append(word)
        for word in qwords:
            if (word not in self.stop_words)&(word not in string.punctuation):
                words_in_query.append(word)
        for word in words_in_doc:
            common_words.append(word)
        for word in words_in_query:
            if word not in common_words:
                common_words.append(word)
        for word in common_words:
            if word in words_in_doc:
                doc_vector.append(1)
            else:doc_vector.append(0)
        for word in common_words:
            if word not in words_in_query:
                query_vector.append(0)
            else:query_vector.append(self.get_tf_idf(word,doc))
        return doc_vector,query_vector
    def cos_sim(self,v1,v2):
        return np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    def get_rank(self,query):
        similarity={}
        rank={}
        for doc in range(len(self.doc_content)):
            doc_vector,query_vector=self.vectorizer(self.doc_content[doc],query)
            similarity[self.doc_ids[doc]]=self.cos_sim(doc_vector,query_vector)
        keys=list(similarity.keys())
        values=list(similarity.values())
        sorted_value_index=np.argsort(values)
        rank={keys[i]:values[i] for i in sorted_value_index}
        return rank
find_rank=InformationRetrieval(documents,query)
find_rank.get_rank(queries[0])





        
		
        





            






















