import base64
import pytest

from browser_use.browser.service import BrowserService


@pytest.fixture
def browser():
	browser_service = BrowserService(headless=True)
	browser_service.init()
	yield browser_service
	browser_service.close()


@pytest.mark.skip(reason='takes too long')
def test_take_full_page_screenshot(browser):
	# Go to a test page
	browser.go_to_url('https://example.com')

	# Take full page screenshot
	screenshot_b64 = browser.take_screenshot(full_page=True)

	# Verify screenshot is not empty and is valid base64
	assert screenshot_b64 is not None
	assert isinstance(screenshot_b64, str)
	assert len(screenshot_b64) > 0

	# Test we can decode the base64 string
	try:
		base64.b64decode(screenshot_b64)
	except Exception as e:
		pytest.fail(f'Failed to decode base64 screenshot: {str(e)}')
