from sys import exit


def hax(input):
    output = input
    output = output.replace('a', '4')
    output = output.replace('A', '4')
    output = output.replace('i', '1')
    output = output.replace('I', '1')
    output = output.replace('o', '0')
    output = output.replace('O', '0')
    output = output.replace('e', '3')
    output = output.replace('E', '3')
    return output


if __name__ == "__main__":
    phrases = []
    phrases.append(input("[?] Enter first name: "))
    phrases.append(input("[?] Enter second name: "))
    phrases.append(input("[?] Enter pet's name: "))
    phrases.append(input("[?] Enter city: "))
    phrases.append(input("[?] Enter birth' s year: "))
    phrases.append(input("[?] Enter birth's  month: "))
    hax_mode = input("[?] Would you like to use 1337 mode? [Y/N]")
    if hax_mode.lower() == 'y':
        hax_mode = True
    elif hax_mode.lower() == 'n':
        hax_mode = False
    else:
        exit(f"[-] Incorrect value: {hax_mode}. Exiting...")
    file_name = input("[?] Where you want to save generated wordlist? ")
    words = 0
    with open(file_name, 'w') as wordlist:
        for phrase in phrases:
            wordlist.write(phrase + '\n')
            wordlist.write(phrase.lower() + '\n')
            wordlist.write(phrase.upper() + '\n')
            words += 3
            for phrase_two in phrases:
                wordlist.write(phrase + phrase_two + '\n')
                wordlist.write(phrase.lower() + phrase_two + '\n')
                wordlist.write(phrase.upper() + phrase_two + '\n')
                wordlist.write(phrase.lower() + phrase_two.lower() + '\n')
                wordlist.write(phrase.lower() + phrase_two.upper() + '\n')
                wordlist.write(phrase.upper() + phrase_two.lower() + '\n')
                wordlist.write(phrase.upper() + phrase_two.upper() + '\n')
                words += 7

        if hax_mode:
            for phrase in phrases:
                wordlist.write(hax(phrase) + '\n')
                wordlist.write(hax(phrase).lower() + '\n')
                wordlist.write(hax(phrase).upper() + '\n')
                words += 3
                for phrase_two in phrases:
                    wordlist.write(hax(phrase + phrase_two) + '\n')
                    wordlist.write(hax(phrase.lower() + phrase_two + '\n'))
                    wordlist.write(hax(phrase.upper() + phrase_two + '\n'))
                    wordlist.write(
                        hax(phrase.lower() + phrase_two.lower() + '\n'))
                    wordlist.write(
                        hax(phrase.lower() + phrase_two.upper() + '\n'))
                    wordlist.write(
                        hax(phrase.upper() + phrase_two.lower() + '\n'))
                    wordlist.write(
                        hax(phrase.upper() + phrase_two.upper() + '\n'))
                    wordlist.write(hax(phrase) + phrase_two)
                    wordlist.write(phrase + hax(phrase_two))
                    words += 9
        wordlist.close()
    print(f"[+] Generated {words} passwords.")
