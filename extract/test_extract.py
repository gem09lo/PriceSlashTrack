from extract import scrape_from_html, get_html_from_url, get_website_from_url
import pytest
from unittest.mock import MagicMock


def test_website_finder_finds_com_websites():
    assert get_website_from_url(
        "something.com/something-else") == "something.com"


def test_website_finder_finds_co_uk_websites():
    assert get_website_from_url(
        "something.co.uk/something-else") == "something.co.uk"


def test_url_is_not_valid_returns_error_message():
    assert get_html_from_url(
        "https://random_url") == "That URL does not exist."
    assert get_html_from_url("random_url") == "That URL does not exist."


@pytest.fixture
def html_object():
    with open("test_html.txt", "r", encoding="UTF-8") as test_file:
        html_string = test_file.read()
    return html_string


def test_scraper_gets_correct_steam_original_and_discount_price(html_object):
    """ Tests to see that the scraper can get a steam original and discount price. """

    test_product_info = scrape_from_html(html_object)
    assert test_product_info.get("original_price") == "£19.99"
    assert test_product_info.get("discount_price") == "£11.99"
    assert test_product_info.get("game_title") == "The Planet Crafter"
    assert test_product_info.get(
        "website") == "https://store.steampowered.com/"