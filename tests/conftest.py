import pytest

@pytest.fixture
def run_db():
    print("\nstart db")

    yield

    print("\nstop db")

@pytest.fixture
def run_api(run_db):
    print("\nstart api")

    yield

    print("\nstop api")

