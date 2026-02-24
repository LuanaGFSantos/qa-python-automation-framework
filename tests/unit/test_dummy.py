from app import app

def test_app_is_created():
    assert app is not None

def test_route_home_exists():
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/" in routes
