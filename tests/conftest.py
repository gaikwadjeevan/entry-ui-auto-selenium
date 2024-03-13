# import os
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from core.data_classes import Logger, Config, Remote
from core import logger
import os

# os.environ['WDM_SSL_VERIFY'] = '0'
current_dir = os.getcwd()
project_root = os.path.abspath(os.path.join(current_dir, ".."))

@fixture(scope="session")
def log() -> Logger:
    return logger.log()


@fixture(scope="session")
def driver() -> Remote:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@fixture(scope="session")
def config(log, driver) -> Config:
    return Config(log, driver)
