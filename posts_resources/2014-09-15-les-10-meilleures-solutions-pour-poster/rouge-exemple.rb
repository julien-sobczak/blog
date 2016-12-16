require 'rouge'

# source = File.read('D:/socledev/workspaces/move/Hitch/includes/test.java')
source = "public static int numberOfTrailingZeros(int i) {\n    // HD, Figure 5-14\n    int y;\n    if (i == 0) return 32;\n    int n = 31;\n    y = i <<16; if (y != 0) { n = n -16; i = y; }\n    y = i << 8; if (y != 0) { n = n - 8; i = y; }\n    y = i << 4; if (y != 0) { n = n - 4; i = y; }\n    y = i << 2; if (y != 0) { n = n - 2; i = y; }\n    return n - ((i << 1) >>> 31);\n}";
formatter = Rouge::Formatters::HTML.new(css_class: 'highlight')
lexer = Rouge::Lexers::Java.new
print formatter.format(lexer.lex(source))