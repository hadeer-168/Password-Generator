# Password Generator

A simple Python project that generates a secure random password, validates it using regular expressions, and stores it with a timestamp in a text file.

## Features

* Generates a **10-character** random password.
* Uses:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters (`! @ # $ % &`)
* Validates the generated password using a regular expression.
* Saves valid passwords to `Passwords.txt`.
* Records the date and time each password was generated.
* Automatically opens the password file in Notepad (Windows).

## Technologies Used

* Python 3
* `random`
* `string`
* `re`
* `datetime`
* `os`
* `subprocess`

## Project Structure

```
PasswordGenerator.py
Passwords.txt   (created automatically after the first successful run)
```

## How It Works

1. Generates a random password.
2. Checks that it contains:

   * At least one uppercase letter
   * At least one lowercase letter
   * At least one digit
   * At least one special character
3. If the password is valid, it is saved to `Passwords.txt` with the current date and time.
4. If the generated password doesn't satisfy the validation rules, the program asks to try again.

## Example Output

```
Valid
```

Contents of `Passwords.txt`

```
aB4@xY8#mQ -> Sun Jul 19 21:35:12 2026
```
