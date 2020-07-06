def test_home_page(driver, live_server):
    driver.get(live_server.url)
    assert 'welcome' in driver.page_source.lower()
