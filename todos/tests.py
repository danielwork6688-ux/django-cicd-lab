from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoModelTest(TestCase):
    def test_str(self):
        todo = Todo(title='Buy milk')
        self.assertEqual(str(todo), 'Buy milk')

    def test_default_completed_is_false(self):
        todo = Todo.objects.create(title='Task')
        self.assertFalse(todo.completed)


class TodoListViewTest(TestCase):
    def test_empty_list(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Todo')

    def test_shows_todos(self):
        Todo.objects.create(title='Learn CI/CD')
        response = self.client.get(reverse('todo_list'))
        self.assertContains(response, 'Learn CI/CD')


class TodoCreateViewTest(TestCase):
    def test_create_todo(self):
        self.client.post(reverse('todo_create'), {'title': 'Deploy app'})
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.first().title, 'Deploy app')

    def test_empty_title_ignored(self):
        self.client.post(reverse('todo_create'), {'title': '   '})
        self.assertEqual(Todo.objects.count(), 0)


class TodoToggleViewTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title='Test toggle')

    def test_toggle_completes(self):
        self.client.post(reverse('todo_toggle', args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)

    def test_toggle_twice_reverts(self):
        self.client.post(reverse('todo_toggle', args=[self.todo.pk]))
        self.client.post(reverse('todo_toggle', args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.completed)


class TodoDeleteViewTest(TestCase):
    def test_delete_todo(self):
        todo = Todo.objects.create(title='Delete me')
        self.client.post(reverse('todo_delete', args=[todo.pk]))
        self.assertEqual(Todo.objects.count(), 0)
