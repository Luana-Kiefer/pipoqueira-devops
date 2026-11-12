import unittest
from app import app

class TestPipoqueira(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_pagina_inicial(self):
        # Verifica se a página inicial carrega com sucesso (Status 200)
        resposta = self.client.get('/')
        self.assertEqual(resposta.status_code, 200)

if __name__ == '__main__':
    unittest.main()