import json
import certifi
import os
from elasticsearch import Elasticsearch

class Company:

    def __init__(self):
        try:
            es_host = os.environ['ESHOST']
            self.es = Elasticsearch(
                [es_host],
            )
        except:
            self.es = Elasticsearch(
                ['https://search-bothouse-lc4sfkmtnmafagc3d3c6tatary.eu-central-1.es.amazonaws.com'],
                use_ssl=True,
                ca_certs=certifi.where()
            )

    
    def fetchSimilarCompanies(self, company_id):
        query = {
            'min_score': 4.3,
            'query': {
                'bool': {
                    'should': [{
                        "more_like_this" : {
                            "fields" : ["description"],
                            "like" : [{
                                "_index" : "companies",
                                "_type" : "company",
                                "_id" : str(company_id)
                            }],
                            "min_term_freq" : 1,
                            "max_query_terms" : 12,
                            "boost": 0.8
                        }
                    },{
                        "more_like_this" : {
                            "fields" : ["zip"],
                            "like" : [{
                                "_index" : "companies",
                                "_type" : "company",
                                "_id" : str(company_id)
                            }],
                            "min_term_freq" : 1,
                            "max_query_terms" : 12,
                            "boost": 0.1
                        }
                    },{
                        "more_like_this" : {
                            "fields" : ["city"],
                            "like" : [{
                                "_index" : "companies",
                                "_type" : "company",
                                "_id" : str(company_id)
                            }],
                            "min_term_freq" : 1,
                            "max_query_terms" : 12,
                            "boost": 0.1
                        }
                    }]
                }
            }
        }
        result = self.es.search(body=query, size=20)
        return result