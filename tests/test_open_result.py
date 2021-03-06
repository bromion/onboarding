from source.pages.MainPage import MainPage
from source.pages.SearchingResultsPage import SearchingResultsPage


def test_click_first_result(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field()

    results_page = SearchingResultsPage(driver)
    results_page.click_first_found_element()


def test_click_result(driver):
    main_page = MainPage(driver)
    main_page.fill_search_field()

    results_page = SearchingResultsPage(driver)
    results_page.click_found_element_with_number(3)
