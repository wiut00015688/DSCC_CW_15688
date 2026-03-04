from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task, Category, Comment


# ── Model Tests ────────────────────────────────────────────────

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        """Test category can be created successfully"""
        category = Category.objects.create(
            name="Work",
            description="Work related tasks"
        )
        self.assertEqual(category.name, "Work")
        self.assertEqual(str(category), "Work")

    def test_category_str(self):
        """Test category string representation"""
        category = Category.objects.create(name="Personal")
        self.assertEqual(str(category), "Personal")


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.category = Category.objects.create(name="Work")

    def test_task_creation(self):
        """Test task can be created successfully"""
        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            owner=self.user,
            category=self.category,
            status="todo",
            priority="medium"
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.status, "todo")
        self.assertEqual(task.owner, self.user)

    def test_task_str(self):
        """Test task string representation"""
        task = Task.objects.create(
            title="My Task",
            owner=self.user
        )
        self.assertEqual(str(task), "My Task")

    def test_task_default_status(self):
        """Test task default status is todo"""
        task = Task.objects.create(
            title="Default Task",
            owner=self.user
        )
        self.assertEqual(task.status, "todo")

    def test_task_default_priority(self):
        """Test task default priority is medium"""
        task = Task.objects.create(
            title="Priority Task",
            owner=self.user
        )
        self.assertEqual(task.priority, "medium")


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.task = Task.objects.create(
            title="Test Task",
            owner=self.user
        )

    def test_comment_creation(self):
        """Test comment can be created successfully"""
        comment = Comment.objects.create(
            task=self.task,
            author=self.user,
            text="This is a test comment"
        )
        self.assertEqual(comment.text, "This is a test comment")
        self.assertEqual(comment.author, self.user)


# ── View Tests ─────────────────────────────────────────────────

class AuthViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_home_page_loads(self):
        """Test home page returns 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_loads(self):
        """Test register page returns 200"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        """Test login page returns 200"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        """Test user can register successfully"""
        _ = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@test.com',
            'password1': 'complexpass123!',
            'password2': 'complexpass123!',
        })
        self.assertEqual(User.objects.filter(username='newuser').count(), 1)

    def test_user_login(self):
        """Test user can login successfully"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123',
        })
        self.assertRedirects(response, reverse('dashboard'))

    def test_dashboard_requires_login(self):
        """Test dashboard redirects unauthenticated users"""
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/login/?next=/dashboard/')

    # ── Task CRUD Tests ────────────────────────────────────────────

    class TaskCRUDTest(TestCase):
        def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user(
                username="testuser",
                password="testpass123"
            )
            self.client.login(username="testuser", password="testpass123")
            self.task = Task.objects.create(
                title="Existing Task",
                owner=self.user,
                status="todo"
            )

        def test_task_list_loads(self):
            """Test task list page loads for logged in user"""
            response = self.client.get(reverse('task_list'))
            self.assertEqual(response.status_code, 200)

        def test_task_create(self):
            """Test task can be created via POST"""
            _ = self.client.post(reverse('task_create'), {
                'title': 'New Task',
                'description': 'New Description',
                'status': 'todo',
                'priority': 'medium',
            })
            self.assertEqual(Task.objects.filter(title='New Task').count(), 1)

        def test_task_detail_loads(self):
            """Test task detail page loads"""
            response = self.client.get(reverse('task_detail', args=[self.task.pk]))
            self.assertEqual(response.status_code, 200)

        def test_task_edit(self):
            """Test task can be edited"""
            _ = self.client.post(
                reverse('task_edit', args=[self.task.pk]), {
                    'title': 'Updated Task',
                    'status': 'in_progress',
                    'priority': 'high',
                }
            )
            self.task.refresh_from_db()
            self.assertEqual(self.task.title, 'Updated Task')

        def test_task_delete(self):
            """Test task can be deleted"""
            _ = self.client.post(
                reverse('task_delete', args=[self.task.pk])
            )
            self.assertEqual(Task.objects.filter(pk=self.task.pk).count(), 0)
