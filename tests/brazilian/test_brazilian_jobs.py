from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    get_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in get_jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
