import pytest
import mock
from config import *
from src.scraper import Scraper
from src.providerFactory import ProviderFactory
from bs4 import BeautifulSoup


@pytest.fixture
def mock_browser_non_200(mocker):
    mocked_browser = mock.Mock()
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://example.com"
    mockedResponse.status_code = 404
    mocked_browser.fetch_page.return_value = None
    return mocked_browser


def test_handlesNon200Response(mock_browser_non_200):
    scraper = Scraper(mock_browser_non_200)
    url = "https://example.com"

    mockedExportPropertyDataToCSV = mock_browser_non_200.patch.object(
        Scraper, "exportPropertyDataToCSV"
    )

    scraper.exportPropertiesDataToCSV(url)

    assert mockedExportPropertyDataToCSV.call_count == 0


def test_getProvider(mocker):
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://www.zonaprop.com.ar/"
    mockedResponse.text = "Mocked HTML content"
    scraper = Scraper(mock.Mock())
    parsedData = BeautifulSoup(mockedResponse.text, "html.parser")

    mockedCreateProvider = mocker.patch.object(ProviderFactory, "create_provider")

    provider = scraper.getProvider(mockedResponse)

    assert provider is not None
    mockedCreateProvider.assert_called_once_with(mockedResponse.url, parsedData)
