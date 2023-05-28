from unittest import TestCase
from app import app
from flask import session, request
from boggle import Boggle

test_boggle = Boggle()

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    ### TODO -- write tests for every view function / feature!
    def test_newgame(self):
        with app.test_client() as client:
            with client.session_transaction() as sesh:
                res = client.get('/')
                html = res.get_data(as_text = True)
                self.assertEqual(res.status_code, 200)
                self.assertIn('<!DOCTYPE html>', html)


    def test_guess(self):
        with app.test_client() as client:
            with client.session_transaction() as sesh:
                sesh['board'] = test_boggle.make_board()
            res = client.post('/guess', data = {
                "guess": "tan"
            })
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.is_json, True)

            res = client.post('/guess', data = {
                "guess": "zzkkz"
            })
            resData = res.get_json()
            self.assertEqual(resData['result'], 'not-word')

    def test_end(self):
        with app.test_client() as client:
            with client.session_transaction():
                res = client.post('/end', data = {
                    'score': 6
                })
                resData = res.get_json()
                self.assertEqual(res.status_code, 200)
                self.assertEqual(resData['highScore'], 6)

                res = client.post('/end', data = {
                    'score': 18
                })
                resData = res.get_json()
                self.assertEqual(res.status_code, 200)
                self.assertEqual(resData['highScore'], 18)

                res = client.post('/end', data = {
                    'score': 7
                })
                resData = res.get_json()
                self.assertEqual(res.status_code, 200)
                self.assertEqual(resData['highScore'], 18)

                res = client.post('/end', data = {
                    'score': 7
                })
                resData = res.get_json()
                self.assertEqual(resData['count'], 4)
                self.assertEqual(resData['highScore'], 18)