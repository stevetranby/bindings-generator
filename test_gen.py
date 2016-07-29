#!/usr/bin/env python

import clang.cindex
from clang.cindex import CursorKind
from clang.cindex import Index
from clang.cindex import TypeKind

import sys

clang.cindex.Config.set_library_path("/Library/Developer/CommandLineTools/usr/lib")
index = clang.cindex.Index(clang.cindex.conf.lib.clang_createIndex(False, True))
translation_unit = index.parse(sys.argv[1], ['-x', 'c++'])

print "AST:"
for cursor in translation_unit.cursor.get_children():
    # Ignore AST elements not from the main source file (e.g from included files).
    if not cursor.location.file or cursor.location.file.name != 'test_gen.cpp':
        print 'N/A'
        continue

    # Ignore AST elements not a function declaration.
    if cursor.kind != CursorKind.FUNCTION_DECL:
        print 'N/A: ' + cursor.kind.name
        continue

    # Obtain the return Type for this function.
    result_type = cursor.type.get_result()

    print 'Function: %s' % cursor.spelling
    print '  Return type: %s' % result_type.kind.spelling
    print '  Arguments:'

    # Function has no arguments.
    if cursor.type.kind == TypeKind.FUNCTIONNOPROTO:
        print '    None'
        continue

    for arg_type in cursor.argument_types():
        print '    %s' % arg_type.kind.spelling

print "Diagnostics:"
for diag in translation_unit.diagnostics:
    print "******"
    print diag.severity
    print diag.location
    print diag.spelling
    print diag.option


########################################################
#
# #import clang.cindex, asciitree, sys
# import clang.cindex
# import asciitree
# import sys
#
# clang.cindex.Config.set_library_path("/Library/Developer/CommandLineTools/usr/lib")
# index = clang.cindex.Index(clang.cindex.conf.lib.clang_createIndex(False, True))
# translation_unit = index.parse(sys.argv[1], ['-x', 'c++'])
#
# print "steve.."
# print translation_unit.cursor
# # print asciitree.draw_tree(translation_unit.cursor,
# #   lambda n: n.get_children(),
# #   lambda nn: "%s (%s)" % (nn.spelling or nn.displayname, str(nn.kind).split(".")[1]))
#
