import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course

# def test_example():
#     assert False, "Just test example"

URL = '/api/v1/courses/'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course(client, courses_factory):
    course = courses_factory(_quantity=10)
    id_course = 1
    response = client.get(URL + f'{id_course}/')
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == course[id_course - 1].name
    assert data['id'] == course[id_course - 1].id


@pytest.mark.django_db
def test_list_course(client, courses_factory):
    courses = courses_factory(_quantity=20)
    response = client.get(URL)
    data = response.json()
    for i, course in enumerate(courses):
        assert data[i] == {'id': course.id,
                           'name': course.name,
                           'students': []}
    assert response.status_code == 200


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=10)
    id_course = 1
    response = client.get(URL + f'?id={courses[id_course - 1].id}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[id_course - 1].name
    assert data[0]['id'] == courses[id_course - 1].id


@pytest.mark.django_db
def test_filter_name(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_filter = courses[0]
    response = client.get(URL + f'?name={course_filter.name}')
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == courses[0].name
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post(URL, data={'name': 'django',
                                      'students': []})
    assert response.status_code == 201

    date = response.json()
    assert date['name'] == 'django'
    assert date['students'] == []
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory()
    count = Course.objects.count()
    response = client.patch(URL + f'{course.id}/', data={'name': 'django',
                                      'students': []})
    date = response.json()
    assert response.status_code == 200
    assert Course.objects.count() == count
    assert Course.objects.count() == count
    assert date['name'] == 'django'


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory()
    count = Course.objects.count()
    response = client.delete(URL + f'{course.id}/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert not Course.objects.filter(id=course.id).exists()