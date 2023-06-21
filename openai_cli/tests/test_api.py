import unittest


from openai_cli.completion.api import complete_prompt


class CompletePromptTestCase(unittest.TestCase):
    def test_complete_prompt(self):
        prompt = "Write a tag line for an cafe in Vancouver"
        max_tokens = 1000
        verbose = True

        result = complete_prompt(prompt, max_tokens, verbose)

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

        success = result[0]
        self.assertIsInstance(success, bool)
        self.assertTrue(success)

        metadata = result[1]
        self.assertIsInstance(metadata, dict)
        self.assertIn("text", metadata)

        self.assertIn("status", metadata)
        self.assertEqual(metadata["status"], "choice: stop")


unittest.main()
