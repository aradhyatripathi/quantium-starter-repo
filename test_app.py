import pytest
from app import app

@pytest.fixture
def dash_app():
    app.config.suppress_callback_exceptions = True
    return app

def test_header_present(dash_app):
    layout = str(dash_app.layout)
    assert 'Pink Morsel Sales Visualiser' in layout

def test_visualisation_present(dash_app):
    layout = str(dash_app.layout)
    assert 'sales-chart' in layout

def test_region_picker_present(dash_app):
    layout = str(dash_app.layout)
    assert 'region-filter' in layout