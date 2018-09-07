from rbnf.easy import build_parser, build_language, Language

grammar = """
keyword cast := 'commit' 'Author:'
sig := R'[0-9a-f]+'

space := R'\n|\s+'

head ::= 'commit' as mark 
                space sig as sig (~'\n')* '\n'
         (~'Author:')*
         'Author:' 
                 (~'<')+ as author '<' (~'>')+ as email '>'
         with mark.colno <= 1
         rewrite sig.value, ''.join(e.value for e in author).strip(), ''.join(e.value for e in email).strip()

section ::= head as sig (~head)+
            rewrite sig
            
lexer_helper := R'.'
partial_text ::= (~section)* section as it
                 rewrite it
                 
text ::= (section to [it] | ~section)+
         rewrite it
"""

lang = Language("git-log")

build_language(grammar, lang, '<python-internal>')

parse = build_parser(lang, use_parser='text')
partial_parse = build_parser(lang, use_parser='partial_text')
