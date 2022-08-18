import re
import markdown as md
import argparse as ap

light = """body {
    font: 400 16px/1.5 "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #111;
    background-color: #fdfdfd;
    -webkit-text-size-adjust: 100%;
    -webkit-font-feature-settings: "kern" 1;
    -moz-font-feature-settings: "kern" 1;
    -o-font-feature-settings: "kern" 1;
    font-feature-settings: "kern" 1;
    font-kerning: normal;
    padding: 30px;
  }
  
  @media only screen and (max-width: 600px) {
    body {
      padding: 5px;
    }
  
    body > #content {
      padding: 0px 20px 20px 20px !important;
    }
  }
  
  body > #content {
    margin: 0px;
    max-width: 900px;
    border: 1px solid #e1e4e8;
    padding: 10px 40px;
    padding-bottom: 20px;
    border-radius: 10px;
    margin-left: auto;
    margin-right: auto;
  }
  
  hr {
    color: #bbb;
    background-color: #bbb;
    height: 1px;
    flex: 0 1 auto;
    margin: 1em 0;
    padding: 0;
    border: none;
  }
  
  /**
   * Links
   */
  a {
    color: #0366d6;
    text-decoration: none; }
    a:visited {
      color: #0366d6; }
    a:hover {
      color: #0366d6;
      text-decoration: underline; }
  
  pre {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
  }
  
  /**
    * Code blocks
    */
  
  code {
    background-color: rgba(27,31,35,.05);
    border-radius: 3px;
    font-size: 85%;
    margin: 0;
    word-wrap: break-word;
    padding: .2em .4em;
    font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace;
  }
  
  pre > code {
    background-color: transparent;
    border: 0;
    display: inline;
    line-height: inherit;
    margin: 0;
    overflow: visible;
    padding: 0;
    word-wrap: normal;
    font-size: 100%;
  }
  
  
  /**
   * Blockquotes
   */
  blockquote {
    margin-left: 30px;
    margin-top: 0px;
    margin-bottom: 16px;
    border-left-width: 3px;
    padding: 0 1em;
    color: #828282;
    border-left: 4px solid #e8e8e8;
    padding-left: 15px;
    font-size: 18px;
    letter-spacing: -1px;
    font-style: italic;
  }
  blockquote * {
    font-style: normal !important;
    letter-spacing: 0;
    color: #6a737d !important;
  }
  
  /**
   * Tables
   */
  table {
    border-spacing: 2px;
    display: block;
    font-size: 14px;
    overflow: auto;
    width: 100%;
    margin-bottom: 16px;
    border-spacing: 0;
    border-collapse: collapse;
  }
  
  td {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
  }
  
  th {
    font-weight: 600;
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
  }
  
  tr {
    background-color: #fff;
    border-top: 1px solid #c6cbd1;
  }
  
  table tr:nth-child(2n) {
    background-color: #f6f8fa;
  }
  
  /**
   * Others
   */
  
  img {
    max-width: 100%;
  }
  
  p {
    line-height: 24px;
    font-weight: 400;
    font-size: 16px;
    color: #24292e; }
  
  ul {
    margin-top: 0; }
  
  li {
    color: #24292e;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5; }
  
  li + li {
    margin-top: 0.25em; }
  
  * {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    color: #24292e; }
  
  a:visited {
    color: #0366d6; }
  
  h1, h2, h3 {
    border-bottom: 1px solid #eaecef;
    color: #111;
    /* Darker */ }
"""

