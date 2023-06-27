# Document-Query-Ranking
## Description of the Project
The aim of the project was to build a search engine from scratch. The dataset whose link is given below contains two distinct json files, one containing queries and the other containing documents. Given a query, we want to return a ranked list of documents based on their similarity with the query. The similarity between query and document was measured by euclidean cosine similarity measure. The vectorization (without using any python package) was done using TF-IDF algorithm.

## Description of the dataset

The dataset can be obtained from the following link 'https://ir.dcs.gla.ac.uk/resources/test_collections/cran/'. I have used two datasets from this, one is cran_docs and the other is cran_queries. Cran docs is a json file that contains a colelction of documents and cran_queries contains the collection of queries.
