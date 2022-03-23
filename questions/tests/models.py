from util.tests.global_setup import GlobalTestSetUp
from ..models import Question, Answer
from .mockdata import question_mockdata1, create_question_mock, answer_mockdata1, create_answer_mock


# Question Tests
class TestQuestionCase(GlobalTestSetUp):
    def setUp(self):
        super().setUp()
        create_question_mock(question_mockdata1)


    def test_if_exists(self) -> None:
        question_count = Question.objects.count()
        self.assertEqual(question_count, 1)
        self.assertNotEqual(question_count, 0)
    
    
    def test_instance(self) -> None:
        question = Question.objects.get(id=1)
        self.assertTrue(isinstance(question, Question))
       
    
    def test_create(self) -> None:
        question = Question.objects.get(id=1)
        name = question.name
        text = question.text
        likes = question.likes.count()
        author = question.author.id
        difficulty_id = question.difficulty_id.id
        
        self.assertEqual(name, question_mockdata1['name'])
        self.assertEqual(text, question_mockdata1['text'])
        self.assertEqual(likes, 1)
        self.assertEqual(author, 2)
        self.assertEqual(difficulty_id, 1)


    def test_str(self) -> None:
        question = Question.objects.get(id=1)
        self.assertEqual(str(question), question_mockdata1['name'])
    
    
    def test_count_likes(self) -> None:
        question = Question.objects.get(id=1)
        self.assertEqual(question.count_likes, 1)
    
    
    def test_toggle_public(self) -> None:
        question = Question.objects.get(id=1)
        question.toggle_public()
        self.assertEqual(question.is_public, True)
    

# Answer Tests
class TestAnswerCase(GlobalTestSetUp):

    def setUp(self) -> None:
        super().setUp()
        create_answer_mock(answer_mockdata1)
    
    
    def test_if_exists(self) -> None:
        answer_count = Answer.objects.count()
        self.assertEqual(answer_count, 1)
        self.assertNotEqual(answer_count, 0)
    
         
    def test_instance(self) -> None:
        answer = Answer.objects.get(id=1)
        self.assertTrue(isinstance(answer, Answer))
       
        
    def test_create(self) -> None:
        answer = Answer.objects.get(id=1)
        name = answer.name
        text = answer.text
        likes = answer.likes.count()
        author = answer.author.id
        question_id = answer.question_id.id
        
        self.assertEqual(name, answer_mockdata1['name'])
        self.assertEqual(text, answer_mockdata1['text'])
        self.assertEqual(likes, 1)
        self.assertEqual(author, 1)
        self.assertEqual(question_id, 1)
       


    def test_str(self) -> None:
        answer = Answer.objects.get(id=1)
        self.assertEqual(str(answer), answer_mockdata1['name'])
    

    def test_count_likes(self) -> None:
        question = Answer.objects.get(id=1)
        self.assertEqual(question.count_likes, 1)
    
