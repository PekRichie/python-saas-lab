"""Külső függőség nélküli BM25 szövegkereső motor."""
import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-ZáéíóöőúüűÁÉÍÓÖŐÚÜŰ0-9]+", text.lower())


class Bm25Index:
    def __init__(self, docs: list[str], k1: float = 1.5, b: float = 0.75) -> None:
        self.docs = docs
        self.k1 = k1
        self.b = b
        self.tokens = [tokenize(d) for d in docs]
        self.avgdl = sum(len(t) for t in self.tokens) / max(1, len(docs))
        self.df: Counter[str] = Counter()
        for t in self.tokens:
            for w in set(t):
                self.df[w] += 1

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, float]]:
        q_terms = tokenize(query)
        n = len(self.docs)
        scores = []
        for idx, doc_toks in enumerate(self.tokens):
            tf = Counter(doc_toks)
            dl = len(doc_toks)
            score = 0.0
            for term in q_terms:
                if term not in tf:
                    continue
                idf = math.log((n - self.df[term] + 0.5) / (self.df[term] + 0.5) + 1.0)
                f = tf[term]
                score += idf * (f * (self.k1 + 1)) / (f + self.k1 * (1 - self.b + self.b * dl / max(1e-9, self.avgdl)))
            if score > 0:
                scores.append((idx, round(score, 4)))
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
