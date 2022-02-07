#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:19:58 2021

@author: asep

reference from
[1] https://github.com/nju-websoft/ESBM/tree/master/v1.2
[2] https://github.com/nju-websoft/DeepLENS/blob/master/code/train_test.py
"""

import math

class ndcg:
    """NDCG stand for Normalized Discounted Cumulative Gain"""
    def get_score(self, triple_gold_summaries, triples_rank):
        """ the score is to measure the quality of a set of search results"""
        triple_grade = {}
        for triple_gold_sum in triple_gold_summaries:
            for t in triple_gold_sum:
                if t not in triple_grade:
                    triple_grade[t]=1
                else:
                    triple_grade[t]= triple_grade[t]+1
        grade_list = list(triple_grade.values())
        grade_list.sort(reverse=True)
        
        dcg = 0
        idcg = 0
        
        max_rank_pos = len(triples_rank)
        max_ideal_pos = len(grade_list)
        
        for pos in range(1, max_rank_pos+1):
            t = triples_rank[pos-1]
            try:
                rel = triple_grade[t]
            except:
                rel=0
            dcg_item = rel/math.log(pos + 1, 2)
            dcg += dcg_item
            
            if (pos<=max_ideal_pos):
                idealRel = grade_list[pos-1]
                idcg += idealRel/math.log(pos + 1, 2)
        
        score = dcg/idcg
        return score