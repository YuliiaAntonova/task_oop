import json
from signers import Singer

if __name__ == '__main__':
    a = Singer("123", "235")

    with open("data.json", "r") as file:
        data = json.load(file)

    if type(data) is list:
        tokens = []

        for i in data:
            if type(i) is dict:
                token = a.pyjwt_encode(i)
                print(token)
                tokens.append(token)
            else:
                raise LookupError("Who r u?")
        print(tokens)
        with open('tokens.json', 'w') as f:
            json.dump(tokens, f, indent=4)

    else:
        raise ValueError("Hmm, what is it?")

    with open("tokens.json", "r") as file:
        data = json.load(file)

    if type(tokens) is list:
        decoded_list = []

        for i in tokens:
            if type(i) is str:
                decoded = a.pyjwt_decode(i)
                print(decoded)
                decoded_list.append(decoded)
            else:
                raise LookupError("Who r u?")
        print(decoded_list)
        with open('decoded-data.json', 'w') as f:
            json.dump(data, f, indent=4)

    else:
        raise ValueError("Hmm, what is it?")

    # itsdangerous lib
    with open("token.json", "r") as file:
        data = json.load(file)

    if type(data) is list:
        tokens = []

        for i in data:
            if type(i) is dict:
                token = a.its_encode(i)
                print(token)
                tokens.append(token)
            else:
                raise LookupError("Who r u?")
        print(tokens)
        with open('its-tokens.json', 'w') as f:
            json.dump(tokens, f, indent=4)

    else:
        raise ValueError("Hmm, what is it?")

    with open("its-tokens.json", "r") as file:
        data = json.load(file)

    if type(tokens) is list:
        decoded_list = []

        for i in tokens:
            if type(i) is str:
                decoded = a.its_decode(i)
                print(decoded)
                decoded_list.append(decoded)
            else:
                raise LookupError("Who r u?")
        print(decoded_list)
        with open('its-decoded-data.json', 'w') as f:
            json.dump(data, f, indent=4)

    else:
        raise ValueError("Hmm, what is it?")
