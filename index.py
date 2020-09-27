a = "abcdefasdkjlasldhsjabdlsajbdkasbdlpoqugasbcawleknqwusoaicjxbzcpiasdjwqdnsaxasdncmzxc"

t = dict()


def make_dict(t1):
    for letter in a:
        if letter in t1:
            t1[letter] = t1[letter] + 1
        else:
            t1[letter] = 1


make_dict(t)


def reverse_dict(t1):
    t2 = dict()
    for key in t1:
        if not t1[key] in t2:
            t2[t1[key]] = [key]
        else:
            t2[t1[key]].append(key)
    return t2


t3 = reverse_dict(t)
print(t3)
