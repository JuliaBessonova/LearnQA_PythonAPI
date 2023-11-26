class TestExample:
    def test_check_short_phrase(self):
        phrase = input("Enter short phrase: ")
        max_length = 15
        assert len(phrase) < max_length, f"Entered phrase is longer than {max_length} symbols"