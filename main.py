import click
import logging
import string
import random

"""
Logging for the program
"""

logging.basicConfig(
        level=logging.INFO,
        format='{asctime} - {levelname} - {message}',
        style='{',
        datefmt="%Y-%m-%d: %H:%M",
        handlers=[
            logging.StreamHandler()
        ]
    )


class PasswordManager:
    """
    Password Manager class. Handles instanciating necessary characters for generating new passwords
    """
    @staticmethod 
    def characters() -> list[list]:
        """
        Returns a list of all characters including:
        1. all lowercase letters
        2. all uppercase letters
        3. all digits
        4. all punctuations
        """
        all_lowercase_letters = list(string.ascii_lowercase)
        all_uppercase_letters = list(string.ascii_uppercase)
        all_digits = list(string.digits)
        all_punctuations = list(string.punctuation)
        all_characters = [
            all_lowercase_letters,
            all_uppercase_letters,
            all_digits,
            all_punctuations,
        ]

        return all_characters
         
    @staticmethod
    @click.command()
    @click.option('-l', '--length', default=8, help="length of password", show_default=True)
    def generate_password(length) -> str:
        """
        @param length: Specifies length of password
        Returns a generated of length <length>
        """
        password = []

        if length < 8:
            click.echo("Standard password length cannot be less than 8")
            return 
            
        all_characters = PasswordManager.characters()
        for _ in range(length):
            
            selected_character_list = random.choice(all_characters)
            password.append(random.choice(selected_character_list))
        logging.info(f"New password is: {''.join(password)}")

        return "".join(password)


    @click.command()
    def encrypt_password() -> None:
        """
        Returns encrypted password
        """
        pass


    @click.command()
    def store_password() -> None:
        """
        Store password in mongoDB
        """
        pass


def main():
    pm = PasswordManager()
    pm.generate_password()
    
    
if __name__ == "__main__":
    main()
