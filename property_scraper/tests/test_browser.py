import pytest
import mock
from src.browser import Browser


@pytest.fixture
def mock_scraper(mocker):
    mocked_scraper = mocker.patch("src.browser.cloudscraper.create_scraper")
    mocked_response = mock.Mock()
    mocked_response.status_code = 200
    mocked_response.text = "Mocked response content"
    mocked_scraper.return_value.get.return_value = mocked_response
    return mocked_scraper


@pytest.fixture
def mock_scraperWithResponseNot200(mocker):
    mocked_scraper = mocker.patch("src.browser.cloudscraper.create_scraper")
    mocked_response = mock.Mock()
    mocked_response.status_code = 404
    mocked_scraper.return_value.get.return_value = mocked_response
    return mocked_scraper


def test_fetchPageSuccess(mock_scraper):
    browser = Browser()
    url = "https://www.example.com"
    response = browser.fetch_page(url)

    assert response is not None
    assert response.status_code == 200
    assert "Mocked response content" in response.text


def test_fetchPageNot200(mock_scraperWithResponseNot200):
    browser = Browser()
    url = "https://www.example.com"
    response = browser.fetch_page(url)

    assert response is None
