import builder

if __name__ == '__main__':
    data = {"email": "testtest@mail.ru", "password": "short5test"}
    validator = builder.DataValidator(data)
    errors = validator.validate_email().validate_password().get_errors()

    if errors:
        print(errors)

    print(validator.data)