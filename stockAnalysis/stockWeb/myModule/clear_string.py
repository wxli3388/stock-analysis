import re

class ClearString:
    def clean_html(self, htmlString):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', htmlString)
        return cleantext