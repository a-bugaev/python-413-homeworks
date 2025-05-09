"""
HW 30: Using patterns "strategy" and "Facade" for checking polyndromes
"""

from abc import ABC, abstractmethod
import re


class PalindromeStrategy(ABC):
    """
    abstraction for all check strategies
    """

    @abstractmethod
    def is_palindrome(self, text: str) -> bool:
        """
        placeholder
        """


class SingleWordPalindrome(PalindromeStrategy):
    """
    checks single words
    """

    def is_palindrome(self, text: str) -> bool:
        cleaned_text = text.lower()
        return cleaned_text == cleaned_text[::-1]


class MultiWordPalindrome(PalindromeStrategy):
    """
    checks phrases
    """

    def is_palindrome(self, text: str) -> bool:
        cleaned_text = "".join(
            re.split(r'[ \n\r\t.,!?;:()\[\]{}\'"<>/?\\]+', text)
        ).lower()
        return cleaned_text == cleaned_text[::-1]


class PalindromeContext:
    """
    wrapper for strategy selection and checking
    """

    def __init__(self, strategy: PalindromeStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PalindromeStrategy) -> None:
        """
        allows set change strategy
        """
        self.strategy = strategy

    def check(self, text: str) -> bool:
        """
        performs check using selected strategy
        """
        return self.strategy.is_palindrome(text)


class PalindromeFacade:
    """
    facade for simple usage
    """

    def __init__(self):
        self.context = PalindromeContext(SingleWordPalindrome())

    def check_palindrome(self, text: str) -> bool:
        """
        selects strategy and applies it
        """
        words = text.split()
        if len(words) == 1:
            self.context.set_strategy(SingleWordPalindrome())
        else:
            self.context.set_strategy(MultiWordPalindrome())
        return self.context.check(text)


if __name__ == "__main__":
    facade = PalindromeFacade()

    test_data = [
        "A Toyota",
        "Was it a car or a cat I saw",
        "A Santa at NASA",
        "No lemon, no melon",
        "Never odd or even",
        "Able was I, I saw Elba",
        "Step on no pets",
        "Racecar",
        "Level",
        "Rotor",
        "Mom",
        "Dad",
        "Kayak",
        "Anna",
        "Eye",
        "Wow",
        "Bob",
        "Hello, World!",
        "РАЗ РАЗ РАЗ ЭТО ХАРБАСС!",
        "А роза упала на лапу Азора...",
    ]

    for text_for_test in test_data:
        print(f"'{text_for_test}' is {'' if facade.check_palindrome(text_for_test) else 'not'} palindrome")
