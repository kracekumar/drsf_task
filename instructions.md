### Step 1: Getting Started

- Setup requirements and migrations.
- Cd into todo's app and create serializers.py file.
- Go to `models.py` and see definition.
- Create a `TodoSerializer` subclassed from `serializers.ModelSerializer`.
- Create a `Meta` nested class inside `TodoSerializer` with attributes `model, fields`.
- Add fields `id, name, priority, created_by, created_at, is_completed`
- Create a field `created_by` of type SlugRelatedField with `queryset, slug_field`.
- Open `views.py` create `TodoViewSet` subclassed from `ModelViewSet`.
- Add `queryset` and `serializer_class` as attributes to `TodoViewSet`.
- Open `urls.py` in `drsf_task` and create router of `DefaultRouter` instance.
- `register` `TodoViewSet`.
- Add `router.urls` to urlpatterns.
- Now run `python manage.py runserver.py` from command line.
-  `python manage.py createsuperuser`
- Head over to `localhost:8000`.
- View have finally Nice looking `Rest Framework interface`.
- Add few todos from Interface.
- Update, Read, Delete few todos.
- Repeat above step using Python requests library from shell.

### Step 2: Filters
- open `views.py` in `TodoViewSet`, add `filter_backends=[filters.OrderingFilter]` as attribute.
- Add `filter_fields` attribute as list of fields which should be allowed.
- Try few following urls `http://localhost:8000/todos/`, 
- `http://localhost:8000/todos/?ordering=is_completed`, `http://localhost:8000/todos/?ordering=-is_completed`
- `http://localhost:8000/todos/?ordering=-priority`, `http://localhost:8000/todos/?ordering=priority`
- Add `DjangoFilterBackEnd` to `filter_backends`.
- Try few filters with `__gte`, `__lte` etc ...
- `http://localhost:8000/todos/?priority__gte=0`
- `http://localhost:8000/todos/?priority=2`
- `http://localhost:8000/todos/?is_completed=False`
- `http://localhost:8000/todos/?created_by=1&is_completed=True`
- Play around with filters

### Step 3: Authentication and Permission
- Add `authentication_classes` attribute to `TodoViewSet` with value `BasicAuthentication`.
- Add `permission_classes` attribute to `TodoViewSet` with value `IsAuthenticated`.
- Now login with user details.
- Create few records.
- Try the url in `http://localhost:8000/todos/2/.json` incognito. It will prompt for basic auth
- Use requests to create a new record.
- `requests.post('http://localhost:8000/todos/.json', json=data_in_dict, auth=(username, password))`
- You can create your custom classes for Permission but it should have `has_permission` method and return `True` or `False`.

### Step 4: Write some tests
-  Open `tests.py` and see through `test_create_todo`.
-  Write the test for `list, update, get, delete` case.

### Step 5: Create Class Based View for User Creation
- Create a `UserSerializer` with `username, password, email` field.
- `username, password` are character field but password is write-only.
- Make all three fields required.
- Create `UserListApiView` inheriting from `APIView`.
- Set `authentication_classes`, `permission_classes`.
- Implement `get` method. Pass `many=True` to serializer.
- Implement `post` method.
- Register the view in `urls.py`. `url(r'^users/$', UserListApiView.as_view()),`
- Try `http://localhost:8000/users/`.
- Create a new class `UserDetailApiView` subclassing `APIView`.
-  Add a method `get_object` which will fetch the item from db given a `pk`.
-  Add methods `get` and `post`.
-  Register the `UserDetailApiView` in `urls.py`. `url(r'^users/(?P<pk>[0-9]+)/$', UserDetailApiView.as_view()),`
-  Create a new users using requests.

### Hope, you learnt something! DRSF code is clean and Pythonic.
