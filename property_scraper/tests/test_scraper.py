import pytest
import mock
from config import *
from src.scraper import Scraper
from src.providerFactory import ProviderFactory
from bs4 import BeautifulSoup
from freezegun import freeze_time


@pytest.fixture
def mock_browserWithResponseNot200(mocker):
    mocked_browser = mock.Mock()
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://example.com"
    mockedResponse.status_code = 404
    mocked_browser.fetch_page.return_value = None
    return mocked_browser


@pytest.fixture
def mock_browserWithResponse200(mocker):
    mocked_browser = mock.Mock()
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://example.com"
    mockedResponse.status_code = 200
    mocked_browser.fetch_page.return_value = mockedResponse
    return mocked_browser


def test_scraperHandlesNon200Response(mock_browserWithResponseNot200):
    scraper = Scraper(mock_browserWithResponseNot200, False)
    url = "https://example.com"

    mockedExportPropertyDataToCSV = mock_browserWithResponseNot200.patch.object(
        Scraper, "exportPropertyDataToCSV"
    )

    scraper.exportPropertiesDataToCSV(url)

    assert mockedExportPropertyDataToCSV.call_count == 0


def test_scraperGetProviderCorrectly(mocker):
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://www.zonaprop.com.ar/"
    mockedResponse.text = "Mocked HTML content"
    scraper = Scraper(mock.Mock(), False)
    parsedData = BeautifulSoup(mockedResponse.text, "html.parser")

    mockedCreateProvider = mocker.patch.object(ProviderFactory, "create_provider")

    provider = scraper.getProvider(mockedResponse)

    assert provider is not None
    mockedCreateProvider.assert_called_once_with(mockedResponse.url, parsedData)


@freeze_time("2000-01-01 12:00:00")
def test_scraperExportPropertyDataToCSVWithCorrectFilename(mocker):
    filename = "property_data-2000-01-01-12:00:00.csv"
    expectedOutputDataDir = os.path.join(DATA_DIR, filename)

    mockedPropertyData = mocker.Mock()
    mockedPropertyData.to_csv = mocker.Mock()
    scraper = Scraper(mock.Mock(), False)

    scraper.exportPropertyDataToNewCSV(mockedPropertyData)

    mockedPropertyData.to_csv.assert_called_once_with(expectedOutputDataDir, index = False)


def test_exportPropertiesDataToCSVStopsOnRepeatURL(mocker, mock_browserWithResponse200):
    mocked_provider = mocker.Mock()
    mocked_provider.getNextPageURL.return_value = "https://example.com"

    mocked_scraper = Scraper(mock_browserWithResponse200, False)

    mocker.patch.object(Scraper, "getProvider", return_value=mocked_provider)

    mocked_exportPropertyDataToCSV = mocker.patch.object(
        Scraper, "exportPropertyDataToNewCSV"
    )

    mocked_scraper.exportPropertiesDataToCSV("https://example.com")

    assert mocked_exportPropertyDataToCSV.call_count == 1
    mocked_provider.getNextPageURL.assert_called_once()
