import pytest
import mock
from config import *
from src.scraper import Scraper
from src.providerFactory import ProviderFactory
from bs4 import BeautifulSoup
from freezegun import freeze_time


@pytest.fixture
def mock_browserWithResponseNot200(mocker):
    mockedBrowser = mock.Mock()
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://example.com"
    mockedResponse.status_code = 404
    mockedBrowser.fetch_page.return_value = None
    return mockedBrowser


@pytest.fixture
def mock_browserWithResponse200(mocker):
    mockedBrowser = mock.Mock()
    mockedResponse = mock.Mock()
    mockedResponse.url = "https://example.com"
    mockedResponse.status_code = 200
    mockedBrowser.fetch_page.return_value = mockedResponse
    return mockedBrowser


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

    mockedCreateProvider = mocker.patch.object(ProviderFactory, "createProvider")

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

    mockedPropertyData.to_csv.assert_called_once_with(
        expectedOutputDataDir, index=False
    )


def test_exportPropertiesDataToCSVStopsOnRepeatURL(mocker, mock_browserWithResponse200):
    mockedProvider = mocker.Mock()
    mockedProvider.getNextPageURL.return_value = "https://example.com"

    mockedScraper = Scraper(mock_browserWithResponse200, False)

    mocker.patch.object(Scraper, "getProvider", return_value=mockedProvider)

    mocked_exportPropertyDataToCSV = mocker.patch.object(
        Scraper, "exportPropertyDataToNewCSV"
    )

    mockedScraper.exportPropertiesDataToCSV("https://example.com")

    assert mocked_exportPropertyDataToCSV.call_count == 1
    mockedProvider.getNextPageURL.assert_called_once()
