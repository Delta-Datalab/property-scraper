import pytest
import mock
from src.browser import Browser


@pytest.fixture
def mock_scraper(mocker):
    mockedScraper = mocker.patch("src.browser.cloudscraper.create_scraper")
    mockedResponse = mock.Mock()
    mockedResponse.status_code = 200
    mockedResponse.text = "Mocked response content"
    mockedScraper.return_value.get.return_value = mockedResponse
    return mockedScraper


@pytest.fixture
def mock_scraperWithResponseNot200(mocker):
    mockedScraper = mocker.patch("src.browser.cloudscraper.create_scraper")
    mockedResponse = mock.Mock()
    mockedResponse.status_code = 404
    mockedScraper.return_value.get.return_value = mockedResponse
    return mockedScraper


def test_fetchPageSuccess(mock_scraper):
    browser = Browser()
    url = "https://www.example.com"
    response = browser.fetchPage(url)

    assert response is not None
    assert response.status_code == 200
    assert "Mocked response content" in response.text


def test_fetchPageNot200(mock_scraperWithResponseNot200):
    browser = Browser()
    url = "https://www.example.com"
    response = browser.fetchPage(url)

    assert response is None
