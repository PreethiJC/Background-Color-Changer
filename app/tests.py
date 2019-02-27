import unittest
from app import app
import flask
import random

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    #Test cases start from here
    def test_index(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_reset(self):
        with self.app as c:
            res = c.get("/", follow_redirects=True)
            res = c.get("/reset", follow_redirects=True)
            self.assertEqual(flask.session, {})

    # def test_persistance(self):
    #     with self.app as c:
    #         with c.session_transaction() as sess:
    #             sess["color"] = "blue"
    #             for i in range(1, 9):
    #                 res = c.get("/", follow_redirects=True)
    #             self.assertEqual(["color"], "blue")

    def test_same_color(self):
        with self.app as c:
            res = c.get("/")
            color = flask.session["color"]
            for i in range(1, 10):
                res = c.get("/")
                self.assertEqual(flask.session["color"], color)

    def test_randomness(self):
        random.seed(0)
        with self.app as c:
            res = c.get("/")
            self.assertEqual(flask.session["color"], "blue")

if __name__ == "__main__":
    unittest.main()