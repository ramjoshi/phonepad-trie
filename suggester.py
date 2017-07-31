from trie import patricia

KEYMAP = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

ptrie = patricia()

def keysearch(seq):
    suggestions = {}
    if len(seq) == 3:
        for ci in KEYMAP[seq[0]]:
            for cj in KEYMAP[seq[1]]:
                for ck in KEYMAP[seq[2]]:
                    word = ''.join([ci,cj,ck])
                    results = search(word)
                    if results:
                        suggestions.update(results)
    return suggestions

def search(word):
    data = ptrie.search(word)
    popular = {}
    if data:
        popularity(word, data, popular)
    return popular

def popularity(word, data, popular):
    w = data[0]
    if w is not '':
        word += w
    node = data[1]
    for n in node:
        if n == 'count':
            if not word in popular:
                popular[word] = 0
            popular[word] += node['count']
        elif n == '':
            if not word in popular:
                popular[word] = 0
            popular[word] += node[''][1]['count']
        else:
            popularity(word+n, node[n], popular)


def train(file):
    with open(file) as source:
        for l in source.readlines():
            for word in l.split(' '):
                word = omit_chars(word)
                ptrie.addWord(word.lower())

def omit_chars(text, chars=None):
    if chars is None:
        chars = '\n\r,.:;!?()"\''
    for c in chars:
        text = text.replace(c, '').rstrip('-')
    return text
