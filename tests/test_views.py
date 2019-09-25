# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products/")
        products = response.json
        self.assertIsInstance(products, list)
        print(len(products))
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_delete_id_products(self):
        response = self.client.delete("/api/v1/products/1")
        product = response.json
        print(product)
        self.assertEqual(response.status_code, 204)
        result = self.client.get("/api/v1/products/1")
        self.assertEqual(result.status_code, 404)

    def test_CRUD_read_json(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product, {
                                    'id' : 1,
                                    'name': "Skello"
                                    })

    def test_read_not_equal_json(self):
        response = self.client.get("/api/v1/products/6")
        product = response.json
        self.assertEqual(response.status_code, 404)

    def test_add_json(self):
        response = self.client.post("/api/v1/products/")
        self.assertEqual(response.status_code, 201)


