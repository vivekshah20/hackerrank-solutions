import re
import sys 

stringToMatch=sys.stdin.read()

p = re.compile(r"""
(id="question-summary-(?P<id>\d+)")
(.*?)
(<h3><a\s*?href=".*?">(?P<subject>.*?)</a></h3>)
(.*?)
(<span\s+?title=".*?"\s+?class="relativetime"[^>]*>(?P<relativetime>.*?)</span>)
""",re.VERBOSE|re.DOTALL)

for match in p.finditer(stringToMatch):
    print ";".join([match.group("id"),match.group("subject"),match.group("relativetime")])