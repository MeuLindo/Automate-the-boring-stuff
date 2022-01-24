#! python3
# mlcip.py - A multi-clipboard program

import sys, pyperclip

TEXT = {
    'agree': """Yes, surething. That sounds amazing.""",
    'disagree': """Nah, that's weird. Let's NOT do that""",
    'wtf': """Wtf are you talking about. Don't you know you sound crazy?""",
}

if len(sys.argv) < 2:
    print('Tell me what you need to be copied via the cmdline.')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    print(f'Copiando\n{TEXT[keyphrase]}\npara seu ctrl-c')
    pyperclip.copy(TEXT[keyphrase])
else:
    print(f'I\'ve got nothing for {keyphrase}')
