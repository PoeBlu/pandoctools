import panflute as pf


# noinspection PyUnusedLocal
def action(elem, doc):
    if (isinstance(elem, (pf.Code, pf.CodeBlock))) and elem.classes:
        elem.classes[0] = f'language-{elem.classes[0]}'


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
