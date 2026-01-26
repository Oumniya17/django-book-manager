def test_edit_requires_login(self):
    response = self.client.get(f"/bookapp/{self.book.id}/edit")
    self.assertNotEqual(response.status_code, 200)


def test_delete_requires_login(self):
    response = self.client.get(f"/bookapp/{self.book.id}/delete")
    self.assertNotEqual(response.status_code, 200)


def test_detail_logged_user(self):
    self.client.login(username="user", password="1234")
    response = self.client.get(f"/bookapp/{self.book.id}/detail")
    self.assertEqual(response.status_code, 200)
