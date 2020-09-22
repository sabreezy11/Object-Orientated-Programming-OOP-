# html document is a structured document that uses tags to enclose text. The browser
# uses those tags to work on how to display the text.

class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):  # to return a string
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
    def display(self, file=None): # adding this file parameter let's us send the output to a file
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')  # name, contents
        #  Creates a new tag with the name title and the contents being the text that
        #  was passed in to the init method.
        if title:
            self._title_tag = Tag('title', title) # use Tag to use the start/end tags and contents
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)  # displays body tag with the full contents


class HtmlDoc(object):  # this will contain the classes above and make use of the attributes
    # Polymorphic behavior: it's an html doc, but can be used in place of any of our tag
    # subclasses when we pass functions that just need the display method.
    # Therefore, we are using composition here instead of inheritance because we are not calling
    # from the 'Tag' class.

    def __init__(self, title=None):
        self._doc_type = DocType()  # composition
        self._head = Head(title)  # composition
        self._body = Body()  # composition

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)  # using 'add_tag' from 'Body' class

    # now we want to display the html tags
    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)  # opening html tag
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)  # closing html tag



if __name__ == '__main__':
    my_page =HtmlDoc('Demo HTML Document') # 'Demo HTML Document' is our title parameter
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub Heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    with open('test.html', 'w') as test_doc: # this creates the file test.html doc
        # you need to add the .html tag to be able to open the file in your browser
        my_page.display(file=test_doc)











