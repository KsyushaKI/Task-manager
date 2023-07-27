from django.test import TestCase
from task_manager.users.models import CustomUser
from django.urls import reverse


class UsersSignUpViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/users/create/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_and_url_accessible_by_name(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/signup.html')

    def test_signup_user(self):
        resp = self.client.post(
            reverse('signup'), {
                'first_name': 'FirstNameTest1',
                'last_name': 'LastNameTest1',
                'username': 'UserNameTest1',
                'password1': 'passwordTest1',
                'password2': 'passwordTest1',
            }
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        user = CustomUser.objects.last()
        self.assertEqual(user.first_name, 'FirstNameTest1')
        self.assertEqual(user.last_name, 'LastNameTest1')
        self.assertEqual(user.username, 'UserNameTest1')


class UsersListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_users = 13
        for user_num in range(number_of_users):
            CustomUser.objects.create(
                first_name='Ivan%s' % user_num,
                last_name='Ivanov%s' % user_num,
                username='ivanivanov%s' % user_num,
                password='ivanovpassword%s' % user_num,
            )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/users/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_and_url_accessible_by_name(self):
        resp = self.client.get(reverse('users_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/customuser_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('users_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['customuser_list']) == 10)

    def test_lists_all_authors(self):
        resp = self.client.get(reverse('users_list')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] is True)
        self.assertTrue(len(resp.context['customuser_list']) == 3)


class UsersUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_users = 3
        for user_num in range(number_of_users):
            CustomUser.objects.create(
                first_name='Ivan%s' % user_num,
                last_name='Ivanov%s' % user_num,
                username='ivanivanov%s' % user_num,
                password='ivanovpassword%s' % user_num,
            )

    def test_view_url_exists_at_desired_location(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get('/users/1/update/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_and_url_accessible_by_name(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_update', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/update.html')

    def test_redirect_if_user_is_not_log_in(self):
        resp = self.client.get(reverse('user_update', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

    def test_redirect_if_logged_in_user_is_not_selected_user(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_update', kwargs={'pk': 2}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users_list'))

    def test_update_user(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_update', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
                reverse('user_update', kwargs={'pk': user.id}), {
                    'first_name': 'Ivan',
                    'last_name': 'Petrov',
                    'username': 'ivanivanov',
                }
            )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users_list'))

        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Ivan')
        self.assertEqual(user.last_name, 'Petrov')
        self.assertEqual(user.username, 'ivanivanov')


class UsersDeleteViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_users = 3
        for user_num in range(number_of_users):
            CustomUser.objects.create(
                first_name='Ivan%s' % user_num,
                last_name='Ivanov%s' % user_num,
                username='ivanivanov%s' % user_num,
                password='ivanovpassword%s' % user_num,
            )

    def test_view_url_exists_at_desired_location(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get('/users/1/delete/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_and_url_accessible_by_name(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/confirm_delete.html')

    def test_redirect_if_user_is_not_log_in(self):
        resp = self.client.get(reverse('user_delete', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

    def test_redirect_if_logged_in_user_is_not_selected_user(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_delete', kwargs={'pk': 2}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users_list'))

    def test_delete_user(self):
        user = CustomUser.objects.get(id=1)
        self.client.force_login(user)
        resp = self.client.get(reverse('user_delete', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
                reverse('user_delete', kwargs={'pk': user.id}),
            )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('users_list'))
        self.assertEqual(CustomUser.objects.count(), 2)
