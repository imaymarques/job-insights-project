from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries = []
    for job in jobs:
        industry = job["industry"]
        if industry not in industries:
            industries.append(industry)
    return list(filter(len, industries))
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_by_industries = [
        by_industry
        for by_industry in jobs
        if by_industry["industry"] == industry
    ]
    return filter_by_industries
    raise NotImplementedError
