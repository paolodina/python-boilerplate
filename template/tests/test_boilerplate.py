from {{python_package_name}}.common.main import hello_world


class TestBoilerplate:
    def test_hello_world(self):
        assert "Hello" in hello_world()
