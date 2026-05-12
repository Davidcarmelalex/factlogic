"""FactLogic — Investigation Tests"""
import pytest
from agents.investigator import investigate, Verdict, InvestigationResult

def test_returns_investigation_result():
    result = investigate("Vaccines cause autism")
    assert isinstance(result, InvestigationResult)

def test_scores_in_range():
    result = investigate("Test claim")
    assert 0 <= result.logic_score <= 10
    assert 0 <= result.science_score <= 10

def test_verdict_is_valid():
    result = investigate("Test claim")
    assert result.verdict in Verdict
