'''Tests for EmotionDetection'''
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDecector(unittest.TestCase):
    '''Tests for emotion_detector'''
    def test_emotion_detector(self):
        '''Unit tests for emotion_detector'''
        joy_example = "I am glad this happened"
        anger_example = "I am really mad about this"
        disgust_example = "I feel disgusted just hearing about this"
        sadness_example = "I am so sad about this"
        fear_example = "I am really afraid that this will happen"
        self.assertEqual(emotion_detector(joy_example)['dominant_emotion'], 'joy')
        self.assertEqual(emotion_detector(anger_example)['dominant_emotion'], 'anger')
        self.assertEqual(emotion_detector(disgust_example)['dominant_emotion'], 'disgust')
        self.assertEqual(emotion_detector(sadness_example)['dominant_emotion'], 'sadness')
        self.assertEqual(emotion_detector(fear_example)['dominant_emotion'], 'fear')

unittest.main()
