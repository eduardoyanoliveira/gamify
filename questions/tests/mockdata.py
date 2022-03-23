from game_config.tests.mockdata import difficulty_mockdata1, create_difficulty_mock
from accounts.models import CustomUser
from ..models import Answer, Question

question_mockdata1 = {  
    "name": 'Question',
    "text": 'test text'
}

def create_question_mock(question_mockdata) -> Question:
    difficulty = create_difficulty_mock(difficulty_mockdata1)
    
    question = Question.objects.create(
        name= question_mockdata['name'],
        text= question_mockdata['text'],
        author = CustomUser.objects.get(id=2),
        difficulty_id = difficulty
    )
    
    question.likes.set([CustomUser.objects.get(id=1)])
    
    return question


answer_mockdata1 ={
    "name": 'Answer',
    "text": 'test text'
}

def create_answer_mock(answer_mockdata) -> Answer:
    question = create_question_mock(question_mockdata1)
    
    answer = Answer.objects.create(
        name = answer_mockdata['name'],
        text = answer_mockdata['text'],
        question_id= question,
        author = CustomUser.objects.get(id=1)
    )
    
    answer.likes.set([CustomUser.objects.get(id=2)])
    
    return answer