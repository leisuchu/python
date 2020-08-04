def getPLabel(func):
    def pLabel(name):
        return '<p>{0}</p>'.format(func(name))

    return pLabel


def getDiv(func):
    def div(name):
        return '<div>{0}</div>'.format(func(name))

    return div


@getDiv
@getPLabel
def getContent(name):
    return 'my name is {0}'.format(name)


print(getContent('leisuchu'))