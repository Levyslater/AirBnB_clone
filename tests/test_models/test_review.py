import unittest
from models.review import Review
from datetime import datetime
import models
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_review_inherits_from_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        review_data = {
            "user_id": "789",
            "place_id": "101",
            "text": "Great experience!"
        }
        review = Review(**review_data)

        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(review.user_id, "789")
        self.assertEqual(review.place_id, "101")
        self.assertEqual(review.text, "Great experience!")

    def test_save_method_updates_updated_at(self):
        review = Review()
        original_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(original_updated_at, review.updated_at)

    def test_to_dict_method_returns_dict(self):
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")

    def test_to_dict_method_contains_attributes(self):
        review = Review(user_id="456", place_id="202", text="Amazing views!")
        review_dict = review.to_dict()

        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["place_id"], "202")
        self.assertEqual(review_dict["text"], "Amazing views!")

    def test_default_values_for_new_instance(self):
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.text, "")

    def test_invalid_datetime_string_raises_exception(self):
        with self.assertRaises(ValueError):
            review_data = {"created_at": "invalid_datetime_string"}
            review = Review(**review_data)

    def test_updated_at_changes_after_save(self):
        review = Review()
        original_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(original_updated_at, review.updated_at)

if __name__ == "__main__":
    unittest.main()
