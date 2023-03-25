from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    max_salary = []
    for salary in read(path):
        if salary["max_salary"].isnumeric():
            max_salary.append(int(salary["max_salary"]))
    return max(max_salary)
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    min_salary = []
    for salary in read(path):
        if salary["min_salary"].isnumeric():
            min_salary.append(int(salary["min_salary"]))
    return min(min_salary)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        min_salary = float(job['min_salary'])
        max_salary = float(job['max_salary'])
        salary = float(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError('Salaries are not valid')

    if min_salary > max_salary:
        raise ValueError('Min salary is greater than max salary')

    return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
