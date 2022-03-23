from ..models import Subject, Content, Keyword

subject_mockdata1 = {
    "name": 'Subject'
}

def create_subject_mock(subject_mockdata) -> Subject:
    return  Subject.objects.create(name=subject_mockdata['name'])

content_mockdata1 = {
    "name": 'Content',
    "url": 'http://test'
}

def create_content_mock(content_mockdata) -> Content:
    subject = create_subject_mock(subject_mockdata1)
    return Content.objects.create(
        name = content_mockdata['name'],
        url = content_mockdata['url'],
        subject_id = subject
    )

keyword_mockdata1 = {
    "keyword": 'Keyword test'
}

def create_keyword_mock(keyword_mockdata) -> Keyword:
    content = create_content_mock(content_mockdata1)
    return Keyword.objects.create(
        keyword = keyword_mockdata['keyword'],
        content_id = content
    )
    
    