dark = """body {
    font: 400 16px/1.5 "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #ffffff;
    background-color: #0d1117;
    -webkit-text-size-adjust: 100%;
    -webkit-font-feature-settings: "kern" 1;
    -moz-font-feature-settings: "kern" 1;
    -o-font-feature-settings: "kern" 1;
    font-feature-settings: "kern" 1;
    font-kerning: normal;
    padding: 30px;
  }
  
  @media only screen and (max-width: 600px) {
    body {
      padding: 5px;
    }
  
    body > #content {
      padding: 0px 20px 20px 20px !important;
    }
  }
  
  body > #content {
    margin: 0px;
    max-width: 900px;
    border: 1px solid #30363d;
    padding: 10px 40px;
    padding-bottom: 20px;
    border-radius: 10px;
    margin-left: auto;
    margin-right: auto;
  }
  
  hr {
    color: #bbb;
    background-color: #bbb;
    height: 1px;
    flex: 0 1 auto;
    margin: 1em 0;
    padding: 0;
    border: none;
  }
  
  /**
   * Links
   */
  a {
    color: #0366d6;
    text-decoration: none; }
    a:visited {
      color: #0366d6; }
    a:hover {
      color: #0366d6;
      text-decoration: underline; }
  
  pre {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    overflow: auto;
    padding: 16px;
  }
  
  /**
    * Code blocks
    */
  
  code {
    background-color: #343942;
    color: #c9d1d9;
    border-radius: 3px;
    font-size: 85%;
    margin: 0;
    word-wrap: break-word;
    padding: .2em .4em;
    font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,Courier,monospace;
  }
  
  pre > code {
    background-color: transparent;
    border: 0;
    display: inline;
    line-height: inherit;
    margin: 0;
    overflow: visible;
    padding: 0;
    word-wrap: normal;
    font-size: 100%;
  }
  
  
  /**
   * Blockquotes
   */
  blockquote {
    margin-left: 30px;
    margin-top: 0px;
    margin-bottom: 16px;
    border-left-width: 3px;
    padding: 0 1em;
    color: #828282;
    border-left: 4px solid #30363d;
    padding-left: 15px;
    font-size: 18px;
    letter-spacing: -1px;
    font-style: italic;
  }
  blockquote * {
    font-style: normal !important;
    letter-spacing: 0;
    color: #6a737d !important;
  }
  
  /**
   * Tables
   */
  table {
    border-spacing: 2px;
    display: block;
    font-size: 14px;
    overflow: auto;
    width: 100%;
    margin-bottom: 16px;
    border-spacing: 0;
    border-collapse: collapse;
  }
  
  td {
    padding: 6px 13px;
    border: 1px solid #30363d;
  }
  
  th {
    font-weight: 600;
    padding: 6px 13px;
    border: 1px solid #30363d;
  }
  
  tr {
    background-color: #fff;
    border-top: 1px solid #30363d;
  }
  
  table tr:nth-child(2n) {
    background-color: #f6f8fa;
  }
  
  /**
   * Others
   */
  
  img {
    max-width: 100%;
  }
  
  p {
    line-height: 24px;
    font-weight: 400;
    font-size: 16px;
    color: #c9d1d9; }
  
  ul {
    margin-top: 0; }
  
  li {
    color: #c9d1d9;
    font-size: 16px;
    font-weight: 400;
    line-height: 1.5; }
  
  li + li {
    margin-top: 0.25em; }
  
  * {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    color: #24292e; }
  
  em {
    color: #8b949e;
  }
  
  a:visited {
    color: #0366d6; }
  
  strong {
    color: #c9d1d9;
  }
  
  h1, h2, h3 {
    border-bottom: 1px solid #21262d;
    color: #c9d1d9;
    /* Darker */ }
"""

parser = ap.ArgumentParser(description='Convert Markdown to HTML in GitHub Readme style')
parser.add_argument('file', help='Markdown file to convert')
parser.add_argument('-m', '--mode', help='Color mode', choices=['light', 'dark', 'l', 'd'], default='light', required=False)
""" parser.add_argument('-i', '--input', help='Input file', required=True)
parser.add_argument('-m', '--mode', help='Color mode (light(l)/dark(d))', required=False) """
args = parser.parse_args()

mds = open(args.file, 'r', encoding="utf-8").read()

print('Converting Markdown to HTML...')

if args.mode is not None:
  if args.mode == 'light' or args.mode == 'l':
    css = light
  elif args.mode == 'dark' or args.mode == 'd':
    css = open('./res/dark.css', 'r').read()
  else:
    print('Invalid color mode, using light mode...')
    css = dark
else:
  css = light

body = md.Markdown(extensions=['md_in_html', 'tables', 'nl2br']).convert(mds)
pre = '''<html>
      <head>
        <title>''' + str(args.file).split('.md')[0] + '''</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>
      <body>
        <div id='content'>
    '''
post = '''</div>
        <style type='text/css'>''' + css + '''</style>
      </body>
    </html>'''

with open('result.html', 'w', encoding='utf-8') as f:
    f.write(pre + body + post)

print('Done!')