from {{python_package_name}}.common.main import hello_world


class TestBoilerplate:
    def test_hello_world(self):
        assert "We are here" in hello_world()
