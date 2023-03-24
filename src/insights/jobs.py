from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    print(path)
    with open(path, encoding='utf-8') as file:
        results = csv.DictReader(file)
        data = [
            result
            for result in results
        ]
        return data
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    jobs_type = []
    for job in data:
        if job["job_type"] not in jobs_type:
            jobs_type.append(job["job_type"])
    return jobs_type
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_by_job_types = [
        job
        for job in jobs
        if job["job_type"] == job_type
    ]

    return filter_by_job_types
    raise NotImplementedError
