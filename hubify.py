import re
import markdown as md
import argparse as ap

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
    css = open('./res/light.css', 'r').read()
  elif args.mode == 'dark' or args.mode == 'd':
    css = open('./res/dark.css', 'r').read()
  else:
    print('Invalid color mode, using light mode...')
    css = open('light.css', 'r').read()
else:
  css = open('./res/light.css', 'r').read()

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