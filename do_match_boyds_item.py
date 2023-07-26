import re

boyds_re = '\d+\s+\d+\.\d{2}\s+\$(\d+\.\d{2})\s+(.*)'
# boyds_re = '\d+\s+\d+\.\d{2}\s+\$(\d+\.\d{2})\s+(.*)\s+(.*)(\d+)\s+(\d+\.\d{2})\s+\$(\d+\.\d{2})\s+(.*)\s+(.*)'

valid_line_item = """1 21.00 $18.78
new amsterdam vodka 1.754.
total tem discount: $3.20
"""

print(valid_line_item)

match = re.search(boyds_re, valid_line_item)

if hasattr(match, 'group'):
    article_name = match.group(1)

    article_sum = match.group(2)

    """
    if match.group(2) == "-":
        article_sum = "-" + match.group(3).replace(",", ".")
    else:
        article_sum = match.group(3).replace(",", ".")
    """

    print('{} {}'.format(article_name, article_sum))
else:
    print('Not found')