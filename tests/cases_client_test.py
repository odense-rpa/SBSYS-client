from .fixtures import base_client, cases_client


def test_get_case(cases_client):
    case_id = "737962"  # Example case ID, replace with a valid one for your tests
    case = cases_client.get_case(case_id)

    # Assertions to validate the response
    assert isinstance(case, dict), "Case details should be a dictionary"
    assert case["SagsTitel"] == "Aktindsigt test 110325"


def test_get_cases_by_citizen(cases_client):
    cpr = "2222222222"  # Example CPR number, replace with a valid one for your tests
    cases = cases_client.get_cases_by_citizen(cpr)

    # Assertions to validate the response
    assert "Results" in cases, "Cases response should contain a 'Results' array"
    assert isinstance(cases["Results"], list), "'Results' should be a list"
    assert len(cases["Results"]) > 0, "'Results' array should have more than 0 entries"
    assert cases["Results"][0]["PrimaryPart"]["Navn"] == "test testsen"


def test_get_cases_by_caseid(cases_client):
    case_id = 6  # Test case ID
    cases = cases_client.get_cases_by_caseid(case_id)

    # Assertions to validate the response
    assert len(cases["Results"]) > 0, "'Results' array should have more than 0 entries"
    assert cases["Results"][0]["SagSkabelon"]["Navn"] == "Test skabelon"

